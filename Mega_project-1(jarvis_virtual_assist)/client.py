from openai import OpenAI
client=OpenAI(    
        api_key="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"
)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "command"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")