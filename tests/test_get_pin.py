from tests.test_base import TestBase
import time
import unittest


class TestGetPin(TestBase):

    def test_get_pin(self):
        self.blynk.start_blynk_heartbeat()
        while True:
            try:
                pin_value = self.blynk.get_pin_value('V1')
                print("Pin V1: {}".format(pin_value))

                pin_value = self.blynk.get_pin_value('V2')
                print("Pin V2: {}".format(pin_value))

                pin_value = self.blynk.get_pin_value('V3')
                print("Pin V3: {}".format(pin_value))

                pin_value = self.blynk.get_pin_value('V4')
                print("Pin V4: {}".format(pin_value))

                pin_value = self.blynk.get_pin_value('V5')
                print("Pin V5: {}".format(pin_value))

                pin_value = self.blynk.get_pin_value('V6')
                print("Pin V6: {}".format(pin_value))

            except:
                print("Exception")

            time.sleep(1)

if __name__ == '__main__':
    unittest.main()
