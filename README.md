# Charles

This is a chatbot that uses ChatterBot for basic conversation and GPT-2 for more advanced responses. It also learns from GPT-2 over time to become similar. I hope you enjoy!

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/my-chatbot-repo.git
    cd my-chatbot-repo
    ```

2. Ensure you have Python 3.8.19 installed. You can use `pyenv` to manage Python versions:
    ```sh
    pyenv install 3.8.19
    pyenv local 3.8.19
    ```

3. Alternatively, you can use the provided setup script to create a virtual environment:
    ```sh
    ./setup.sh
    source venv/bin/activate
    ```

4. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

5. Or you can install dependencies using `poetry` Instead:
    ```sh
    poetry install
    ```

6. Run the chatbot:
    ```sh
    python chatbot.py
    ```

## Usage

Start the conversation by typing a message and pressing Enter. The bot will respond to your input. You can provide feedback on the bot's responses and help it learn by suggesting better responses.

Type 'bye', 'exit', or 'quit' to end the conversation.
