# doc.py

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq_key = os.getenv("GROQ_KEY")

client = Groq(
    api_key=groq_key,
)

# def understand_file(filename):
#     f = open(filename,"r")
#     pass

# def documented_file(filename):
#     f = open(filename,"r")
#     pass



# content = f.read()

# query = "\document these function using the best practice for python"
# content += query

# # print(content)

# chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": query
#             }
#         ],
#         # model="llama-3.3-70b-versatile",
#         model="deepseek-r1-distill-llama-70b",
#     )

# response = chat_completion.choices[0].message.content

