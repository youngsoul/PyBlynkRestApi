from tests.test_base import TestBase
import time
import unittest


class TestGetTimeInput(TestBase):

    def test_get_pin(self):
        self.blynk.start_blynk_heartbeat()
        while True:
            try:
                pin_value = self.blynk.get_pin_value('V13')
                print("Pin V13: {}".format(pin_value))


            except Exception as exc:
                print("Exception")

            time.sleep(1)

if __name__ == '__main__':
    unittest.main()
