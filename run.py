from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

import run

app = Flask(__name__)

# ursprünglich 999 Zeilen, ab Jahr 999 und jeder Name
df = pd.read_csv("data/names.csv", index_col=0)

# df_2000 = df[df["Year"] >= 2000]
# df_2000.to_csv("data/names.csv")
# df_over100 = {}
# for o in df:
# df_over100 =

to_plot = dict()
remove_png = []


@app.route("/")
def currency():
    currencies = [("US Dollar", "USD", 1.0), ("Euro", "EUR", 0.9), ("Jordanian Dinar", "JOD", 0.7),
                  ("Thai Baht", "THB", 35.9),
                  ("Chinese Yuan Renminbi", "CNY", 7.2), ("Japanese Yen", "JPY", 150.3)]
    amount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 50, 100, 200, 500]

    exchange_money = {}
    exchange_rate = currencies[0][2] * currencies[1][2]

    currency1 = request.args.get("currency1")
    name1 = currencies[0][0]
    iso1 = currencies[0][1]
    exchange_rate1 = currencies[0][2]

    for item in currencies:
        if item[1] == currency1:
            name1 = item[0]
            iso1 = item[1]
            exchange_rate1 = item[2]

    currency2 = request.args.get("currency2")
    name2 = currencies[1][0]
    iso2 = currencies[1][1]
    exchange_rate2 = currencies[1][2]

    for item in currencies:
        if item[1] == currency2:
            name2 = item[0]
            iso2 = item[1]
            exchange_rate2 = item[2]

    exchange_rate = (exchange_rate2 / exchange_rate1)
    exchange_rate_rounded = "{:.2f}".format(exchange_rate)

    for a in amount:
        exchange_money[a] = "{:.2f}".format(a * exchange_rate)

    return render_template("currency.html",
                           currency1=currency1, currency2=currency2,
                           name1=name1, iso1=iso1,
                           name2=name2, iso2=iso2,
                           amount=amount, currencies=currencies,
                           exchange_rate=exchange_rate, exchange_money=exchange_money,
                           exchange_rate_rounded=exchange_rate_rounded
                           )


@app.route("/namesinusa")
def names():
    button_del = True

    names = df["Name"].drop_duplicates().sort_values()
    states = df["State"].drop_duplicates().sort_values()
    gender = df["Gender"].drop_duplicates().sort_values()
    plt.savefig("static/images/namesinusa.png")
    source = "static/images/namesinusa.png"

    dt = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")

    get_name = request.args.get("name")
    get_gender = request.args.get("gender")
    get_state = request.args.get("state")

    df_1 = df[df["Name"] == get_name]
    df_2 = df_1[df_1["Gender"] == get_gender]
    df_3 = df_2[df_2["State"] == get_state]

    if request.args.get("name") != None and request.args.get("delete") == None:
        if len(to_plot) < 3:
            to_plot[(request.args.get("name"), request.args.get("gender"),
                     request.args.get("state"))] = (df_3["Year"], df_3["Count"])
            source = "static/images/namesinusa" + dt + ".png"
            if len(to_plot) != 0:
                for i in to_plot:
                    plt.plot(to_plot[i][0], to_plot[i][1], label=i)
                plt.legend()
                plt.savefig("static/images/namesinusa" + dt + ".png")
                plt.clf()
        elif len(to_plot) == 3:
            source = "static/images/" + os.listdir("static/images/")[1]

    elif request.args.get("delete") != None:
        print(len(to_plot))
        if len(to_plot) > 0:
            del to_plot[list(to_plot)[-1]]
            source = "static/images/namesinusa" + dt + ".png"
            for i in to_plot:
                plt.plot(to_plot[i][0], to_plot[i][1], label=i)
            if len(to_plot) > 0:
                plt.legend()
                plt.savefig("static/images/namesinusa" + dt + ".png")
                plt.clf()
            else:
                source = "static/images/namesinusa.png"

    if len(os.listdir("static/images/")) == 3:
        remove_png = os.listdir("static/images/")[1]
        os.remove("static/images/" + remove_png)

    return render_template("namesinusa.html", names=names, states=states, gender=gender,
                           to_plot=to_plot, source=source, button_del=button_del)
