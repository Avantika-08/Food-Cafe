import mysql.connector
import pandas as pd
import time

print('-'*80)
print('-'*80)
print('\t'*3,"Welcome to Graphic Food Cafe",'\t'*3)
print('-'*80)
print('-'*80)

user=pd.read_csv('user_data.csv')

time.sleep(1)
##print("List of Users")
print('+'*30)
time.sleep(1)
##print(user["username"])
print('+'*30)

p=list(user["username"])
q=list(user["password"])
time.sleep(1)
a=int(input("Press 1 for Existing User/Press 2 for New User: "))
if a == 1:
    username = input("Enter Username: ")
    if username in p:
        password = input("Enter Password: ")
        if password in q:
            print('+' * 30)
            print("Logged in Successfully")
            print('+' * 30)
            print("Welcome", username)
        else:
            l = input("Forgot Password Y/N: ")
            if l == "Y":
                #print(p)
                new_password = input("Enter new PASSWORD: ")
                if new_password in q:
                    print('+' * 30)
                    print("Welcome", username)
                else:
                    print('+' * 30)
                    print("THANKS FOR USING OUR APP")
            else:
                print("INVALID USERNAME")
                print("TRY AGAIN")
    else:
        print("Username not found. Please try again.")
