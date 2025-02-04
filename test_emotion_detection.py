from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        case_1 = emotion_detector("I am glad this happened")
        self.assertEqual(case_1['dominant_emotion'], 'joy')

        case_2 = emotion_detector("I am really mad about this")
        self.assertEqual(case_2['dominant_emotion'], 'anger')

        case_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(case_3['dominant_emotion'], 'disgust')

        case_4 = emotion_detector("I am so sad about this")
        self.assertEqual(case_4['dominant_emotion'], 'sadness')

        case_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(case_5['dominant_emotion'], 'fear')

unittest.main()