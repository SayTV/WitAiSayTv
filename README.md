# SayTV

## Installation
To install our system you can do it using one of the following methods:
1. Use our SayTV OS Image which is a fork based on Raspian OS  (Recommended)

1. Build the code with the project's files using the Raspian OS   

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
-	Download SayTV OS image https://drive.google.com/file/d/1WydbjiYMkScXZumLkYwyYs20qHwCZ4U_/view
-	Extract the Zip file
-	Insert your SDcard into computer
-	Lunch win32diskimager
-	Choose the image file “rpi_SayTVFork.img” from the extracted Zip File
-	Choose the SDcard drive
-	Click on write and wait until it is completed
-	Once the SDcard is loaded open the PiWifi.exe and type your SSID and Password and click Save
-	Eject the SDcard and insert it into your PI and power it up
-	Wait until the robot is shown on the Screen and enjoy




### Build the code with the project's files using the Raspberry Pi OS
Start by installing the Raspian on your raspberry pi, refeere to this link for steps on how to install Raspberry Pi OS https://www.raspberrypi.org/software/
install **espeak** using this command
`sudo apt-get install espeak`

then install **Chromium Widevine** with the following commands
`sudo apt install libwidevinecdm0
git clone https://github.com/Botspot/pi-apps
~/pi-apps/install`
Run Pi Apps, from the Raspberry Pi Menu -> Accessories -> Pi Apps
Then check the **Chromium Widevine** option and install it

Then using pip3 install the python package dependencies for the project using the following commands:
`cd kid_assest
pip3 install -r requirements.txt`

To run the code

We need to install the chrome extention:
1. Launch the chromium browser using the command `chromium-browser`in the terminal
2. Navigate to the following URL: chrome://extensions/
3. Start developer mode if not started
4. click on "Load Unpacked"
5. Browse and choose the extension directory provided in WitAiSayTv 

move to the kid_assest dir to /home/pi using the following command:
`cd /home/pi/kid_assest`
Now you're ready to launch your SayTv
`python3 dict.py`

we have also built a tool to help you prepare your pi to get connected to your wifi directly called PiWifi
so you just put it in the boot drive on the SD card, run it enter your ssid and password  and it will order the py to connect to your network when booting.
It is located in the PiWifi directory from this project.










