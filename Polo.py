import machine
import time

uart_xbee = machine.UART(0, baudrate=9600, tx=machine.Pin(16), rx=machine.Pin(17))

def loop():
    while 1:
        time.sleep(0.1)
        data = uart_xbee.read()
        if data == b'marco':
            respond()
        
response = 'polo'

def respond():
    uart_xbee.write(response)

loop()
