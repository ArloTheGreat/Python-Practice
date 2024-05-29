#random
import random
random.randint(1,3)
#question format
QUESTION_FORMAT = "{}\nA. {} B. {} C. {} D.{}"
#The users score
score = 1
#Ask the user their name and store it
name = input("What's your name?")
#Greet the user and introduce the quize
print("This quiz is about animals.")
print("Please answer the questions using a simple 'Yes' or 'No'")
#List of my questions
QUESTIONS = ["What animal has the most population?"]
OPTIONS = [["Fish", "Insects", "Human", "Birds"]]
SHORT_OPTIONS = ["a", "b", "c", "d"]
ANSWERS = [1]
#Good and Bad commejts
GOOD_COMMENT = ["Good job", "Keep it up", "Fantastic"]
BAD_COMMENT = ["Maybe next time", "You got this", "Dont give up"] 
#Ask the user question 0
answer = input(QUESTION_FORMAT.format(QUESTIONS[0], OPTIONS[0][0], OPTIONS[0][1], OPTIONS[0][2], OPTIONS[0][3]))
#Tell them if the correct answer
if answer == OPTIONS[0][ANSWERS[0]] or answer == SHORT_OPTIONS[ANSWERS[0]]:
elif answer in SHORT_OPTIONS or answer in OPTIONS[0]:
    print("Wrong")
    print(random.choice(BAD_COMMENT))
else:
    print("That wasn't an option")
#Ask the user question 1
answer = input("Do you like Crocodiles?").lower()
#Tell them if the correct answer
if answer == "Yes".lower():
    print(random.choice(GOOD_COMMENT))
    score *= 1
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print(random.choice(BAD_COMMENT))
    score += 1
print("I like crocodiles.")
#Ask the user question 2
answer = input("Do you like Sharks?").lower()
#Tell them if the correct answer
if answer == "Yes".lower():
    print(random.choice(GOOD_COMMENT))
    score *= 2
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print(random.choice(BAD_COMMENT))
    score += 2
print("I like Sharks.")
#Ask the user question 3
answer = input("Do you like Molerats?").lower()
#Tell them if the correct answer
if answer == "Yes".lower():
    print(random.choice(GOOD_COMMENT))
    score *= 3
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print(random.choice(BAD_COMMENT))
    score += 3
print("I like Molerats.")
#Ask the user question 4
answer = input("Do you like Dogs?").lower()
#Tell them if the correct answer
if answer == "Yes".lower():
    print(random.choice(GOOD_COMMENT))
    score *= 4
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print(random.choice(BAD_COMMENT))
    score += 4
print("I like Dogs.")
#Ask the user question 5
answer = input("Do you like Cats?").lower()
#Tell them if the correct answer
if answer == "Yes".lower():
    print(random.choice(GOOD_COMMENT))
    score *= 5
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print(random.choice(BAD_COMMENT))
    score += 5
print("I like Cats.")
#Ask the user question 6
answer = input("Do you like Snakes?").lower()
#Tell them if the correct answer
if answer == "Yes".lower():
    print(random.choice(GOOD_COMMENT))
    score *= 6
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print(random.choice(BAD_COMMENT))
    score += 6
print("I like snakes")
#Ask the user question 7
answer = input("Do you like Pigs?").lower()
#Tell them if the correct answer
if answer == "Yes".lower():
    print(random.choice(GOOD_COMMENT))
    score *= 7
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print(random.choice(BAD_COMMENT))
    score += 7
print("I like Pigs.")
#Ask the user question 8
answer = input("Do you like Lions?").lower()
#Tell them if the correct answer
if answer == "Yes".lower():
    print(random.choice(GOOD_COMMENT))
    score *= 8
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print(random.choice(BAD_COMMENT))
    score += 8
print("I like Lions.")
#Ask the user question 9
answer = input("Do you like Bevers?").lower()
#Tell them if the correct answer
if answer == "Yes".lower():
    print(random.choice(GOOD_COMMENT))
    score *= 9
elif answer == "":
    print("TRY ANSWERING THE NEXT QUESTION")
else:
    print(random.choice(BAD_COMMENT))
    score += 9
print("I like Bevers")
#Ask the user question 10
answer = input("Do you like Frogs?").lower()
#Tell them if the correct answer
if answer == "Yes".lower():
    print(random.choice(GOOD_COMMENT))
    score *= 10
elif answer == "":
    print("Dumb")
else:
    print(random.choice(BAD_COMMENT))
    score += 10
print("Frogs are my favorite.")
#End the quiz
print("Thanks for playing, {}, you gots a score of, {}, good job, and i hope you have a great day".format(name, score))
print("-Bob")