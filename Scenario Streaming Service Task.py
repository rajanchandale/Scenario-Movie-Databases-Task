#Scenario Streaming Service Task

#Libraries
import sqlite3
import random
import sys
import re

#Classes
class Users:
     def __init__(self, username,password,confPassword,firstName,surname,address,DOB,gender,interests,last_films,fav_actor,fav_film):#Constructor
          self.username = username
          self.password = password
          self.confPassword = confPassword
          self.firstName = firstName
          self.surname = surname
          self.address = address
          self.DOB = DOB
          self.gender = gender
          self.interests = interests
          self.interest1 = self.interests[0]
          self.interest2 = self.interests[1]
          self.interest3 = self.interests[2]
          self.last_films = last_films
          self.last_film1 = self.last_films[0]
          self.last_film2 = self.last_films[1]
          self.last_film3 = self.last_films[2]
          self.last_film4 = self.last_films[3]
          self.last_film5 = self.last_films[4]
          self.last_film6 = self.last_films[5]
          self.last_film7 = self.last_films[6]
          self.last_film8 = self.last_films[7]
          self.last_film9 = self.last_films[8]
          self.last_film10 = self.last_films[9]
          self.fav_actor = fav_actor
          self.fav_film = fav_film
          #This defines all of the attributes for the objects of the 'users' class

     def ContSign_up(self):
          last_films = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
          details = Users(username,password,confPassword,firstName,surname,address,DOB,gender,interests,last_films," "," ")
          details.insert_table()#calls insert table procedure to enter all data in db 
          self.create_user_liked_table()#creates a table for each user to store liked movies
          login()
          #This Is The Second Half Of The Sign Up Subroutine
          #I Split The Subroutine Into The One Part Which Does Not Require OOP, And This Continued Half Which Makes Use Of OOP


     def contLogin(self):
          #Split Function into areas which require OOP and other ares which don't require OOP
          user_database = sqlite3.connect("User Databases.db")
          c = user_database.cursor()
          c.execute('''SELECT * FROM Users WHERE Username = ?''',(username,))
          fetched = c.fetchall()#Fetches all stored data for the user which has just logged in

          genre = [fetched[0][7],fetched[0][8],fetched[0][9]]
          films = [fetched[0][10],fetched[0][11],fetched[0][12],fetched[0][13],fetched[0][14],fetched[0][15],fetched[0][16],fetched[0][17],fetched[0][18],fetched[0][19]]
                    
          globals()[username] = Users(fetched[0][0],fetched[0][1],fetched[0][1],fetched[0][2],fetched[0][3],fetched[0][4],fetched[0][5],fetched[0][6],genre,films,fetched[0][20],fetched[0][21])
          #Creates user as temporary object whilst they are signed in
          #globals()[username] turns the value of a variable into the name of the variable
          #therefore I can use each user's username as their temporary object name 
          user_database.commit()
          user_database.close()

          self.Homepage()#Loads homepage
          

     def insert_table(self):
          user_database = sqlite3.connect("User Databases.db")
          c = user_database.cursor()
          c.execute('''INSERT INTO Users VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(self.username,self.password,self.firstName,self.surname,self.address,self.DOB,self.gender,self.interest1,self.interest2,self.interest3,self.last_film1,self.last_film2,self.last_film3,self.last_film4,self.last_film5,self.last_film6,self.last_film7,self.last_film8,self.last_film9,self.last_film10,self.fav_actor,self.fav_film))

          user_database.commit()
          user_database.close()

     def create_user_liked_table(self):
          user_database = sqlite3.connect("User Likes.db")
          c = user_database.cursor()
          c.execute('''CREATE TABLE %s (Film_ID text,Film_Name text,Liked integer)'''%(self.username))#creates a table of all liked films for the user

          user_database.commit()
          user_database.close()#Creates table to store a list of liked movies for the user
          #%s allows the table name to be the username of the current user
          #meaning each table will have a unique name as two users cannot have the same username (PK for each user)
               
     def random_movies(self):
          #This Method returns 5 randomly generated movies based on the 3 genres which the user expressed interest in during their sign up process
          if self.interest1 == "2" or self.interest2 == "2" or self.interest3 == "2":
               Vars = random.sample(range(1,10),5)
               var1 = Vars[0]
               var2 = Vars[1]
               var3 = Vars[2]
               var4 = Vars[3]
               var5 = Vars[4]
               #Generates 5 distinct random numbers which can be used to correspond with the record number of 5 movies from the db
               #Thus, the movies are randomly selected
               
               movie_database = sqlite3.connect("Movies.db")
               c = movie_database.cursor()

               c.execute('''SELECT Film_Name FROM Action_Films WHERE ActRecord_Number IN (?,?)''',(var1,var2))
               act1 = c.fetchall()
               c.execute('''SELECT ActRecord_Number FROM Action_Films WHERE ActRecord_Number IN (?,?)''',(var1,var2))
               actNum = c.fetchall()

               c.execute('''SELECT Film_Name FROM Action_Films WHERE ActRecord_Number IN (?,?)''',(var3,var4))
               act2 = c.fetchall()
               c.execute('''SELECT ActRecord_Number FROM Action_Films WHERE ActRecord_Number IN (?,?)''',(var3,var4)) 
               actNum2 = c.fetchall()
               
               c.execute('''SELECT Film_Name FROM Action_Films WHERE ActRecord_Number = ?''',(var5,))
               act3 = c.fetchall()
               c.execute('''SELECT ActRecord_Number FROM Action_Films WHERE ActRecord_Number = ?''',(var5,))
               actNum3 = c.fetchall()

               print("Movies For Action Lovers: ", "                                                                                                                 **")
               print(actNum[0][0],".",act1[0][0],"|",actNum[1][0],".",act1[1][0],"|",actNum2[0][0],".",act2[0][0],"|",actNum2[1][0],".",act2[1][0],"|",actNum3[0][0],".",act3[0][0])
               print("**                                                                                                                                          **")
               #Returns the Movies
               
               movie_database.commit()
               movie_database.close()

          if self.interest1 == "3" or self.interest2 == "3" or self.interest3 == "3":#Same as above except for animated movies
               numbers = random.sample(range(11,20),5)
               number1 = numbers[0]
               number2 = numbers[1]
               number3 = numbers[2]
               number4 = numbers[3]
               number5 = numbers[4]

               movie_database = sqlite3.connect("Movies.db")
               c = movie_database.cursor()

               c.execute('''SELECT Film_Name FROM Animated_Films WHERE AniRecord_Number IN (?,?)''',(number1,number2))
               ani1 = c.fetchall()
               c.execute('''SELECT AniRecord_Number FROM Animated_Films WHERE AniRecord_Number IN (?,?)''',(number1,number2))
               aniNum = c.fetchall()

               c.execute('''SELECT Film_Name FROM Animated_Films WHERE AniRecord_Number IN (?,?)''',(number3,number4))
               ani2 = c.fetchall()
               c.execute('''SELECT AniRecord_Number FROM Animated_Films WHERE AniRecord_Number IN (?,?)''',(number3,number4))
               aniNum2 = c.fetchall()

               c.execute('''SELECT Film_Name FROM Animated_Films WHERE AniRecord_Number = ?''',(number5,))
               ani3 = c.fetchall()
               c.execute('''SELECT AniRecord_Number FROM Animated_Films WHERE AniRecord_Number = ?''',(number5,))
               aniNum3 = c.fetchall()

               print("Animated Movies For Your Inner-Child: ")
               print(aniNum[0][0],".",ani1[0][0],"|",aniNum[1][0],".",ani1[1][0],"|",aniNum2[0][0],".",ani2[0][0],"|",aniNum2[1][0],".",ani2[1][0],"|",aniNum3[0][0],".",ani3[0][0])
               print("**                                                                                                                                          **")

               movie_database.commit()
               movie_database.close()

          if self.interest1 == "1" or self.interest2 == "1" or self.interest3 == "1":#Selecting 5 Comedy Movies
               nums = random.sample(range(21,30),5)#Generates 5 random non-duplicate numbers between 1 and 10
               num1 = nums[0]
               num2 = nums[1]
               num3 = nums[2]
               num4 = nums[3]
               num5 = nums[4]

               movie_database = sqlite3.connect("Movies.db")
               c = movie_database.cursor()

               c.execute('''SELECT Film_Name FROM Comedy_Films WHERE ComRecord_Number IN (?,?)''',(num1,num2))#IN function only allows 2 search conditions at a time
               fetched1 = c.fetchall()
               c.execute('''SELECT ComRecord_Number FROM Comedy_Films WHERE ComRecord_Number IN (?,?)''',(num1,num2))
               comNum = c.fetchall()

               c.execute('''SELECT Film_Name FROM Comedy_Films WHERE ComRecord_Number IN (?,?)''',(num3,num4))#5 movies chosen which correspond to random nums
               fetched2 = c.fetchall()
               c.execute('''SELECT ComRecord_Number FROM Comedy_Films WHERE ComRecord_Number IN (?,?)''',(num3,num4))
               comNum2 = c.fetchall()

               c.execute('''SELECT Film_Name FROM Comedy_Films WHERE ComRecord_Number = ?''',(num5,))#chosen through 3 SQL statements
               fetched3 = c.fetchall()
               c.execute('''SELECT ComRecord_Number FROM Comedy_Films WHERE ComRecord_Number = ?''',(num5,))
               comNum3 = c.fetchall()

               movie_database.commit()
               movie_database.close()
               
               print("Comedy Movies To Tickle Your Funny Bone: ")
               print(comNum[0][0],".",fetched1[0][0],"|",comNum[1][0],".",fetched1[1][0],"|",comNum2[0][0],".",fetched2[0][0],"|",comNum2[1][0],".",fetched2[1][0],"|",comNum3[0][0],".",fetched3[0][0])#outputs 5 comedy movies to the user 
               print("**                                                                                                                                          **")
                     

          if self.interest1 == "4" or self.interest2 == "4" or self.interest3 == "4":#5 random SciFi Movies
               variables = random.sample(range(31,40),5)
               variable1 = variables[0]
               variable2 = variables[1]
               variable3 = variables[2]
               variable4 = variables[3]
               variable5 = variables[4]

               movie_database = sqlite3.connect("Movies.db")
               c = movie_database.cursor()

               c.execute('''SELECT Film_Name FROM SciFi_Films WHERE SciRecord_Number IN (?,?)''',(variable1,variable2))
               sf1 = c.fetchall()
               c.execute('''SELECT SciRecord_Number FROM SciFi_Films WHERE SciREcord_Number IN (?,?)''',(variable1,variable2))
               sciNum = c.fetchall()

               c.execute('''SELECT Film_Name FROM SciFi_Films WHERE SciRecord_Number IN (?,?)''',(variable3,variable4))
               sf2 = c.fetchall()
               c.execute('''SELECT SciRecord_Number FROM SciFi_Films WHERE SciRecord_Number IN (?,?)''',(variable3,variable4))
               sciNum2 = c.fetchall()

               c.execute('''SELECT Film_Name FROM SciFi_Films WHERE SciRecord_Number = ?''',(variable5,))
               sf3 = c.fetchall()
               c.execute('''SELECT SciRecord_Number FROM SciFi_Films WHERE SciRecord_Number = ?''',(variable5,))
               sciNum3 = c.fetchall()

               print("Sci-Fi Movies For Our Valued Geeks: ")
               print(sciNum[0][0],".",sf1[0][0],"|",sciNum[1][0],".",sf1[1][0],"|",sciNum2[0][0],".",sf2[0][0],"|",sciNum2[1][0],".",sf2[1][0],"|",sciNum3[0][0],".",sf3[0][0])
               print("**                                                                                                                                          **")
               
               movie_database.commit()
               movie_database.close()

     def updating_last_ten_movies(self,latest_movie):#Updates the list of last ten movies viewed by the user

          user_database = sqlite3.connect("User Databases.db")
          c = user_database.cursor()

          c.execute('''SELECT Last_Film1,Last_Film2,Last_Film3,Last_Film4,Last_Film5,Last_Film6,Last_Film7,Last_Film8,Last_Film9,Last_Film10 FROM Users WHERE Username = ?''',(self.username,))
          films = c.fetchall()
          
          c.execute('''UPDATE Users SET Last_Film2 = ?,Last_Film3 = ?,Last_Film4 = ?,Last_Film5 = ?,Last_Film6 = ?,Last_Film7 = ?,Last_Film8 = ?,Last_Film9 = ?,Last_Film10 = ? WHERE Username = ?''',(films[0][0],films[0][1],films[0][2],films[0][3],films[0][4],films[0][5],films[0][6],films[0][7],films[0][8],self.username))

          c.execute('''UPDATE Users SET Last_Film1 = ? WHERE Username = ?''',(latest_movie,self.username))
          #Logic: All the films are shifted one place to the right on the list (position 1 becomes position 2 etc)
          #We are then left with [0] & [1] holding the same value. Effectively [0] is empty as the previous value of [0] has a new position
          #Position Number 10 is consequently removed from the list
          #We can then replace [0] with the last viewed movie of the user
          
          user_database.commit()
          user_database.close()

     def viewing_last_ten_movies(self):

          user_database = sqlite3.connect("User Databases.db")

          c = user_database.cursor()
          c.execute('''SELECT Last_Film1,Last_Film2,Last_Film3,Last_Film4,Last_Film5,Last_Film6,Last_Film7,Last_Film8,Last_Film9,Last_Film10 FROM Users WHERE Username = ?''',(self.username,))
          
          films = c.fetchall()
          user_database.commit()
          user_database.close()

          print("Recently Viewed Movies: ")
          print("= = = = = = = = = = = = =")
          print(films[0][0],"|",films[0][1],"|",films[0][2],"|",films[0][3],"|",films[0][4])
          print(films[0][5],"|",films[0][6],"|",films[0][7],"|",films[0][8],"|",films[0][9])
          #This simply returns the list of the last ten movies
     

     def searchWebsite(self):#This gives the user the ability to search the website for movies
          print("SEARCH SCENARIO! MOVIES. ENTER MOVIE NAME: ")
          print("*****************************************  ")
          movieName = str(input("SEARCH: "))
    
          movies_database = sqlite3.connect("Movies.db")

          c = movies_database.cursor()
          c.execute('''SELECT Film_Name,ActRecord_Number FROM Action_Films WHERE Film_Name LIKE '%%{a}%%' '''.format(a = movieName))
          #searches the movie db for all records which are like the user input
          #First looks in the action films table
          fetched = list(c.fetchall())
          finalSearched = []
          
          if fetched != []:
               if (len(fetched)) == 1:
                    actSearched = []
                    count = 0
                    for i in range(len(fetched[0])):
                         actSearched.append(fetched[0][count])
                         count += 1
                         #appends each record to a new list one by one

                    count = 1
                    count2 = 0
                    length = int((len(actSearched)) / 2)
                                   
                    for i in range(length):
                         finalSearched.append(actSearched[count])
                         finalSearched.append(actSearched[count-1])
                         count += 1
                         #finalSearched is a list which consists of the movies found from all four searches of the four tables
               elif (len(fetched)) > 1:
                    actSearched = []
                    count = 0
                    for i in range(len(fetched[0])):
                         actSearched.append(fetched[count])
                         count += 1
                         
                    count = 1
                    count2 = 0
                    length = int((len(actSearched)))
                                   
                    for i in range(length):
                         finalSearched.append(actSearched[count2][count])
                         finalSearched.append(actSearched[count2][count-1])
                         count2 += 1
                    #It must be appended differently depending how many movies are found which meet requirements
                              
          movies_database = sqlite3.connect("Movies.db")
          c = movies_database.cursor()
          c.execute('''SELECT Film_Name,AniRecord_Number FROM Animated_Films WHERE Film_Name LIKE '%%{a}%%' '''.format(a = movieName))
          fetched2 = list(c.fetchall())
          #The same as above, except now we are searching through the animated films table

          if fetched2 != []:
               if (len(fetched2)) == 1:
                    aniSearched = []
                    count = 0
                    for i in range(len(fetched2[0])):
                         aniSearched.append(fetched2[0][count])
                         count += 1
                         
                    count = 1
                    count2 = 0
                    length = int((len(aniSearched)) / 2)                                   
                                   
                    for i in range(length):
                         finalSearched.append(aniSearched[count])
                         finalSearched.append(aniSearched[count-1])
                         count += 1

               elif (len(fetched2)) > 1:
                    aniSearched = []
                    count = 0
                    for i in range(len(fetched2[0])):
                         aniSearched.append(fetched2[count])
                         count += 1
                         
                    count = 1
                    count2 = 0
                    length = int((len(aniSearched)))
                                   
                    for i in range(length):
                         finalSearched.append(aniSearched[count2][count])
                         finalSearched.append(aniSearched[count2][count-1])
                         count2 += 1
      
          movies_database = sqlite3.connect("Movies.db")
          c = movies_database.cursor()
          c.execute('''SELECT Film_Name,ComRecord_Number FROM Comedy_Films WHERE Film_Name LIKE '%%{a}%%' '''.format(a = movieName))
          fetched3 = list(c.fetchall())
          #Searching through comedy films

          if fetched3 != []:
               if (len(fetched3)) == 1:
                    comSearched = []
                    count = 0
                    for i in range(len(fetched3[0])):
                         comSearched.append(fetched3[0][count])
                         count += 1

                    count = 1
                    count2 = 0
                    length = int((len(comSearched)) / 2)                                   
                                   
                    for i in range(length):
                         finalSearched.append(comSearched[count])
                         finalSearched.append(comSearched[count-1])
                         count += 1
     
               elif (len(fetched3)) > 1:
                    comSearched = []
                    count = 0
                    for i in range(len(fetched3[0])):
                         comSearched.append(fetched3[count])
                         count += 1
                         
                    count = 1
                    count2 = 0
                    length = int((len(comSearched)))
                                   
                    for i in range(length):
                         finalSearched.append(comSearched[count2][count])
                         finalSearched.append(comSearched[count2][count-1])
                         count2 += 1
                              

          movies_database = sqlite3.connect("Movies.db")
          c = movies_database.cursor()
          c.execute('''SELECT Film_Name,SciRecord_Number FROM SciFi_Films WHERE Film_Name LIKE '%%{a}%%' '''.format(a = movieName))
          fetched4 = list(c.fetchall())
          #searching through sci fi films
          
          if fetched4 != [] :
               if (len(fetched4)) == 1:
                    sciSearched = []
                    count = 0
                    for i in range(len(fetched4[0])):
                         sciSearched.append(fetched4[0][count])
                         count += 1
                         
                    count = 1
                    count2 = 0
                    length = int((len(sciSearched)) / 2)                                   
                                   
                    for i in range(length):
                         finalSearched.append(sciSearched[count])
                         finalSearched.append(sciSearched[count-1])
                         count += 1

               elif(len(fetched4)) > 1:
                    sciSearched = []
                    count = 0
                    for i in range(len(fetched4[0])):
                         sciSearched.append(fetched4[count])
                         count += 1
                         
                    count = 1
                    count2 = 0
                    length = int((len(sciSearched)))
                                   
                    for i in range(length):
                         finalSearched.append(sciSearched[count2][count])
                         finalSearched.append(sciSearched[count2][count-1])
                         count2 += 1
     
          
          if finalSearched == []:
               print("A Search Of Scenario! Movies Found No Results.")
               print("Relocating To Homepage...")
               self.Homepage()
               #if the accumulation of all four searches returns nothing, then the movie is not available in my db


          elif finalSearched != []:
               if (len(finalSearched)) == 1:
                    print("Search Results: ")
                    print("= = = = = = = = =")
                    count = 1
                    count2 = 0
                    length = int((len(finalSearched)) / 2)

                    for i in range(length):
                         print(finalSearched[count],".",sciSearched[count-1])

               elif (len(finalSearched)) > 1:
                    print("Search Results: ")
                    print("= = = = = = = = =")
                    count = 1
                    count2 = 0
                    length = int((len(finalSearched)) / 2)

                    for i in range(length):
                         print(finalSearched[count2],".",finalSearched[count2+1])
                         count2 += 2
               #outputs the returned values from the search of the db 

               movieNum = int(input("Enter The Corresponding Number To The Movie You Wish To Watch: \n"))
               #Allows the user to pick which movie they wish to view from the returned list

               if movieNum >= 1 and movieNum <= 10:
                    movies_database = sqlite3.connect("Movies.db")
                    c = movies_database.cursor()
                    c.execute('''SELECT Film_Name FROM Action_Films WHERE ActRecord_Number = ?''',(movieNum,))

                    returned = c.fetchall()

                    movies_database.commit()
                    movies_database.close()

                    self.updating_last_ten_movies(returned[0][0])
                    self.Action_MovieDisplay(movieNum)
                    #Determines which type of movie display to output
                    #This can be determined by the range which the number falls into 


               elif movieNum >= 11 and movieNum <= 20:
                    movies_database = sqlite3.connect("Movies.db")
                    c = movies_database.cursor()
                    c.execute('''SELECT Film_Name FROM Animated_Films WHERE AniRecord_Number = ?''',(movieNum,))

                    returned = c.fetchall()
                    
                    movies_database.commit()
                    movies_database.close()

                    self.updating_last_ten_movies(returned[0][0])
                    self.Animated_MovieDisplay(movieNum)

               elif movieNum >= 21 and movieNum <= 30:
                    movies_database = sqlite3.connect("Movies.db")
                    c = movies_database.cursor()
                    c.execute('''SELECT Film_Name FROM Comedy_Films WHERE ComRecord_Number = ?''',(movieNum,))

                    returned = c.fetchall()

                    movies_database.commit()
                    movies_database.close()

                    self.updating_last_ten_movies(returned[0][0])
                    self.Comedy_MovieDisplay(movieNum)

               elif movieNum >= 31 and movieNum <= 40:
                    movies_database = sqlite3.connect("Movies.db")
                    c = movies_database.cursor()
                    c.execute('''SELECT Film_Name FROM SciFi_Films WHERE SciRecord_Number = ?''',(movieNum,))

                    returned = c.fetchall()

                    movies_database.commit()
                    movies_database.close()

                    self.updating_last_ten_movies(returned[0][0])
                    self.SciFi_MovieDisplay(movieNum)

               elif movieNum < 1 or movieNum > 40:
                    print("Invalid Input: Out Of Range.")
                    print("Relocating To Homepage...")
                    self.Homepage()

               

     def signOut(self):
          print("ARE YOU SURE YOU WOULD LIKE TO SIGN OUT OF %s"%(self.username))
          decision = input("Enter 'Y' To Sign Out Or Enter 'N' To Return To The Homepage \n").upper()
          x = False
          while x == False:
               if decision == "Y":
                    print("Signed Out...")
                    x = True
                    exit()

               if decision == "N":
                    print("Relocating To Homepage ...")
                    self.Homepage()
                    x = True
               else:
                    x = False
          #A method which allows the user to sign out and exit the program 


     def viewAccountDetails(self):
          movies_database = sqlite3.connect("User Databases.db")
          
          c = movies_database.cursor()
          c.execute('''SELECT * FROM Users WHERE Username = ?''',(self.username,))

          accDetails = c.fetchall()
          print("\n\n")
          print(" Account Details")
          print("*****************")
          print("\n")
          print("1. Username: ", accDetails[0][0])
          print("2. Password: ", accDetails[0][1])
          print("3. Firstname: ", accDetails[0][2])
          print("4. Surname: ", accDetails[0][3])
          print("5. Address: ", accDetails[0][4])
          print("6. DOB: ", accDetails[0][5])
          print("7. Gender: ", accDetails[0][6])
          #Returns the stored account details 

          decision = 0
          while decision != 8:
               decision = int(input("If There Are Any Details You Would Like To Change, Please Press The Corresponing Number To Change That Detail. If You Do Not Want Change Any Details Enter '8' \n"))
               print("NOTE: You Cannot Change Username")
               #username cannot be changed as it is the PK for that user
               #The below statements allow the user to change any details they wish 
               if decision == 2:
                    x = False
                    while x == False:
                         newPassword = input("Enter New Password: ")
                         newConfPassword = input("Re-Enter New Password: ")
                    #Password Check
                         count = 0
                         samepwCheck = False
                         numberCheck = False
                         upperCheck = False
          
                         if newPassword == newConfPassword:
                              samepwCheck = True

                         for count in range(len(password)):
                              if password[count].isdigit():
                                   numberCheck = True
                              if password[count].isupper():
                                   upperCheck = True

                              count += 1
                    

                         if (samepwCheck == True) and (numberCheck == True) and (upperCheck == True):
                              x = True

                         elif samepwCheck == False:
                              print("\n Your Passwords Did Not Match \n")
                              x = False

                         elif numberCheck == False:
                              print("\n Your Password Must Contain At Least One Number \n")
                              x = False

                         elif upperCheck == False:
                              print("\n Your Password Must Contain At Least One Uppercase Character \n")
                              x = False

                    #End Of Password Check
                              
               elif decision == 3:
                    newFirstName = input("Enter First Name: ").upper()

                    user_database = sqlite3.connect("User Databases.db")
                    c = user_database.cursor()

                    c.execute('''UPDATE Users SET Firstname = ? WHERE Username = ?''',(newFirstName,self.username))

                    user_database.commit()
                    user_database.close()
                    print("First Name Changed To: ",newFirstName)

               elif decision == 4:
                    newSurname = input("Enter Surname: ").upper()

                    user_database = sqlite3.connect("User Databases.db")
                    c = user_database.cursor()

                    c.execute('''UPDATE Users SET Surname = ? WHERE Username = ?''',(newSurname,self.username))

                    user_database.commit()
                    user_database.close()

               elif decision == 5:
                    newAddress = input("Enter Address: ")

                    user_database = sqlite3.connect("User Databases.db")
                    c = user_database.cursor()

                    c.execute('''UPDATE Users SET Address = ? WHERE Username = ?''',(newAddress,self.username))

                    user_database.commit()
                    user_database.close()

               elif decision == 6:
                    newDOB = input("Enter New Date Of Birth: (DD/MM/YYYY)")

                    user_database = sqlite3.connect("User Databases.db")
                    c = user_database.cursor()

                    c.execute('''UPDATE Users SET Date Of Birth = ? WHERE Username = ?''',(newDOB,self.username))

                    user_database.commit()
                    user_database.close()

               elif decision == 7:
                    newGender = input("Enter New Gender: ('M' = Male, 'F' = Female, 'O' = Other)").upper()

                    user_database = sqlite3.connect("User Databases.db")
                    c = user_database.cursor()

                    c.execute('''UPDATE Users SET Gender = ? WHERE Username = ?''',(newGender,self.username))

                    user_database.commit()
                    user_database.close()

               elif decision < 1:
                    print("Invalid Input. Please Try Again ")

               elif decision > 8:
                    print("Invalid Input. Please Try Again ")
          
          print("Relocating To Homepage...")
          self.Homepage()

     def Add_Pref(self):
          print("Below Are Options For Additional Preferences To Find Movies")
          print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
          print("= 1. Movie Rating                                                                         =")
          print("= 2. Search By Age Rating                                                                 =")
          print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
          #This gives the user the chance to search the db by other additional preferences or filters they may have

          option = int(input("Enter The Corresponding Number: \n"))
          
          if option == 1:
               #This function will return all values which match the rating and genre chosen by the user 
               x = False
               while x == False:
                    rating = int(input("Enter Minimum Movie Rating: "))
                    
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print("xx 1. Action              xx")
                    print("xx 2. Animated            xx")
                    print("xx 3. Comedy              xx")
                    print("xx 4. Science Fiction     xx")
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

                    
                    genre = int(input("Enter Number Corresponding To Genre: \n"))

                    if genre == 1:
                         movies_database = sqlite3.connect("Movies.db")
                         c = movies_database.cursor()
                         c.execute('''SELECT Film_Name, ActRecord_Number FROM Action_Films WHERE Rating >= ?''',(rating,))

                         fetched = list(c.fetchall())
                         
                         if fetched == []:
                              found = None
                         else:
                              found = True

                         if found == None:
                              print("A Search Of Scenario! Movies Found No Results Which Fit Your Description.")
                              print("Relocating To Homepage...")
                              self.Homepage()

                         act_lst = []
                         count = 0
                         for i in range(len(fetched)):
                              act_lst.append(fetched[count])
                              count += 1
                              
                         print("Results Of Your Search: ")
                         print("= = = = = = = = = = = = =")
                         count = 0
                         for i in range(len(act_lst)):
                              print(act_lst[count][1],".",act_lst[count][0])
                              count += 1

                         movies_database.commit()
                         movies_database.close()

                         userChoice = int(input("Enter The Corresponding Number To Movie You Wish To Watch: \n"))
                         self.MovieSelector(userChoice)

                         x = True

                    elif genre == 2:
                         movies_database = sqlite3.connect("Movies.db")
                         c = movies_database.cursor()
                         c.execute('''SELECT Film_Name, AniRecord_Number FROM Animated_Films WHERE Rating >= ?''',(rating,))

                         fetched2 = list(c.fetchall())
                       
                         if fetched2 == []:
                              found = None
                         else:
                              found = True

                         if found == None:
                              print("A Search Of Scenario! Movies Found No Results Which Fit Your Description.")
                              print("Relocating To Homepage...")
                              self.Homepage()

                         ani_lst = []
                         count = 0
                         for i in range(len(fetched2)):
                              ani_lst.append(fetched2[count])
                              count += 1
                              
                         print("Results Of Your Search: ")
                         print("= = = = = = = = = = = = =")
                         count = 0
                         for i in range(len(ani_lst)):
                              print(ani_lst[count][1],".",ani_lst[count][0])
                              count += 1

                         movies_database.commit()
                         movies_database.close()

                         userChoice = int(input("Enter The Corresponding Number To Movie You Wish To Watch: \n"))
                         self.MovieSelector(userChoice)

                         x = True
                         
                    elif genre == 3:
                         movies_database = sqlite3.connect("Movies.db")
                         c = movies_database.cursor()
                         c.execute('''SELECT Film_Name, ComRecord_Number FROM Comedy_Films WHERE Rating >= ?''',(rating,))

                         fetched3 = list(c.fetchall())
               
                         if fetched3 == []:
                              found = None
                         else:
                              found = True

                         if found == None:
                              print("A Search Of Scenario! Movies Found No Results Which Fit Your Description.")
                              print("Relocating To Homepage...")
                              self.Homepage()

                         com_lst = []
                         count = 0
                         for i in range(len(fetched3)):
                              com_lst.append(fetched3[count])
                              count += 1
                              
                         print("Results Of Your Search: ")
                         print("= = = = = = = = = = = = =")
                         count = 0
                         for i in range(len(com_lst)):
                              print(com_lst[count][1],".",com_lst[count][0])
                              count += 1

                         movies_database.commit()
                         movies_database.close()

                         userChoice = int(input("Enter The Corresponding Number To Movie You Wish To Watch: \n"))
                         self.MovieSelector(userChoice)

                         x = True
                    elif genre == 4:
                         movies_database = sqlite3.connect("Movies.db")
                         c = movies_database.cursor()
                         c.execute('''SELECT Film_Name, SciRecord_Number FROM SciFi_Films WHERE Rating >= ?''',(rating,))

                         fetched4 = list(c.fetchall())
               
                         if fetched4 == []:
                              found = None
                         else:
                              found = True

                         if found == None:
                              print("A Search Of Scenario! Movies Found No Results Which Fit Your Description.")
                              print("Relocating To Homepage...")
                              self.Homepage()

                         sci_lst = []
                         count = 0
                         for i in range(len(fetched4)):
                              sci_lst.append(fetched4[count])
                              count += 1
                              
                         print("Results Of Your Search: ")
                         print("= = = = = = = = = = = = =")
                         count = 0
                         for i in range(len(sci_lst)):
                              print(sci_lst[count][1],".",sci_lst[count][0])
                              count += 1

                         movies_database.commit()
                         movies_database.close()

                         userChoice = int(input("Enter The Corresponding Number To The Movie You Wish To Watch: \n"))
                         self.MovieSelector(userChoice)

                         x = True

                    if genre > 1:
                         print("Invalid Input: Out Of Range")
                         x = False

                    if genre < 4:
                         print("Invalid Input: Out Of Range")
                         x = False

          if option == 2:
               #This will return all movies which fit the age rating chosen by the user
               x = False
               while x == False:
                    print(":::::::::::::::::::::::::::::::::")
                    print(":: 1. Age 3                    ::")
                    print(":: 2. Age 7                    ::")
                    print(":: 3. Age 12                   ::")
                    print(":: 4. Age 15                   ::")
                    print(":: 5. Age 18                   ::")
                    print(":::::::::::::::::::::::::::::::::")

                    age_rating = int(input("Enter The Corresponding Number To The Maximum Age Rating: \n"))

                    if age_rating == 3:
                         age_rating = 12

                         x = 1
                    
                    elif age_rating == 1 or age_rating == 2:
                         age_rating = 3
                         
                         x = 1

                    elif age_rating == 4 or age_rating == 5:
                         age_rating = 18

                         x = 1 

                    if age_rating < 1:
                         print("Invalid Input: Out Of Range")
                         print("Relocating To Homepage ...")
                         self.Homepage()

                    if age_rating > 5:
                         print("Invalid Input: Out Of Range")
                         print("Relocating To Homepage ...")
                         self.Homepage()

                    if x == 1:
                         
                         print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                         print("xx 1. Action                   xx")
                         print("xx 2. Animated                 xx")
                         print("xx 3. Comedy                   xx")
                         print("xx 4. Science Fiction          xx")
                         print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

                         genre = int(input("Enter The Corresponding Number To The Genre: \n"))
                         if genre == 1:
                              movies_database = sqlite3.connect("Movies.db")
                              c = movies_database.cursor()
                              c.execute('''SELECT Film_Name,ActRecord_Number FROM Action_Films WHERE Age_Rating <= ?''',(age_rating,))

                              actFilms = list(c.fetchall())

                              if actFilms == []:
                                   found = None
                                   
                              else:
                                   found = True

                              if found == None:
                                   print("A Search Of Scenario! Movies Found No Results Which Fit Your Description.")
                                   print("Relocating To Homepage...")
                                   self.Homepage()
                         
                              actLst = []
                              count = 0 
                              for i in range(len(actFilms)):
                                   actLst.append(actFilms[count])
                                   count += 1
                              
                              print("Results Of Your Search: ")
                              print("= = = = = = = = = = = = =")
                              count = 0 
                              for i in range(len(actLst)):
                                   print(actLst[count][1],".",actLst[count][0])
                                   count += 1

                              movies_database.commit()
                              movies_database.close()

                              userChoice = int(input("Enter Corresponding To Movie You Wish To View: \n"))
                              self.MovieSelector(userChoice)

                              x = True

                         elif genre == 2:
                              movies_database = sqlite3.connect("Movies.db")
                              c = movies_database.cursor()
                              c.execute('''SELECT Film_Name,AniRecord_Number FROM Animated_Films WHERE Age_Rating <= ?''',(age_rating,))

                              aniFilms = list(c.fetchall())

                              if aniFilms == []:
                                   found = None
                                   
                              else:
                                   found = True

                              if found == None:
                                   print("A Search Of Scenario! Movies Found No Results Which Fit Your Description.")
                                   print("Relocating To Homepage...")
                                   self.Homepage()
                    
                              aniLst = []
                              count = 0 
                              for i in range(len(aniFilms)):
                                   aniLst.append(aniFilms[count])
                                   count += 1
                              
                              print("Results Of Your Search: ")
                              print("= = = = = = = = = = = = =")
                              count = 0 
                              for i in range(len(aniLst)):
                                   print(aniLst[count][1],".",aniLst[count][0])
                                   count += 1

                              movies_database.commit()
                              movies_database.close()

                              userChoice = int(input("Enter Corresponding To Movie You Wish To View: \n"))
                              self.MovieSelector(userChoice)

                              x = True

                         elif genre == 3:
                              movies_database = sqlite3.connect("Movies.db")
                              c = movies_database.cursor()
                              c.execute('''SELECT Film_Name,ComRecord_Number FROM Comedy_Films WHERE Age_Rating <= ?''',(age_rating,))

                              ComFilms = list(c.fetchall())

                              if ComFilms == []:
                                   found = None
                                   
                              else:
                                   found = True

                              if found == None:
                                   print("A Search Of Scenario! Movies Found No Results Which Fit Your Description.")
                                   print("Relocating To Homepage...")
                                   self.Homepage()
                         
                              ComLst = []
                              count = 0 
                              for i in range(len(ComFilms)):
                                   ComLst.append(ComFilms[count])
                                   count += 1
                              
                              print("Results Of Your Search: ")
                              print("= = = = = = = = = = = = =")
                              count = 0
                              count2 = 1 
                              for i in range(len(ComLst)):
                                   print(ComLst[count][1],".",ComLst[count][0])
                                   count += 1

                              movies_database.commit()
                              movies_database.close()

                              userChoice = int(input("Enter Corresponding To Movie You Wish To View: \n"))
                              self.MovieSelector(userChoice)

                              x = True

                         elif genre == 4:
                              movies_database = sqlite3.connect("Movies.db")
                              c = movies_database.cursor()
                              c.execute('''SELECT Film_Name,SciRecord_Number FROM SciFi_Films WHERE Age_Rating <= ?''',(age_rating,))

                              sciFilms = list(c.fetchall())

                              if sciFilms == []:
                                   found = None
                                   
                              else:
                                   found = True

                              if found == None:
                                   print("A Search Of Scenario! Movies Found No Results Which Fit Your Description.")
                                   print("Relocating To Homepage...")
                                   self.Homepage()
                         

                              sciLst = []
                              count = 0 
                              for i in range(len(sciFilms)):
                                   sciLst.append(sciFilms[count])
                                   count += 1
                              
                              print("Results Of Your Search: ")
                              print("= = = = = = = = = = = = =")
                              count = 0
                              count2 = 1 
                              for i in range(len(sciLst)):
                                   print(sciLst[count][1],".",sciLst[count][0])
                                   count += 1

                              movies_database.commit()
                              movies_database.close()

                              userChoice = int(input("Enter Corresponding To Movie You Wish To View: \n"))
                              self.MovieSelector(userChoice)

                              x = True

                         elif genre > 1:
                              print("Invalid Input")
                              x = False

                         elif genre < 4:
                              print("Invalid Input")
                              x = False

               if option < 1 or option > 2:
                    print("Invalid Input: Out Of Range")
                    x = False

               
                    

               

              
     def Homepage(self):
          #Homepage from which the user can centrally navigate the program
          print("\n")
          print("**********************************************************************************************************************************************")
          print("**********************************************************************************************************************************************")
          print("%s's Account                                           SCENARIO! MOVIES                                          Press 'S' To Search Movies"%(self.firstName))
          print("**  = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = **")
          print("**                                                                                                                                          **")
          self.random_movies()
          print("**                                                                                                                                          **")
          print("**                                                                                                                                          **")
          print("**                                                                                                                                          **")
          print("**                                                                                                                                          **")
          self.viewing_last_ten_movies()              
          print("**                                                                                                                                          **")
          print("**                                                                                                                                          **")
          print("**   _ _ _ _ _ _ _ _ _ _ _ _ _          _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _          _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _        **")
          print("**  |                         |        |                                   |        |                                               |       **")
          print("**  |Press 'F' To Sign Out    |        |Press 'A' To See Account Details   |        |Press 'P' To Add Additional Viewing Preferences|       **")
          print("**  |                         |        |                                   |        |                                               |       **")
          print("**********************************************************************************************************************************************")
          #statements which correspond to user input as they navigate program
          x = False
          while x == False:
               print("Enter 'M' To Choose A Movie Or Enter 'O' To Do A Different Function")

               decision = input().upper()

               if decision == "O":
                    choice = input("Enter The Corresponding Letter To The Function: \n").upper()
                    if choice == "S":
                         self.searchWebsite()

                         x = True

                    if choice == "F":
                         print(self.signOut())

                         x = True

                    if choice == "A":
                         self.viewAccountDetails()

                         x = True

                    if choice == "P":
                         self.Add_Pref()

                         x = True
                         
               elif decision == "M":
                    
                    choice = int(input("Enter The Corresponding Number To The Movie You Wish To Watch: \n"))
                    self.MovieSelector(choice)
                    x = True
                    
     def MovieSelector(self,number):
          #Shorter method to display movie based on its record number which indicates the genre which it falls in 
          count = 1
          while count != 11:
               if number == count:
                    movies_database = sqlite3.connect("Movies.db")

                    c = movies_database.cursor()
                    c.execute('''SELECT Film_Name FROM Action_Films WHERE ActRecord_Number = ?''',(count,))
                    fetched = c.fetchall()
                    film = fetched[0][0]

                    movies_database.commit()
                    movies_database.close()

                    rec = count

                    self.updating_last_ten_movies(film)
                    print("Loading Movie...")
                    self.Action_MovieDisplay(rec)
               count += 1

          count = 11
          while count != 21:
               if number == count:
                    movies_database = sqlite3.connect("Movies.db")

                    c = movies_database.cursor()
                    c.execute('''SELECT Film_Name FROM Animated_Films WHERE AniRecord_Number = ?''',(count,))
                    fetched2 = c.fetchall()
                    film2 = fetched2[0][0]

                    movies_database.commit()
                    movies_database.close()

                    rec = count
                    self.updating_last_ten_movies(film2)
                    print("Loading Movie...")
                    self.Animated_MovieDisplay(rec)
               count += 1

          count = 21
          while count != 31:
               if number == count:
                    movies_database = sqlite3.connect("Movies.db")

                    c = movies_database.cursor()
                    c.execute('''SELECT Film_Name FROM Comedy_Films WHERE ComRecord_Number = ?''',(count,))
                    fetched3 = c.fetchall()
                    film3 = fetched3[0][0]
                    movies_database.commit()
                    movies_database.close()

                    rec = count
                    self.updating_last_ten_movies(film3)
                    print("Loading Movie...")
                    self.Comedy_MovieDisplay(rec)
               count += 1

          count = 31
          while count != 41:
               if number == count:
                    movies_database = sqlite3.connect("Movies.db")

                    c = movies_database.cursor()
                    c.execute('''SELECT Film_Name FROM SciFi_Films WHERE SciRecord_Number = ?''',(count,))
                    fetched4 = c.fetchall()
                    film4 = fetched4[0][0]
                    movies_database.commit()
                    movies_database.close()

                    rec = count
                    self.updating_last_ten_movies(film4)
                    print("Loading Movie...")
                    self.SciFi_MovieDisplay(rec)
               count += 1

          if number < 1 or number > 40:
               print("Invalid Input")
               print("Relocating To Homepage...")
               self.Homepage()
               

     def Action_MovieDisplay(self,num):
          #A Display for an action movie 
          user_database = sqlite3.connect("User Databases.db")

          c = user_database.cursor()
          c.execute('''SELECT Last_Film1 FROM Users WHERE Username = ?''',(self.username,))

          a = c.fetchall()
          name = a[0][0]
          
          print(" --------------------------------------------------------------------------------------------------------------------------")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("                              PLAYING: %s"%(name))
          print("|                                                                                                                          |")
          print("|                             *********************************************************                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                     ' ' ' ' ' '                       *                                    |")
          print("|                             *                     ' *       '                       *                                    |")
          print("|                             *                     ' *  *    '                       *                                    |")
          print("|                             *                     ' *     * '                       *                                    |")
          print("|                             *                     ' *  *    '                       *                                    |")
          print("|                             *                     ' *       '                       *                                    |")
          print("|                             *                     '''''''''''                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *********************************************************                                    |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|   Press 'L' To Add This Movie To 'Liked Movies'                                                                          |")
          print("|   Press 'E' To Exit This Movie And Return To The Homepage                                                                |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print(" -------------------------------------------------------------------------------------------------------------------------- ")

          ext = False
          while ext == False:
               choice = input().upper()
               if choice == "L":
                    #Inserts the movie into the liked table and changes the status to 1 which indicates that Liked = True 
                    movies_database = sqlite3.connect("Movies.db")
                    c = movies_database.cursor()
                    c.execute('''SELECT Film_Name FROM Action_Films WHERE ActRecord_Number = ?''',(num,))
                    film = c.fetchall()
                    final_film = film[0][0]

                    c.execute('''SELECT ActionFilmID FROM Action_Films WHERE ActRecord_Number = ?''',(num,))
                    ID = c.fetchall()
                    finalID = ID[0][0]

                    movies_database.commit()

                    status = 1
                    
                    movies_database = sqlite3.connect("User Likes.db")
                    c = movies_database.cursor()
                    c.execute('''INSERT INTO %s VALUES (?,?,?)'''%self.username,(final_film,finalID,status))

                    movies_database.commit()
                    movies_database.close()
                    
                    print("You Have Liked This Movie :)")
                    ext = False
          
               if choice == "E":
                    print("Relocating To Homepage...")
                    self.Homepage()
                    ext = True
               #allows user to exit display and return to homepage

     def Animated_MovieDisplay(self,num):
          #Same as above except for animated movies
          user_database = sqlite3.connect("User Databases.db")

          c = user_database.cursor()
          c.execute('''SELECT Last_Film1 FROM Users WHERE Username = ?''',(self.username,))

          a = c.fetchall()
          name = a[0][0]
          
          print(" --------------------------------------------------------------------------------------------------------------------------")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("                              PLAYING: %s"%(name))
          print("|                             *********************************************************                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                     ' ' ' ' ' '                       *                                    |")
          print("|                             *                     ' *       '                       *                                    |")
          print("|                             *                     ' *  *    '                       *                                    |")
          print("|                             *                     ' *     * '                       *                                    |")
          print("|                             *                     ' *  *    '                       *                                    |")
          print("|                             *                     ' *       '                       *                                    |")
          print("|                             *                     '''''''''''                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *********************************************************                                    |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|   Press 'L' To Add This Movie To 'Liked Movies'                                                                          |")
          print("|   Press 'E' To Exit This Movie And Return To The Homepage                                                                |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print(" -------------------------------------------------------------------------------------------------------------------------- ")

          ext = False
          while ext == False:
               choice = input().upper()
               if choice == "L":
                    movies_database = sqlite3.connect("Movies.db")
                    c = movies_database.cursor()
                    c.execute('''SELECT Film_Name FROM Animated_Films WHERE AniRecord_Number = ?''',(num,))
                    film = c.fetchall()
                    final_film = film[0][0]

                    c.execute('''SELECT AnimatedFilmID FROM Animated_Films WHERE AniRecord_Number = ?''',(num,))
                    ID = c.fetchall()
                    finalID = ID[0][0]

                    movies_database.commit()

                    status = 1
                    
                    movies_database = sqlite3.connect("User Likes.db")
                    c = movies_database.cursor()
                    c.execute('''INSERT INTO %s VALUES (?,?,?)'''%self.username,(final_film,finalID,status))

                    movies_database.commit()
                    movies_database.close()
                    
                    print("You Have Liked This Movie :)")
                    ext = False
          
               if choice == "E":
                    print("Relocating To Homepage...")
                    self.Homepage()
                    ext = True
          
     def Comedy_MovieDisplay(self,num):
          #same as above except for comedy movies
          user_database = sqlite3.connect("User Databases.db")

          c = user_database.cursor()
          c.execute('''SELECT Last_Film1 FROM Users WHERE Username = ?''',(self.username,))

          a = c.fetchall()
          name = a[0][0]
          
          print(" --------------------------------------------------------------------------------------------------------------------------")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("                              PLAYING: %s"%(name))
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                             *********************************************************                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                     ' ' ' ' ' '                       *                                    |")
          print("|                             *                     ' *       '                       *                                    |")
          print("|                             *                     ' *  *    '                       *                                    |")
          print("|                             *                     ' *     * '                       *                                    |")
          print("|                             *                     ' *  *    '                       *                                    |")
          print("|                             *                     ' *       '                       *                                    |")
          print("|                             *                     '''''''''''                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *********************************************************                                    |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|   Press 'L' To Add This Movie To 'Liked Movies'                                                                          |")
          print("|   Press 'E' To Exit This Movie And Return To The Homepage                                                                |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print(" -------------------------------------------------------------------------------------------------------------------------- ")

          ext = False
          while ext == False:
               choice = input().upper()
               if choice == "L":
                    movies_database = sqlite3.connect("Movies.db")
                    c = movies_database.cursor()
                    c.execute('''SELECT Film_Name FROM Comedy_Films WHERE ComRecord_Number = ?''',(num,))
                    film = c.fetchall()
                    final_film = film[0][0]

                    c.execute('''SELECT ComedyFilmID FROM Comedy_Films WHERE ComRecord_Number = ?''',(num,))
                    ID = c.fetchall()
                    finalID = ID[0][0]

                    movies_database.commit()

                    status = 1
                    
                    movies_database = sqlite3.connect("User Likes.db")
                    c = movies_database.cursor()
                    c.execute('''INSERT INTO %s VALUES (?,?,?)'''%self.username,(final_film,finalID,status))

                    movies_database.commit()
                    movies_database.close()
                    
                    print("You Have Liked This Movie :)")
                    ext = False
          
               if choice == "E":
                    print("Relocating To Homepage...")
                    self.Homepage()
                    ext = True

     def SciFi_MovieDisplay(self,num):
          #same as above for sci fi movies
          user_database = sqlite3.connect("User Databases.db")

          c = user_database.cursor()
          c.execute('''SELECT Last_Film1 FROM Users WHERE Username = ?''',(self.username,))

          a = c.fetchall()
          name = a[0][0]
          
          print(" --------------------------------------------------------------------------------------------------------------------------")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("                              PLAYING: %s"%(name))
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                             *********************************************************                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                     ' ' ' ' ' '                       *                                    |")
          print("|                             *                     ' *       '                       *                                    |")
          print("|                             *                     ' *  *    '                       *                                    |")
          print("|                             *                     ' *     * '                       *                                    |")
          print("|                             *                     ' *  *    '                       *                                    |")
          print("|                             *                     ' *       '                       *                                    |")
          print("|                             *                     '''''''''''                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *                                                       *                                    |")
          print("|                             *********************************************************                                    |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|   Press 'L' To Add This Movie To 'Liked Movies'                                                                          |")
          print("|   Press 'E' To Exit This Movie And Return To The Homepage                                                                |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print("|                                                                                                                          |")
          print(" -------------------------------------------------------------------------------------------------------------------------- ")

          ext = False
          while ext == False:
               choice = input().upper()
               if choice == "L":
                    movies_database = sqlite3.connect("Movies.db")
                    c = movies_database.cursor()
                    c.execute('''SELECT Film_Name FROM SciFi_Films WHERE SciRecord_Number = ?''',(num,))
                    film = c.fetchall()
                    final_film = film[0][0]

                    c.execute('''SELECT SciFiFilmID FROM SciFi_Films WHERE SciRecord_Number = ?''',(num,))
                    ID = c.fetchall()
                    finalID = ID[0][0]

                    movies_database.commit()

                    status = 1
                    
                    movies_database = sqlite3.connect("User Likes.db")
                    c = movies_database.cursor()
                    c.execute('''INSERT INTO %s VALUES (?,?,?)'''%self.username,(final_film,finalID,status))

                    movies_database.commit()
                    movies_database.close()
                    
                    print("You Have Liked This Movie :)")
                    ext = False
          
               if choice == "E":
                    print("Relocating To Homepage...")
                    self.Homepage()
                    ext = True
          
          
#Subroutines
def creating_databases():#This only needs to be run once to create the file and table through python
     user_database = sqlite3.connect("User Databases.db")
     c = user_database.cursor()#Cursor used to navigate the db 
     c.execute('''CREATE TABLE Users
     (Username text,
      Password text,
      Firstname text,
      Surname text,
      Address text,
      Date Of Birth text,
      Gender text,
      Interest1 text,
      Interest2 text,
      Interest3 text,
      Last_Film1 text,
      Last_Film2 text,
      Last_Film3 text,
      Last_Film4 text,
      Last_Film5 text,
      Last_Film6 text,
      Last_Film7 text,
      Last_Film8 text,
      Last_Film9 text,
      Last_Film10 text,
      Favourite_Actor text,
      Favourite_Film text)''')#This creates a table in SQLite with the listed headings to hold a user's details 

     user_database.commit()#Executes actions
     user_database.close()#Closes the database once it has been created
     print("Done")#Message for developer to indicate the statement has worked 

def sign_up():
     x = False
     while x == False:
          print("Please Fill Out This Form To Register For The Website: ")
          print("-------------------------------------------------------")
          print(" \n ")
     
          username = input("Username: \n")#Takes the details from the user for the corresponding fields

          print("NOTE: All Passwords Must Contain: At Least One Number And One Uppercase Letter")
          password = input("Password: \n") 
          confPassword = input("Please Confirm Your Password: \n")

          firstName = input("Firstname: \n").upper()
          
          surname = input("Surname: \n").upper()

          address = input("Address: \n")

          DOB = input("Date Of Birth (DD/MM/YYYY)\n")

          print("Please Enter Your Gender: (Enter 'M' For Male, 'F' For Female, or 'O' For Other)")
          gender = input()
          gender = gender.upper()

          print("Enter 3 Numbers For Your 3 Favourite Genres: ")
          print("1. Comedy ")
          print("2. Action ")
          print("3. Animated ")
          print("4. Science Fiction ")
          interests = list(input())#Organises the 3 inputs into a list of 3 seperate integers from 1 input

          #Username Check
          user_database = sqlite3.connect("User Databases.db")
          c = user_database.cursor()
          c.execute('''SELECT Username FROM Users WHERE Username = ?''', (username,))#Searching db for record with existing username
          check = c.fetchall()

          if check != username:
               x = True

          else:
               print("\n This Username Is Already Taken \n")
               x = False

          user_database.commit()
          user_database.close()

          
          
          #Password Check
          count = 0
          samepwCheck = False
          numberCheck = False
          upperCheck = False
          
          
          
          
          if password == confPassword:
               samepwCheck = True
               for count in range(len(password)):
                    if password[count].isdigit():
                         numberCheck = True
                         #checks at least one character in the input is a number
                    if password[count].isupper():
                         upperCheck = True
                         #checks at least one character is uppercase

                    count += 1
                    

          if (samepwCheck == True) and (numberCheck == True) and (upperCheck == True):
               x = True

          elif samepwCheck == False:
               print("\n Your Passwords Did Not Match \n")
               x = False

          elif numberCheck == False:
               print("\n Your Password Must Contain At Least One Number \n")
               x = False

          elif upperCheck == False:
               print("\n Your Password Must Contain At Least One Uppercase Character \n")
               x = False

          #End Of Password Check

          #Gender Check
          if gender == "M" or gender == "F" or gender == "O":
               x = True

          else:
               print("\n The Gender That Was Entered Did Not Meet The Outlined Options \n")
               x = False
          #End Of Gender Check

          #Interest Check

          #Checks only 3 numbers are input

          if len(interests) == 3:
               x = True
               contTo_R_Check = True

          elif len(interests) > 3:
               print("\n More Than Three Interests Were Entered \n")
               x = False
               contTo_R_Check = False

          elif len(interests) < 3:
               print("\n Less Than Three Interests Were Entered \n")
               x = False
               contTo_R_Check = False

          #Checking The Numbers in Interest Are In Range:

          if contTo_R_Check == True:
               firstNum = False
               secondNum = False
               thirdNum = False

               if interests[0] == "1" or interests[0] == "2" or interests[0] == "3" or interests[0] == "4":
                    firstNum = True
               elif interests[0] != "1" or interests[0] != "2" or interests[0] != "3" or interests[0] != "4":
                    firstNum = False

               if interests[1] == "1" or interests[1] == "2" or interests[1] == "3" or interests[1] == "4":
                    secondNum = True
               elif interests[1] != "1" or interests[1] != "2" or interests[1] != "3" or interests[1] != "4":
                    secondNum = False

               if interests[2] == "1" or interests[2] == "2" or interests[2] == "3" or interests[2] == "4":
                    thirdNum = True
               elif interests[2] != "1" or interests[2] != "2" or interests[2] != "3" or interests[2] != "4":
                    thirdNum = False

               if firstNum == True and secondNum == True and thirdNum == True:
                    x = True

               elif firstNum == False or secondNum == False or thirdNum == False:
                    print("\n The 'Genre Interests' Input Was Out Of Range \n")
                    x = False
          #End Of Interests Check
          

          last_films = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
          details = Users(username,password,confPassword,firstName,surname,address,DOB,gender,interests,last_films," "," ")
          details.insert_table()
          details.create_user_liked_table()
          details.login()
            
def login():
     var = False
     userCheck = False
     pwCheck = False
     while var == False:
          print("::::::::::::::::::::::::::::::::::::")
          print(":: Press '1' To Login             ::")
          print(":: Press '2' To Create An Account ::")
          print("::::::::::::::::::::::::::::::::::::")

          choice = int(input())

          if choice == 1:
               global username
               print("Enter Username: ")
               username = input()

               print("Enter Password: ")
               password = input()

               user_database = sqlite3.connect("User Databases.db")
               c = user_database.cursor()
               c.execute('''SELECT * FROM Users WHERE Username = ?''', (username,))#Searching db for record with existing username
               check = c.fetchall()

               if check is None:
                    print("\n Either Your Password Or Username Is Incorrect \n")#If this username is not found then the user will be unable to continue
                    var = False
                    userCheck = False

               else:
                    userCheck = True

               user_database.commit()
               user_database.close()

               if userCheck == True:#Should The username be correct then the password will be checked
                    user_database = sqlite3.connect("User Databases.db")
                    c = user_database.cursor()
                    c.execute('''SELECT * FROM Users WHERE Username = ?''',(username,))#Fetches the pw stored in db where the username is the PK for that record
                    fetched = c.fetchone()

                    if fetched is not None:
                         if fetched[1] == password:
                              pwCheck = True
                         
                    elif fetched is None:
                         print("\n Either Your Password Or Username Is Incorrect \n")
                         pwCheck = False
                         var = False

               if userCheck == True and pwCheck == True:
                    user_database = sqlite3.connect("User Databases.db")
                    c = user_database.cursor()
                    c.execute('''SELECT * FROM Users WHERE Username = ?''',(username,))
                    name = c.fetchone()

                    print("\n Login Successful \n")
                    print("Welcome" , name[2], name[3])
                    var = True

                    user_database.commit()
     
                    
               elif userCheck == False or pwCheck == False:
                    print("\n Login Failed \n")
                    var = False

          if choice == 2:
               sign_up()

          elif choice > 2:
               print("\n Invalid Input \n")
               var = False

          elif choice < 1:
               print("\n Invalid Input \n")
               var = False

     user_database = sqlite3.connect("User Databases.db")
     c = user_database.cursor()
     c.execute('''SELECT * FROM Users WHERE Username = ?''',(username,))

     fetched = c.fetchall()

     user_database.commit()
     user_database.close()

     genres = fetched[0][7],fetched[0][8],fetched[0][9]

     recents = fetched[0][10],fetched[0][11],fetched[0][12],fetched[0][13],fetched[0][14],fetched[0][15],fetched[0][16],fetched[0][17],fetched[0][18],fetched[0][19]
                   
     obj = Users(fetched[0][0],fetched[0][1],fetched[0][1],fetched[0][2],fetched[0][3],fetched[0][4],fetched[0][5],fetched[0][6],genres,recents,fetched[0][20],fetched[0][21])

     obj.contLogin() #creates a temporary object to allow user to access methods          

def addingRating_Column():
     #This is for my own use and not for the view of the user
     #In the development of the program, changes had to be made to the overall design and the layout of the dbs
     #In this instance, an extra column for the imdb rating for each film was required
     movies_database = sqlite3.connect("Movies.db")

     c = movies_database.cursor()
     c.execute('''ALTER TABLE Action_Films ADD COLUMN Rating integer''')

     print("Done")

     movies_database.commit()

     movies_database = sqlite3.connect("Movies.db")

     c = movies_database.cursor()
     c.execute('''ALTER TABLE Animated_Films ADD COLUMN Rating integer''')

     print("Done")

     movies_database.commit()

     movies_database = sqlite3.connect("Movies.db")

     c = movies_database.cursor()
     c.execute('''ALTER TABLE Comedy_Films ADD COLUMN Rating integer''')

     movies_database.commit()

     movies_database = sqlite3.connect("Movies.db")

     c = movies_database.cursor()
     c.execute('''ALTER TABLE SciFi_Films ADD COLUMN Rating integer''')

     movies_database.commit()
     movies_database.close()

def addingAll_Ratings():
     #Add movie ratings
     #For myself to quickly enter the ratings of each movie through python
     count = 1
     while count != 11:
          choice = int(input("Enter Rating"))
          movies_database = sqlite3.connect("Movies.db")
          c = movies_database.cursor()
          c.execute('''UPDATE Action_Films SET Rating = ? WHERE ActRecord_Number = ?''',(choice,count))
          movies_database.commit()

          count += 1

     count = 11
     while count != 21:
          choice = int(input("Enter Rating"))
          movies_database = sqlite3.connect("Movies.db")
          c = movies_database.cursor()
          c.execute('''UPDATE Animated_Films SET Rating = ? WHERE AniRecord_Number = ?''',(choice,count))
          movies_database.commit()

          count += 1
     count = 21
     while count != 31:
          choice = int(input("Enter Rating"))
          movies_database = sqlite3.connect("Movies.db")
          c = movies_database.cursor()
          c.execute('''UPDATE Comedy_Films SET Rating = ? WHERE ComRecord_Number = ?''',(choice,count))
          movies_database.commit()

          count += 1
     count = 1
     while count != 41:
          choice = int(input("Enter Rating"))
          movies_database = sqlite3.connect("Movies.db")
          c = movies_database.cursor()
          c.execute('''UPDATE SciFi_Films SET Rating = ? WHERE SciRecord_Number = ?''',(choice,count))
          movies_database.commit()

          count += 1
          
     movies_database.close()
     
def creating_genre_tables():
     #Creates a db where comedy films can be stored 
     movies_database = sqlite3.connect("Movies.db")
     c = movies_database.cursor()
     c.execute('''CREATE TABLE Comedy_Films
     (ComRecord_Number integer,
      ComedyFilmID text,
      Film_Name text,
      Release_Date text,
      Age_Rating integer)''')

     movies_database.commit()
     movies_database.close()

     #Creates a table in db where action films can be stored 
     movies_database = sqlite3.connect("Movies.db")
     c = movies_database.cursor()
     c.execute('''CREATE TABLE Action_Films
     (ActRecord_Number integer,
      ActionFilmID text,
      Film_Name text,
      Release_Date text,
      Age_Rating integer)''')

     movies_database.commit()
     movies_database.close()

     #Creates a table in db where animated films can be stored
     movies_database = sqlite3.connect("Movies.db")
     c = movies_database.cursor()
     c.execute('''CREATE TABLE Animated_Films
     (AniRecord_Number integer,
      AnimatedFilmID text,
      Film_Name text,
      Release_Date text,
      Age_Rating integer)''')

     movies_database.commit()
     movies_database.close()

     #Creates a table in db where Sci-fi films can be stored
     movies_database = sqlite3.connect("Movies.db")
     c = movies_database.cursor()
     c.execute('''CREATE TABLE SciFi_Films
     (SciRecord_Number integer,
      SciFiFilmID text,
      Film_Name text,
      Release_Date text,
      Age_Rating integer)''')

     movies_database.commit()
     movies_database.close()

def inserting_comedy_movies():
     #Faster and simpler way for me to insert movies into Comedy table from python
     x = 0
     while x != 5:
          ComRecordNum = input("Enter Record Number: \n")
          ComFilmID = input("Enter The Film ID: \n")
          Com_Film_Name = input("Enter The Name Of The Film: \n")
          Com_Release_Date = input("Enter The Release Date Of The Movie (DD/MM/YYYY): \n")
          Com_Age_Rating = int(input("Enter The Age Rating Of The Movie: \n"))

          inserting_comedy_moviesDB(ComRecordNum,ComFilmID,Com_Film_Name,Com_Release_Date,Com_Age_Rating)
          x += 1


def inserting_comedy_moviesDB(CRN,CID,CFN,CRD,CAR):
     #Inserting Comedy Movies Into DB
     movies_database = sqlite3.connect("Movies.db")
     c = movies_database.cursor()
     c.execute('''INSERT INTO Comedy_Films VALUES (?,?,?,?,?)''',(CRN,CID,CFN,CRD,CAR,))

     movies_database.commit()
     movies_database.close()

def inserting_action_movies():
     #Faster and simpler way for me to insert movies into Action table from python
     x = 0
     while x != 5:
          ActRecordNum = int(input("Enter Record Number: \n"))
          ActFilmID = input("Enter The Film ID: \n")
          Act_Film_Name = input("Enter The Name Of The Film: \n")
          Act_Release_Date = input("Enter The Release Date Of The Movie (DD/MM/YYYY): \n")
          Act_Age_Rating = input("Enter The Age Rating Of The Movie: \n")

          inserting_action_moviesDB(ActRecordNum,ActFilmID,Act_Film_Name,Act_Release_Date,Act_Age_Rating)
          #Passes the variables into another subroutine so they can be inserted into a table
          x += 1

def inserting_action_moviesDB(ARN,AID,AFN,ARD,AAR):
     #SQL statement to insert movies into table
     movies_database = sqlite3.connect("Movies.db")
     c = movies_database.cursor()
     c.execute('''INSERT INTO Action_Films VALUES (?,?,?,?,?)''',(ARN,AID,AFN,ARD,AAR,))

     movies_database.commit()
     movies_database.close()

def inserting_animated_movies():
     #Faster and simpler way for me to insert movies into Animated table from python
     x = 0
     while x != 5:
          AniRecordNum = int(input("Enter Record Number: \n"))
          AniFilmID = input("Enter The Film ID: \n")
          Ani_Film_Name = input("Enter The Name Of The Film: \n")
          Ani_Release_Date = input("Enter The Release Date Of The Movie (DD/MM/YYYY): \n")
          Ani_Age_Rating = input("Enter The Age Rating Of The Movie: \n")

          inserting_animated_moviesDB(AniRecordNum,AniFilmID,Ani_Film_Name,Ani_Release_Date,Ani_Age_Rating)
          #Passes the variables into another subroutine so they can be inserted into a table
          x += 1

def inserting_animated_moviesDB(ANRN,ANID,ANFN,ANRD,ANAR):
     #SQL statement to insert movies into table
     movies_database = sqlite3.connect("Movies.db")
     c = movies_database.cursor()
     c.execute('''INSERT INTO Animated_Films VALUES (?,?,?,?,?)''',(ANRN,ANID,ANFN,ANRD,ANAR))

     movies_database.commit()
     movies_database.close()

def inserting_SciFi_movies():
     #Faster and simpler way for me to insert movies into Animated table from python
     x = 0
     while x != 5:
          SciRecordNum = int(input("Enter Record Number: \n"))
          SciFilmID = input("Enter The Film ID: \n")
          Sci_Film_Name = input("Enter The Name Of The Film: \n")
          Sci_Release_Date = input("Enter The Release Date Of The Movie (DD/MM/YYYY): \n")
          Sci_Age_Rating = input("Enter The Age Rating Of The Movie: \n")

          inserting_SciFi_moviesDB(SciRecordNum,SciFilmID,Sci_Film_Name,Sci_Release_Date,Sci_Age_Rating)
          #Passes the variables into another subroutine so they can be inserted into a table

          x += 1

def inserting_SciFi_moviesDB(SRN,SID,SFN,SRD,SAR):
     #SQL statement to insert movies into table
     movies_database = sqlite3.connect("Movies.db")
     c = movies_database.cursor()
     c.execute('''INSERT INTO SciFi_Films VALUES (?,?,?,?,?)''',(SRN,SID,SFN,SRD,SAR))

     movies_database.commit()
     movies_database.close()

def updating_movie_numbers():
#I realised I had made a logic error regarding the record number of the movies
#Many had the same record number
#Although record number was not primary key they had to be changed to be unique identifiers for each record so they could be selected from homescreen
#Had to be changed to fit my logic

     #Updating Animated record numbers

     count = 1
     newNum = 11
     for i in range(10):
          movies_database = sqlite3.connect("Movies.db")
          
          c = movies_database.cursor()
          c.execute('''UPDATE Animated_Films SET AniRecord_Number = ? WHERE AniRecord_Number = ?''',(newNum,count))

          movies_database.commit()
          movies_database.close()

          count += 1
          newNum += 1

     print("Done")

     count = 1
     newNum = 21

     for i in range(10):
          movies_database = sqlite3.connect("Movies.db")

          c = movies_database.cursor()
          c.execute('''UPDATE Comedy_Films SET ComRecord_Number = ? WHERE ComRecord_Number = ?''',(newNum,count))

          movies_database.commit()
          movies_database.close()

          count += 1
          newNum += 1
     print("Done")

     count = 1
     newNum = 31
     for i in range(10):
          movies_database = sqlite3.connect("Movies.db")

          c = movies_database.cursor()
          c.execute('''UPDATE SciFi_Films SET SciRecord_Number = ? WHERE SciRecord_Number = ?''',(newNum,count))

          movies_database.commit()
          movies_database.close()
          count += 1
          newNum += 1
     print("Done")
          
#Main Body
login()
