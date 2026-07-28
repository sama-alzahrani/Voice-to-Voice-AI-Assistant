import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from RealtimeSTT import AudioToTextRecorder

def speech_to_text():
    print("🎤 تكلم الآن...")

    recorder = AudioToTextRecorder(
        model="base",
        language="ar"
    )

    text = recorder.text()

    print("النص:", text)

    return text


if __name__ == "__main__":
    speech_to_text()
