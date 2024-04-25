#!/data/data/com.termux/files/usr/bin/bash
# This is a simple bash script for installing Termux gui version work on Termux-x11.
#cradit Sanatani-hacker.
clear
echo "TERMUX ngrok SETUP SCRIPT BY SANATANI-HACKER "
echo "Telegram: https://t.me/temuxhacking"
echo "Github: https://github.com/dark-assist"
sleep 2.5
cd $HOME
echo "Updating Termux and Installing Dependencies...."
apt update ;apt install wget -y
echo "Detecting CPU architecture..."
arch=$(dpkg --print-architecture)
case "$arch" in
    amd64)
        url="https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz"
        ;;
    arm64)
        url="https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz"
        ;;
    armhf)
        url="https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm.tgz"
        ;;
    i386)
        url="https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-386.tgz"
        ;;
esac
echo "Downloading NGROK for $arch..."
wget "$url"
tar -xvf ngrok*.tgz
echo "NGROK Downloaded and Extracted Successfully!"
sleep 1.5
clear
echo "Opening Ngrok Dashboard...."
termux-open-url "https://dashboard.ngrok.com/get-started/your-authtoken"
sleep 2
ln -sf /data/data/com.termux/files/home/ngrok /data/data/com.termux/files/usr/bin/
echo "Run 'ngrok authtoken (your token)' to Add Your Authorization Token...."
echo "Usage Example:- ngrok http 8080"
echo "If Forwarding Not Start Try to Turn On Your Phone's Hotspot...."
echo "If Any Problem Watch This Video...."
echo "Video: Coming Soon... :)"
