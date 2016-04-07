# 2016 CommuniTree
# Author: Kris Hunt
#
# This program is inspired from code used from Adafruit Industries & Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
import time
import pygame

import Adafruit_MPR121.MPR121 as MPR121

print 'CommuniTree Installation Capacitive Touch'

# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize communication with MPR121 using default I2C bus of device, and
# default I2C address (0x5A).  On BeagleBone Black will default to I2C bus 0.
if not cap.begin():
    print 'Error initializing MPR121.  Check your wiring!'
    sys.exit(1)

# Alternatively, specify a custom I2C address such as 0x5B (ADDR tied to 3.3V),
# 0x5C (ADDR tied to SDA), or 0x5D (ADDR tied to SCL).
#cap.begin(address=0x5B)

# Also you can specify an optional I2C bus with the bus keyword parameter.
#cap.begin(bus=1)

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

# Define mapping of capacitive touch pin presses to sound files
# tons more sounds are available in /opt/sonic-pi/etc/samples/ and
# /usr/share/scratch/Media/Sounds/
# All sounds are open source/fair use, must be .wav format. 
SOUND_MAPPING = {
  0: '/home/pi/sounds/glory_and_wind.wav',
  1: '/home/pi/sounds/air_pipe.wav',
  2: '/home/pi/sounds/01-BodhiSounds-Sunyata-roots.wav',
  3: '/home/pi/sounds/FX-Abstract20.wav',
  4: '/home/pi/sounds/trickle.wav',
  5: '/home/pi/sounds/Amb_Test1.wav',
  6: '/home/pi/sounds/nature/swamp_y.wav',
  7: '/home/pi/sounds/nature/crickets_y.wav',
  8: '/home/pi/sounds/nature/strong_wind_y.wav',
  9: '/home/pi/sounds/nature/light_rain_y.wav',
  10: '/home/pi/sounds/nature/forest_ambience.wav',
  11: '/home/pi/sounds/nature/wind_and_rain.wav',
}
# Array sounds set for 12 pins.
sounds = [0,0,0,0,0,0,0,0,0,0,0,0]

for key,soundfile in SOUND_MAPPING.iteritems():
        sounds[key] =  pygame.mixer.Sound(soundfile)
        sounds[key].set_volume(1);

# Main loop to print a message every time a pin is touched.
print 'Press Ctrl-C to quit.'
last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    # Check each pin's last and current state to see if it was pressed or released.
    for i in range(12):
        # Each pin is represented by a bit in the touched value.  A value of 1
        # means the pin is being touched, and 0 means it is not being touched.
        pin_bit = 1 << i
        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
            print '{0} touched!'.format(i)
            if (sounds[i]):
                sounds[i].play(-1)
        if not current_touched & pin_bit and last_touched & pin_bit:
            print '{0} released!'.format(i)
            if (sounds[i]):
                sounds[i].fadeout(2000)

    # Update last state and wait a short period before repeating.
    last_touched = current_touched
    time.sleep(0.1)

    # Alternatively, if you only care about checking one or a few pins you can
    # call the is_touched method with a pin number to directly check that pin.
    # This will be a little slower than the above code for checking a lot of pins.
    #if cap.is_touched(0):
    #    print 'Pin 0 is being touched!'

    # If you're curious or want to see debug info for each pin, uncomment the
    # following lines:
    #print '\t\t\t\t\t\t\t\t\t\t\t\t\t 0x{0:0X}'.format(cap.touched())
    #filtered = [cap.filtered_data(i) for i in range(12)]
    #print 'Filt:', '\t'.join(map(str, filtered))
    #base = [cap.baseline_data(i) for i in range(12)]
    #print 'Base:', '\t'.join(map(str, base))
