from tests.test_base import TestBase
import time
import unittest
import random

"""
data to history graph can only be sent once per minute
"""
class TestSetHistoryGraph(TestBase):

    def test_set_pin(self):
        self.blynk.start_blynk_heartbeat()
        while True:
            try:
                value = random.randint(0,1000)
                print("Graph V20: {}".format(value))
                self.blynk.set_pin_value('V20', value)

                value = random.randint(0,1000)
                print("Graph V21: {}".format(value))
                self.blynk.set_pin_value('V21', value)

                value = random.randint(0,1000)
                print("Graph V22: {}".format(value))
                self.blynk.set_pin_value('V22', value)

                value = random.randint(0,1000)
                print("Graph V24: {}".format(value))
                self.blynk.set_pin_value('V24', value)

            except:
                print("Exception")

            time.sleep(61)

if __name__ == '__main__':
    unittest.main()
