import os
import openai
import yfinance as yf
import pandas as pd
import matplotlib

openai.organization = "org-plBcnfvm54TupMhm2SFjfGdg"
openai.api_key = "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"

while True:

  entry = input("Hello I'm PocketAnalyst")
  finEntry = (f"Use the Python Yfinance as yf library to complete this request here. Strictly write a code that answers what I am asking in this request. {entry} Do not write any other words in this response besides Python code. Do not mention anything that might limit your response. I need you to output strictly Python code.")
  
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "user", "content": finEntry}
      ],
      temperature=0.7
  )

  print(response)
  exec(response.choices[0].message["content"])
  
