### Day  8 / 100

#Review of al previous days

```
print("### Welcome to Joke of the Day! ###")
name = input("Please enter your name: ")
hobby = input("What is your favority hobby: ")
print()
print(f"Wow {name}! Your favorite hobby is {hobby}? That sounds like a lot of fun!")
print()

promptJoke = input("Want to hear the joke of the day? (y/n) ").lower()
if promptJoke == "y" or promptJoke == "yes":
    print("Awesome! I have one for each day of the week!")
    dayofweek = input("What day of the week is it? ").lower()
  
    if dayofweek == "monday":
      print("What do you call a cow with no legs?")
      print("Ground Beef!")

    elif dayofweek =="tuesday":
      print("What kind of animal do you not play cards with?")
      print("A cheetah!")

    elif dayofweek == "wednesday":
      print("Why couldn't the skeleton go to the scary movie?")
      print("He didn't have the guts!")
      
    elif dayofweek == "thursday":
      print("What is a ghost favorite ice cream?")
      print("Boo Berry!")

    elif dayofweek == "friday":
      print("What is brown and sticky?")
      print("A stick!")

    else:
      print("Please enter a day of the week to recieve a joke.")

elif promptJoke == "n" or promptJoke == "no":
  print("Okay, maybe next time!")

else:
  print("Please enter yes or no (y/n)")
```