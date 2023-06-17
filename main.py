import openai
from config import OPENAI_API_KEY

# get the API key from environment
openai.api_key = OPENAI_API_KEY

# block of generation of a text according to task
text = openai.Completion.create(
  model="text-davinci-003",
  prompt="Description of the rubber duck including detailed information about the used materials, design features and purpose",
  max_tokens=150
)

# receiving a text from response of text generation block
text_request = text['choices'][0]['text']

# generation of an image according to a response of the generation text block
response = openai.Image.create(
  prompt=text_request,
  n=1,
  size="1024x1024"
)

# receiving the URL to a generated image
image_url = response['data'][0]['url']

# show results to a user
print("Request:\n", text_request)
print("\nURL to a generated image:\n", image_url)
