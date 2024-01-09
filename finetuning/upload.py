from openai import OpenAI

OPEN_AI_KEY = "OPEN_AI_KEY"
client = OpenAI()
client.files.create(
  file=open("dataLLM.jsonl", "rb"),
  purpose="fine-tune"
)


# fileID = file-Ip8i2YfaOJjuOed0k0fveP1q