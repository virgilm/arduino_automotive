# arduino_automotive
SPI interface to program EEPROM used in various cars (BMW, ....)

USE THIS AT YOUR OWN RISK! I ACCEPT NO RESPONSIBILITY FOR ANY DAMAMGE YOU MAY INFLICT TO YOUR VEHICLE!

READ THE CODE FIRST, DON'T RUN IT BLINDLY!

* run the Arduino scetch in read mode
* you can use the non-human form to read the binary from the serial console (19200 baud rate)
* copy the binary form to a file called "st95080_roc_dump.bin"
* clear the errors, save the output into the same binary file.
* run 'python3 read_file.py'
* copy and replace the generated buffer structure into the arduino sketch
* uncomment the last few lines that write the buffer to the EEPROM
* the sketch re-reads the EEPROM to make sure it's been written properly. 
* done!
