# My Python Journey
This is my github repo for learning python. I will be working on replit website and then posting here each day of what I learn.


### Day 1 / 100
```
# Day 1/100 - Strings and Printing Output
# Using 3 double quotes can be used to print a lot of words in exactly the format you want rather than printing all on one line.

print("""Alex
July 21st, 2019
I am signing up for Replit's 100 days of Python challenge!
I will make sure to spend some time every day coding along, for a minium of 10 minutes a day.
I'll be using Replit, an amzing onine IDE so I can do this from my phone wherever I happen to be. No execuses for not coding from the middle of a field!
I am feeling 😎
You can follow my progress at replit.com/@alexdavis101""")
```

### Day 2 / 100
```
# Day 2 - Learning variables and input request
# You can print variables by using either methods below

print("Hello, and welcome!")
print()
userName = input("What is your name? ")
userFood = input("What is your favorite food? ")
userMusic = input("What is your favorite type of music genre? ")
userHome = input("What state are you from? ")
print("Thank you for your input!")
print()
print(f"So you are {userName}, your favorite food is {userFood}, your favorite music genre is {userMusic}, and you live in the great state of {userHome}. That's really cool! ")
```

### Day 3 / 100
```
# Day 3 - Concatenation
# You can concatenate strings and variables using the "," in between to easily use variables in your print outputs.

print("=== Your Song Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
song, totally copyright free 😭""")
print()
name = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your person's name: ")
print()
print("There was a person called", name)
print("Who did something cool like", thing, "at the wonderful", place, "where you'll find me", rhyme)
```print("=== Your Song Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
song, totally copyright free 😭""")
print()
name = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your person's name: ")
print()
print("There was a person called", name)
print("Who did something cool like", thing, "at the wonderful", place, "where you'll find me", rhyme)
```

### Day 4 / 100
```
# Concatenation project for adventure simulation with colored text
# You can add color to text by inserting \033["color text"m before the text and end it.

print("=== Your Adventure Simulator ===")
print("""You'll be asked a bunch of questions that will then be used to create the story with YOU as the star!""")

print()
name = input("Your name: ")
boss = input("Your worst enemy's name: ")
superPower = input("Your super power: ")
print()

print("Our story begins as our hero named", name, "approaches a", "\033[31m", "foreboading castle", "\033[0m","...")
print()

print("Suddenly, a","\033[33m", "bolt of lighting","\033[0m", "strikes the ground and revals the terrible", boss, "who has been striking fear in the land.")
print()

print("You, however, the amazing", name, "have been training and have gained the power of", superPower, "to help you fight the evil", boss, "and save everyone!")
print()

print("With the power of", superPower, "you fight bravely and finally bring down", boss, "for good!")

```