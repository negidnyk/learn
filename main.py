import openai
from config import OPENAI_API_KEY


openai.api_key = OPENAI_API_KEY

# request = num = input('Enter a request for a picture to be generated: ')

text = openai.Completion.create(
  model="text-davinci-003",
  prompt="Description of the rubber duck including detailed information about the used materials, design features and purpose",
  max_tokens=150
)

response = openai.Image.create(
  prompt=text['choices'][0]['text'],
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']


print("Request:\n", text['choices'][0]['text'])
print("\nURL to a generated image:\n", image_url)
