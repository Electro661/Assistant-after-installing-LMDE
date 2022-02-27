# pip`s command`s for install 
# pip install requests 
# pip install subprocess
#print('If you dont want to install any software, then remove the command yourself');
 #print('Welcome to AFIL(Assistant-after-installing-LMDE');
import subprocess

subprocess.call('sudo su', shell=True) #this command is needed in order not to constantly enter the password
subprocess.call('apt-get update --allow-releaseinfo-change', shell=True)
subprocess.call('apt dist-upgrade', shell=True)
subprocess.call(' apt-get install neofetch ', shell=True)
subprocess.call(' apt-get install wine', shell=True)
subprocess.call(' apt-get install winetricks', shell=True)
subprocess.call(' apt install keepassxc', shell=True)
subprocess.call('apt-get install wireshark', shell=True)
subprocess.call('apt-get install qbittrent ', shell=True)
#Thanks for using my soft =)
