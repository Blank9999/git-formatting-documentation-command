# doc.py

import os
import sys
from dotenv import load_dotenv
from groq import Groq

def understand_file(filename):
    f = open(filename,"r")
    pass

def document_file(filename):
    f = open(filename,"r")
    pass



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


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 doc.py <understand_file|document_file> <file_path>")
        sys.exit(1)
    
    command = sys.argv[1]
    file_path = sys.argv[2]
    
    load_dotenv()
    groq_key = os.getenv("GROQ_API_KEY")
    if not groq_key:
        raise ValueError("GROQ_API_KEY is missing. Make sure it's set in the .env file.")
    
    client = Groq(api_key=groq_key)
    message_history = [{"role": "system", "content": "Understand the provided file content for context."}]
    
    if command == "understand_file":
        understand_file(file_path, message_history)
    elif command == "document_file":
        document_file(file_path, client, message_history)
    else:
        print("Invalid command. Use 'understand_file' or 'document_file'.")
        sys.exit(1)
