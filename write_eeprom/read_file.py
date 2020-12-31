import re
import sys

# Build a C byte array out of the binary contents of a file.

string = "byte buffer[SIZE] = {"

list = re.findall('..','1234567890') 
with open("st95080_roc_dump.bin", "rb") as f:
    while (byte := f.read(1)):
        # Do stuff with byte.
        string = string + str(int.from_bytes(byte, byteorder=sys.byteorder)) + ", "

string = string[:-2] + "}"

print(string)

