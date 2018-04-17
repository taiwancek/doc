print("test")

import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('AndroidAP5B29', 'zvxr5951')


from machine import Pin
pinBLUE = Pin(2, Pin.OUT)
pinBLUE.value(1)

import hashlib
def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()

md5sum('test.mpy')    