#!/usr/bin/env python3.6
from password import Password


def create_password(self, first_name, last_name, user_name, password):
    new_password = Password(self, first_name, last_name, user_name, password)
    return new_password


def generate_password():
     
     password = Password.generate_password()
     return password

def save_password(password):
        password.save_password()


def delete_passwords(Password):
        Password.delete_passwords()


def display_passwords():
       return Password.display_passwords()




def main():
       print(">>Welcome to your password list. kindly enter your name?<<")
       user_name = input()

       print(f">>hello {user_name}. What would you like to start with?<<")
       print('\n')

       while True:

              print( ">>use these short codes for better understanding :  cp - create new password, gp - generate password, dp -display passwords, ex - exit the password list , dc- delete password<<")

              short_code = input().lower()
              if short_code == 'cp':
                      print("New Password")
                      print(" 🤖 "*10)

                      print(">>which social media account?<<")
                      self = input()
                      print("First Name")
                      first_name = input()

                      print("Last Name")
                      last_name = input()

                      print("Username")
                      user_name = input()
                      while True:
                              print('\n')
                              print('Use : \n gp >>Generate a password \n ep >> Input your own password')
                              shorter_code = input().lower()
                              if shorter_code == 'gp':
                                      password = generate_password()
                                      break
                              elif shorter_code == 'ep':
                                       print("Password")
                                       password = input()
                                       break
                              else:
                                      pass
                     
                      save_password(create_password(self, first_name, last_name, user_name, password))
                      print('\n')
                      print(f"New Password {first_name} {last_name} created")
                      print('\n')
        #       elif short_code == 'dc':
        #               print("Are you sure you wanna delete your passwords?")
        #               print(">> yes    no <<")
        #               ('\n')
        #               delete_passwords = input()
        #               delete_passwords(save_password(create_password(self, first_name, last_name, user_name, password))
        #               print('\n')
        #               print(f"Passwords {create_password} deleted")
        #               print('\n')                  

              elif short_code == 'dp':
                    if display_passwords():
                        print(">>Here is a list of all your passwords<<")
                        print('\n')

                    for password in display_passwords():
                        print(f" First name = {password.first_name}\n \n Last name = {password.last_name}\n \n Username = {password.user_name} \n \n  password = {password.password}")

                        print('\n')

        #       else:
        #                 print('\n')
        #                 print("You don't seem to have any password")
        #                 print('\n')

        #       elif short_code == 'ex':
        #                 print("Bye .......")
        #                 break
              elif short_code == 'ex':
                        print("Bye .......")
                        # break:
                        print('\n')
                        print(">>You don't seem to have any password <<")
                        print('\n')
              else:
                        print("I really didn't get that. Please use the short codes provided")

if __name__ == '__main__':
        main()
