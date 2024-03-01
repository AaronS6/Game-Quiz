import random


animals = {"monkey":"loves to eat bananas!",
           "dog":"A fun friend in your house!",
           "bird":"Who doesn't want to fly in the sky?",
           "beaver":"My sharp teeth can chop through trees like a axe!",
           "penguin":"I love the water! Also fish."}


start = print("Welcome to the animal guessing game "
              "A) Start B) Quit")
ask = input("Enter here: ")
if ask == "A" or "a":
    print(f"Welcome! Can you get a score of {len(animals)}")
userScore = 0
funFacts = list(animals.values())
while (len(funFacts) > 0):
    randomFact = random.choice(funFacts) #choosing a random fact
    funFacts.remove(randomFact)
    answer = input(f"Fact: {randomFact} Your answer here: ")
    try:
        if (animals[answer] == randomFact):
            print("Well done you got it!")
            userScore += 1
    except:
        print("That was the wrong answer: ")

print(f"You got a score of {userScore}")
match userScore:
    case 5:
        print("Wellll done! You are great at knowing you animals! :)")
    case 4:
        print("Wow! Your good at this!")
    case 3:
        print("You average. WELL done")
    case 2:
        print("You can do better tho")
    case 1:
        print("Did you even try? :P")
    case _:
        print("???? Have you never seen animals? :)")




if ask == "B" or "b":
    print("Game Finished...")




