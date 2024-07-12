# Web Page Question Answering App

This application allows users to ask questions about the content of a web page using advanced natural language processing techniques. It combines web scraping, text processing, and AI-powered question answering to provide informative responses based on the content of any given web page.

## Features

- Web page content extraction
- Text processing and vectorization
- AI-powered question answering using GPT-4
- Command-line interface
- Web-based user interface using Streamlit

## Technologies Used

- Python 3.8+
- LangChain: For building the retrieval-augmented generation (RAG) pipeline
- OpenAI GPT-4: For natural language understanding and generation
- Chroma: For vector storage and similarity search
- BeautifulSoup4: For web scraping
- Streamlit: For the web-based user interface

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/timkitch/yt-coding-assistants-rag-tutorial.git
   cd yt-coding-assistants-rag-tutorial
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

## Usage

### Command-line Interface

Run the main script:

```
python main.py
```

Follow the prompts to enter a URL and ask questions about the web page content.

### Web Interface

Launch the Streamlit app:

```
streamlit run streamlit_app.py
```

Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

1. Enter the URL of the web page you want to analyze.
2. Wait for the page to be processed.
3. Enter your questions in the text input field.
4. View the AI-generated answers based on the web page content.

## Project Structure

- `main.py`: Contains the core logic for document processing, vector store creation, and RAG chain setup.
- `utils.py`: Utility functions for user input and output handling.
- `streamlit_app.py`: Streamlit web application interface.
- `requirements.txt`: List of Python dependencies.
- `.env`: Configuration file for environment variables (not tracked in git).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
