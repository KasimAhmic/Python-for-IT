import re

def firstTest(password):
    # Setup boolean variables matching password requirements
    upper = False
    lower = False
    digit = False
    length = False

    # Loop through all characters in password and determine if each of the requirements are met
    for char in password:
        if char.isupper(): # Tests for uppercase letters
            upper = True
        elif char.islower(): # Tests for lowercase letters
            lower = True
        elif char.isdigit(): # Tests for numbers
            digit = True

    if len(password) >= 8: # Tests for password length
        length = True

    # If any of the requirements are not met, give a reason as to why
    reason = ''
    if not upper:
        reason += ' - password has no uppercase letters'
    if not lower:
        reason += ' - password has no lowercase letters'
    if not digit:
        reason += ' - password has no numbers'
    if not length:
        reason += ' - password is too short'

    # If all password requirements are met, return True. Otherwise return the reason that the password is not strong enough
    if upper and lower and digit and length:
        return True
    else:
        return reason

def secondTest(password):
    # Setup boolean variables matching password requirements
    upper = bool(re.search(r'[A-Z]', password)) # Tests for uppercase letters
    lower = bool(re.search(r'[a-z]', password)) # Tests for lowercase letters
    digit = bool(re.search(r'[0-9]', password)) # Tests for numbers
    length = bool(re.search(r'\S{8,}', password)) # Tests for password length

    # If any of the requirements are not met, give a reason as to why
    reason = ''
    if not upper:
        reason += ' - password has no uppercase letters'
    if not lower:
        reason += ' - password has no lowercase letters'
    if not digit:
        reason += ' - password has no numbers'
    if not length:
        reason += ' - password is too short'

    # If all password requirements are met, return True. Otherwise return the reason that the password is not strong enough
    if upper and lower and digit and length:
        return True
    else:
        return reason

def main():
    # Continuously prompt user for password entry
    while True:
        # Prompt user for password
        password = input('Enter a password (or \'quit\' to exit): ')

        # If user enters 'quit' exit the program
        if password == 'quit':
            print('\nBye!')
            break

        # Run firstTest and secondTest functions and assign the results to their respective variables
        firstResult = firstTest(password)
        secondResult = secondTest(password)

        # If the users password is strong, print Strong. Otherwise print Not Strong along with the reason
        if firstResult == True:
            print('First Test: Strong')
        else:
            print('First Test: Not Strong' + firstResult)

        if secondResult == True:
            print('Second Test: Strong')
        else:
            print('Second Test: Not Strong' + secondResult)

        # If password passes both tests, exit the program
        if firstResult == True and secondResult == True:
            print('\nBye!')
            break

        print()

if __name__ == '__main__':
    main()