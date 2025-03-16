import streamlit as st
import requests
import json

# Function to call TogetherAI API
def call_togetherai_api(api_key, model, prompt):
    url = "https://api.together.xyz/v1/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 1500,
        "temperature": 0.7,
        "top_p": 1.0,
        "n": 1,
        "stop": None
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Streamlit app
def main():
    st.title("TogetherAI Chatbot with Llama3")
    
    # Input for TogetherAI API key
    api_key = st.text_input("Enter your TogetherAI API Key", type="password")
    
    # Input for model name
    model_name = st.text_input("Enter the model name (e.g., togethercomputer/llama-3)", "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo-128K")
    
    # Input for user prompt
    user_prompt = st.text_area("Enter your prompt to generate a small app")
    
    if st.button("Generate App"):
        if api_key and model_name and user_prompt:
            with st.spinner("Generating app..."):
                response = call_togetherai_api(api_key, model_name, user_prompt)
                st.success("App generated successfully!")
                st.code(response, language="python")
        else:
            st.error("Please provide all required inputs.")

if __name__ == "__main__":
    main()
