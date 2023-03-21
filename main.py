import openai

#######

#######
with open('passwd.txt', 'r') as file:

    # Read the first line of the file and assign it to a string variable
    openai.api_key = file.readline()

model_engine = "text-davinci-003"

prompt = "Hello, how are you today?"

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)