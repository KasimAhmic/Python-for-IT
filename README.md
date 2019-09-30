# COP 4931 - Python for IT
A small collection of Python coursework I did in college. All the files can be run by running the following command:

```python
py FILENAME.py
```

## Assignment 1 - a1.py - Grade: 100%
I am unable to find the page that lists the requirements for Assignment 1. It is a shopping cart application that when run, presents a user with a menu. The user then input their name, and the current date. From there, they input the items they'd like to purcahse, the price, and the quantity. Once their cart is filled, they can modify it by adjusting the quantities and remove the items altogether.

## Project 1 - p1.py - Grade: 100%
The requirements for Project 1 were as follows:

Write a program in Python that asks the user to enter a password (a string) and checks if the password is strong.
- A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.
- Your program must test the password twice, by calling 2 different functions (that you must write).
  - The first function uses a loop to check each character in the string and decide if the password is strong. Do not use regular expressions in the first function.
  - The second function uses regular expressions to make sure the password is strong.  You may need to test the string against multiple regex patterns to validate its strength.
- Display messages to the user indicating whether or not the password is strong.
  - If your message can give the user more details (what was wrong), that is even better.
- Allow the user to keep entering passwords until a strong password is entered, or until the user types 'quit'.

## Project 2 - p2.py - Grade 100%
The requirements for Project 2 were as follows:

Write a program in Python that takes (from the command-line) the URL of a web page, and then lists the URLs for every link in the given web page. It also displays whether or not those links lead to existing pages or if they are broken links. 
- If the given URL is not valid (broken link), display a message. 
- If the URL is valid, look for all links in that page.
- The program should list the URL for each link and a status (valid or broken). Hint: when trying to access a web page, a 404 “Not Found” status code indicates a broken link.
- Your program must work with any URL passed on the command-line.

## Project 3 - p3.py - Grade: 120%
The requirements for Project 3 were as follows:

Write a program that reads an Excel spreadsheet with students' names and grades, and finds the students with missing grades and the total number of missing grades. For extra credit, use the Twilio module to send a text message (sms) with the missing grades to a given phone number.

- The program must accept 5 command-line arguments, in the following order:
  - Excel filename
  - Twilio account SID
  - Twilio authorization token
  - Phone number that will receive the text message.
  - Phone number that will send the text message.
- If you choose not to do the extra credit, your program will use only the first command-line argument (filename) and ignore the others.
- The program will attempt to load the Excel file (aka workbook) and access the active worksheet.
  - If there are any errors (eg. file not found), a friendly error message must be displayed (instead of a runtime error).
  - A sample Excel file is here: p3.xlsx
  - We will test your code with different test files.
  - The test file will only have one sheet (which is the active sheet).
  - The first row always has the column titles (student, assignment 1, ...).
  - The first column always has the names of the students. The other columns have grades.
  - Each test file may have a different number of rows and columns (the number of students and assignments is different from the sample file).
- The program will count the number of empty cells (missing grades).
- The program will display a message with the total number of missing grades and the names of the students that have missing grades.
  - Each student should be displayed only once (even if the student has many missing grades).
- Extra credit: Use Twilio to send a text message with the same information you displayed on the screen.
  - You will need a trial account with Twilio (free). 
  - The SID, authorization token, "to" number, and "from" number must be taken from the command-line arguments - do not hard-code them in your program. I'll use my own twilio account and phone number when testing the programs.