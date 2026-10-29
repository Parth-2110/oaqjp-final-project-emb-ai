
from EmotionDetection.emotion_detection import emotion_detector


def test_emotion_detector():
    statements = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for statement, expected_emotion in statements.items():
        result = emotion_detector(statement)
        print(f"Statement: {statement}")
        print(f"Expected emotion: {expected_emotion}")
        print(f"Result: {result}")
        print()

if __name__ == "__main__":
    test_emotion_detector()
