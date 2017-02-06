from tests.test_base import TestBase
import time
import unittest


def pin_v1_handler(value, pin_number, blynk):
    print("READ {} value: {}".format(pin_number, value))

v9_counter = 0
def pin_v9_handler( pin_number, blynk):
    global v9_counter
    v9_counter += 1
    print("SET {} value: {}".format(pin_number, v9_counter))
    return v9_counter

v4_counter = 0
v4_add_value = 1
def pin_v4_handler(pin_number, blynk):
    global v4_counter, v4_add_value
    v4_counter += v4_add_value
    if v4_counter > 100:
        v4_add_value = -1
    if v4_counter <= 0:
        v4_add_value = 1

    return v4_counter

class TestRunHandlers(TestBase):

    def test_set_pin(self):
        self.blynk.start_blynk_heartbeat()
        self.blynk.add_read_pin_handler('V1', pin_v1_handler)
        self.blynk.add_set_pin_handler('V9', pin_v9_handler)
        self.blynk.add_set_pin_handler('V4', pin_v4_handler)
        self.blynk.run(2)

        while True:
            print("in sample main routine")
            time.sleep(5)

if __name__ == '__main__':
    unittest.main()
