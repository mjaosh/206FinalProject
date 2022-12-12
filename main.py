import unittest
import sqlite3
import json
import os
import requests
import finalproject
import calculations
import visualizations

HOLIDAY_URL = 'https://holidayapi.com/v1/holidays?pretty&key=1e2c4690-615b-421a-a1c7-cb9cd52ad2b0&country=US&year=2021'
MAMA_URL = 'https://raw.githubusercontent.com/Fadyazmy/yo-mamma/master/yo_mama_jokes.txt'



 
def main(): 

    #Create database
    cur, conn = finalproject.setUpDatabase('data.db')

    #Create all the tables
    finalproject.create_holiday_table(cur, conn)
    finalproject.create_mama_table(cur,conn)
    finalproject.create_harry_table(cur, conn)
    finalproject.create_harry_id_table(cur,conn)



    cur.execute('select count(*) as total from YoMama')
    count = cur.fetchall()
    count = count[0][0]


    #Put data in prospective tables
    if count != 500:
        finalproject.get_holiday_data(cur, conn, HOLIDAY_URL)
        finalproject.get_mama_data(cur,conn, MAMA_URL)
        finalproject.get_harry_data(cur,conn)

    elif count == 500:
        #Calculations
         mama = calculations.gather_mama(cur, conn)
         harry = calculations.gather_harry(cur,conn)

         termID_list = calculations.get_harry_jokes(cur, conn, mama,harry)
         calculations.join_harry_id(termID_list, cur,conn)
         calculations.calculate_harry_percentages(cur, conn)

         holidays = calculations.gather_holidays(cur, conn)

         calculations.get_holiday_jokes(cur,conn, mama, holidays)
         calcs = calculations.calculate_holiday_percentages(cur, conn)
         calculations.write_calculations()
         visualizations.hp_type_pie(calcs)
         visualizations.in_yomama_pie(calcs)
         visualizations.hp_vs_holiday_bar(calcs)





if __name__ == "__main__":
    main()