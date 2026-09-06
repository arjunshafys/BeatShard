# test_beatshard.py
"""
Tests for BeatShard module.
"""

import unittest
from beatshard import BeatShard

class TestBeatShard(unittest.TestCase):
    """Test cases for BeatShard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BeatShard()
        self.assertIsInstance(instance, BeatShard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BeatShard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
