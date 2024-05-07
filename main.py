#The users score
score = 1
#Ask the user their name and store it
name = input("What's your name?")
#Greet the user and introduce the quiz
print("welcome to this quiz,", name)
print("This quiz is about animals.")
print("Please answer the questions using a simple 'Yes' or 'No'")
#Ask the user question 1
answer = input("Do you like Crocodiles?")
#Tell them if the correct answer
if answer == "Yes":
    print("That's cool")
    score *= 5
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("...ok")
#Ask the user question 2
answer2 = input("Do you like Sharks?")
#Tell them if the correct answer
if answer == "Yes":
    print("Nice answer" )
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("...ok")
#Ask the user question 3
answer = input("Do you like Rats?")
#Tell them if the correct answer
if answer == "No":
    print("Rats are bad")
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("...why")
#Ask the user question 4
answer = input("Do you like Dogs?")
#Tell them if the correct answer
if answer == "Yes":
    print("You are correct")
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("You are wrong")
#Ask the user question 5
answer = input("Do you like Cats?")
#Tell them if the correct answer
if answer == "Yes":
    print("You are correct")
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("You are wrong")
#Ask the user question 6
answer = input("Do you like Snakes?")
#Tell them if the correct answer
if answer == "Yes":
    print("Snakes are very noodle like")
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("Snakes are very noodle like")
#Ask the user question 7
answer = input("Do you like Pigs?")
#Tell them if the correct answer
if answer == "Yes":
    print("Bacon, bacon, bacon")
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("Bacon, bacon, bacon")
#Ask the user question 8
answer = input("Do you like Lions?")
#Tell them if the correct answer
if answer == "Yes":
    print("Lions are very dangerous")
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("That's cool")
#Ask the user question 9
answer = input("Do you like Birds?")
#Tell them if the correct answer
if answer == "Yes":
    print("ok.")
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("ok.")
#Ask the user question 10
answer = input("Do you like Frogs?")
#Tell them if the correct answer
if answer == "Yes":
    print("Very bouncy boys")
elif answer == "":
    print("Dumb")
else:
    print("Very bouncy boys")
#End the quiz
print("Thanks for playing, goodbye")