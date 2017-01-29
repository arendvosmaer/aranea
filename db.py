#db.py

import sqlite3
import config

conn = sqlite3.connect(config.db_location)
conn.text_factory = str
cur = conn.cursor()

def tableExists(table_name, db_con):
    lower_name = table_name.lower()
    table = cur.execute(""" SELECT name 
                            FROM sqlite_master
                            WHERE type='table'
                            AND name like lower(?);
                        """, (table_name, ))
    no_of_tables = len(cur.fetchall())
    if no_of_tables == 1:
        return True
    elif no_of_tables == 0:
        return False
    else:
        print("Expected to find 1 table, found: " + str(no_of_tables))

def createTable(table_name, db_con):
    if not tableExists(table_name):
        cur.execute

def makeQueue(max_length = 10):
    cur.execute("""
        SELECT      ecli 
        FROM        Cases 
        WHERE       casetext is NULL 
        AND         error is NULL 
        OR          parsed_date < 1485725155
        ORDER BY    ecli DESC 
        LIMIT       ?
        """, (max_length, ))
    try:
        res = cur.fetchall()
        return res
    except:
        print("no new case numbers found")
        input("press enter to exit")
        exit()

pages = """
        CREATE TABLE IF NOT EXISTS CASES
        (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
        ,ECLI TEXT UNIQUE
        ,PAGE BLOB
        ,ERROR INTEGER
        ,OLD_RANK REAL
        ,NEW_RANK REAL)
        """

links = """
        CREATE TABLE IF NOT EXISTS links
        (FROM_ID INTEGER
        TO_ID INTEGER)
        """

