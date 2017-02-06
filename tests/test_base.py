import unittest
from pyblynkrestapi.PyBlynkRestApi import PyBlynkRestApi


class TestBase(unittest.TestCase):

    def __init__(self,*args, **kwargs):
        super(TestBase, self).__init__(*args, **kwargs)
        self.auth_token = ''
        self.blynk = PyBlynkRestApi(auth_token=self.auth_token)

