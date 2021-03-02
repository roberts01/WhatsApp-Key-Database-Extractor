import re
from CustomCI import CustomPrint
import os
from subprocess import check_output
from packaging import version

# Global variables
# appURLWhatsAppCDN = 'https://www.cdn.whatsapp.net/android/2.11.431/WhatsApp.apk'
appURLWhatsCryptCDN = 'https://whatcrypt.com/WhatsApp-2.11.431.apk'

def TermuxMode(ADBSerialId) : 
    _deviceName= 'adb -s ' + ADBSerialId + ' shell getprop ro.product.model'
    CustomPrint('Connected to ' + re.search("(?<=b')(.*)(?=\\\\n)", str(check_output(_deviceName.split()))).group(1) , 'green')

    _sdkVersionText = 'adb -s ' + ADBSerialId + ' shell getprop ro.build.version.sdk'
    SDKVersion = int(re.search('[0-9]{2,3}', str(check_output(_sdkVersionText.split()))).group(0))
    if (SDKVersion <= 13) : 
        CustomPrint('Unsupported device. This method only works on Android v4.0 or higer.', 'green')
        CustomPrint('Cleaning up temporary direcory.', 'green')
        os.system('rm -r -f tmp/*')
        Exit()
    _waPathText = 'adb -s ' + ADBSerialId + ' shell pm path com.whatsapp'
    WhatsAppapkPath = re.search('(?<=package:)(.*)(?=apk)', str(check_output(_waPathText.split()))).group(1) + 'apk'
    if not (WhatsAppapkPath) : CustomPrint('Looks like WhatsApp is not installed on device.') ; Exit()
    #SDPath = re.search("(?<=b')(.*)(?=\\\\n)", str(check_output('adb shell "echo $EXTERNAL_STORAGE"'.split()))).group(1)
    contentLength = int(re.search("(?<=Content-Length:)(.*[0-9])(?=)", str(check_output('curl -sI http://www.cdn.whatsapp.net/android/2.11.431/WhatsApp.apk'.split()))).group(1))
    _versionNameText = 'adb -s ' + ADBSerialId + ' shell dumpsys package com.whatsapp'
    versionName = re.search("(?<=versionName=)(.*?)(?=\\\\n)", str(check_output(_versionNameText.split()))).group(1)
    
    CustomPrint('WhatsApp Version' + versionName + ' installed on device') 
    return 1, SDKVersion, WhatsAppapkPath, versionName

def Exit():
    CustomPrint('\nExiting...', 'green')
    os.system('adb kill-server')
    quit()


