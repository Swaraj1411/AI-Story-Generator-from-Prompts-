import os
import google.generativeai as genai

genai.configure(api_key='AIzaSyDdrF4zxOppHdXt-LpwRUv3cegWEIcFKkg')

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_story(prompt: str) -> str:
    try:
        response = model.generate_content(
            f"Write a short, imaginative story based on this prompt: {prompt}",
            generation_config={
                "temperature": 0.8,
                "max_output_tokens": 500,
                "top_p": 1.0,
                "top_k": 40
            }
        )
        return response.text.strip()
    except Exception as e:
        return f"Error generating story: {e}"
