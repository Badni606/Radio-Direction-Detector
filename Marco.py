import machine
import time

uart_xbee = machine.UART(0, baudrate=9600, tx=machine.Pin(16), rx=machine.Pin(17))
led_pin = machine.Pin(25, machine.Pin.OUT)

def loop:
    while 1:
        time.sleep(0.5)
        led_pin.off()
        uart_xbee.write('marco')
        

def waitForResponse():
    time.sleep(0.2)
    response = uart_xbee.read()
    if response = b'polo':
        led_pin.on()
        
loop()