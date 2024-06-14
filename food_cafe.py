import mysql.connector
import pandas as pd
import time

print('-' * 80)
print('-' * 80)
print('\t' * 3, "Welcome to Graphic Food Cafe", '\t' * 3)
print('-' * 80)
print('-' * 80)

user = pd.read_csv('user_data.csv')

time.sleep(1)
print('+' * 30)
time.sleep(1)
print('+' * 30)

p = list(user["username"])
q = list(user["password"])

time.sleep(1)
a = int(input("Press 1 for Existing User/Press 2 for New User: "))

if a == 1:
    username = input("Enter Username: ")
    if username in p:
        index = p.index(username)
        password = input("Enter Password: ")
        if password == q[index]:
            print()
            print('+' * 30)
            print("Logged in Successfully")
            print('+' * 30)
            print("Welcome ", username.upper())
        else:
            l = input("Forgot Password Y/N: ")
            if l.upper() == "Y":
                print(user)
                new_password = input("Enter new Password: ")
                if new_password == q[index]:
                    print()
                    print('+' * 30)
                    print("Welcome ", username.upper())
                else:
                    print("Thanks for using our app")
            else:
                print("Invalid Password")
                print("Try Again")
    else:
        print("Invalid Username")
        print("Try Again")
elif a == 2:
    print("New User Registration")
    new_username = input("Enter Username: ")
    new_password = input("Create Your password: ")
    new_user = pd.DataFrame([[new_username, new_password]], columns=["username", "password"])
    user = user._append(new_user, ignore_index=True)
    user.to_csv('user_data.csv', index=False)
    #print(user)
    print()
    print('+' * 30)
    print("User Created")
    print('+' * 30)
    print("Welcome", new_username.upper())
else:
    print("Invalid Option")


conn=mysql.connector.connect(user='root',password='avantika',host='localhost',charset='utf8')
con=conn.cursor()

con.execute("drop databse id exists menu;")
con.execute("create database menu;")
con.execute("use menu;")
con.execute("create table snacks(SNACKS varchar(25),Price_in_Rs int(3));")
con.execute("insert into snacks values('Veg-Sandwich',57);")
con.execute("insert into snacks values('Idli',86);")
con.execute("insert into snacks values('Medu Vada',95);")
con.execute("insert into snacks values('Samosa',10);")
con.execute("create table beverages(BEVERAGES varchar(25),Price_in_Rs int(3));")
con.execute("insert into beverages values('Cold Drink',100);")
con.execute("insert into beverages values('Lassi',50);")
con.execute("insert into beverages values('Masala Tea',40);")
con.execute("insert into beverages values('Coffee',50);")
con.execute("create table breakfast(BREAKFAST varchar(25),Price_in_Rs int(3));")
con.execute("insert into breakfast values('Fresh Seasonal Fruits',200);")
con.execute("insert into breakfast values('Vegetable Cutlet',275);")
con.execute("insert into breakfast values('Stuffed Paratha',275);")
con.execute("insert into breakfast values('Poori Bhaji',275);")
con.execute("insert into breakfast values('Masala Dosa',275);")
con.execute("create table lunch(LUNCH varchar(25),Price_in_Rs int(3));")
con.execute("insert into lunch values('Sambar Rice',125);")
con.execute("insert into lunch values('Pan Fried Noodles',170);")
con.execute("insert into lunch values('Hakka Noodles',140);")
con.execute("insert into lunch values('Fried Rice',120);")
con.execute("insert into lunch values('Matka Biryani',150);")
con.execute("create table dinner(DINNER varchar(25),Price_in_Rs int(3));")
con.execute("insert into dinner values('Steamed Rice',150);")
con.execute("insert into dinner values('Soya Dum Biryani',300);")
con.execute("insert into dinner values('Veg-Choupsy',200);")
con.execute("insert into dinner values('Sambar Vada',170);")
con.execute("insert into dinner values('Plain Dosa',150);")
con.execute("create table dessert(DESSERT varchar(25),Price_in_Rs int(3));")
con.execute("insert into dessert values('Gulab Jamun with Rabdi',210);")
con.execute("insert into dessert values('Matka Kheer',250);")
con.execute("insert into dessert values('Paan Ice Cream',165);")
con.execute("insert into dessert values('Chocolate Gulla',180);")
con.execute("insert into dessert values('Ras Malai',100);")
con.commit()

print((" "*15)+('_'*40))
print("\t\t\t\t\t\t\t\tMENU")
print((" "*15)+('_'*40))
time.sleep(1)
print()
df1=pd.read_sql("select * from snacks;",cn)
df2=pd.read_sql("select * from beverages;",cn)
df3=pd.read_sql("select * from breakfast;",cn)
df4=pd.read_sql("select * from lunch;",cn)
df5=pd.read_sql("select * from dinner;",cn)
df6=pd.read_sql("select * from dessert;",cn)