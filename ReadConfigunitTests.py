import unittest
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class ReadConfigunitTests(unittest.TestCase):

    def test_getConfig_from_env(self):
        config =  os.environ.get('CONFIG')
        assert config is not None
        
    def test_string_config(self):
        config =  os.environ.get('CONFIG')
        self.assertEqual('configtest', config)

    def test_getConfig1_from_env(self):
        config =  os.environ.get('CONFIG1')
        assert config is not None

if __name__ == '__main__':
    unittest.main()
