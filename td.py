import os

print("Installing dependencies...")

print("Updating Termux")
os.system('pkg update && pkg upgrade')

print("Allow storage permission for storing extracted whatsapp.ab in interal storage:")
os.system('termux-setup-storage')

print("Installing required packaged dependencies...")
os.system('pkg install curl grep tar proot wget -y')
os.system('pip install termcolor packaging')


#os.system('wget https://github.com/MasterDevX/Termux-ADB/raw/master/InstallTools.sh && bash InstallTools.sh')
os.system('git clone https://github.com/MasterDevX/Termux-ADB.git && bash InstallTools.sh')
try:
    os.system('rm -r -f installjava') # Deleting any previous instance of installjava.
except Exception as e : 
    pass

#os.system('wget https://raw.githubusercontent.com/MasterDevX/java/master/installjava && sh installjava')
#os.system('git clone https://github.com/MasterDevX/Termux-Java.git && sh installjava')
os.system('git clone https://github.com/roberts01/tjava.git && sh installjava')

os.system('proot login')

print("Connecting ADB with local device:")
os.system('adb connect localhost')
print("Succesfully installed all dependencies.")
