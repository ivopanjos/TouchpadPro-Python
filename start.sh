#!/bin/bash

clear

echo "xinput"
id_number=$(xinput | grep Touchpad | cut -f2 | cut -d '=' -f 2)

echo "Your touchpad id is:" $id_number


echo "xinput --list-props $id_number"
event_output=$(xinput --list-props $id_number | grep /dev/input/ | cut -f3 | cut -d '"' -f 2)

event_number=${event_output:16}


echo "Your event number is:" $event_number

echo "sudo python Main.py $event_number"

sudo python Main.py $event_number

