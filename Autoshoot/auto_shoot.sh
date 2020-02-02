#!/bin/bash
COUNT=$1
BULB=$2
NAME=$3

if test $# -ne 3 ; then
	echo "Usage: $0 <number of shots> <exposure time> <filename base>"
	exit
fi
ps aux | fgrep "gphoto" | awk '{print $2}' | xargs kill -9 

C=0
while test $C -ne $COUNT ; do
	echo
	echo "Capturing shot $C"
	echo
	gphoto2 -B $BULB --capture-image-and-download --no-keep --filename "$NAME-$C".cr2 
	echo "Waiting for camera to become available again"
	while ! gphoto2 --list-config >/dev/null  ; do
		echo -n "."
		sleep 1
	done
	echo
	C=$((C+1))
done
