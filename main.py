import asyncio

from speech_to_text import speech_to_text
from llm import generate_response
from text_to_speech import speak


def main():

    print("=" * 50)
    print("🤖 Voice-to-Voice AI Assistant")
    print("=" * 50)
    print("قل (خروج) لإنهاء البرنامج.\n")

    while True:

        # تحويل الصوت إلى نص
        user_text = speech_to_text()

        if not user_text:
            continue

        print(f"\n👤 أنت: {user_text}")

        # إنهاء البرنامج
        if user_text.strip().lower() in ["خروج", "انهاء", "وقف", "exit", "quit"]:
            print("👋 إلى اللقاء!")
            break

        # إرسال النص إلى Cohere
        ai_response = generate_response(user_text)

        print(f"\n🤖 المساعد: {ai_response}\n")

        # تحويل الرد إلى صوت
        asyncio.run(speak(ai_response))


if __name__ == "__main__":
    main()