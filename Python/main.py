#!/bin/env python



from doctest import BLANKLINE_MARKER
import hashlib
from termcolor import colored
from os.path import exists
import sys
import chardet


# open wordlist
def read_wordlist(wordlist_name):
    wordlist = []
    raw_woldlist = open(wordlist_name,'r', encoding="utf8", errors='ignore')
    read_wordlist = raw_woldlist.readlines()
    e_list = []
    e_list =  [encode_wordlist.encode('utf-8') for encode_wordlist in read_wordlist]
    return e_list

#create rainbow table
def create_r_table():
    wordlist_path = sys.argv[2]
    hash_type = sys.argv[3]
    if exists(wordlist_path) and hash_type:
        x = read_wordlist(wordlist_path)
        print('\n')
        for line in x:
            line = line.rstrip()
            h = hashlib.new(hash_type)
            #line = chardet.detect(line)['encoding']               ###########################
            #line = line.encode('utf-8')
            
            h.update(line)
            line_hashed = h.hexdigest()
            r_table = open('rainbow_table.txt','a')
            line = line.decode('utf-8')
            print(line_hashed +' : '+ line )
            r_table.write(line_hashed + ' : ' + line + '\n' )
        r_table.close()
        print('\nDone')
    else:
        print('\nWordlist doesn\'t exist')
        exit()

def read_r_table(rainbow_table_path,hash):
    print('\n- Wait a one year ¯\_(ツ)_/ \n')
    r_table = open(rainbow_table_path,'r')
    rainbow_table = r_table.readlines()
    for raw_line in rainbow_table:
        line = raw_line.replace('\n','')
        if hash in line :
            print('- Or not ¯\_(ツ)_/   =====> '+colored(line,'red'))
            print(' (・3・) Tank you for using Y_oss tools ')
            exit()
            
        
        
        
        


#find hash
def find():
    hash = sys.argv[3]
    rambow_table_path = sys.argv[2]
    if exists(rambow_table_path):
        read_r_table(rambow_table_path,hash)
    else:
        print('\nWordlist doesn\'t exist')
        exit()
    

                                            # https://github.com/BouchmamaYoussef
                                            # https://twitter.com/y_oss1


def main():
    banner = '''

 $$$$$$\          $$\     $$\                                 
$$  __$$\         \$$\   $$  |                                
$$ /  $$ |$$\   $$\\$$\ $$  /    $$$$$$\   $$$$$$$\  $$$$$$$\ 
$$ |  $$ |\$$\ $$  |\$$$$  /    $$  __$$\ $$  _____|$$  _____|
$$ |  $$ | \$$$$  /  \$$  /     $$ /  $$ |\$$$$$$\  \$$$$$$\  
$$ |  $$ | $$  $$<    $$ |      $$ |  $$ | \____$$\  \____$$\ 
 $$$$$$  |$$  /\$$\   $$ |      \$$$$$$  |$$$$$$$  |$$$$$$$  |
 \______/ \__/  \__|  \__|$$$$$$\\______/ \_______/ \_______/ 
                          \______|                            
                                                                                                                                
                                            https://github.com/BouchmamaYoussef
                                            https://twitter.com/y_oss1
'''
    print(banner)
    help = 'usage :\n\n'+sys.argv[0]+' create < Wordlist.txt > < Hash name >\n\n'+sys.argv[0]+' find < rambow_table.txt > < Hash >'
    if (len(sys.argv)) <= 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help' :
        print(help)
        exit()
    elif 'create' in sys.argv :
        if 4 <= len(sys.argv) :
            create_r_table()
        else :
            print(help)
    elif 'find' in sys.argv :
        if 4 <= len(sys.argv) :
            find()
        else :
            print(help)
    else : 
        print(help)

    




main()









