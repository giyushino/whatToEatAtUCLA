from transformers import pipeline, set_seed

# Set up the text generation pipeline with the model
generator = pipeline('text-generation', model='distilgpt2', device=0)  # device=0 for GPU (use -1 for CPU)

# Set the seed for reproducibility
set_seed(42)

# Generate text based on the input prompt
output = generator("Hello, I’m a language model", 
                   max_length=20, 
                   num_return_sequences=5, 
                   truncation=True)  # Explicitly set truncation=True

# Print generated outputs
for idx, result in enumerate(output):
    print(f"Generated {idx + 1}: {result['generated_text']}")

