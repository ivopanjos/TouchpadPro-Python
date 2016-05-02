
Run the start.sh file and probably everything is going to work.

Remember this is a WIP so expected a few issues.
If you have any problem running this try to use the old information, lots of useful info there.



//Old Information

- touchpad moves around fronm input/eventX to Y
	- need to find a way to make it stick
	- or to find it inside dev/input/event?

- automatize start of this service
	- sudo modprobe uinput

- allow app to run as sudo (window)
	- xhost +

How to run:

xhost +
find the event number and fix the script


Resources need:

sudo pip install evdev
sudo pip install ewmh


Get all the info needed:

list all devices, check number of touchpad
	- xinput list

see what event is listening to touchpad
	- xinput --list-props 15

list codes and test events
	- sudo evtest /dev/input/event16

