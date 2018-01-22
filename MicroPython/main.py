from bot_on_off import pisca, server


#This script is run on boot
def clear():
    print('\x1b[2J', end='')
    print('\x1b[H', end='')

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    # sta_if.ifconfig(('192.168.0.40', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
    sta_if.ifconfig(('10.224.24.40', '255.255.0.0', '10.224.0.1', '8.8.8.8'))
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('garoa', '')
        while not sta_if.isconnected():
            pass
    print('network config: ', sta_if.ifconfig())

do_connect()
pisca()
server()