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
print("List of Users")
print('+'*30)
time.sleep(1)
print(user["username"])
print('+'*30)

p=list(user["username"])
q=list(user["password"])
time.sleep(1)
a=int(input("Press 1 for Existing User/Press 2 for New User: "))
if a==1:
    Username=input("Enter Username: ")
    if Username in p:
        for o in range (len(p)):
            if Username==p[o]:
                Password=input("Enter Password: ")
                for u in range (len(q)):
                    if Password==q[u]:
                        print('+'*30)
                        print("Logged in Succesfully")
                        print('+'*30)
                        print("Welcome ",Username)
                        break
                    elif Password!=q[u]:
                        continue
                else:
                    
                    l=input("Forgot Password Y/N: ")
                    if l == "Y":
                        print(user)
                        Pass = int(input("Enter PASSWORD: "))
                        for w in range(len(q)):
                            if Pass == q[w]:
                                print()
                                print('+' * 30)
                                print("Welcome", Username)
                            else:
                                print()
                                print('+' * 30)
                                print("THANKS FOR USING OUR APP")
                        else:
                                print("THANKS FOR USING OUR APP")
                                break