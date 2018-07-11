#!/bin/sh
echo “**************************** ** Mise à jour en cours ** ** veuillez patienter ** ****************************”  
sudo apt-get update 
sudo apt-get upgrade -y 
sudo apt-get dist-upgrade -y 
sudo apt-get clean 
sudo apt-get autoclean 
sudo rpi-update 
sudo reboot
