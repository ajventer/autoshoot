# autoshoot
A simple utility for automated astro-photography.

The included auto_shoot.sh script is designed to automatically take a series of pictures of with gphoto2 and the exposure time of your choosing.
It cannot take shots less than 1s long.
The camera must be in BULB mode to allow arbitrary exposure times.
This is an alternative to using a remote shutter trigger, with the option of automatically taking as many shots as you need, for example on a tracking platform or barn-door tracker.

The MasterTemplate folder is a convenient replica of a standard astrophotography directory, with the four most common types of frame folders allready added. Each folder (except lights - because those are the obvious ones you always takes) also contains a brief HOWTO that explains how to take that kind of frame and how many are suggested. This is handy when in the field shooting, especially if you are still learning, as a quick reminder of the process.

When you start your session, just copy the Master_Template directory a new path describing the shoot. Let's say you I was doing a shoot on Sirius.

`
$ cp /path/to/Master_Template ~/Pictures/Astro/Sirius-$(date +%Y-%m-%d)
$ cd Picutres/Astro/Sirus-$(date +%Y-%m-%d)
$ cd darks
$ cat HOWTO
Right after imaging
With the same settings as used for the lights.
Put lense cap on
Take a 20-50 shots

$ /path/to/auto_shoot.sh 30 45 dark-sirius

`
