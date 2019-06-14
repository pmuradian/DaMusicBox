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
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
#SPI_PORT   = 0
#SPI_DEVICE = 0
#mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

print('Press Ctrl-C to quit...')
while True:
    for i in range(8):

        value = mcp.read_adc(i)
    print('Channel 0 minus 1: {0}'.format(value))
    time.sleep(0.1)
