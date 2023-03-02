import openai
import streamlit as st
import os

# Set up the OpenAI API key from the environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Function to send a message to the OpenAI chatbot model and return its response
def send_message(message_log):
    # Use OpenAI's ChatCompletion API to get the chatbot's response
    response = openai.Completion.chat.create(
        engine="chat-3.5-turbo",      # The name of the OpenAI chatbot model to use
        prompt=message_log,    # The conversation history up to this point, as a string
        max_tokens=4024,       # The maximum number of tokens (words or subwords) in the generated response
        stop=None,             # The stopping sequence for the generated response, if any (not used here)
        temperature=0.7,       # The "creativity" of the generated response (higher temperature = more creative)
    )

    # Get the generated response from the API response
    return response.choices[0].text

# Main function that runs the chatbot
def main():
    # Add a sidebar with a text input box for the API key
    st.sidebar.title("OpenAI Chatbot")
    api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

    # Set up the OpenAI API key from the input value
    openai.api_key = api_key

    # Initialize the conversation history with a message from the chatbot
    message_log = "You are a helpful assistant.\n"

    # Start a loop that runs until the user types "quit"
    while True:
        # Get the user's input and add it to the conversation history
        user_input = st.text_input("You:", "")
        message_log += f"User: {user_input}\n"

        # If the user types "quit", end the loop and print a goodbye message
        if user_input.lower() == "quit":
            st.write("Goodbye!")
            break

        # Send the conversation history to the chatbot and get its response
        response = send_message(message_log)

        # Add the chatbot's response to the conversation history and print it to the console
        message_log += f"Chatbot: {response}\n"
        st.write("Chatbot:", response)

# Call the main function
if __name__ == "__main__":
    main()
