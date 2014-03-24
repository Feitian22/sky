#!/usr/bin/env python
# Filename: addressbook.py

import datetime
import MySQLdb
from config.config import database

# Connect to DB
try:
     host, user, passwd, db, charset = database
     conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, charset=charset)
     db_action = conn.cursor()  
except:
     print 'Connect to Mysql error...'

# Function
def input_infor():
    name = raw_input('Please input your name :')
    sex = input('Please input your sex :')
    tel = raw_input('Please input your phone :')
    bir = raw_input('Please input your birthday :')
    all = (name, sex, tel, bir)
    print all
    db_action.execute('insert into txl (name, sex, tel, birthday) values(%s, %s, %s, %s)', all)

def select_name():
    choice = raw_input('Please input your choice: ') 
    db_action.execute("select * from txl where name = %s", choice) 
    print 'Row_No.\t\t\Name\t\t\Sex\t\tTelephone\t\tBirthday'
    print db_action.fetchall()

def select_phone():
    phone = raw_input('Please input phone number: ')
    db_action.execute('select * from txl where tel = %s', phone)
    print 'Row_no.\tName\t\Sex\Telephone\tBirthday'
    print db_action.fetchall()
    
    
def logout():
    db_action.close()
    conn.commit()
    conn.close()
    exit()
    
# main
while True:
    msg = '''
        ##################################
        #       Welcome to Mysql         #
        #         L   Exit               #
        #         A   Add                #
        #         N   Select name        #
        #         P   Select phone       #
        #         D   Dispaly all        #
        #         R   Remove record      #
        ##################################
    '''
    print msg
    option = {'A': add_book, 'N': select_name, 'P': select_phone, 'L': logout, 'D': display_all ,'R': delete_record}
    option_list = raw_input('Please select your operation: ')
    option[option_list]()
