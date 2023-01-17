import random
import string
import os
import time
import webbrowser
import subprocess
import pyttsx3
from requests import get
#pyttsx3 function

engine = pyttsx3.init()
engine.setProperty('rate', 150) # 150 words per minute





#Notes/todo
#Fix the encrypt/decrypt

ascii_art = """ 
   _____                      _    _____                  
  / ____|                    | |  / ____|                 
 | (___  _ __ ___   __ _ _ __| |_| (___  _   _ _ __   ___ 
  \___ \| '_ ` _ \ / _` | '__| __|\___ \| | | | '_ \ / __|
  ____) | | | | | | (_| | |  | |_ ____) | |_| | | | | (__ 
 |_____/|_| |_| |_|\__,_|_|   \__|_____/ \__, |_| |_|\___|
                                          __/ |           
                                         |___/              """







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
            engine.say(choice)
            engine.runAndWait
            main()
      elif choice == "N":
            main()
      else:
            print("Invalid choice. Please enter 'Y' or 'N'.")
            main()



def delete_file():
      choice = input("Are you sure you want to remove the following file? (Y/N): ")
      if choice == "Y":
            engine.say(choice)
            engine.runAndWait()
            os.remove(input('FileName: '))
      if choice == "N":
            main()
      else:
           say = print("The following file doesnt Exist")
           engine.say(say)
           engine.runAndWait
      main()


    
def rename_file():
      choice = input("Are you sure you want to rename the following file? (Y/N): ")
      if choice == "Y":
            engine.say(choice)
            engine.runAndWait()
            os.rename(input('OLDNAME.txt: '), input('NEW_NAME.txt: '))
      elif choice == "N":
            main()
      else:
            output = print("Invalid choice. Please enter 'Y' or 'N'.")
            engine.say(output)
            engine.runAndWait()
            main()




def good_bye():
      choice = input("Are you sure you wish to leave? (Y/N): ")
      engine.say(choice)
      engine.runAndWait()
      if choice == "Y":
        output = ("goodbye")
        engine.say(output)
        engine.runAndWait()
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
    engine.say(length)
    engine.runAndWait

    password = generate_password(int(length))
    output = print(f"Your password is: {password}")
    engine.say(output)
    engine.runAndWait()
    main()


def youtube():
      webbrowser.open("https://www.youtube.com")
      output = ("Opening Youtube.com")
      engine.say(output)
      engine.runAndWait()
      main()


def github():
      webbrowser.open("https://www.github.com")
      output = ("Opening Github.com")
      engine.say(output)
      engine.runAndWait()
      main()



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



def quotes():
    with open("quotes.txt") as f:
        lines = f.readlines()
    line = random.choice(lines)
    engine.say(line)
    engine.runAndWait()
    main()



#NOT ADDED#
def school():
      teams_path = "C:/Users/WIJA0601/AppData/Local/Microsoft/Teams"
      chrome_path = youtube()
      word_path = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/word.exe"
      subprocess.Popen([word_path])
      subprocess.Popen([teams_path])
      subprocess.Popen([chrome_path])
      main()

def cmd():
      os.system('start cmd')
      output = print("Opening CMD")
      engine.say(output)
      engine.runAndWait

def whatsmyip():
      ip = get('https://api.ipify.org').text
      output = ("This is your ip" + {ip})
      engine.say(output)
      engine.runAndWait()




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
      print("9. Quotes")
      print("10. Whats my IP")
      print("11. Open CMD")
      print("12. Goodbye")
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
            quotes()
      elif choice == "10":
            whatsmyip()
      elif choice == "11":
            cmd()
      elif choice == "12":
            good_bye()
      else:
            print("Invalid Selection, Please try again")
      
main()
