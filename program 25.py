import openai

# Set your OpenAI API key
openai.api_key = 'sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'  # Replace with your actual API key

def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or use another available model
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

prompt = "Once upon a time"
generated_text = generate_text(prompt)
print(generated_text)
