import openai

# Ganti dengan API key kamu
openai.api_key = "API_KEY_KAMU"

def tanya_ai(pertanyaan):
    client = openai.OpenAI()  # Inisialisasi client

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Kamu adalah asisten pintar."},
            {"role": "user", "content": pertanyaan}
        ]
    )
    jawaban = response.choices[0].message.content
    return jawaban

while True:
    user_input = input("Kamu: ")
    if user_input.lower() in ["exit", "keluar", "quit"]:
        break
    hasil = tanya_ai(user_input)
    print("AI:", hasil)
