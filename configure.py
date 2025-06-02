import machine
import time

uart = machine.UART(0, baudrate=9600,tx=machine.Pin(16),rx=machine.Pin(17))

def sendCommand(command):
    uart.write(command)

def config_coordinator():
    sendCommand('+++')
    
    #have to wait for command mode to be entered
    time.sleep(1)
    sendCommand('ATRE')
    
    # Send AT command to set operating mode to API mode 2 (API mode without escaping)
    sendCommand('ATAP2')

    # Send AT command to set device role to coordinator
    sendCommand('ATCE1')
    
    # Set PAN ID
    pan_id = '21'
    response = sendCommand('ATID{}'.format(pan_id))

    # Send AT command to write changes to non-volatile memory
    sendCommand('ATWR')
    
    # Apply changes (not strictly neccessary but eh)
    response = sendCommand('ATAC')

    # Send AT command to exit command mode
    sendCommand('ATCN')
    print("Finshed Configuring")

# Function to get configuration parameter
def get_configuration(parameter):
    sendCommand('AT{}'.format(parameter))
    time.sleep(0.1)
    response = uart.readline() #.decode().strip()
    return response


def checkConfig():
    # List of configuration parameters to retrieve
    parameters = ['ID', 'DH', 'DL', 'MY', 'BD', 'NC', 'AP', 'CE']
    sendCommand('+++')
    time.sleep(1)
    # Retrieve and print configuration parameters
    for parameter in parameters:
        value = get_configuration(parameter)
        print('{}: {}'.format(parameter, value))
    sendCommand('ATCN')
    print("Finished Checking")
    

config_coordinator()
checkConfig()
    