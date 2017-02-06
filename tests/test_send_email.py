import time
from pyblynkrestapi import PyBlynk

def test_send_email():
    auth_token = '6972da34051e44ba8115b7d3c2fa8514'
    blynk = PyBlynk.PyBlynk(auth_token=auth_token)

    blynk.start_blynk_heartbeat()
    try:
        blynk.send_email('new subject', 'contents', 'theyoungsoul@gmail.com')
        blynk.send_push_notification('blynk push')
        print("Done")
        time.sleep(300)
    finally:
        blynk.is_stopped = True


if __name__ == '__main__':
    test_send_email()
    print("Done testing send email")
