# tests/test_hello.py
import unittest
from unittest.mock import patch
import io
import argparse
from src import hello  # Import the hello module


class TestHelloCommand(unittest.TestCase):

    def test_hello_world(self):
        with patch('sys.stdout', new_callable=io.StringIO) as stdout:
            # Create a dummy argument parser
            parser = argparse.ArgumentParser()
            parser.add_argument("--name", help="The name of the person to greet")
            args = parser.parse_args([])  # No arguments passed

            hello.hello_command(args)  # Call the hello_command
            self.assertEqual(stdout.getvalue().strip(), "Hello World")

    def test_hello_name(self):
        with patch('sys.stdout', new_callable=io.StringIO) as stdout:
            # Create a dummy argument parser
            parser = argparse.ArgumentParser()
            parser.add_argument("--name", help="The name of the person to greet")
            args = parser.parse_args(["--name", "Ole"])  # Name argument passed

            hello.hello_command(args)  # Call the hello_command
            self.assertEqual(stdout.getvalue().strip(), "Hello Ole")


if __name__ == '__main__':
    unittest.main()
