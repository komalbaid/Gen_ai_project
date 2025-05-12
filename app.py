from transformers import pipeline, set_seed
import streamlit as st

# Load pre-trained GPT-2 generator
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

# Streamlit UI
st.title("📚 Story Generator using Generative AI")
st.write("Enter a sentence or story beginning and let AI complete it!")

input_text = st.text_input("Enter the beginning of your story:")

if input_text:
    st.subheader("🔮 Generated Story Continuations:")
    outputs = generator(input_text, max_length=100, num_return_sequences=3)
    for i, output in enumerate(outputs):
        st.markdown(f"**{i+1}.** {output['generated_text']}")
