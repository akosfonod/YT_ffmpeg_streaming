import netifaces as ni

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

DEBUG = True

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware SPI:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Initialize library.
disp.begin()

# Get display width and height.
width = disp.width
height = disp.height

# Clear display.
disp.clear()
disp.display()

# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (width, height))

# Load default font.
font = ImageFont.load_default()

# Create drawing object.
draw = ImageDraw.Draw(image)

# Define text and get total width.
text = 'SSD1306 ORGANIC LED DISPLAY. THIS IS AN OLD SCHOOL DEMO SCROLLER!! GREETZ TO: LADYADA & THE ADAFRUIT CREW, TRIXTER, FUTURE CREW, AND FARBRAUSCH'
maxwidth, unused = draw.textsize(text, font=font)


def getIpAddresses():
    netifs  = ni.interfaces()
    for interface in netifs:
        try:
            ip = ni.ifaddresses(netifs[interface])[ni.AF_INET][0]['addr']
            netifs[interface] + " " + ip
            if DEBUG:
                print netifs[interface]
        except KeyError:
            if DEBUG:
                print "No IP addr. available for " + netifs[interface]
            netifs[interface] + ' -'
        except, e:
            if DEBUG:
                print "Unexpected exception" + str(e)
    return netifs
