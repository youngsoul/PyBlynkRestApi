from tests.test_base import TestBase
import time
import unittest
import random

class TestTerminal(TestBase):

    def test_set_pin(self):
        self.blynk.start_blynk_heartbeat()
        while True:
            try:
                value = random.randint(0,1000)
                msg = "Graph: {}\n".format(value)
                print(msg)
                self.blynk.set_pin_value('V12', "{}\r".format(value))
                # value = self.blynk.get_pin_value('V12')
                # print(value)
            except:
                print("Exception")

            time.sleep(1)

if __name__ == '__main__':
    unittest.main()
