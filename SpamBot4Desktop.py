############################################
#
#               ѕραмвσт4∂єѕктσρ
#
#	     Made by @_AppleExpert
#
# Support:
# Twitter- https://twitter.com/_AppleExpert
#
############################################


from keyboard import press
from time import sleep
import pyautogui, os

def end(): #Exit function with a message
    print('\nThanks for using SpamBot4Desktop\n')
    exit(0)

def main(): #main function
    os.system('cls')
    print('''
 
ѕραмвσт4∂єѕктσρ
                
Steps:
1. Type your text that you would to spam and the number of times to spam.
2. Hit enter and point your cursor to the input box.
3. The spam will begin in 10 seconds.

IMPORTANT: This tool will spam anywhere your cursor points at, so make sure you put it where you want it.

''')

    spam = input("Enter text:\n-> ")
    num = input("\nHow many times do you want to spam? (Leave it blank for unlimited):\n-> ")
   
    print('\nThe spam will begin in 10 seconds... BRACE YOURSELF !!!\n')
    print("To stop the spam, return to terminal and close it\n\n")
    sleep(10)

    for _ in range(int(num)):
        sleep(0.4)
        pyautogui.typewrite(spam)
        press('enter')
    
    end()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopping script')
        end()
