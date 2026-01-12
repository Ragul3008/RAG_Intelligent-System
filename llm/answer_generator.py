from transformers import pipeline

# Local instruction-tuned model
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def generate_answer(prompt, model_name=None):
    output = generator(
        prompt,
        max_length=256,
        do_sample=False
    )
    return output[0]["generated_text"]
