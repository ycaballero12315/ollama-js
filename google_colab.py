from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

def generate_with_temp(prompt, temperature=1.0):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    
    outputs = model.generate(
        inputs,
        max_length=100,
        temperature=temperature,
        do_sample=True,
        top_p=0.95,
        num_return_sequences=3
    )
    
    for i, output in enumerate(outputs):
        text = tokenizer.decode(output, skip_special_tokens=True)
        print(f"\n--- Temperature {temperature} - Sample {i+1} ---")
        print(text)

# Probar diferentes temperaturas
for temp in [0.2, 0.7, 1.2]:
    generate_with_temp("El futuro de la IA es", temperature=temp)