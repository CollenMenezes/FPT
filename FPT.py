"""
MIT License

Copyright (c) 2022 Collen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import time
import requests
import random

def main():

    class color():
        b = "\u001b[1m"

    key_list = ["kxtKQ4u52rWkKYJVxZiOKXofQzC7FTpq","dkvdxkjQTMPTIzyObiRXUkuKYoq6zGcb"]
    key = random.choice(key_list)

    def banner():
        os.system ("clear")
        print (f"""
███████╗██████╗ ████████╗
██╔════╝██╔══██╗╚══██╔══╝
█████╗  ██████╔╝   ██║   
██╔══╝  ██╔═══╝    ██║   
██║     ██║        ██║   
╚═╝     ╚═╝        ╚═╝
{color.b}Fraud Prevention Tools\n""")
        time.sleep(1)

    def ip_scan():

        banner()
        ip_input = input("[-] PASTE OR ENTER THE ADDRESS HERE: ")
        
        try:
            url = requests.get (f"https://ipqualityscore.com/api/json/ip/{key}/{ip_input}")
        except:
            banner()
            print("[-] IT LOOKS LIKE YOU'RE NOT CONNECTED TO THE INTERNET!")
            time.sleep(3)
            main()

        data = url.json()

        
        if data["success"]:
            banner()
            print ("[-] COUNTRY CODE:", data["country_code"])
            time.sleep(1)
            print ("[-] CITY:", data["city"])
            time.sleep(1)
            print ("[-] REGION:", data["region"])
            time.sleep(1)
            print ("[-] LATITUDE:", data["latitude"])
            time.sleep(1)
            print ("[-] LONGITUDE:", data["longitude"])
            time.sleep(1)
            print ("[-] TIMEZONE:", data["timezone"])
            time.sleep(1)     
            print ("[-] FRAUD SCORE:", data["fraud_score"])
            new_ip_scan = input("\n[-] DO YOU WANT TO MAKE A NEW SCAN? (Y/N) ")
            if new_ip_scan == "Y" or new_ip_scan == "y":
                ip_scan()
            elif new_ip_scan == "N" or new_ip_scan == "n":
                main()
            else:
                banner()
                print ("[-] INVALID OPTION!")
                time.sleep(3)
                main()

        else:
            banner()
            print ("[-] MAKE SURE YOU ENTERED THE DATA CORRECTLY!")
            time.sleep(3)
            ip_scan()

    def email_scan():

        banner()
        email_input = input("[-] PASTE OR ENTER THE EMAIL HERE: ")

        try:
            url = requests.get (f"https://ipqualityscore.com/api/json/email/{key}/{email_input}")
        except:
            banner()
            print("[-] IT LOOKS LIKE YOU'RE NOT CONNECTED TO THE INTERNET!")
            time.sleep(3)
            main()
            
        data = url.json()

        if data["valid"]:
            banner()
            print ("[-] FISRT NAME:", data["first_name"])
            time.sleep(1)
            var_suspect = "Yeah" if data["suspect"] else "Nope"
            print ("[-] SUSPECT?", var_suspect)
            time.sleep(1)
            print ("[-] FRAUD SCORE:", data["fraud_score"])
            time.sleep(1)
            var_leaked = "Yeah" if data["leaked"] else "Nope"
            print ("[-] LEAKED?", var_leaked)
            #print ("[-] USER ACTIVITY:", data["user_activity"])
            new_email_scan = input ("\n[-] DO YOU WANT TO MAKE A NEW SCAN? (Y/N) ")
            if new_email_scan == "Y" or new_email_scan == "y":
                email_scan()
            elif new_email_scan == "N" or new_email_scan == "n":
                main()
            else:
                banner()
                print ("[-] INVALID OPTION!")
                time.sleep(3)
                main()

        else:
            banner()
            print("[-] MAYBE THIS EMAIL IS NOT VALID!")
            time.sleep(3)
            email_scan()

    def number_scan():
        
        banner()
        phone_input = input ("[-] PASTE OR ENTER THE PHONE NUMBER HERE: ")
        try:
            url = requests.get (f"https://ipqualityscore.com/api/json/phone/{key}/{phone_input}")
        except:
            banner()
            print ("[-] IT LOOKS LIKE YOU'RE NOT CONNECTED TO THE INTERNET!")
            time.sleep(3)
            main()
        
        data = url.json()

        if data["success"]:
            banner()
            print ("[-] FORMATTED:", data["formatted"])
            time.sleep(1)
            print ("[-] LOCAL FORMAT:", data["local_format"])
            time.sleep(1)
            var_active = "Yeah" if data["active"] else "Nope"
            print ("[-] ACTIVE?", var_active)
            time.sleep(1)
            var_spam = "Yeah" if data["spammer"] else "Nope"
            print ("[-] SPAMMER?", var_spam)
            time.sleep(1)
            print ("[-] COUNTRY:", data["country"])
            time.sleep(1)
            print ("[-] REGION:", data["region"])
            time.sleep(1)
            print ("[-] CITY:", data["city"])
            time.sleep(1)
            print ("[-] ZIP CODE:", data["zip_code"])
            time.sleep(1)
            print ("[-] FRAUD SCORE:", data["fraud_score"])
            new_phone_scan = input("[-] DO YOU WANT TO MAKE A NEW SCAN? (Y/N) ")
            if new_phone_scan == "Y" or new_phone_scan == "y":
                number_scan()
            elif new_phone_scan == "N" or new_phone_scan == "n":
                main()
            else:
                banner()
                print ("[-] INVALID OPTION!")
                time.sleep(3)
                main()

        else:
            banner()
            print ("[-] INVALID PHONE NUMBER! YOU MUST PUT LIKE THIS EXAMPLE: +18007132618")
            time.sleep(3)
            number_scan()

    def url_scan():

        banner()
        url_input = input ("[-] PASTE OR ENTER THE URL HERE: ")
        try:
            url = requests.get (f"https://ipqualityscore.com/api/json/url/{key}/{url_input}")
        except:
            banner()
            print("[-] IT LOOKS LIKE YOU'RE NOT CONNECTED TO THE INTERNET!")
            time.sleep(3)
            main()

        data = url.json()

        if data["success"]:
            banner()
            var_safe = "Nope" if data["unsafe"] else "Yeah"
            print ("[-] SAFE?", var_safe)
            time.sleep(1)
            print ("[-] DOMAIN:", data["domain"])
            time.sleep(1)
            print ("[-] IP ADDRESS:", data["ip_address"])
            time.sleep(1)
            print ("[-] STATUS CODE:", data["status_code"])
            time.sleep(1)
            var_spam = "Yeah" if data["spamming"] else "Nope"
            print ("[-] SPAM?", var_spam)
            time.sleep(1)
            var_malware = "Yeah" if data["malware"] else "Nope"
            print ("[-] MALWARE?", var_malware)
            time.sleep(1)
            var_phish = "Yeah" if data["phishing"] else "Nope"
            print ("[-] PHISHING?", var_phish)
            new_url_scan = input ("[-] DO YOU WANT TO MAKE A NEW SCAN? (Y/N) ")
            if new_url_scan == "Y" or new_url_scan == "y":
                url_scan()
            elif new_url_scan == "N" or new_url_scan == "n":
                main()
            else:
                banner()
                print ("[-] INVALID OPTION!")
                time.sleep(3)
                main()

        else:
            banner()
            print ("[-] THE LINK MAY BE WRONG OR ENTER ACCORDING TO THE EXAMPLE: www.google.com")
            time.sleep(3)
            url_scan()

    def show_menu():

        banner()
        print ("[01] - IP SCAN\n[02] - EMAIL VERIFICATION\n[03] - PHONE NUMBER VALIDATION\n[04] - URL SCANNER\n[00] - EXIT")

        try:
            menu_choice = int(input ("\n[-] CHOOSE A TASK: "))
        except ValueError:
            banner()
            print ("[-] INVALID OPTION!")
            time.sleep(3)
            main()

        if menu_choice == 1:
            ip_scan()
        elif menu_choice == 2:
            email_scan()
        elif menu_choice == 3:
            number_scan()
        elif menu_choice == 4:
            url_scan()
        elif menu_choice == 0:
            banner()
            print ("[-] SEE YOU!")
            time.sleep(3)
            os.system("clear")
            exit()
        else:
            banner()
            print ("[-] INVALID OPTION")
            time.sleep(3)
            main()

    show_menu()

main ()
