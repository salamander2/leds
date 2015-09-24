leds
====

Introductory Python programs for controlling LEDs using a Raspberry Pi (for my workshop)

### Build this circuit first
![one](https://raw.githubusercontent.com/salamander2/leds/master/circuits/RPI_LED_Circuit1.png)

* Connections to the T-Cobbler (it's really hard to read the numbers):
 * the black wires go to GND.
 * the yellow wire for from the Red LED resistor goes to #25
 * the blue wire for from the Green LED resistor goes to #20
 * the red wire from the switch is connected to #6

=====
* With this circuit you can run all of the programs in this repository.
* To copy all of these programs, type 

**<pre>git clone https://github.com/salamander2/leds</pre>**

This will make a folder called "leds" in your current dicrectory and put the programs in it.

* Type `cd leds` to change directory to "leds".
* Type `ls -l` to see a listing of the programs.
* The programs get more complex and refined from #1 to #5. 
* Example: **`sudo python light2.py`** to run program 2.

=====
You can also run the the "Pulse2.py" program which will pulse the two LEDS using PWM mode.

=====
### Add the 3 colour LED
![two](https://raw.githubusercontent.com/salamander2/leds/master/circuits/RPI_LED_Circuit2.png)

* Connections:
 * the long leg of the LED goes to GND.
 * the three resistors connect to the short legs and also connect to #13, #19, #26
 
Now you can run the TriColour program "Tricolour.py". Press 'r', 'g', and 'b' keys to increase the red, green, and blue.  Use capital R G B to decrease the amounts.

### Bigger and Better Things ...
For the repository that contains everything, please go to the one called "RaspberryPi" https://github.com/salamander2/RaspberryPi
