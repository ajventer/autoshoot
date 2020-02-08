#!/bin/bash 
COUNT=$1
BULB=$2
NAME=$3

if test $# -ne 3 ; then
	echo "Usage: $0 <number of shots> <exposure time> <filename base>"
	exit
fi
ps aux | fgrep "gphoto" | fgrep -q 'fgrep' | awk '{print $2}' | xargs kill -9 

gphoto2 -B $BULB --capture-image-and-download --no-keep  --frames $COUNT --interval 10 --filename $NAME-%n.%C

