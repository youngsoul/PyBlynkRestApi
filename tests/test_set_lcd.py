from tests.test_base import TestBase
import time
import unittest

class TestSetLcd(TestBase):

    def test_set_pin(self):
        self.blynk.start_blynk_heartbeat()
        i = 0
        while True:
            try:
                #self.blynk.set_pin_value('V5', i)
                #self.blynk.set_pin_value('V6', i*100)
                #lcd.line0_value = "Line 0: {}".format(i)
                #lcd.line1_value = "Line 1: {}".format(i*100)
                self.blynk.set_lcd('V5', "Line 0: {}".format(i), 'V6', "Line 1: {}".format(i*100))
                i += 1
            except:
                print("Exception")

            time.sleep(1)

if __name__ == '__main__':
    unittest.main()
