import unittest
import eliza

class Eliza_Tests(unittest.TestCase):

    def test_hello(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        self.assertEqual(el.initial(), 'How do you do. Please tell me your problem.')
        self.assertIn(el.respond('Hello'), [
            'Hey, I am Eliza. How are you today ?',
            'How do you do.  Please state your problem.',
            'Hi.  What seems to be your problem ?',
            'Hey, How can I help you today ?'
        ])
        self.assertEqual(el.final(), 'Goodbye, Thank you for talking to me.')
    
    def test_happy_animal(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        self.assertEqual(el.initial(), 'How do you do. Please tell me your problem.')
        self.assertIn(el.respond('I am happy about my dog.'), ['fur friends are great companions for people dealing with anxiety and depression'])
        self.assertEqual(el.final(), 'Goodbye, Thank you for talking to me.')
        
    def test_sad_animal(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        self.assertEqual(el.initial(), 'How do you do. Please tell me your problem.')
        self.assertIn(el.respond('I am sad about my cat.'), ['What happened to your cat ?'])
        self.assertEqual(el.final(), 'Goodbye, Thank you for talking to me.')
        
    # Add more test methods here

if __name__ == '__main__':
    unittest.main()