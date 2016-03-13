import threading
import time
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("USR3", GPIO.OUT)

ledOn = False

def setInterval(interval, times = -1):
    # This will be the actual decorator,
    # with fixed interval and times parameter
    def outer_wrap(function):
        # This will be the function to be
        # called
        def wrap(*args, **kwargs):
            stop = threading.Event()

            # This is another function to be executed
            # in a different thread to simulate setInterval
            def inner_wrap():
                i = 0
                while i != times and not stop.isSet():
                    stop.wait(interval)
                    function(*args, **kwargs)
                    i += 1

            t = threading.Timer(0, inner_wrap)
            t.daemon = True
            t.start()
            return stop
        return wrap
    return outer_wrap

@setInterval(1)
def flipLED():
    GPIO.output("USR3", GPIO.LOW if ledOn else GPIO.HIGH)
    print "Flipped " + ("LOW" if ledOn else "HIGH")
    ledOn = !ledOn

stopper = flipLED()

time.sleep(100)
stopper.set()
