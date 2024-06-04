# Medical-Chat-Bot

This project leverages generative AI to create a medical chatbot that provides suggestions based on the GALE Encyclopedia of Medicine 2. The system uses `Python`, `LangChain`, `ChromaDB`, `LLaMA2`, and `Hugging Face` to generate accurate responses to user queries.

## Features

- Uses GALE Encyclopedia of Medicine 2 as the knowledge base.
- Embeds the encyclopedia content using an embedding LLM.
- Utilizes LLaMA2, an offline generative AI model, to provide accurate responses.
- Stores embeddings in a vector database (ChromaDB) for efficient retrieval.
- Provides medical suggestions based on user queries.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- GALE Encyclopedia of Medicine 2 in digital format (PDF or TXT)
- LLaMA2 model from Hugging Face
- ChromaDB
- LangChain
- Hugging Face Transformers

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/medical-chatbot.git
    cd medical-chatbot
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Download and set up the LLaMA2 model:
    - Follow the instructions on [Hugging Face](https://huggingface.co) to download the LLaMA2 model.
    - Place the model files in the `models/llama2` directory.

## Setup

1. Prepare the GALE Encyclopedia of Medicine 2 content:
    - Convert the content to a suitable format (if necessary).
    - Embed the content using an embedding LLM.

2. Store the embeddings in ChromaDB:
    - Use the provided script `embed_and_store.py` to process the encyclopedia and store the embeddings in ChromaDB.
    ```bash
    python embed_and_store.py
    ```

3. Configure the environment:
    - Create a file named `.env` in the root directory and add necessary configuration:
        ```env
        LLM_MODEL_PATH=models/llama2
        CHROMADB_PATH=db/chromadb
        ```

## Usage

1. Run the chatbot application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://localhost:8000` to interact with the chatbot.

3. Enter your medical query to receive suggestions based on the GALE Encyclopedia of Medicine 2.

## Project Structure

- `app.py`: Main application file for running the chatbot.
- `embed_and_store.py`: Script to embed the encyclopedia content and store in ChromaDB.
- `chatbot.py`: Logic for interacting with the user and generating responses.
- `requirements.txt`: List of Python packages required for the project.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please contact us at your- ss.forcodin@gmail.com.

---
