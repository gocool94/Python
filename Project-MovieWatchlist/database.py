# title ,released , watched

import datetime
import sqlite3

CREATE_TABLE_QWERY = """


CREATE TABLE IF NOT EXISTS MOVIES (

title TEXT,
release_timestamp REAL,


);
"""

CREATE_WATCHLIST_TABLE = """

CREATE TABLE IF NOT EXISTS watched (

watcher_name TEXT,
title TEXT

);

"""

INSERT_MOVIES = """

INSERT INTO MOVIES (title,release_timestamp) values (?,?);
"""
DELETE_QWERY = "delete from movies where title = ?;"


SELECT_ALL_MOVIES = "SELECT * from MOVIES;"

SELECT_UPCOMING_MOVIES = "SELECT * from MOVIES where release_timestamp > ?;"


SELECT_WATCHED_MOVIES = """select * from watched where watcher_name = ?;"""
INSERT_WATCHED_MOVIES = "insert into watched (watcher_name,title) values (?,?);"
SET_WATCHED_MOVIES = "UPDATE movies SET watched = 1 where title = ?;"



connection = sqlite3.connect("data.db") #Create a connection

def create_tables():
    with connection:
        connection.execute(CREATE_TABLE_QWERY) #perfect
        connection.execute(CREATE_WATCHLIST_TABLE)

def add_movie(title,release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES,(title,release_timestamp)) #perfect

def get_movies(upcoming=False):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        if upcoming==True:
            today_time = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES,(today_time,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)

        #print(cursor.fetchall())
        #print(cursor.fetchall())
        return cursor.fetchall()
        #return cursor.fetchall()



def watch_movies(username,title):
    with connection:
        connection.execute(DELETE_QWERY,(title,))
        connection.execute(INSERT_WATCHED_MOVIES,(username,title))

def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES,(username,))
        return cursor.fetchall()

def delete_qwery():
    with connection:
        connection.execute(DELETE_QWERY)

#UPDATE tablename SET columnname = 'value' where columname = 'sss'

#where is the necesssary to update a column so update is a important one.


