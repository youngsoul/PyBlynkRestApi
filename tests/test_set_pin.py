from tests.test_base import TestBase
import time
import unittest


class TestSetPin(TestBase):

    def test_set_pin(self):
        self.blynk.start_blynk_heartbeat()
        i = 0
        while True:
            try:
                self.blynk.set_pin_value('V9', i)
                i += 1
            except:
                print("Exception")

            time.sleep(1)

if __name__ == '__main__':
    unittest.main()
