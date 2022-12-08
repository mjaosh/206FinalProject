import unittest
import sqlite3
import json
import os
import requests


HOLIDAY_URL = 'https://holidayapi.com/v1/holidays?pretty&key=1e2c4690-615b-421a-a1c7-cb9cd52ad2b0&country=US&year=2021'
HARRY_CHARACTERS_URL = 'https://fedeperin-harry-potter-api-en.herokuapp.com/db'
MAMA_URL = 'https://yomamma-api.herokuapp.com/jokes?count=500'


# Create Database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


#Create the holiday table
def create_holiday_table(cur, conn):
    cur.execute('create table if not exists Holidays(holiday_id INTEGER PRIMARY KEY AUTOINCREMENT, holiday_name CHAR(50), date VARCHAR(50))')
    conn.commit()


#Gather the data
def get_holiday_data(cur, conn, url):
    try: 
        r = requests.get(url).text
        dict = json.loads(r)

        cur.execute('select count(*) as total from Holidays')
        count = cur.fetchall()
        count = count[0][0]

        for i in range (count, count + 24):
            item =  dict['holidays'][i] 
            conn.execute('insert into Holidays (holiday_name, date) values(?,?)', (item['name'].lower(), item['date'].lower()))
            conn.commit()
    except: 
        print("Holiday API done")

    

def create_mama_table(cur, conn):
    cur.execute('create table if not exists YoMama(joke_id INTEGER PRIMARY KEY AUTOINCREMENT, joke TEXT)')
    conn.commit()

def get_mama_data(cur, conn, url): 
    r = requests.get(url).text
    dict = json.loads(r)

    cur.execute('select count(*) as total from YoMama')
    count = cur.fetchall()
    count = count[0][0]



    for i in range (count, count + 25):
        conn.execute('insert into YoMama (joke) values(?)', (dict[i].lower(),))
        conn.commit()
        count += 1

    

def create_harry_table(cur, conn):
    cur.execute('create table if not exists HarryPotter(term_id INTEGER PRIMARY KEY AUTOINCREMENT, term_type INTEGER, term TEXT)')
    conn.commit()

def get_harry_data(cur, conn):

    cur.execute('select count(*) as total from HarryPotter')
    count = cur.fetchall()
    count = count[0][0]

    if count == 0:

        char_url = 'https://legacy--api.herokuapp.com/api/v1/characters?page=1'
        species_url = 'https://legacy--api.herokuapp.com/api/v1/species?page=1'
        books_url = 'https://legacy--api.herokuapp.com/api/v1/books?page=1'

        r = requests.get(char_url).text
        s = requests.get(species_url).text
        b = requests.get(books_url).text

        char_dict = json.loads(r)
        species_dict = json.loads(s)
        book_dict = json.loads(b)

        for i in range (0,10): 
            name = char_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (1,name))
            conn.commit()

            species = species_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (2,species))
            conn.commit()

        for i in range (0,4):
            title = book_dict[i]['title'][21:].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (3,title))
            conn.commit()

    elif count == 24: 

        char_url = 'https://legacy--api.herokuapp.com/api/v1/characters?page=1'
        species_url = 'https://legacy--api.herokuapp.com/api/v1/species?page=1'
        books_url = 'https://legacy--api.herokuapp.com/api/v1/books?page=1'

        r = requests.get(char_url).text
        s = requests.get(species_url).text
        b = requests.get(books_url).text

        char_dict = json.loads(r)
        species_dict = json.loads(s)
        book_dict = json.loads(b)

        for i in range (10,20): 
            name = char_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (1,name))
            conn.commit()

            species = species_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (2,species))
            conn.commit()

        for i in range (4,7):
            title = book_dict[i]['title'][21:].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (3,title))
            conn.commit()


    elif count == 47: 
        char_url = 'https://legacy--api.herokuapp.com/api/v1/characters?page=2'
        species_url = 'https://legacy--api.herokuapp.com/api/v1/species?page=2'


        r = requests.get(char_url).text
        s = requests.get(species_url).text

        char_dict = json.loads(r)
        species_dict = json.loads(s)

        for i in range (0,10): 
            name = char_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values(?,?)', (1,name))
            conn.commit()

            species = species_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (2,species))
            conn.commit()

    elif count == 67:
        char_url = 'https://legacy--api.herokuapp.com/api/v1/characters?page=2'
        species_url = 'https://legacy--api.herokuapp.com/api/v1/species?page=2'

        r = requests.get(char_url).text
        s = requests.get(species_url).text

        char_dict = json.loads(r)
        species_dict = json.loads(s)

        for i in range (10,20): 
            name = char_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (1,name))
            conn.commit()

            species = species_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)',(2,species))
            conn.commit()

    elif count == 87: 
        char_url = 'https://legacy--api.herokuapp.com/api/v1/characters?page=3'
        species_url = 'https://legacy--api.herokuapp.com/api/v1/species?page=3'

        r = requests.get(char_url).text
        s = requests.get(species_url).text


        char_dict = json.loads(r)
        species_dict = json.loads(s)

        for i in range (0,10): 
            name = char_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (1,name))
            conn.commit()

            species = species_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (2,species))
            conn.commit()

    elif count == 107: 
        char_url = 'https://legacy--api.herokuapp.com/api/v1/characters?page=3'
        species_url = 'https://legacy--api.herokuapp.com/api/v1/species?page=3'

        r = requests.get(char_url).text
        s = requests.get(species_url).text


        char_dict = json.loads(r)
        species_dict = json.loads(s)

        for i in range (10,20): 
            name = char_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (1,name))
            conn.commit()

            species = species_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (2,species))
            conn.commit()

    elif count == 127: 
        char_url = 'https://legacy--api.herokuapp.com/api/v1/characters?page=4'
        species_url = 'https://legacy--api.herokuapp.com/api/v1/species?page=4'

        r = requests.get(char_url).text
        s = requests.get(species_url).text


        char_dict = json.loads(r)
        species_dict = json.loads(s)

        for i in range (0,10): 
            name = char_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (1,name))
            conn.commit()

            species = species_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (2,species))
            conn.commit()     

    elif count == 147: 
        char_url = 'https://legacy--api.herokuapp.com/api/v1/characters?page=4'
        species_url = 'https://legacy--api.herokuapp.com/api/v1/species?page=4'

        r = requests.get(char_url).text
        s = requests.get(species_url).text


        char_dict = json.loads(r)
        species_dict = json.loads(s)

        for i in range (10,20): 
            name = char_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (1,name))
            conn.commit()

            species = species_dict[i]['name'].lower()
            conn.execute('insert into HarryPotter (term_type, term) values (?,?)', (2,species))
            conn.commit()    

    else: 
        print("Harry Potter Data Done")

def create_harry_id_table(cur, conn): 
    cur.execute('drop table if exists HarryPotterTermCategories')
    cur.execute('create table if not exists HarryPotterTermCategories(term_type int PRIMARY KEY, category TEXT)')
    conn.commit()

    conn.execute('insert into HarryPotterTermCategories (term_type, category) values (?,?)', (1, 'character'))
    conn.execute('insert into HarryPotterTermCategories (term_type, category) values (?,?)', (2, 'species'))
    conn.execute('insert into HarryPotterTermCategories (term_type, category) values (?,?)', (3, 'book title'))
    conn.commit()





