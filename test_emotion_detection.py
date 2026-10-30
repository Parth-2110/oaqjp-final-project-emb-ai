import json
import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def get_emotions(self, statement):
        response = emotion_detector(statement)
        result = json.loads(response)
        return result["emotionPredictions"][0]["emotion"]

    def test_joy(self):
        emotions = self.get_emotions("I am glad this happened")
        self.assertGreater(emotions["joy"], emotions["anger"])

    def test_anger(self):
        emotions = self.get_emotions("I am really mad about this")
        self.assertGreater(emotions["anger"], emotions["joy"])

    def test_disgust(self):
        emotions = self.get_emotions(
            "I feel disgusted just hearing about this"
        )
        self.assertGreater(emotions["disgust"], emotions["joy"])

    def test_sadness(self):
        emotions = self.get_emotions("I am so sad about this")
        self.assertGreater(emotions["sadness"], emotions["joy"])

    def test_fear(self):
        emotions = self.get_emotions(
            "I am really afraid that this will happen"
        )
        self.assertGreater(emotions["fear"], emotions["joy"])


if __name__ == "__main__":
    unittest.main()
