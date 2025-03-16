# Llama-Coder

A Streamlit application that leverages TogetherAI's Llama 3 models to help users generate code and build applications through natural language prompts.

## Description

Llama-Coder is a tool designed to assist developers in coding tasks by utilizing the power of large language models (LLMs). By providing natural language descriptions of what you want to build, Llama-Coder generates functioning code snippets or complete applications using Meta's Llama 3 models via the TogetherAI API.

## Features

- Generate code snippets and applications from natural language descriptions
- Connect seamlessly to TogetherAI's API using your personal API key
- Access powerful Llama 3 models (default is Meta-Llama-3.1-8B-Instruct-Turbo-128K)
- Instantly view and copy generated code with syntax highlighting
- Suitable for prototyping, learning new programming concepts, or solving coding challenges

## Requirements

- Python 3.6+
- Streamlit
- Requests

## Installation

### Setting up a Virtual Environment

It's recommended to use a virtual environment to avoid conflicts with other Python projects:

#### For Windows:
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate
```

#### For macOS and Linux:
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

### Installing Dependencies

Once your virtual environment is activated:

1. Clone this repository or download the source code
2. Install the required dependencies:

```bash
pip install streamlit requests
```

## Usage

1. Ensure your virtual environment is activated
2. Run the Streamlit application:

```bash
streamlit run app.py
```

3. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)
4. Enter your TogetherAI API key (you can get this from your TogetherAI account)
5. Choose a model or use the default Meta-Llama-3.1-8B-Instruct-Turbo-128K
6. Describe the code or application you want to generate
7. Click "Generate App" to receive the code

## API Key Security

Please note that while the API key input field is masked for privacy, you should be careful about sharing your application or code with others. Your API key is sensitive information that should be kept private.

## Example Prompts

- "Create a Flask API with endpoints for user registration and login"
- "Write a Python function that analyzes sentiment from text input"
- "Generate a Streamlit dashboard that visualizes stock market data"
- "Build a simple web scraper that extracts product information from an e-commerce site"
- "Create a machine learning model that predicts house prices based on features"

## Tips for Better Results

1. Be specific about the programming language and frameworks you want to use
2. Describe the functionality you need in detail
3. Mention any specific libraries or approaches you prefer
4. For complex applications, consider breaking down your request into smaller components

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- [TogetherAI](https://together.xyz/) for providing the API access to Llama models
- [Meta](https://ai.meta.com/) for developing the Llama 3 models
- [Streamlit](https://streamlit.io/) for the web application framework
