import unittest
import eliza

class Eliza_Tests(unittest.TestCase):

    def test_hello_goodbye(self):
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
    
    def test_syn_1(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        # Test matching synonyms
        self.assertEqual([['am']], el._match_decomp(['@be'], ['am']))
        self.assertEqual([['am']], el._match_decomp(['@be', 'a'], ['am', 'a']))
        self.assertEqual([['am']], el._match_decomp(['a', '@be', 'b'], ['a', 'am', 'b']))

    def test_syn_2(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        # Test non-matching synonyms
        self.assertIsNone(el._match_decomp(['@be'], ['a']))
        
    def test_happy(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        self.assertIn(el.respond('I am happy.'), ['That\'s wonderful! Tell me more', 'That\'s wonderful! What\'s been bringing you joy?'])

    def test_happy_animal(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        self.assertEqual(el.initial(), 'How do you do. Please tell me your problem.')
        self.assertIn(el.respond('I am happy about my dog.'), ['fur friends are great companions for people dealing with anxiety and depression'])
        self.assertEqual(el.final(), 'Goodbye, Thank you for talking to me.')
   
    def test_sad(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        self.assertIn(el.respond('I am happy.'), ['That\'s wonderful! Tell me more', 'That\'s wonderful! What\'s been bringing you joy?'])

    def test_sad_animal(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        self.assertEqual(el.initial(), 'How do you do. Please tell me your problem.')
        self.assertIn(el.respond('I am sad about my cat.'), ['What happened to your cat ?'])
        self.assertEqual(el.final(), 'Goodbye, Thank you for talking to me.')


    def test_angry(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        self.assertIn(el.respond('I am mad at my sister.'), ['Please tell me more about why you are mad at your sister .'])
        
    def test_surprise(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        self.assertIn(el.respond('I am surprised about the news.'), ['Why are you surprised about the news ?'])
       
    def test_fear(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        self.assertIn(el.respond('I am afraid of spiders.'),  ['Visualize yourself successfully facing and overcoming your fear in your mind\'s eye. Imagining yourself coping calmly and confidently with the fear-inducing situation can help build your confidence and resilience.'])

if __name__ == '__main__':
    unittest.main()