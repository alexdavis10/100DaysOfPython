### Day 7 / 100
```
# Nested if statements. Can nest additional if statements inside other if statements to add additional questions/conditions for program.

tvShow = input("What is your favorite tv show? ")

if tvShow == "star wars":
  print("I'm sure you do.")
  q1 = input("What is your favorite trilogy? prequel, original, sequal: ")
  if q1 == "prequel":
    print("Yeah Haden is pretty great!")
  elif q1 == "original":
    print("You can't beat James Earl Jones!")
  elif q1 == "sequal":
    print("Get out...")
else:
  print(f"{tvShow} is pretty cool. You should watch Star Wars.")
  ```