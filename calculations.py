import unittest
import sqlite3
import json
import os
import requests



calculations_dict = {}


def gather_mama(cur, conn):

    cur.execute('select joke from YoMama')
    x = cur.fetchall() 
    return x

def gather_harry(cur, conn): 
    cur.execute('select term from HarryPotter')
    x = cur.fetchall() 
    return x


def gather_holidays(cur, conn): 
    cur.execute('select holiday_name from Holidays')
    x = cur.fetchall() 
    return x

def get_harry_jokes(cur, conn, mama, harry): 
    cur.execute('create table if not exists HPxYoMama(joke_id int, HPterm_id int, term_type int)')
    termId_list = []

    for joke in mama: 
        joke = joke[0].lower()

        for term in harry: 
            term = term[0].lower()
            
            if term in joke: 
                #insert into table

                cur.execute('SELECT joke_id from YoMama where joke = ?', (joke,))
                conn.commit()

                joke_id = cur.fetchall()
                joke_id = joke_id[0][0]
    

                cur.execute('SELECT term_id from HarryPotter where term = ?', (term,))
                conn.commit()

                term_id = cur.fetchall()
                term_id = term_id[0][0]
                termId_list.append(term_id)

                conn.execute('insert into HPxYoMama(joke_id, HPterm_id) values (?,?)', (joke_id,term_id))
                conn.commit()
    return termId_list




def join_harry_id(termId_list, cur, conn): 
    #SELECT form table JOIN table terms on this table.hp term id = that table.term id JOIN third table (term types) on term type on type id = terms.type_id
    #conn.execute("select HarryPotter.term_type from HarryPotter JOIN HPxYomama ON HPxYomama.HPterm_id =  HarryPotter.term_id JOIN HarryPotterTermCategories on HarryPotterTermCategories.term_type = HarryPotter.term_type")
    cur.execute('select HarryPotter.term_type FROM HarryPotter JOIN HPxYoMama on HarryPotter.term_id = HPxYoMama.HPterm_id')
    conn.commit()
    results = cur.fetchall()


    for i in range(len(results)): 
        cur.execute('UPDATE HPxYoMama SET term_type = ? WHERE HPterm_id = ?', (results[i][0], termId_list[i]))
        conn.commit()





def calculate_harry_percentages(cur, conn):

    #Calculate the total percentage of Yomama jokes that are Harry Potter related
    cur.execute('select count(*) as total from YoMama')
    conn.commit()
    total_jokes = cur.fetchall()
    total_jokes = total_jokes[0][0]

    cur.execute('select count(*) as total from HPxYoMama')
    total_harry_jokes = cur.fetchall()
    total_harry_jokes = total_harry_jokes[0][0]

    percent_harry_jokes = total_harry_jokes / total_jokes * 100 

    #Calculate the total percentage of Harry Potter Yomama jokes that reference characters
    cur.execute('select term_type FROM HPxYoMama where term_type = 1')
    conn.commit()
    total_character_jokes = cur.fetchall()
    total_character_jokes = len(total_character_jokes)

    percent_character_jokes = total_character_jokes / total_harry_jokes * 100

    #Calculate the total percentage of Harry Potter Yomama jokes that reference species
    cur.execute('select term_type FROM HPxYoMama where term_type = 2')
    conn.commit()
    total_species_jokes = cur.fetchall()
    total_species_jokes = len(total_species_jokes)

    percent_species_jokes = total_species_jokes / total_harry_jokes * 100

    #Calculate the total percentage of Harry Potter Yomama jokes that reference specific books
    cur.execute('select term_type FROM HPxYoMama where term_type = 3')
    conn.commit()
    total_book_jokes = cur.fetchall()
    total_book_jokes = len(total_book_jokes)

    percent_book_jokes = total_book_jokes / total_harry_jokes * 100

    calculations_dict["total_harry_jokes"] = total_harry_jokes
    calculations_dict["percent_harry_jokes"] = percent_harry_jokes
    calculations_dict["percent_character_jokes"] = percent_character_jokes
    calculations_dict["percent_species_jokes"] = percent_species_jokes
    calculations_dict["percent_book_jokes"] = percent_book_jokes




def clean_holiday_data(holidays):
    cleaned_holiday_list = []
    cleaned_holiday_longest_word = []

    for holiday in holidays:

        #First item in the tuple
        original_holiday = holiday[0]

        #Split up the holiday name 
        cleaned_holiday = original_holiday.split()

        new_holiday = []

        for word in cleaned_holiday: 
            new_holiday.append((len(word), word))


        new_holiday = sorted(new_holiday, key = lambda t: t[0])
        cleaned_holiday = new_holiday[-1][1]
        
        if cleaned_holiday not in cleaned_holiday_longest_word and len(cleaned_holiday) > 3 and cleaned_holiday != 'birthday' and cleaned_holiday != 'chinese' and cleaned_holiday != 'wars' and cleaned_holiday != 'kentucky' and cleaned_holiday != "washington's":
            cleaned_holiday_longest_word.append(cleaned_holiday)
            cleaned_holiday_list.append((cleaned_holiday, original_holiday ))

    return cleaned_holiday_list


def get_holiday_jokes(cur, conn, mama, holiday): 

    cur.execute('create table if not exists HolidaysxYoMama(joke_id int, holiday_id int)')
    cleaned_holiday = clean_holiday_data(holiday)

    for joke in mama: 
        joke = joke[0]

        for day in cleaned_holiday: 

            if day[0] in joke: 

                cur.execute('SELECT joke_id from YoMama where joke = ?', (joke,))
                conn.commit()

                joke_id = cur.fetchall()
                joke_id = joke_id[0][0]
    
                print(day)
                cur.execute('SELECT holiday_id from Holidays where holiday_name = ?', (day[1],))
                conn.commit()

                holiday_id = cur.fetchall()
                holiday_id = holiday_id[0][0]


                conn.execute('insert into HolidaysxYoMama(joke_id, holiday_id) values (?,?)', (joke_id,holiday_id))
                conn.commit()




def calculate_holiday_percentages(cur, conn):

    #Calculate the total percentage of Yomama jokes that are Harry Potter related
    cur.execute('select count(*) as total from YoMama')
    conn.commit()
    total_jokes = cur.fetchall()
    total_jokes = total_jokes[0][0]


    cur.execute('select count(*) as total from HolidaysxYoMama')
    total_holiday_jokes = cur.fetchall()
    total_holiday_jokes = total_holiday_jokes[0][0]

    percent_holiday_jokes = total_holiday_jokes / total_jokes * 100 

    calculations_dict["total_holiday_jokes"] = total_holiday_jokes
    calculations_dict["percent_holiday_jokes"] = percent_holiday_jokes
    return calculations_dict




def write_calculations():
    f = open("calculations.txt", "w")

    for item in calculations_dict:
        f.write(item + ": " + str(calculations_dict[item]))
        f.write('\n')

    f.close()











