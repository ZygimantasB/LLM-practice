import ollama

res = ollama.chat(
    model='llava:13b',
    messages=[{
        'role': 'user',
        'content': 'Does this image contain a gun or drug if gus yes yes of drugs say drug if no gu nand drug say no?',
        'images': ['F:\\Python GitHub ZygimantasB\\LLM-practice\\AI agent\\images\\R (5).jpeg']
    }]
)

print(res['message']['content'])

