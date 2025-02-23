import os
from dotenv import load_dotenv
from openai import OpenAI
import sys

load_dotenv()
your_api = os.getenv("YOUR_API_KEY")
your_model = "YOUR_MODEL"
your_base_url = "https://YOUR_BASE_URL_PATH"

client = OpenAI(
    api_key=your_api,
    base_url=your_base_url
)

def understand_file(file_list) :
    relation = ""
    for file in file_list:
        f = open(file,"r")
        content = f.read()

        prompt = relation + f"\n Analyze the following file:{content} and. \nFigure out the relation of this with other files and return the analysis. Dont hallucinate and create random names use the path i give which is {file} and dont make up things. give a small summary of how the relations work if they are being ipmorted from other files or not.You dont need to return unneccary code"
        response = client.chat.completions.create(
            model=your_model,
            n=1,
            messages=[
                {"role": "system", "content": "You are a professional code analyzer. Analyze the relation of the code across different files I give and write the analysis in order to understand if functions are being imported to other files where it is being imported from. Just understand the relation you dont have to write paragraphs on what is happening."},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        analysis = response.choices[0].message.content
        relation += f"\nAnalysis of file {file} is {analysis}"
    return relation

def document_file(file_list, relation):
    for file in file_list:
        f = open(file,"r")
        content = f.read()

        response = client.chat.completions.create(
            model=your_model,
            n=1,
            messages=[
                {"role": "system", "content": f"You are a AI Code Commentator. Write relevant comments for functions or any lines that require some explanation. When given code, only respond with the output code with relevant comments and use the analysis for the file when writing the code. Here is the analysis{relation}"},
                {
                    "role": "user",
                    "content": content
                }
            ]
        )

        text = response.choices[0].message.content
        print(f"This is the documented version of the file \n {text} \n")

        base, ext = file.rsplit('.', 1)
        documented_file = f"{base}_documented.{ext}"
        with open(documented_file,"w") as file_write:
            file_write.write(text)
        
    return 

def main():
    file_list = sys.argv[1:]
    if len(sys.argv) > 1:
        relation = understand_file(file_list)
        print("Finished analyzing the different files")
        document_file(file_list,relation)

if __name__ == "__main__":
    main()