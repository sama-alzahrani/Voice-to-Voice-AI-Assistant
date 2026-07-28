import asyncio
import edge_tts
import pygame

VOICE = "ar-SA-HamedNeural"

async def speak(text):
    communicate = edge_tts.Communicate(text=text, voice=VOICE)

    await communicate.save("response.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)


if __name__ == "__main__":
    asyncio.run(speak("مرحباً، أنا مساعدك الصوتي الذكي."))