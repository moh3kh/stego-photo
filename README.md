
This simple program uses stepic module to hide(encode)/extract(decode) the data inside/from the png images. By adding authentication password to extract the hidden data, it became more reliable. 

The program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License


USAGE:

encode.py [-h] -i INPUT -o OUTPUT -t TEXT -p PASSWORD

arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT         specify image to have secret message
  -o OUTPUT, --output OUTPUT      specify output image including secret message
  -t TEXT, --text TEXT            specify text to hide
  -p PASSWORD, --password PASSWORD

decode.py [-h] -p PASSWORD -i INPUT

arguments:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD      enter password to get the secret message
  -i INPUT, --input INPUT      specify image to have secret message


Future work would be enhancing the tool to work on all image types.



