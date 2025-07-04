import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_story(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a creative story writer."},
                {"role": "user", "content": f"Write a short, imaginative story based on this prompt: {prompt}"}
            ],
            max_tokens=500,
            temperature=0.8,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error generating story: {e}"
