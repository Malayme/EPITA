from llama_cpp import Llama

llm = Llama(model_path="models/mistral7b.gguf", n_ctx=512)
output = llm("USER: How can I protect my password?\nASSISTANT:", max_tokens=100)
print(output["choices"][0]["text"].strip())
