import openai

client = openai.OpenAI()


def summarize(text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Summarize: {text}"}],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print(summarize("Scheduled scans run Detect AI and Create BOMs on a cadence."))
