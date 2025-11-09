import sys
import os
import unittest

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import from app.py file, not app/ directory
import app  # noqa: E402


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(app.greet("World"), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
