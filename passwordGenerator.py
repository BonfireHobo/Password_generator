from random import randint

# Generates password
def password_generator(password_length):
    # Avalible signs for the password
    avaliable_signs = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

    #The password
    password = ""

    # Creates the random password
    for _ in range(password_length):
        # Chose a randome characther
        x = randint(0, len(avaliable_signs) - 1)

        # Adds new random characther to the password
        password += f"{avaliable_signs[x]}"

    # Returns the generated password
    return password


# Main and front end
def main():
    # Wihle loop so you can generate more passwords
    while True:
        # User desides the length of the password
        len_password = int(input("Lengt of password? "))

        # Print out the random generated password
        print(password_generator(len_password))


# Runs main if program is runned as maain program
if __name__ == "__main__":
    main()