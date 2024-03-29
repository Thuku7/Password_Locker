#!/usr/bin/env python3.8
from unittest import result
from user import User
from credentials import Credentials
import random
import string
import sys


def create_user(fname, lname, password):
    """
    Function that will create a new user
    """
    new_user = User(fname, lname,password)
    return new_user

def save_user(user):
    """
    Function to save user
    """
    user.save_user()


def create_user_credentials(platform_name, platform_username, platform_password):
    """
    Function that will create a new credential
    """
    new_user_credentials = Credentials(social_name, social_username, social_password)
    return new_user_credentials

def save_user_credentials(credential):
    """
    Function to save user credentials
    """
    Credentials.save_credentials(credential)


def display_credentials():
    """
    A function that will return the credential list
    """
    return Credentials.display_credentials()

def find_user(username):
    """
    Function that will find a user by their username and return the user
    """
    return User.find_by_username(username)

def delete_credentials(credential):
    """
    Function that will delete a user credential
    """
    Credentials.delete_credentials() 

def find_credentials(credential):
    """
    Function that will look for a specific account in the stored credentials
    """

    return Credentials.find_credentials(credential)


def check_existing_credentials(platform):
    """
    Function that will check for a credential
    """
    return Credentials.credential_exists(platform)

@classmethod
def password_gen(length):
    """
    generate random password
    """
    letters = string.ascii_lowercase
    result1 = ''.join((random.sample(letters, length)))  
    platform_password = result1
    return platform_password  


def main():
    print("\n")
    print("\u001b[Welcome to Password-Locker!.\u001b[0m")
    print("\n")

    user_name = input("\u001b[36mEnter your user name: \u001b[0m")


    print(f"What would you like to do? A. Login | B. Create an account")

    short_code = input().lower()

    while True:
        if short_code == "a":
            print()
           
            platform_search = input("Enter the Social Media you want to search for: ")
            if check_existing_credentials(social_search):
                search_credential = find_credentials(social_search)

            else:
                print("\u001b[31;1mThe credential was not found, Try Again\u001b[0m")
                
                sys.exit()

        elif short_code == "b":

            print("Create an Account")

            new_user_first_name = input("Enter your first name: ")
            new_user_last_name = input("Enter your last name: ")
            print("Would you like to create your password or generate one, A. Create | B. Generate")
            create_password_option = input().lower()

            if create_password_option == "Cr":
                create_password = input("Enter your password: ")
                confirmed_password = input("\u001b[33mConfirm password: \u001b[0m")
                if confirmed_password == create_password:
                    print("\u001b[32mAccount Created Succesfully.\u001b[0m")
                    new_user_password = confirmed_password
                    save_user(create_user(new_user_first_name, new_user_last_name,new_user_password))

                
                else:
                    print("\N{ESC}[31mPassword Doesn't match. Try again\u001b[0m")
                    break
            elif create_password_option == "b": 

                password_length = int(input("What length would you like your password to be,i.e 5,8..."))

                letters = string.ascii_lowercase
                auto_gen_password =  ( ''.join(random.choice(letters) for i in range(password_length)))


                print("\u001b[35;1mYour generated password is: \u001b[0m", auto_gen_password)
                new_user_password = auto_gen_password

                while True:

                    save_user(create_user(new_user_first_name, new_user_last_name, new_user_password))
                    print("\n")                  
                    print(f"\u001b[32;1mSuccessfully, created {new_user_first_name} account\u001b[0m")
                    user_decision = input("\u001b[34mA. To view Your saved Passwords | B. Exit\u001b[0m: ").lower()

                    if user_decision == "a":
                        if display_credentials():
                            print("Heres a list of your credentials")

                            for credential in display_credentials():
                                print(f"Account: {credential.platform_name}")

                        else:
                            print("\u001b[31mYou don't seem to have any credentials saved\u001b[0m")
                            print("Exit")
                            sys.exit()

                    elif user_decision == "b":
                        print(f"You have logged out {new_user_first_name} .Remember: We remember your passwords so that you dont have to.")
                        sys.exit()

            
            while True:
                print("\n")
                print("Proceed to login")


                login_name = input("Enter your name: ")
                login_password = input("Enter password: ")
                new_user_password = input("\u001b[33mConfirm password: \u001b[0m")


                if login_name == new_user_first_name and login_password == confirmed_password:
                    print(f"\u001b[32m{new_user_first_name} Login successful!\u001b[0m")
                    print("\n")


                    print("Create a Password Vault")
                    platform = input("Enter platform name...")
                    platform_username  = input("Enter your user name: ")
                    platform_pswrd = input("Enter password: ")


                    save_user_credentials(create_user_credentials(platform,platform_username, platform_pswrd))


                    print(f"\u001b[32mPassword Vault for {platform} with the username {platform_username} created successfully\u001b[0m")

                    print("\u001b[34mA. To view Your saved Passwords | B. Exit| C. Delete Credential\u001b[0m")
                    choice = input().lower()

                    if choice == "a":
                        if display_credentials():
                            print("\n")
                            print("Here is a list of all your credentials")
                            print("\n")

                            for credential in display_credentials():
                                # print("We should be getting something")
                                print(f"Account: {credential.platform_name}")

                        else:
                            print("\u001b[31mYou don't seem to have any credentials saved\u001b[0m")

                    elif choice == "b":

                        print(f"You have logged out {login_name} .Remember: We remember your passwords so that you dont have to.")
                        break


                    elif choice == "c":
                        print("Which account would you like to delete? ")
                        delete_acc = input("Enter account name, i.e insatgram: ")
                        delete_credentials(find_credentials(delete_acc))
                        print(f"{delete_acc} has been deleted succesfully!")

                else:
                    print("\N{ESC}[31mLogin Failed. Enter valid credentials\u001b[0m")
                    break  

            print("Bye")
            break                            


if __name__ == "__main__":
    main()