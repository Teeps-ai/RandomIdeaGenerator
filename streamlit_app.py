import streamlit as st
import openai

# OpenAI API Configuration
openai.api_key = st.secrets["openai_secret_key"]

# Function to generate a new random idea using GPT
def generate_random_idea():
    prompt = (
        "Generate creative and fun AI tool ideas for professionals. These tools should transform an input like an image, "
        "a document, or a conversation extract into a clear and actionable result in the form of a table, graph, or visual. "
        "The ideas must be original, accessible, and address everyday professional situations while remaining playful and engaging. "
        "Each idea should also include a 'haha moment' — a surprising, humorous, or delightfully unexpected twist that makes the tool stand out. "
        "Clearly describe the tool's purpose, how it works, and the format of the output."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use GPT-4 for higher creativity
        messages=[
            {"role": "system", "content": prompt}
        ],
        temperature=0.9,  # Higher temperature for more creative outputs
        max_tokens=200
    )
    idea = response["choices"][0]["message"]["content"]
    return idea

# Streamlit App
def main():
    st.title("Random Tool Idea Generator")
    st.write("Click the button to generate a completely random tool idea for your video content.")

    if st.button("Generate an Idea"):
        with st.spinner("Generating a creative idea with a 'haha moment'..."):
            random_idea = generate_random_idea()
            st.markdown("### Here's your random tool idea:")
            st.write(random_idea)

if __name__ == "__main__":
    main()
