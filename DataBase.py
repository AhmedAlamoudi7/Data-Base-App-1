
# -----------------------------------------------------
# -- Databases => SQLite => Create App  Part 1 --
# -----------------------------------------------------
import webbrowser
import termcolor
import pyfiglet

import sqlite3
print(termcolor.colored(pyfiglet.figlet_format("Soon Ahmed"), color='green'))
result = termcolor.colored(pyfiglet.figlet_format(
    "Keek", font="isometric1"), color='red')
print(result)


# Input Big Message
input_message = """
What Do You Want To Do ?
"s" => Show All information
"a" => Add New Information
"d" => Delete items in DataBase
"u" => Update itemes in DataBase
"q" => Quit The App
"""
## show Orders
print(input_message)
## Enter order
input_order = str(input("choose option: ")).strip()
## connect to DataBase
db = sqlite3.connect(r"C:\Users\khatib\Desktop\DB\app.db")
cr = db.cursor()
## function to do orders


def orders():
    ## Order to Show All itemes
    if input_order == "s":

        type_table = input("(Users || Skills)")
        ##Show All itemes in Skills
        if type_table == "skills":
            # Fetch Data From Database
         cr.execute(
             "create table if not exists skills (user_id integer, name text,progress integer)")
         cr.execute("select * from skills")

         # loop to  show all
         results = cr.fetchall()
         for row in results:
            print(f"name -> {row[0]},", end=" || ")
            print(f"progress -> {row[1]}", end=" || ")
            print(f"id user -> {row[2]}")
         print("Show All Successfully❤❤")
        elif type_table == "users":
            cr.execute("select * from users")
            # show all
            results = cr.fetchall()
            for row in results:
                print(f"user id -> {row[0]},", end=" || ")
                print(f"user name -> {row[1]}")

            print("Show All Users Succesfully❤❤")

     ##Order to  add to Db into Skills
    if input_order == "a":
         number_input = int(input("enter number input items? ".strip()))
         for num in range(number_input):
             name = str(input("name : ")).strip()
             progress = int(input("progress: "))
             user_id = int(input("user id : "))
             cr.execute(
                 "INSERT INTO skills (user_id , name ,progress) VALUES(?, ?, ?)", (user_id, name, progress))
             db.commit()

     ##Order to Delete items formm DataBAse
    if input_order == "d":
        Stop = ""
        ## while stop !=s continue
        while Stop != "s":
          type_table = str(input("Enter table name (Users ||Skills)"))
          ## Delete items formm users
          if type_table == "users":
            user = input("enter user id ? ")
            cr.execute(f"delete from users where user_id={user}")
            print("Deleteing form DataBase successfully❤❤ ")
          ## Delete items formm Skills
          elif type_table == "skills":
            user1 = input("enter user name ? ")
            cr.execute(f"delete from skills where name='{user1}'")
            print("Deleteing form DataBase successfully❤❤ ")
          db.commit()
          Stop = input("to Stop enter S")
        else:
            print("erorr input😒")
     ## Order to to update itemes from DataBase
    if input_order == "u":
         Stop = ""
        ## while stop !=s continue
         while Stop != "s":
           type_table = str(input("Enter table name (Users ||Skills)"))
           ## update items formm users
           if type_table == "users":
               user_Name = input("Enter user name ? ")
               user_Id = input("Enter user id")
               cr.execute(
                   f"update users set name='{user_Name}' where user_id ={user_Id} ")
               print("updating to DataBase Successfully❤❤")

           ## update items formm skills
           if type_table == "skills":
               user_Name = input("Enter user name ? ")
               user_Id = input("Enter user id")
               progress_ID = input("enter progress? ")
               cr.execute(
                   f"update skills set name='{user_Name}' where user_id ={user_Id} ")
               cr.execute(
                   f"update skills set progress='{progress_ID}' where user_id ={user_Id}")
               print("updating to DataBase Successfully❤❤")
           db.commit()
           Stop = input("to Stop enter S")
         else:
            print("erorr input😒")
      ## last order Closed The App
    if input_order == "q":
         db.commit()
         db.close()
         print("Closed The App successfully ❤❤")


orders()
print("🤞"*40)
print("--------Made By Love---------")
print("🤞"*40)
