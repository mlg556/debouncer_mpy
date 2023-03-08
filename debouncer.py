""" MicroPython library for debouncing a digital pin.

Usage
------
```
from debouncer import Debouncer
from machine import Pin

led = Pin(15, Pin.OUT)
pin = Pin(42, Pin.IN, Pin.PULL_UP)
button = Debouncer(pin=pin, delay=50)

while True:
    led.value(button.read())
```
"""

# micropython port of https://github.com/wkoch/Debounce
# mirac gulgonul 2023 - MIT Licensed.

from machine import Pin
from time import ticks_ms, ticks_diff


class Debouncer:
    """Initializes debouncing for the given digital pin.

    Parameters
    ----------
    pin: Pin
        The digital pin to debounce. The pin must be set to input mode with the appropriate pull up/down beforehand. For example `pin = Pin(42, Pin.IN, Pin.PULL_UP)`
    delay: int
        The debounce time in milliseconds. Increase if the output flickers. Default is 50 ms.
    """

    def __init__(self, pin: Pin, delay: int = 50, invert: bool = False):
        self.pin = pin
        self.delay = delay  # ms
        self.reading = pin.value()
        self.state = self.last_state = self.reading
        self.last = ticks_ms()

        self.delay = 0
        self.last = 0

        self.wait = False

    # returns the debounced button state: 1 or 0.
    def read(self) -> bool:
        self.reading = self.pin.value()

        if self.reading != self.last_state:
            self.last = ticks_ms()
            self.wait = True

        if self.wait and ticks_diff(ticks_ms(), self.last) > self.delay:
            if self.reading != self.state:
                self.state = self.reading
                self.wait = False

        self.last_state = self.reading
        return self.state
