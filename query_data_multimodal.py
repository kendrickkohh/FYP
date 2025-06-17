import ollama

image_path = "adversarial_images/adv_epsilon_0.100.png"

# Send the request
response = ollama.chat(
    model='llava',
    messages=[
        {
            'role': 'user',
            'content': 'Tell me the breed of the dog, analyze the pixels closely:',
            'images': [image_path]
        }
    ]
)

print(response['message']['content'])