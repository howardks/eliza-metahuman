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
    def test_happy_day(self):
        el = eliza.Eliza()
        el.load('api/doctor.text')
        self.assertEqual(el.initial('I went out'), 'How was your day')
        self.assertIn(el.respond('I went to the park.'), ['That is great, Spending time in the nature is always a good idea'])
        self.assertEqual(el.final(), 'Goodbye, Thank you for talking to me.')
    
    def test_custom_patterns(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        # Add custom patterns (e.g., related to hobbies)
        el.add_pattern('hobby', ['Tell me about your favorite hobby.'])
        # Test response for custom pattern
        self.assertEqual(el.respond('I love gardening.'),
                        'Tell me about your favorite hobby.')
   
   
    def test_syn_1(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        # Test matching synonyms
        self.assertEqual([['am']], el._match_decomp(['@be'], ['am']))
        self.assertEqual([['am']], el._match_decomp(['@be', 'a'], ['am', 'a']))
        self.assertEqual([['am']],
                        el._match_decomp(['a', '@be', 'b'], ['a', 'am', 'b']))

    def test_syn_2(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')
        # Test non-matching synonyms
        self.assertIsNone(el._match_decomp(['@be'], ['a']))
        


    def test_random_response(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')  # Load patterns (or use your own patterns)
        input_phrase = 'Tell me about your day.'
        # Generate multiple responses and check if they vary
        responses = set()
        for _ in range(10):
            responses.add(el.respond(input_phrase))
        self.assertGreater(len(responses), 1)  # Ensure there's variation


    def test_edge_cases(self):
        el = eliza.Eliza()
        el.load('api/doctor.txt')  # Load patterns 
        # Test with empty input
        self.assertEqual('I am listening.', el.respond(''))
        # Test with single-word input
        self.assertEqual('Tell me more about it.', el.respond('Hello'))
        # Test with input containing special characters
        self.assertEqual('What do you mean by "123@xyz"?',
                        el.respond('What is 123@xyz?'))
        # Test with long input
        long_input = ' '.join(['word'] * 100)
        self.assertEqual('I am listening.', el.respond(long_input))

if __name__ == '__main__':
    unittest.main()