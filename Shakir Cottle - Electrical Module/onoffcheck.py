# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain

# Import SPI library (for hardware SPI) and MCP3008 library.
import SPI_1 as SPI
import Adafruit_MCP3008

from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

from time import sleep, strftime
from datetime import datetime
 
import RPi.GPIO as IO
import time, sys

# Software SPI configuration:
#CLK  = 18
#MISO = 23
#MOSI = 24
#CS   = 25
#mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

#Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

IO.setmode(IO.BCM)

print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)
# Main program loop.

def get_time_now():     # get system time
    return datetime.now().strftime('    %H:%M:%S')

def destroy():
    lcd.clear()

def loop():
    mcp1.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns
    offBuffer = 3
    onBuffer = 9
    while True:
        # Read all the ADC channel values in a list.
        values = [0]*8
        for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
            values[i] = mcp.read_adc(i)
        # Print the ADC values.
            print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
        # Pause for half a second.
        if (values[0] > offBuffer):
            lcd.setCursor(0,0)  # set cursor position
            lcd.message('Outlet: ON   \n')
            lcd.message( get_time_now() )   # display the time
            sleep(1)
        elif (values[0] < onBuffer):
            lcd.setCursor(0,0)  # set cursor position
            lcd.message('Outlet: OFF    \n')
            lcd.message( get_time_now() )   # display the time
            sleep(1)
        time.sleep(0.5)
        
if __name__ == '__main__':
    print ('Program is starting ... ')
#--------------------------SETUP------------------------------------------------#
    PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
    PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
    # Create PCF8574 GPIO adapter.
    try:
        mcp1 = PCF8574_GPIO(PCF8574_address)
    except:
        try:
            mcp1 = PCF8574_GPIO(PCF8574A_address)
        except:
            print ('I2C Address Error !')
            exit(1)
    # Create LCD, passing in MCP GPIO adapter.
    lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp1)
#---------------------------SETUP END-------------------------------------------#
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
