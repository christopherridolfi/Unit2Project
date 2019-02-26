"""
read in each student, store as tuple, use as a key to a dictionary
value for dictionary is the number of times it matches
if the value is equal to the number of conditions then print the student data(key)
"""
#2
diction = (1,2,3,4)#This is the tuple for the parameter.
def extremeTuple(args):
    length = len(args)#This fines the length of the arge parameter.
    if length == 0:#This makes sure that if you don't have any numbers in the parameter then you can't procede.
        print("There is No Maximum or Minimum value because you have no values")
    if length > 0:#This activates the lines below if the lengh of the args parameter is greater then 0.
        maximum = max(args)#This finds the max number in the tuple.
        minimum = min(args)#This finds the minimum number in the diction duple.
        print("Your Maximum Value is " + str(maximum))#Prints the maximum value.
        print("You Minimum Value is " + str(minimum))#prints the minimum value.
"""This function has 2 if statements. The second if statements only activates if you have a number over 0. This then finds the max and minimum value in the tuple.
It then is printed. The first only activates when there are no numbers in the parameter. And this if statement just tells
the user you don't have a max or minimum statement as you have no numbers in the tuple."""
extremeTuple(diction)#calls the function.

#3'
#line = []
#sto = [""]
open = open("Queries.txt", "r")#Opens the Queries Text file I use in this challenge question.
fn = input("What Is The First Name of The Student You Are Looking For").lower()
#Asks the user the first name of who they are looking for.
ln = input("What Is The Last Name of The Student You Are Looking For").lower()
#Asks the last name of the user they are looking for.
ad = input("What advisor does the studen have").lower()
#Asks the advisor of who they are looking for.
gd = input("What grade is your student in").lower()
#Asks the grade the student they are looking for are in.
house = input("What house is your student in.").lower()
#Asks the house the students they are looking for are in.

data = open.readlines()#A variable that reads the lines of the open variable which is the Queries text file.
r = 0
countd = 0
listv = []#This is a list that I use later in the code to Make a list of a index point.
def changer2(index):#This is a function I created so I can shorten down a long line of code I use with different index's.
    test2 = (listv[0].strip().split(",")[index])
    return test2
    #This returns the test 2 variable.
for x in range(len(data)):#This is a range statement that goes through the lenght of data.
    if fn in data[x] and ln in data[x] and ad in data[x] and gd in data[x] and house in data[x]:
        listv.append(data[x])#above reads through all the inputs and sees if the input is in the data[x] list.
        """Line 46 then adds data[x] into a listv list."""
        changer2(1)
        if changer2(1) == fn or fn == "":#This sees if fn is in the index point where the first name would be in listv.
            if changer2(0) == ln or ln == "":#This sees if ln is in the index point where the last name would be in listv.
                if changer2(4) == ad or ad == "":#Repeated code with new index points that relate to advisor variable..
                    if changer2(2) == gd or gd == "":#Repeated code with new index points and relate to grade variable.
                        if changer2(3) == house or house == "":#REPEATED CODE
                            if countd == 0:
                                print("The students You are Looking For Are...\n")#I added this for theatrics and to make it look cooler.
                                countd = countd + 1#makes countd not equal to 0 to stop from printing the line again.
                            print(data[x])
                            """This whole peice of code basically sees if the inputed variables are in the changer index
                            if they are it continues on if it doesn't it also continues on. But later it lists all the 
                            information that is related to the inputs I gave. The last if statements prints out the data
                            found."""





#4
hopsuc = []#This is a list that is used to activate an if statements that tells the user if they can go to there destination.
flight = {"toronto":["brooklyn","florida"],"florida":["toronto","tampa bay"],"tampa bay":["florida","brooklyn"],"brooklyn":["toronto","ohio"]}
"""This is the dictionary for the flight dictionary challenge. Every city (key) can directly fly to two other citys (values)"""
def one_hop(flights,city1,city2):#This is the function for the one hop challenge.
    """The parameters are first of the name of the dictionary, then the city that you start from and then the third
    is where you want to go."""
    cities = flight[city1]#uses the parameter inputed to find the values using the key.
    fw = (cities[0])#makes the variable equal to the first city in the value.
    sw = (cities[1])#makes the variable equal to the second city in the value.
    step2 = flights[fw]#This uses the first city to open the key and find the variables for that city.
    step22 = flights[sw]#this uses the second city to open up the coresponding key in the dictionary.
    if city2 in step2:#This checks if the city your trying to go to is in this dictionary value.
        hopsuc.append("hi")#adds this word to a list.
    if city2 in step22:#Checks if the values of this dictionary key matches with the city2 parameter.
        hopsuc.append("hi")#adds this word to a list.
    if len(hopsuc) > 0:#If there is a word in the hopsuc list that means you can get to your destination using the one_hop method.
        print("You can get to your destination")
        return True
    else:
        print("You cannot get to " + city2 + " from " + city1 + " using the one hop method")
        return False

