### Day 5 / 100
#elif statements can be used to do add additional conditions to if statements that might also be true or trigger events.
#can use "and" or "or" statements to also give more conditions on top of that.
```
print("LOGIN HERE")
print("##########")
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "admin":
  print("Welcome, admin! We hope you are having a great day today!")
elif username == "alex" and password == 'davis':
  print("Welcome, Alex! We hope you are having a great day today!")
elif username == "felicia" and password == 'davis':
  print("Welcome, Felicia! We hope you are having a great day today!")
else:
  print("Wrong username or password!")
  ```