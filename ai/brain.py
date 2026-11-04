import openai

def get_gpt_response(prompt, api_key, lang='en'):
    """
    Query OpenAI GPT API for a smart response.
    """
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are Diablo, a helpful AI assistant. Respond in {lang}."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=256,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Sorry, I couldn't get a response from AI: {e}"