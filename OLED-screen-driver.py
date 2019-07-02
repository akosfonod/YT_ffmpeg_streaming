#!/usr/bin/python2

import netifaces as ni
import time
import sys
import subprocess

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

x = 2
top = 2
spacing = 8

cpu_cmd  = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
mem_cmd  = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
temp_cmd = "cat /sys/devices/virtual/thermal/thermal_zone0/temp | awk '{printf \"SoC Temp: %.1f C\",$1/1000f}'"
disk_cmd = "df --output=pcent | awk 'FNR == 2 {printf \"Disk: %s\", $1}'"

def main():
    try:
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

            IPs      = getIpAddresses() #get all the IP addresses for all interface in a list
            CPU      = subprocess.check_output(cpu_cmd,  shell = True )
            TEMP     = subprocess.check_output(temp_cmd, shell = True )
            MemUsage = subprocess.check_output(mem_cmd,  shell = True )
            DiskUsage= subprocess.check_output(disk_cmd, shell = True )

            draw.text((x, top),             str(CPU),       font=font, fill=255)
            draw.text((x, top+spacing),     str(TEMP),      font=font, fill=255)
            draw.text((x, top+spacing*2),   str(MemUsage),  font=font, fill=255)
            draw.text((x, top+spacing*3),   str(DiskUsage), font=font, fill=255)

            addresses = iter(IPs)
            next(addresses,None) #skipping first interface address, which is the loopback
            for i, IP in enumerate(addresses):
                draw.text((x, top+spacing*4+spacing*i),   str(IP),    font=font, fill=255)

            if DEBUG:
                print (CPU)
                print (TEMP)
                print (MemUsage)
                print (DiskUsage)
                for IP in IPs:
                    print (IP)
                print 60 * "="

            disp.image(image)
            disp.display()

            time.sleep(2)

    except KeyboardInterrupt:
        if DEBUG:
            print ("Interrupted with keyboard!")
    except:
        if DEBUG:
            print ("Unexpected exception: " , sys.exc_info()[0])
    finally:
        # Clear display.
        disp.clear()
        disp.display()


def getIpAddresses():
    DEBUG = False
    netifs  = ni.interfaces()
    for i, interface in enumerate(netifs):
        try:
            ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
            netifs[i] = netifs[i] + " : " + ip
            if DEBUG:
                print (netifs[i] + " " + ip)
        except KeyError:
            if DEBUG:
                print ("No IP addr. available for " + netifs[i])
            netifs[i] = netifs[i] + ' : -'
        except:
            if DEBUG:
                print ("Unexpected exception: " , sys.exc_info()[0])
    return netifs

#Main entrace for the script
if __name__ == "__main__":
    main()

#TODO: streaming progress printout, maybe as a parameter input.