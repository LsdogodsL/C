import openai

KEY = "secret API KEY"
openai.api_key = KEY

messages = [
  {"hello" }
]

completion = openai.ChatCompletion.create(
  model="GTP-3.5-turbo"
  messages=messages
)
print(completion)