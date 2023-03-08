from debouncer import Debouncer
from machine import Pin

led = Pin(15, Pin.OUT)

pin = Pin(42, Pin.IN, Pin.PULL_UP)

button = Debouncer(pin=pin, delay=50)

while True:
    led.value(button.read())
