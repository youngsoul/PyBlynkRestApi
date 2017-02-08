PyBlynkRestApi
==============

This package is a simple wrapper around the Blynk Rest API.  

To install
----------

pip install pyblynkrestapi

Overview
--------

The Blynk Rest API is not the most efficient way to interact with the 
Blynk Cloud and mobile application.  If you can find a native client
that uses TCP sockets - that would be the most efficient.  

This was written for the cases where you cannot find a suitable TCP 
client, or your integration needs are just different enough that access
to the Rest API is the better route.

This package leverages work from:

https://github.com/erazor83/pyblynk

and in particular uses the PING message capability.

Not every Blynk UI element is supported via the Rest API.  In particular
the following are not supported:

*   Terminal
*   Most everything in the 'Other' section
*   Table - I have not worked with this to see if it is possible
*   I was never able to get push notifications to trigger via the Rest API

This class and Rest interaction has only been tested when the pin specification is Virtual and the interaction is always 'Push'

Creating an instance
--------------------

To create an instance to the PyBlynkRestApi:

pyblynk = PyBlynkRestApi(auth_token, start_heartbeat=False)

*   auth_token - required parameter
*   start_heartbeat - Optional, defaults to False.  If True - it will start the heatbeat ping with the Blynk server.

If you select false, then to start the heatbeat ping use the method:

*   start_blynk_heartbeat()

To read values from the Blynk server/app
----------------------------------------

### get_pin_value(blynk_pin_number)

the method will make a read request for the value associated with the blynk pin number.  

To set values to the Blynk server/app
----------------------------------------

### set_pin_value(blynk_pin_number, value)

the method will make a post request and set the value specified for the given blynk pin number.

Setting a Blynk LED
----------------------------------------

On for the LED is the value 255.  There are convenience functions such as:

### led_on(blynk_pin_number)

### led_off(blynk_pin_number)

### set_let((blynk_pin_number, value)
value =0 then it is off, any other value will turn it on

Asynchronous Operation
----------------------

The module can operate synchronously, where the client calls the methods above, or asynchronously.

There are 3 types of handlers: 

*   read handlers - where the blynk app will read the pin and provide the value to the handler callback
*   set handlers - where the callback is executed, and the return value is set into the blynk server/app
*   handlers - where the callback is executed and it is up to the handler to decide how to interact with the blynk server/app

### Read Handlers

    def led2_handler(value, blynk_pin_number, blynk):
        pass
        
    blynk = PyBlynkRestApi(auth_token)
    
    blynk.add_read_pin_handler('V12', led2_handler)
    
The PyBlynkRestApi module, will read pin 'V12', and call the set_led2_handler, with the value, the blynk pin number and a reference to the blynk rest api instance.  The implementation of the callback has to figure out what to do with that value.

### Set Handlers

    def gpio_pin_handler(blynk_pin_number, blynk):
        pin_value = read_gpio(rpi_pin)
        return pin_value
        
    blynk = PyBlynkRestApi(auth_token)
    
    blynk.add_read_pin_handler('V13', gpio_pin_handler)

The PyBlynkRestApi module, will call the callback, and use the return value to set the configured Blynk pin.

In the example above, first the gpio_pin_handler is called.  This callback can do anything it needs to, but it is expected to return a value that is then set into the Blynk server/app at the configure Blynk pin of 'V13'

### Handlers

    def rgb_led_handler(blynk):
        # do anything you need to
        # use the blynk reference to get or set values
        
    blynk = PyBlynkRestApi(auth_token)
    
    blynk.add_handler(rgb_led_handler)

The PyBlynkRestApi module, will call the callback but otherwise do nothing else.  It is up to the implementation to decide how to interact with Bynk.

### Run method

To start the asynchronous operation, call the run method with an interval specified.  This interval is how often the read/set/handler are called.

Each of the different handler types are called on their own thread, meaning there is a thread to handle read from Blynk, another thread to set values to Blynk, and other thread to handle the generic handlers.

An example script to configure everything might look like:

    if __name__ == '__main__':
        blynk = init()
        blynk.add_set_pin_handler('V20', read_button_handler)
        blynk.add_read_pin_handler('V21', set_led1_handler)

        blynk.add_handler(set_acc_handler)

        print("running")
        blynk.run(0.5)
        while True:
            print("sleeping")
            time.sleep(60)


Sample Application
------------------

https://github.com/youngsoul/GrovePiBlynkSampleApp

