import unittest
from src.input import InputHandler

class TestInputHandler(unittest.TestCase):
    def setUp(self):
        self.input_handler = InputHandler()

    def test_key_mapping(self):
        self.input_handler.map_key('w', 'move_up')
        self.assertEqual(self.input_handler.key_mapping['w'], 'move_up')

    def test_controller_input(self):
        self.input_handler.map_controller_button('A', 'jump')
        self.assertEqual(self.input_handler.controller_mapping['A'], 'jump')

    def test_invalid_key_mapping(self):
        with self.assertRaises(KeyError):
            self.input_handler.map_key('invalid_key', 'action')

    def test_controller_button_not_mapped(self):
        self.assertIsNone(self.input_handler.get_action_for_controller_button('B'))

if __name__ == '__main__':
    unittest.main()