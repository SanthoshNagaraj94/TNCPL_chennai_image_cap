import requests
from PIL import Image
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    #read url add as file in directory as image

    url=filename
    data = requests.get(url).content
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()
url=st.text_input("Enter the url of the image")
output = query(url)
image = Image.open(requests.get(url, stream=True).raw)

st.image(image)
st.title(output[0]['generated_text'])