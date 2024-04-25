#!/data/data/com.termux/files/usr/bin/python3
# This is a simple Python script for installing Termux gui version work on Termux-x11.
# Credit to Sanatani-hacker.

import os
import subprocess
import platform

print("TERMUX ngrok SETUP SCRIPT BY SANATANI-HACKER")
print("Telegram: https://t.me/temuxhacking")
print("Github: https://github.com/dark-assist")
input("Press Enter to continue...")

print("Updating Termux and Installing Dependencies...")
subprocess.run(["apt", "update"])
subprocess.run(["apt", "install", "wget", "-y"])

print("Detecting CPU architecture...")
arch = platform.machine()
url = ""
if arch == "x86_64":
    url = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz"
    browser_command = "firefox"
elif arch == "aarch64":
    url = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz"
    browser_command = "xdg-open"
elif arch == "armv7l":
    url = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm.tgz"
    browser_command = "xdg-open"
elif arch == "i686":
    url = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-386.tgz"
    browser_command = "firefox"

print("Downloading NGROK for", arch + "...") 
subprocess.run(["wget", "-O", "ngrok.tgz", url]) 
subprocess.run(["tar", "-xvzf", "ngrok.tgz"])
print("NGROK Downloaded and Extracted Successfully!")
input("Press Enter to continue...")
print("Opening Ngrok Dashboard....")
if platform.system() == "Linux":
    subprocess.run([browser_command, "https://dashboard.ngrok.com/get-started/your-authtoken"])
else:
    print("Please open the following link in your browser to get your auth token:")
    print("https://dashboard.ngrok.com/get-started/your-authtoken")
if os.path.exists("/data/data/com.termux/files/home/"):
    subprocess.run(["ln", "-sf", "/data/data/com.termux/files/home/termgrok/ngrok", "/data/data/com.termux/files/usr/bin/"])
elif os.path.exists("/home/termgrok/"):
    subprocess.run(["ln", "-sf", "/home/termgrok/ngrok", "/bin/ngrok"])
else:
    print("Error:Can Not Create Symbolic Link.")
print("Run 'ngrok authtoken (your token)' to Add Your Authorization Token....")
print("Usage Example:- ngrok http 8080")
print("If You are Using Phone and Forwarding Not Start Try to Turn On Your Phone's Hotspot....")
print("If Any Problem Watch This Video....")
print("Video: Coming Soon... :)")

