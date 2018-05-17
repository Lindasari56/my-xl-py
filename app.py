# -*- coding: utf-8 -*-
import os
import sys
import platform
from xlpy import *

def main_menu():
    clear()
    print(
        "   .::XL - Direct Purchase Package::." +
        "\nPlease choose the menu you want to start:"
        "\n[1] Purchase Package" + 
        "\n[2] Request OTP Code" +
        "\n[3] Request Password"  +
        "\n[4] Serviceid" +
        "\n[0] Quit"
    )
    choice = str(input(" >> "))
    exec_menu(choice)
    return

def exec_menu(choice):
    clear()
    if(choice == ''):
        menu_actions['main']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main']()
    return

def menu_1():
    again = 1
    while(again == 1):
        clear()
        print(".::Purchase Package Menu::.")
        msisdn = str(input("Input your MSISDN >> "))
        po = str(input("Input your OTP >> "))
        serviceid = str(input("Input your Service ID >> "))
        xl = XL(msisdn)
        r = xl.loginWithOTP(po)
        if(r != False):
            print(xl.purchasePackage(serviceid)['message'])
            decision = str(input("Want to repeat the process [Y/N]? >> "))
            again = 0 if(decision == 'N' or 'n') else again
        else:
            print("Login failed try again")
            decision = str(input("Want to repeat the process [Y/N]? >> "))
            again = 0 if(decision == 'N' or 'n') else again
    menu_actions['main']()


def menu_2():
    again = 1
    while(again == 1):
        clear()
        print(".::OTP Code Menu::.")
        msisdn = str(input("Input your MSISDN >> "))
        xl = XL(msisdn)
        print(xl.reqOTP()['message'])
        decision = str(input("Want to repeat the process [Y/N]? >> "))
        again = 0 if(decision == 'N' or 'n') else again
    menu_actions['main']()

def menu_4():
    again = 1
    while(again == 1):
        clear()
        print(".::Service Id::.")
 "\n[1]Xtra Kuota 30GB 30hr, 10K 8110577" +
 "\n[1]Xtra Combo Lite 25GB, 30hr, 99.900K 8210886" +
 "\n[1]Xtra Combo Lite 17GB, 30hr, 79.900K 8210885" +
 "\n[1]Xtra Combo Lite 9GB, 30hr, 49.900K 8210884" +
 "\n[1]Xtra Combo Lite 5GB, 30hr, 29.900K 8210883" +
 "\n[1]Xtra Combo Lite 3GB, 30hr, 19.900K 8210882" +
 "\n[1]Combo Xtra 5GB+5GB 30hr,59rb 8211183" +
 "\n[1]Combo Xtra 10GB+10GB 30hr,89rb 8211184
" +
 "\n[1]Combo Xtra 15GB+15GB 30hr,129rb8211185" +
 "\n[1]XL GO IZI,10 GB , Rp0, 7hr 8211231" +
        print(xl.reqOTP()['message'])
        decision = str(input("Want to repeat the process [Y/N]? >> "))
        again = 0 if(decision == 'N' or 'n') else again
    menu_actions['main']()


def menu_3():
    again = 1
    while(again == 1):
        clear()
        print(".::Password Menu::.")
        msisdn = str(input("Input your MSISDN >> "))
        xl = XL(msisdn)
        print(xl.reqPassword()['message'])
        decision = str(input("Want to repeat the process [Y/N]? >> "))
        again = 0 if(decision == 'N' or 'n') else again
    menu_actions['main']()

def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "3" : menu_3,
    "4" : menu_4,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()
