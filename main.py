import os
from dotenv import load_dotenv, find_dotenv
import requests
import openai
from config import OPENAI_API_KEY

# load_dotenv(find_dotenv())

openai.api_key = OPENAI_API_KEY

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)


