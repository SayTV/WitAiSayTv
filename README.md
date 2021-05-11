# SayTV 
![SayTV Image](/extension/splash.png)
## Summary 
Don't you hate typing with a TV remote control! And going through complex lists? SayTV is your personal TV assistant, just tell your TV!

## About SayTV
Most elders find it hard to use new tech, and “the average American over 65 spends about four hours watching TV daily“ SayTV enables using TV's without any trouble, It’s a voice assistant based on Wit.AI to help the elderly interact with new TVs easily, as simple as asking their grandkids to find something for them! We aspire to make life easier for anyone who finds it difficult to use new devices

## Demo Video
You can watch SayTV's Demo using this link
https://drive.google.com/file/d/1EliJ6d-sw3KBFHKqqZyCOEU4CyhJIypB/view


## Installation
To install our system you can do it using one of the following methods:
1. Use our SayTV OS Image which is a fork based on Raspian OS  (Recommended)
1. Build the code with the project's files using the Raspian OS   

### Install using our SayTV OS (Recommended)
SayTV OS  is for empowering the TV with a friendly Wit.ai assistant for voice commands, NLP and chatbot

To have it running on your pi you need.
* USB Microphone
* TV to be Upgraded
* MicroHDMI to HDMI cable
* MicroSD card with 16GB or more+
* MicroSD cards reader(SDCard reader with a bridge)
* 20GB of free disc space to prepare the image
* Raspberry pi4 with 2GB+ Ram
* Win32 Disk Imager : you can find it here   https://sourceforge.net/projects/win32diskimager/

Installing
1.	Download SayTV OS image https://drive.google.com/file/d/1WydbjiYMkScXZumLkYwyYs20qHwCZ4U_/view
1.	Extract the Zip file
1.	Insert your SDcard into computer
1.	Lunch win32diskimager
1.	Choose the image file “rpi_SayTVFork.img” from the extracted Zip File
1.	Choose the SDcard drive
1.	Click on write and wait until it is completed
1.	Once the SDcard is loaded open the PiWifi.exe and type your SSID and Password and click Save
1.	Eject the SDcard and insert it into your PI and power it up
1.	Wait until the robot is shown on the Screen and enjoy




### Build the code with the project's files using the Raspberry Pi OS
Start by installing the Raspian on your raspberry pi, refeere to this link for steps on how to install Raspberry Pi OS https://www.raspberrypi.org/software/
install **espeak** using this command
```
sudo apt-get install espeak
```

then install **Chromium Widevine** with the following commands
```
sudo apt install libwidevinecdm0
git clone https://github.com/Botspot/pi-apps
~/pi-apps/install
```
Run Pi Apps, from the Raspberry Pi Menu -> Accessories -> Pi Apps
Then check the **Chromium Widevine** option and install it

Then using pip3 install the python package dependencies for the project using the following commands:
```
cd kid_assest
pip3 install -r requirements.txt
```

To run the code

We need to install the chrome extention:
1. Launch the chromium browser using the command `chromium-browser`in the terminal
2. Navigate to the following URL: chrome://extensions/
3. Start developer mode if not started
4. click on "Load Unpacked"
5. Browse and choose the extension directory provided in WitAiSayTv 

move to the kid_assest dir to /home/pi using the following command:
```
cd /home/pi/kid_assest
```
Now you're ready to launch your SayTv
```
python3 dict.py
```

we have also built a tool to help you prepare your pi to get connected to your wifi directly called PiWifi
so you just put it in the boot drive on the SD card, run it enter your ssid and password  and it will order the py to connect to your network when booting.
It is located in the PiWifi directory from this project.

### Running the TV
After running the OS, the robot will be shown on the screen
1.	Say “TV” on the Microphone
1. The chatbot will start speaking to you

#### What you can do
You can do the following actions with SayTV OS, say an action, then the action is taken by the robot, then after processing the command using Wit.ai it will execute it, taking into consideration, that we are not dealing with the streaming service provider directly but instead we are exectuing the action on behalf of the user using the chrome extension.
##### The actions you do to start watching TV:

*	Asking about the weather such as ”what is the weather today”
*	Asking for watching a movie on Netflix such as “I want to watch Spiderman on Netflix”
*	Asking for watching a certain TV channel  such as “I want to watch Jordan TV”
*	The channels are stored on dictionary found in tv.py file and you can add as much channels as you want
```
channels_db={
    "jordan":'https://www.jrtv.gov.jo/live-tv',
    "abc":"https://abcnews.go.com/Live",
    'jazeera':'https://www.aljazeera.com/live/',
    'bloomberg':'https://www.bloomberg.com/live/us',
    'sky':'https://www.youtube.com/watch?v=9Auq9mYxFEE&ab_channel=SkyNews',
    'facebook watch':'https://web.facebook.com/watch'
}
```
*	Asking for watching a video on Youtube such as “I want to play Seniorita on Youtube”
*	Asking for surfing Facebook Watch such as saying “open Facebook Watch”

*If you want to watch Netflix on the device, please enter to Netflix.com on the browser and login with your account using a USB keyboard so you can use it.
You can login using this link
https://www.netflix.com/jo-en/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse
*


##### Things you can do while watching on the TV
*	You can say Pause to pause the video, Play to play the video after it has been paused, Exit to stop watching and back to the robot
*	Say "TV" to ask the robot for another action

## Developed by 
* Mahmoud Emad Darawsheh
* Alina Sami Abu Siam
* Amr Emad Darawsheh




