# Capacitive-Touch
Synopsis:
This repository contains all of the program code and info for the capacitive touch system used in CommuniTree's interactive art installation called "Nature's Voice". The system consists of using a Raspbery Pi, having a total of 8 plants connected to a capacitive touch sensor; this system allows for the touch & sound interaction of the Nature's Voice installation. When a plant is touched by a person, the touch sensor picks up on the electrical resistance. The program then uses this to trigger a sound to play as long as touch is maintained with the plant; each plant is assigned its own individual sound. For more information of Nature's Voice please visit: https://uwcommunitree.wordpress.com/


Python library for interfacing with a MPR121 capacitive touch sensor on the Raspberry Pi >> https://www.adafruit.com/products/2340 Code for accessing and controlling the touch sensor is used in this Library (MPR121.py & init.py) borrowed from Tony DiCola and Adafruit Industries. From the CommiTree_Programs folder is final program (sound_touchNew.py by Kris Hunt) for CommuniTree's Interactive Art Installion, this program allows ambient sounds to play while touch is detected. The program has it where each sensor port (total of 12) is assigned to a specific sound; when contact is made a sound plays, if contact ends then the sound will fade out and eventually stop playing. 


The library can be accessed and downloaded from https://github.com/UWCommuniTree/Capacitive-Touch.git.


2016 CommuniTree
Author: Kris Hunt
 This program is inspired from code used from Adafruit Industries & Tony DiCola

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
