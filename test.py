import os
import openai
openai.api_key = "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"


messages=[]
while True:
  user_content = input("user : ")
  messages.append({"role" : "user", "content" : f"{user_content}"})

  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

  assistant_content = completion.choices[0].message['content'].strip()

  messages.append({"role" : "assistant", "content" : f"{assistant_content}"})

  print(f"GPT : {assistant_content}")
