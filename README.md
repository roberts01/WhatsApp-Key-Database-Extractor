# Currently still in developing (beta) phase!

<p align="center">
  <h3 align="center">WhatsApp Extractor</h3>
  <p align="center">
    Extract key/msgstore.db from /data/data/com.whatsapp without root.
    <br />
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

### Preparation 

* MAKE A BACKUP OF YOUR WHATSAPP CHATS!
* USB Debugging must be enabled on the target device: Settings -> Developer Options -> (Debugging) USB debugging  
  * If you cannot find Developer Options then go to: Settings -> About phone/device and tap the Build number multiple times until you're declared a developer.

* device with Android 11 or higher:
  * activated 'ADB over network' setting. Settings -> Developer Options -> ADB over network
* device with Android 4 to 10:
  * a PC with USB functionality and installed [Android Debug Bridge for PC](https://developer.android.com/studio/releases/platform-tools)
  * Run the following commands in a terminal opened in the 'platform-tools' folder. Authorize on your phone when prompted:
   * `adb devices`
   * `adb tcpip 5555`
* Termux: Install from [Play Store](https://play.google.com/store/apps/details?id=com.termux) or [F-Droid](https://f-droid.org/packages/com.termux)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

### Installation and Usage 
Note: run all of the following commands in Termux

1. Get dependencies I
```python
pkg update && pkg upgrade
pkg install python git
```

2. Clone the repo
```python
git clone https://github.com/roberts01/wae.git
```
3. Go into the tools folder
```python
cd WhatsApp-Key-Databse-Extractor/
```

4. Get dependencies II
```python
python helpers/termux_dependencies.py
```

4.2 optional, connect adb to your device
```python
adb connect localhost
```

5. Run the tool
```python
python wa_kdbe.py
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

### Troubleshooting

```sh
* daemon not running. starting it now on port 5037 *
* daemon started successfully *
List of devices attached 
0123a4b5678 device
emulator-5554 unauthorized
```
* Choose device from "List of devices attached" : 0123a4b5678
* If you have never used USB Debugging before, you may also need to verify the fingerprint.  
* If you have set a default backup password in your Android settings, then this MUST be the  backup password that you PROVIDE when prompted to backup your data. Else it WILL fail!  
* If you get an error saying "AES encryption not allowed" then you need to update your Oracle Java Cryptography Extension (JCE) to Unlimited Strength Jurisdiction Policy Files.  
* Try to keep screen on getting termux dependencies.
* WhatsApp crashing? Run `python3 restore_whatsapp.py`. Or "clear data/storage" / uninstall and reinstall from Play Store.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

## Credits
Used and referenced dependencies and tools (big thank you to all of you!):

* [Nikolay Elenkovs Android Backup Extractor](https://github.com/nelenkov/android-backup-extractor/releases)
* [MasterDevXs ADB for Termux](https://github.com/MasterDevX/Termux-ADB)
* [MasterDevXs Java for Termux](https://github.com/MasterDevX/Termux-Java)
* [Python](https://www.python.org/)
* [Bash](https://www.gnu.org/software/bash/)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

## About The Project

This project is inspired by [EliteAndroidApps/WhatsApp-Key-DB-Extractor](https://github.com/EliteAndroidApps/WhatsApp-Key-DB-Extractor). Since Android v4.0+ Google has removed adb backup and apps no longer supported being abcked up by "adb backup -f myApp.ab -apk com.foobar.app". However there is one catch in this scenario and that is some old version of many apps including WhatsApp support that to this day, and that's the idea.

The idea is to install "Legacy Version" of WhatsApp on you device via adb and use "adb backup" to fetch files from "/data/data/com.whatsapp" folder which includes 'msgstore.db' (non encrypted) file and after that restore current WhatsApp.

Distributed under the MIT License. See `LICENSE` for more information.
