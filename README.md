# Flask_CurrencyCalculator_NamesInUSA
### This is a small website with two pages using Python Flask in the backend. For runnig it you just need the "data"-,"templates"- and "static"-Folder as well as the "run.py". The "run.py" is also the file you have to execute then in a Python IDE. 
## CurrencyCalculator
![](/Examples/example_CurrencyCalculator.png)
The first page is a simple currency calculator which shows the exchange rate and the money for certain amounts by choosing two currencies and press "OK". The exchange rates are made-up by myself.

## NamesInUSA
![](/Examples/example_NamesInUSA.png)

The second page is an example for filter and plot Data from a .csv-file with Flask. 
You can choose a Name, the gender, and a state press "OK" and you get the a Plot of the amount over the years for the Name in the choosen state. It is possible to choose up to three Names to let them plot and by pressing "Löschen" you delete the last plotted Name

Id | Name | Year | Gender | State | Count
-------- | -------- | -------- | -------- | -------- | --------
1   | Mary  | 1910 | F | AK | 14  
2   | Annie   | 1910  | F | AK | 12
3   | Anna  | 1910  | F | AK | 10 |  
...   | ...   | ...   | ... | ... | ... | ... 
2474127 | Ramona | 1924 | F | MI | 7  
2474128 | Robert | 1924 | F | MI | 7  
2474129 | Rosa | 1924 | F | MI | 7  
...   | ...   | ...   | ... | ... | ... | ... 
5647424 | Tyce | 2014 | M | WY | 5  
5647425 | Victor | 2014 | M | WY | 5  
5647426 | Waylon | 2014 | M | WY | 5

The .csv-File shows the amount of each Name for each State in the USA in each year from 1910 till 2014... (6 columns, 5647426 rows). Due to the filesize I prefilter it, so that i can upload it to github. 
