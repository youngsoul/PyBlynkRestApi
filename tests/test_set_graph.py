from tests.test_base import TestBase
import time
import unittest
import random

class TestSetGraph(TestBase):

    def test_set_pin(self):
        self.blynk.start_blynk_heartbeat()
        while True:
            try:
                value = random.randint(0,1000)
                print("Graph: {}".format(value))
                self.blynk.set_pin_value('V7', value)
            except:
                print("Exception")

            time.sleep(1)

if __name__ == '__main__':
    unittest.main()
