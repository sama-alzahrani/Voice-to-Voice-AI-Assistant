import os
import cohere
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

# قراءة مفتاح API
api_key = os.getenv("COHERE_API_KEY")

# إنشاء عميل Cohere
co = cohere.ClientV2(api_key)


def generate_response(user_message):
    response = co.chat(
        model="command-r7b-arabic-02-2025",
        messages=[
            {
                "role": "system",
                "content": "أنت مساعد صوتي ذكي، أجب دائماً باللغة العربية الفصحى بإجابة واضحة ومختصرة."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return response.message.content[0].text


if __name__ == "__main__":
    question = input("اكتب سؤالك: ")
    answer = generate_response(question)
    print("\nالرد:")
    print(answer)