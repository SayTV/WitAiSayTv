rm -f /home/pi/kid_assest/busy$2.lg
touch /home/pi/kid_assest/busy$2.lg
chromium-browser --autoplay-policy=no-user-gesture-required --kiosk $1
