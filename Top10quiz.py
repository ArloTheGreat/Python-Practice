POPULAR_SPORTS_ANSWERS = ["Football", "Cricket", "Tennis", "Golf", "Basketball", "Baseball", "Rugby", "Hockey", "Snooker", "Volleyball"]
#---FUNCTIONS---
#welcome user and introduce the quiz
def intro():
    #ask the user thier name
    name = input("What's your name?eyyes")

    #greet the user and introduce the quiz
    print("Welcome to this quiz,", name)
    print("This quiz is about the ten most popular sports in the world. Can you name them")

def getLives():
    while True:
        lives = input("How many chances do you want?")
        try:
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number")
        except:
            print("That wasn't a number")

#--- MAIN CODE ---
intro()
lives = getLives()