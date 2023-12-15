def login():
    # Sample username and password
    correct_username = "user123"
    correct_password = "pass456"

    # Getting user input for username and password
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")

    # Validating the entered credentials
    if entered_username == correct_username and entered_password == correct_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

def main():
    running = True
    while running:
        print("Welcome! Please login.")
        login_successful = login()

        if login_successful:
            running = False  

    print("Program ended.")

if __name__ == "__main__":
    main()
