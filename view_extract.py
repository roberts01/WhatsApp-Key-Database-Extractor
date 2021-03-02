import os
import subprocess
import re

# Global variables
isJAVAInstalled = False

# Global command line helpers
adb = 'adb'
delete = 'rm -rf'
tmp = 'tmp/'
confirmDelete = ''
grep = 'grep'
curl = 'curl'
helpers = 'helpers/'
bin = 'bin/'
tar = 'tar'
extracted = 'extracted/'


if __name__ == "__main__":

    os.system('clear')
    global isJAVAInstalled
    isJAVAInstalled = CheckJAVA()
    ExtractAB(isJAVAInstalled)

def CheckJAVA(): 
    JAVAVersion = re.search('(?<=version ")(.*)(?=")', str(subprocess.check_output('java -version'.split(), stderr=subprocess.STDOUT))).group(1)
    isJAVAInstalled = True if(JAVAVersion) else False
    if (isJAVAInstalled) : 
        print('Found Java installed on system. Continuing...')
        return isJAVAInstalled
    else: 
        noJAVAContinue = print('It looks like you don\'t have JAVA installed on your system. Please install.')
        Exit()



def Exit():
    print('\nExiting...')
    os.system('adb kill-server')
    quit()

def ExtractAB(isJAVAInstalled):
    if not (isJAVAInstalled): 
        print('Can not detect JAVA on system.')
        Exit()

    if(os.path.isfile(tmp + 'whatsapp.ab')) :
        print('Found whatsapp.ab in tmp folder. Continuing')
        userName = input('Enter a reference name for this user. : ') or 'user'
        abPass = input('Please enter password for backup (leave empty for none) : ')
        try : 
            os.system('java -jar ' + bin + 'abe.jar unpack ' + tmp + 'whatsapp.ab ' + tmp + 'whatsapp.tar ' + str(abPass))
            print('Successfully decompressed '+ tmp + 'whatsapp.ab ' + tmp + 'whatsapp.tar ')

            os.mkdir(extracted + userName) if not (os.path.isdir(extracted + userName)) else print('Folder already exists.')
            print('Taking out main files in ' + tmp + ' folder temporaily.')
            try : 
                bin = ''
                os.system(bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/f/key') ; os.replace('tmp/apps/com.whatsapp/f/key', extracted + userName + '/key')
                os.system(bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/db/msgstore.db') ; os.replace('tmp/apps/com.whatsapp/db/msgstore.db', extracted + userName + '/msgstore.db')
                os.system(bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/db/wa.db') ; os.replace('tmp/apps/com.whatsapp/db/wa.db', extracted + userName + '/wa.db')
                os.system(bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/db/axolotl.db') ; os.replace('tmp/apps/com.whatsapp/db/axolotl.db' , extracted + userName + '/axolotl.db')
                os.system(bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/db/chatsettings.db') ; os.replace('tmp/apps/com.whatsapp/db/chatsettings.db', extracted + userName + '/chatsettings.db')
                # Reset bin here...
                
                print('\nIf you do not see any errors in above lines in extracting/fluffing whatsapp.ab you SHOULD choose to clean temporary folder. It contains your chats in UN-ENCRYPTED format.','green')
                _cleanTemp = input('Would you like to clean tmp folder? (default y) : ','green') or 'y'
                if(_cleanTemp.upper()=='y'.upper()): 
                    if(os.path.isdir(tmp)): 
                        print('Cleaning up tmp folder...')
                        os.remove('tmp/whatsapp.tar')
                        os.remove('tmp/whatsapp.ab')
                        #os.remove('tmp\WhatsAppbackup.apk') Not removing backup apk

            except Exception as e : 
                print(e)
                CleanTmp()

        except Exception as e : 
            print(e)
