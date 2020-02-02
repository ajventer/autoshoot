# autoshoot
A simple utility for automated astro-photography.

The included auto_shoot.sh script is designed to automatically take a series of pictures of with gphoto2 and the exposure time of your choosing.
It cannot take shots less than 1s long.
The camera must be in BULB mode to allow arbitrary exposure times.
This is an alternative to using a remote shutter trigger, with the option of automatically taking as many shots as you need, for example on a tracking platform or barn-door tracker.
Runnning the script with no parameters will print the usage:

```Usage: ./auto_shoot.sh <number of shots> <exposure time> <filename base>```

That is to say, the first parameter is how many shots you want to take (this is useful as most cameras won't let you do continous shooting in manual mode), the second is the exposure time per shot, and the third is a filename base to save the results under. The script will download the shots as they are taken directly to the current directory and immediately delete them from the camera, thus it requires very little SD-card space.

This script has been primarily tested using a Canon EOS-40D DSLR, you may need to tweak it for some other cameras as I don't have any to test with. My script automatically sleeps for 3 seconds between shots to give the camera time to reset.

This script uses gphoto2 to actually talk to the camera. Most distros come with this installed by default. On most systems gphoto2 also installs a monitoring service to detect when a camera is plugged in, this service interferes with the commandline operation. Therefore the script will look for any processes like this and kill them before it starts trying to shoot. If you want the monitoring features you need to restart the gphoto-gvfs service (the name will depend on your distro) after running it.

The MasterTemplate folder is a convenient replica of a standard astrophotography directory, with the four most common types of frame folders allready added. Each folder (except lights - because those are the obvious ones you always takes) also contains a brief HOWTO that explains how to take that kind of frame and how many are suggested. This is handy when in the field shooting, especially if you are still learning, as a quick reminder of the process.

When you start your session, just copy the Master_Template directory a new path describing the shoot. Let's say I was doing a shoot on Sirius. I will be doing 45s exposures, and I'm taking the darks to match.

```
$ cp -r /path/to/Master_Template ~/Pictures/Astro/Sirius-$(date +%Y-%m-%d)
$ cd Picutres/Astro/Sirus-$(date +%Y-%m-%d)
$ cd darks
$ cat HOWTO
Right after imaging
With the same settings as used for the lights.
Put lense cap on
Take a 20-50 shots

$ /path/to/auto_shoot.sh 30 45 dark-sirius
```

By the end of the evning the folder Sirius-<todays date> is ready to be used with your favorite stacking software. Wether that is DeepSkyStacker under wine or Siril.
