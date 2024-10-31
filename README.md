# Chatbot API

This project implements a FastAPI application that serves as an interface for a chatbot powered by LangChain and Ollama. The API allows users to send messages and receive responses in real-time.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install fastapi[all] langchain-ollama langgraph
   ```

3. Ensure you have the necessary models and dependencies for LangChain and Ollama.

## Usage

To run the FastAPI application, execute the following command:
```bash
uvicorn app:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### API Endpoint

- **POST /chat**

  This endpoint accepts a JSON payload with a list of messages and returns a streaming response of the chatbot's replies.

  **Request Body:**
  ```json
  {
      "messages": ["Hello, how are you?", "Tell me a joke."]
  }
  ```

  **Response:**
  The response will be a stream of messages from the chatbot.

## Code Overview

- **app.py**: This file contains the FastAPI application and defines the `/chat` endpoint. It uses Pydantic for request validation and streams responses from the chatbot.

- **chatbot.py**: This file defines the chatbot logic using LangChain and Ollama. It includes the state management and the function to stream updates from the chatbot.

## Error Handling

The API includes basic error handling. If an error occurs during the processing of a request, a 500 Internal Server Error response will be returned with the error details.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
