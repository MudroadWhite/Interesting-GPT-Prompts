import openai

############################
# INITIALIZATION
############################
with open('passwd.txt', 'r') as file:

    # Read the first line of the file and assign it to a string variable
    openai.api_key = file.readline()

# MODEL LIST: https://platform.openai.com/docs/models/
# model_engine = "text-davinci-003"
# model_engine = "gpt-4-32k-0314"
model_engine = "gpt-3.5-turbo"
chat_history = []

############################
# PROMPT
# API ref: https://platform.openai.com/docs/guides/chat/introduction
############################

response = openai.ChatCompletion.create(
    model=model_engine,
    messages=[
        {"role": "system", "content": "You are a friendly and helpful assistant. You explain concepts in great depth using simple terms, and you give examples to help people learn. You know what the human thinks, and is eager to help him develop his thoughts"},
        {"role": "user", "content": "Show me what I'm thinking of."},
        {"role": "assistant", "content": "Sure! "},
    ],
    temperature=0,
)

# # calculate the time it took to receive the response
# response_time = time.time() - start_time

# print(response)
print(response["choices"][0]["message"]["content"])