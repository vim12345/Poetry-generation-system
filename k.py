import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
 
# 1. Load the pre-trained GPT-2 model and tokenizer
model_name = "gpt2"  # GPT-2 model (can be replaced with a larger model like gpt2-medium)
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
 
model.eval()  # Set model to evaluation mode
 
# 2. Generate poetry from a prompt
def generate_poetry(prompt, max_length=100, temperature=0.7, top_p=0.9):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    
    # Generate poetry with the model
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1,
                                 temperature=temperature, top_p=top_p, no_repeat_ngram_size=2)
    
    poetry = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return poetry
 
# 3. Example poetry prompt and generation
prompt = "The moonlit sky is full of dreams, where"
generated_poetry = generate_poetry(prompt)
 
print("Generated Poetry:")
print(generated_poetry)
