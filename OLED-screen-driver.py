#TODO: streaming progress printout

import netifaces as ni
import time

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

# Define text and get total width.
text = 'SSD1306 ORGANIC LED DISPLAY.'

top = 2
maxwidth, unused = draw.textsize(text, font=font)

mem_cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
cpu_cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)*100f}'"

    draw.text((x, top),       "IP: " + str(IP),  font=font, fill=255)


def main():
    #main function
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

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    while True:
        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        CPU      = subprocess.check_output(cpu_cmd, shell = True )
        MemUsage = subprocess.check_output(mem_cmd, shell = True )

        draw.text((x, top+8),     str(CPU), font=font, fill=255)
        draw.text((x, top+16),    str(MemUsage),  font=font, fill=255)

        time.sleep(1)


def getIpAddresses():
    netifs  = ni.interfaces()
    for interface in netifs:
        try:
            ip = ni.ifaddresses(netifs[interface])[ni.AF_INET][0]['addr']
            netifs[interface] + " " + ip
            if DEBUG:
                print netifs[interface] + " " + i
        except KeyError:
            if DEBUG:
                print "No IP addr. available for " + netifs[interface]
            netifs[interface] + ' -'
        except, e:
            if DEBUG:
                print "Unexpected exception" + str(e)
    return netifs

#Main entrace for the script
if _name_ == "_main_":
    main()