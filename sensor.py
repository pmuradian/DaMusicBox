# Simple example of reading the MCP3008 analog input channels using its
# differential mode.  Will print the difference of channel 0 and 1.
# Author: Tony DiCola
# License: Public Domain
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25

Clk  = 10
Miso = 9
Mosi = 11
Cs   = 22

mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
mcp2 = Adafruit_MCP3008.MCP3008(clk=Clk, cs=Cs, miso=Miso, mosi=Mosi)


# Hardware SPI configuration:
#SPI_PORT   = 0
#SPI_DEVICE = 0
#mcp2 = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

print('Press Ctrl-C to quit...')
while True:
    for i in range(9):
        value = 0
        if i < 6:
            value = mcp.read_adc(i)
        else:
            value2 = mcp2.read_adc(i - 6)
        print("channel {0} of has value {1}".format(i, value))
        time.sleep(1)
    #print('Channel 0 minus 1: {0}'.format(value))
    #time.sleep(0.1)
