import json
from openai import OpenAI
import streamlit as st
def ask(query):
    # with open("./secrets.json","r") as f:
    #     json_file = json.load(f)

    # key = json_file['api_key']
    # print(key)
    key=st.secrets["OPENAI_API_KEY"]
    client = OpenAI(api_key=key)
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": query}],
    temperature=1,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response.choices[0].message.content


