import random
import string
import os
import time
import webbrowser
import pyttsx3

#pyttsx3 function

engine = pyttsx3.init()
engine.setProperty('rate', 150) # 150 words per minute

#Notes/todo
#Fix the encrypt/decrypt

ascii_art = """ 
  _____ _             _ _   _           _                       _ _   _        _              _ 
  / ____| |           | | | | |         ( )                     | | | (_)      | |            | |
 | (___ | |_ ___  __ _| | |_| |__  _   _|/ ___   _ __ ___  _   _| | |_ _ ______| |_ ___   ___ | |
  \___ \| __/ _ \/ _` | | __| '_ \| | | | / __| | '_ ` _ \| | | | | __| |______| __/ _ \ / _ \| |
  ____) | ||  __/ (_| | | |_| | | | |_| | \__ \ | | | | | | |_| | | |_| |      | || (_) | (_) | |
 |_____/ \__\___|\__,_|_|\__|_| |_|\__, | |___/ |_| |_| |_|\__, |_|\__|_|       \__\___/ \___/|_|
                                    __/ |                   __/ |                                
                                   |___/                   |___/                                 """







#loading screen connected to Ascii art    
def show_loading_screen(text):
    # Display the loading screen with the given text
    print(ascii_art)
    print("{}".format(text))
    # Add a delay to simulate the loading process
    time.sleep(2)

# Example usage
show_loading_screen("Please wait while we load the data....")







#login function
accounts = {
    "William": "ducky2mini",
    "username2": "password2"
}

def login():
    while True:
        try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
        except KeyboardInterrupt:
            continue

        if (username in accounts) and (accounts[username] == password):
            print("Login successful!")
            output = "Welcome " + username + "what can I do for you today?"
            engine.say(output)
            engine.runAndWait()
            break
        else:
            print("Invalid username or password. Please try again.")

login()


    
    
    
    
#all command functions#


def create_file():
      choice = input("Are you sure you wish to create a file? (Y/N): ")
      if choice == "Y":
            f = open('new_file.txt', 'w')
            f.write(input("File content:"))
            f.close()
            main()
      elif choice == "N":
            main()
      else:
            print("Invalid choice. Please enter 'Y' or 'N'.")
            create_file()



def delete_file():
      choice = input("Are you sure you want to remove the following file? (Y/N): ")
      if choice == "Y":
            os.remove(input('FileName: '))
      if choice == "N":
            main()
      else:
            print("The following file doesnt Exist")
            main()


    
def rename_file():
      choice = input("Are you sure you want to rename the following file? (Y/N): ")
      if choice == "Y":
            os.rename(input('OLDNAME.txt: '), input('NEW_NAME.txt: '))
      elif choice == "N":
            main()
      else:
            print("Invalid choice. Please enter 'Y' or 'N'.")
            rename_file()




def good_bye():
      choice = input("Are you sure you wish to leave? (Y/N): ")
      if choice == "Y":
        exit()
      elif choice == "N":
        main()
        


def converter():
      def celsius_to_farenheit(temp_c):
          temp_f = (temp_c * 9/5) + 32
          return temp_f
      
      def farenheit_to_celsius(temp_f):
          temp_c = (temp_f - 32) * 5/9
          return temp_c
      temp = input("Enter a temperature: ")
      unit = input("Enter a unit (C or F): ")
      
      if unit == "C":
          temp_converted = celsius_to_farenheit(float(temp))
          unit_converted = "C"
          
      print(f"{temp} {unit} is {temp_converted} {unit_converted}")
      
      

def password_generator():
    def generate_password(length):
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        return password

    length = input("Enter the desired password length: ")

    password = generate_password(int(length))
    print(f"Your password is: {password}")
    password_generator()



def youtube():
      webbrowser.open("https://www.youtube.com")
      output = ("Opening Youtube.com")
      engine.say(output)
      engine.runAndWait()



def remember():
      output = ("What should I remember?")
      engine.say(output)
      engine.runAndWait()
      choice = input ("What should I remember?: ")
      output = ("gonna remember that for later" + choice)
      engine.say(output)
      engine.runAndWait()
      rem = open('data.txt','w')
      rem.write(choice)
      rem.close()
      main()



def knowing():
      rem_file=open('data.txt','r')
      output = ("you told me to remember that" + rem_file.read())
      engine.say(output)
      engine.runAndWait()
      main()






#Main part of the script

def main():
      print("Welcome to the multitool")
      print("pls select a tool:")
      print("1. Converter")
      print("2. Password Generator")
      print("3. Create File")
      print("4. Rename File")
      print("5. Delete File")
      print("6. Open Youtube")
      print("7. Remember")
      print("8. Knowing")
      print("9. Goodbye")
      choice = input("Enter the number of your selection: ")
      if choice == "1":
            converter()
      elif choice == "2":
            password_generator()
      elif choice == "3":
            create_file()
      elif choice == "4":
            rename_file()
      elif choice == "5":
            delete_file
      elif choice == "6":
            youtube()
      elif choice == "7":
            remember()
      elif choice == "8":
            knowing()
      elif choice == "9":
            good_bye()
      else:
            print("Invalid Selection, Please try again")
      
main()




    
    
