#The users score
score = 1
#Ask the user their name and store it
name = input("What's your name?")
#Greet the user and introduce the quiz
print("welcome to this quiz,", name)
print("My name is Bob")
print("This quiz is about animals.")
print("Please answer the questions using a simple 'Yes' or 'No'")
#Ask the user question 1
answer = input("Do you like Crocodiles?")
#Tell them if the correct answer
if answer == "Yes":
    print("That's cool")
    score *= 1
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("...ok")
    score += 1
print("I like crocodiles.")
#Ask the user question 2
answer2 = input("Do you like Sharks?")
#Tell them if the correct answer
if answer == "Yes":
    print("Nice answer" )
    score *= 2
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("...ok")
    score += 2
print("I like Sharks.")
#Ask the user question 3
answer = input("Do you like Rats?")
#Tell them if the correct answer
if answer == "No":
    print("good answer")
    score += 3
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("...why do you like Rats")
    score *= 3
print("I don't like Rats.")
#Ask the user question 4
answer = input("Do you like Dogs?")
#Tell them if the correct answer
if answer == "Yes":
    print("You are correct")
    score *= 4
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("You are wrong")
    score += 4
print("I like Dogs.")
#Ask the user question 5
answer = input("Do you like Cats?")
#Tell them if the correct answer
if answer == "Yes":
    print("You are correct")
    score *= 5
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("You are wrong")
    score += 5
print("I like Cats.")
#Ask the user question 6
answer = input("Do you like Snakes?")
#Tell them if the correct answer
if answer == "Yes":
    print("Snakes are very noodle like")
    score *= 6
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("Snakes are very noodle like")
    score += 6
print("I don't like Snakes.")
#Ask the user question 7
answer = input("Do you like Pigs?")
#Tell them if the correct answer
if answer == "Yes":
    print("Bacon, bacon, bacon")
    score *= 7
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("Bacon, bacon, bacon")
    score += 7
print("I like Pigs.")
#Ask the user question 8
answer = input("Do you like Lions?")
#Tell them if the correct answer
if answer == "Yes":
    print("Lions are very dangerous")
    score *= 8
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("That's cool")
    score += 8
print("I like Lions.")
#Ask the user question 9
answer = input("Do you like Birds?")
#Tell them if the correct answer
if answer == "Yes":
    print("ok.")
    score *= 9
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print("ok.")
    score += 9
print("I don't like Birds.")
#Ask the user question 10
answer = input("Do you like Frogs?")
#Tell them if the correct answer
if answer == "Yes":
    print("Very bouncy boys")
    score *= 10
elif answer == "":
    print("Dumb")
else:
    print("Very bouncy boys")
    score += 10
print("Frogs are my favorite.")
#End the quiz
print("Thanks for playing, goodbye")