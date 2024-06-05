from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
import gpt_2_simple as gpt2
import os

# Initialize ChatterBot with a SQLite database
def initialize_chatterbot():
    bot = ChatBot(
        'MyBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///shared_database.sqlite3',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, but I do not understand.',
                'maximum_similarity_threshold': 0.1  # Lower confidence threshold
            }
        ]
    )
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train('chatterbot.corpus.english')
    return bot

# Initialize GPT-2
def initialize_gpt2(model_name='124M'):
    if not os.path.exists(f'./checkpoint/run1/{model_name}'):
        gpt2.download_gpt2(model_dir='./checkpoint/run1/', model_name=model_name)
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, model_name=model_name)
    return sess

# Function to interact with GPT-2
def get_gpt2_response(sess, prompt):
    response = gpt2.generate(sess, prefix=prompt, return_as_list=True)[0]
    return response.strip()

# Function to get a response from the chatbot
def get_chatbot_response(bot, user_input):
    response = bot.get_response(user_input)
    return response

# Main conversation loop
def conversation_loop(bot, sess):
    while True:
        user_input = input("You: ")

        # Get response from the bot
        response = get_chatbot_response(bot, user_input)

        # If bot's confidence is low, use GPT-2
        if response.confidence < 0.5:
            bot_response = get_gpt2_response(sess, user_input)
        else:
            bot_response = response.text

        # Print bot's response
        print("Bot:", bot_response)

        # Ask for feedback
        feedback = input("Did the bot's response meet your expectations? (yes/no): ").lower()
        if feedback == "no":
            edit_phrase = input("Please provide the edited response or type 'skip' to continue: ")
            if edit_phrase.lower() != 'skip':
                # Create Statement objects
                edited_statement = Statement(edit_phrase)
                original_statement = Statement(user_input)
                # Learn the edited response
                bot.learn_response(edited_statement, original_statement)

        # Exit loop if user wants to end conversation
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Goodbye!")
            break

if __name__ == "__main__":
    bot = initialize_chatterbot()
    sess = initialize_gpt2()

    try:
        conversation_loop(bot, sess)
    finally:
        # Close the GPT-2 session properly
        gpt2.reset_session(sess)
