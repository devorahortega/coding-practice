# Third page of practice

# 1. Write a program that uses variables to store a first and last name, then prints the full name in one line using string concatenation (the + operator).
firstname = "Ashley"
lastname = "Green"

print(firstname + " " + lastname)

# 2. Write a program that uses variables to store a first and last name, then prints the full name in one line using string interpolation (the #{} operator).
firstname = "Ashley"
lastname = "Green"

print("% s" % firstname, "% s" % lastname)

# 3. Write a program that asks the user to input a word. If the word is "marco", print "polo".
word = input("Enter word:")
print("Word is: " + word)

# 4. Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string concatenation (the + operator).
color1 = "blue"
color2 = "red"
color3 = "green"

print("The three colors in this list are " + color1 + ", " + color2 + ", " + color3 + ".")

# 5. Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string interpolation (the #{} operator).
color1 = "blue"
color2 = "red"
color3 = "green"

print("The three colors in this list are % s" % color1, "% s" % color2, "% s" % color3)

# 6. Write a program that asks the user to enter a name. If the name is not "Santa", print "You're not Santa."

# 7. Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string concatenation (the + operator).
title = "None"
author = "Bob Green"

print("The author of the books " + title + " is " + author + ".")  

# 8. Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string interpolation (the #{} operator).
title = "None"
author = "Bob Green"

print("The author of the books % s" % title, " is " "% s" % author)

# 9. Write a program that asks the user to enter a password. If the password is "Joshua", the program responds "Shall we play a game?". For any other password, the program responds "Access denied"
password = input("Enter password:")

if password == "Joshua":
    print("Shall we play a game?")
else: 
    print("Access denied.")

# 10. Write a program that uses variables to store the names of three cities, then prints out a sentence using that information with string concatenation (the + operator).
city1 = "Chicago"
city2 = "Dallas"
city3 = "Ottawa"

print("The three cities are " + city1 + ", " + city2 + ", " + city3) 
