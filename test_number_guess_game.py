import unittest
from number_guess_game import guess_number

class TestNumberGuessGame(unittest.TestCase):
    
    def test_guess_lower(self):
        """Test when the guess is lower than the target number"""
        result = guess_number(50, 30)
        self.assertEqual(result, 'lower')
    
    def test_guess_higher(self):
        """Test when the guess is higher than the target number"""
        result = guess_number(50, 70)
        self.assertEqual(result, 'higher')
    
    def test_guess_correct(self):
        """Test when the guess is correct"""
        result = guess_number(50, 50)
        self.assertEqual(result, 'correct')
    
    def test_guess_at_boundaries(self):
        """Test guesses at the boundaries (1 and 100)"""
        self.assertEqual(guess_number(1, 1), 'correct')
        self.assertEqual(guess_number(100, 100), 'correct')
        self.assertEqual(guess_number(50, 1), 'lower')
        self.assertEqual(guess_number(50, 100), 'higher')
    
    def test_multiple_comparisons(self):
        """Test multiple sequential guesses"""
        target = 42
        self.assertEqual(guess_number(target, 20), 'lower')
        self.assertEqual(guess_number(target, 60), 'higher')
        self.assertEqual(guess_number(target, 42), 'correct')

if __name__ == '__main__':
    unittest.main()