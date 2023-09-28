### Day 4 / 100
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