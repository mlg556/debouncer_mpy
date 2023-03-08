# MicroPython Debouncer

Really small micropython library for button debouncing. Port of
https://github.com/wkoch/Debounce

# Installation

Copy the file `debouncer.py` in your chip's filesystem. For example with
[mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html), you
can do:

```
git clone github.com/mlg556/debouncer_mpy

cd debouncer_mpy

mpremote connect COMX cp debouncer.py :
```

# Usage

```
from debouncer import Debouncer
from machine import Pin

led = Pin(15, Pin.OUT)
pin = Pin(42, Pin.IN, Pin.PULL_UP)
button = Debouncer(pin=pin, delay=50)

while True:
    led.value(button.read())
```
