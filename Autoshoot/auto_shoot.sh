#!/bin/bash
COUNT=$1
BULB=$2
NAME=$3

ps aux | fgrep "gphoto" | awk '{print $2}' | xargs kill -9 

if test $# -ne 3 ; then
	echo "Usage: $0 <number of shots> <exposure time> <filename base>"
	exit
fi

C=0
while test $C -ne $COUNT ; do
	gphoto2 -B $BULB --capture-image-and-download --no-keep --filename "$NAME-$C".cr2
	sleep $((BULB+3))
	C=$((C+1))
done
