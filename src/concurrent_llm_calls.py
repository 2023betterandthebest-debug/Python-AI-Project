from config import GROQ_API_KEY, MODEL_NAME
import time
import asyncio
from groq import AsyncGroq

client =AsyncGroq(api_key=GROQ_API_KEY)
MODEL_NAME = MODEL_NAME

prompts = [
"Explain AI agents in one sentence.",
"Explain Prompt Engineering in 1 sentence.",
"Explain RAG in one sentence.",
"Explain tool calling in one sentence.",
"Explain agent memory in one sentence"
]

async def call_llm(prompt):
    response = await client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=80)
    return response.choices[0].message.content

async def main():
    start =time.perf_counter()
    tasks = [call_llm(p) for p in prompts]
    results = await asyncio.gather(*tasks)
    end= time.perf_counter()
    for i, r in enumerate(results, 1):
        print(f"\nResponse {i}:\n{r}")
    print(f"\nConcurrent time: {end - start:.2f} seconds")
asyncio.run(main())