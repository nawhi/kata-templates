from unittest import TestCase

from mycode.hello import HelloWorld


class TestHelloWorld(TestCase):
    def test_says_hello(self):
        self.assertEqual("Hello, World!", HelloWorld().hello()),

