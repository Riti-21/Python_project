import os
import platform
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="mansi", database="aat", auth_plugin="mysql_native_password")
from datetime import date
import datetime
mycursor = mydb.cursor()

def manageExp(): #Function For The Expenditure Management System

        #Printing Welcome Message And options For This Program
        print(""" 

  ------------------------------------------------------
       |======== Expenditure Management =======|
  ------------------------------------------------------

Enter 1 : To Add A New Expenditure
Enter 2 : To View A Particular Expenditure & its details
Enter 3 : To View Expenditures Of A Particular Date
Enter 4 : To View Entire List Of Expenditure         
                """)

        try:
                optionInput = int(input("Please Select An Option: ")) #to take user input
        except ValueError:
                exit("\nThat Is Not A Number!!") #error
        else:
                print("\n") #new line

        #options
        if(optionInput == 1): #add new expenditure to the database
                Curdate = date.today()
                uItem = input("Enter Item: ")
                uPrice = input("Enter Price: ")
                sql1 = "INSERT INTO expn (Vardate,item,price) VALUES(%s, %s, %s)"
                vals1 = (Curdate, uItem, uPrice)
                mycursor.execute(sql1, vals1)
                mydb.commit()
                        
        elif(optionInput == 2): #search data from the database
                uItem1 = input("Enter An Item : ")
                mycursor.execute("SELECT Vardate,item,price FROM expn WHERE item=%s", (uItem1,))
                result = mycursor.fetchall()
                if result:
                        for row in result:
                                print("Date:", row[0], )
                                print("Item:", row[1], )
                                print("Price:", row[2], "\n")
                else:
                        print("No Data Found!!")

        elif (optionInput == 3):#search data from the database
                uDate = input("Enter a date(in the format YYYY-MM-DD): ")
                format = "%Y-%m-%d"
                try:
                        datetime.datetime.strptime(uDate,format)

                        mycursor.execute("SELECT Vardate,item,price FROM expn WHERE Vardate=%s", (uDate,))
                        result = mycursor.fetchall()
                        if result:
                                print()
                                print("Items Purchased On ", uDate)
                                for row in result:
                                        print("Item:", row[1], )
                                        print("Price:", row[2], "\n")
                        else:
                                print("No Data Found!!")
                except:
                        print("Incorrect Input!!")




        elif(optionInput == 4): #print list of entire expenditure
                sql2 = "SELECT * FROM expn"
                mycursor.execute(sql2)
                records = mycursor.fetchall()
                print("Entire Data:\n")
                for row in records:
                        print("Date:", row[0],)
                        print("Item:", row[1], )
                        print("Price:", row[2],"\n")
         
        elif(optionInput < 1 or optionInput > 4):
                print("Please Enter Valid Option!") #error
                                                
manageExp()

def runable(): #runable
        run = input("\nWant To Run Again ? Y/N: ")
        if(run.lower() == 'y'):
                if(platform.system() == "Windows"): #checking OS to clear screen
                        print(os.system('cls')) 
                else:
                        print(os.system('clear'))
                manageExp()
                runable()
        elif(run.lower() == 'n'):
                quit #exit

        else:
                print("Invalid Input!!") #error
                runable()
runable()