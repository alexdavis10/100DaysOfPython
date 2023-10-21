### Day 9 / 100

# Can use integers and floats when prompting for input by using int(input("My int input")) or flot(input(My float input)).

print("Generation Generator")
print("Use this to help figure out what generation you belong to.")

print()

print("Enter your birth year:")
birth_year = int(input())

print()

if birth_year < 1925:
    print("You are a caveman! How are you still alive?")
elif birth_year >= 1925 and birth_year <= 1946:
    print("You are a Traditionalist.")
elif birth_year >= 1947 and birth_year <= 1964:
    print("You are a Baby Boomer.")
elif birth_year >= 1965 and birth_year <= 1981:
    print("You are Generation X.")
elif birth_year >= 1982 and birth_year <= 1995:
    print("You are a Millenial.")
elif birth_year >= 1996 and birth_year <= 2015:
    print("You are Generation Z.")
elif birth_year >= 2016:
    print(
        "I don't know what you are, but you are too young to be using this program."
    )
else:
    print("Please enter a valid year.")
