# Poetry-generation-system

# Description:
A poetry generation system is a creative application of generative models that produces poetry based on a given prompt or theme. Similar to story generation, poetry generation requires the model to capture not just the meaning of the text but also the structure, rhythm, and often the rhyme. In this project, we will implement a poetry generation system using a language model (e.g., GPT-2) to create poetic text that adheres to stylistic and structural elements.

# ✅ What It Does:
* Uses a pre-trained GPT-2 model to generate poetry based on a given prompt.

* The tokenizer encodes the input prompt, which is then passed through the model to generate poetic text.

* The model generates a continuation of the input prompt in the style of poetry, considering creativity, rhyme, and rhythm.

# Key features:
* Temperature controls the randomness of predictions, with lower values making the output more deterministic.

* Top-p sampling (nucleus sampling) ensures the model selects tokens from a subset of the probability distribution that covers the cumulative probability of p.

* The model generates short poetic texts with creative expressions, often fitting the input prompt's theme and style.