"""if there is no words in the hopsuc list then you can't get to your parameter using the one_hop method.
also if your values don't match the city2 then it also means you can't go where you want to using the one hop
method."""

one_hop(flight,"toronto","tampa bay")#This calls the function with all three parameters inputed.



#5
t = 0
b=0
whilelist = [] #A list that will be used to end my while statement once I have guessed properly 3 times.
import random#imports random function.
history = [1,2,1]#This is the list for the history of your guesses.
comppoints = []#This is the point counter for the computer.
"""This is used to win the game after guessing enough right answers."""
urpoints = []#This the the score counter for the player.
"""This is also used to activate the win game lines."""
v =0



while t == 0:#does the following until I guess appropreatly 3 times.
    chooser1 = input("Choose a number between 1 and 2")#Allows you to input a number you want to guess.
    try:
        if int(chooser1) > 0 and int(chooser1) <= 2:
            history.append(int(chooser1))#Adds the number to a list.
            del history[0]#deletes the first index in the list so you can only have a history of 3.
            whilelist.append(1)#adds a value to a list to make a history only including 3 numbers.
            if len(whilelist) == 2:#ends the while loop once I made my history.
                t = t + 1#ends the while loop;
                b = b+1#ends the b while list.
                break
            else:
                chooser1 = input("Choose a number between 1 and 2")  # makes sure they input either 1 or 2 as history.
    except ValueError:#I did this becasue it would error out if you didn't enter a number so now it just redoes the input.
            chooser1 = input("Choose a number between 1 and 2")#makes sure they input either 1 or 2 as history.
while v == 0:
    if len(comppoints) == 30:#this sees if the computer guessed right enough times to win the game.
        print("The Computer Wins")#Prints the you win message.
        break#this breaks the while loop so the game will end.
    elif len(urpoints) == 30:#This sees if the computer guessed wrong enough times to see if you win the game.
        print("You win")
        break#breaks the while loop for the same reason above.
    print("The computer is choosing....")#Shows the viewer the computer is thinking.(dramatic effect)
    history.sort()#sorts the history list from lowest number to highest.
    tuple5 = (history[0],history[1],history[2])#puts the three sorted history values into a tuple to be used later.
    prob = {(1,2,2):2,(1,1,1):1,(1,1,2):1,(2,2,2):2}
    """This is a dictionary with all the probabilities the computer will guess. This uses the tuple
    as the key to activate the value the computer will guess."""
    answer = (prob[tuple5])#this makes the variable equal to the value you want.
    finalg = input("What is your Guess?")#asks what you want your final answer to be so the computer may attempt to guess.
    history.append(int(finalg))  # Adds the number to a list.
    print(history)
    del history[0]  # deletes the first index in the list so you can only have a history of 3.
    if int(finalg) == answer:#activates the lines below if you and the computer guess the same number.
        print("The Computer guessed The Same As You")#prints this message.
        comppoints.append(1)#adds a point for the computer into the comppoints list.
        print("The Computer Has " + str(len(comppoints)) + " point(s)")#prints how many points the computer has.
        t = t -1#reennitiated my while loop.
        whilelist = []#deletes the values in my list so I can redo my history.
    else:
        print("The Computer Guessed Wrong")#prints that the computer guessed wrong if your value doesn't match there guess.
        urpoints.append(1)#adds a point to your point list.
        print("You Have " + str(len(urpoints)) + " point(s)")#prints how many points you have.
        t = t-1#reintiates my while loop.
        whilelist = []#remaking my whilelist empty so I can use it again.
        """This is the option in where the computer guessed wrong. This peice of code adds a point to your list and
         prints out how many points I have."""