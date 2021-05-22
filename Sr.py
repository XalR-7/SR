import time
import os

os.system('clear')
print("""
  \033[1;32m
  
  >         <
    >     <
      > < 
  A T T A C K

  """)

print("""Made for SRR by ricin
I wont be held responsible for
Any actions with this script
""")
time.sleep(4)
os.system('clear')  
print("""

░██████╗██████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗
╚█████╗░██████╔╝██████╔╝
░╚═══██╗██╔══██╗██╔══██╗
██████╔╝██║░░██║██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝
LOADING...................
""")
time.sleep(5)
os.system('clear')

from bs4 import BeautifulSoup
from collections import deque
import json
import nmap 
import os
import re
import requests
import requests.exceptions
import time
from time import gmtime, strftime
from urllib.error import URLError
from urllib.parse import urlsplit
import urllib3
import urllib.request
from urllib.request import urlopen


def banner():
    print(""" \033[1;33m
              
    
░██████╗██████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗
╚█████╗░██████╔╝██████╔╝
░╚═══██╗██╔══██╗██╔══██╗
██████╔╝██║░░██║██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝
   """)


def menu():
    print("IP INFO TOOL")
    print("--------------------")
    print("1.   Whois Lookup")
    print("2.   ip tracker")
    print("--------------------")
    print("3.   LEAVE PAGE")

def fun():
    choice = ("1")
    banner()

    while choice != ("3"):
        menu()
        choice = input("\033[1;m \033[1;32mEnter your choice:\033[1;m ")

        if choice == ("1"):
            try:
                target = input("\033[1;93mEnter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34mWhois Lookup: \033[0m".format(target) + target)
                time.sleep(1.5)
                command = ("whois " + target)
                proces = os.popen(command)
                results = str(proces.read())
                print("\033[1;33m" + results + command + "\033[1;m")

            except Exception:
                pass

        elif choice == ("2"):
            try:
                target = input("\033[1;93mEnter Domain or IP Address: \033[1;m").lower()
                url = ("http://ip-api.com/json/")
                response = urllib.request.urlopen(url + target)
                data = response.read()
                jso = json.loads(data)
                os.system("reset")
                print("\033[32m IP tracking: \033[0m".format(url) + target)
                time.sleep(1.5)

                print("\n [+] \033[34mUrl: " + target + "\033[0m")
                os.system('clear')
                print(" ")
                print("IP: " + jso["query"]+ "\033[0m")
                print(" ")
                print("Country: " + jso["country"] + "\033[0m")
                print(" ")
                print("Region: " + jso["regionName"] + "\033[0m") 
                print(" ")
                print("City: " + jso["city"] + "\033[0m")
                print(" ")
                print("Zipcode: " + jso["zip"] + "\033[0m")
                print(" ")
                print("Lat & Lon: " + str(jso['lat']) + " & " + str(jso['lon']) + "\033[0m")
                print(" ")
                print("ISP: " + jso["isp"] + "\033[0m")  
                print(" ")
                print("AS: " + jso["as"] + "\033[0m")
                print(" ")
                print("TimeZone: " + jso["timezone"] + "\033[0m")
                print(" ")

            except URLError:
                print("\033[1;32m[-] Please provide a valid IP address!\033[1;m")
        
            except Exception:
                pass
        
 
        elif choice == ("3"):
            time.sleep(1)
            print("\n\t\033[32mFUCK\033[0m LIFE \033[34mBITCHHHH\033[0m\n")

        else:
            print("\033[1;33m[-] Invalid option!\033[1;m")




if __name__ == "__main__":
    fun()
