from pyblynkrestapi.PyBlynk import PyBlynk
import time

auth_token = '117f1ca4965f43458a24cc8105ca35ee'


pb = PyBlynk(auth_token=auth_token)


if __name__ == '__main__':
    flag = True
    while True:
        #pb.get_pin_value('V1')
        if flag:
            pb.led_on('V10')
            pb.set_pin_value('V9', 'Tripped')
            flag = False
        else:
            flag = True
            pb.led_off('V10')
            pb.set_pin_value('V9', 'OK')
        time.sleep(2)


