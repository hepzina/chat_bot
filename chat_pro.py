import nltk
import streamlit as st
from nltk.chat.util import Chat, reflections

# Define the chatbot data
data = [
    [r"(hi|hey|hello|hey there)", ["Hi, wagwan"]],
    [r"(.*name)", ["My name is Dark"]],
    [r"(.*old|.*age)", ["I am an immortal"]],
    [r"(.*belief|.*religion)", ["I am Christian"]],
    [r"(.*activity|.*interest|.*hobby)", ["I like coding, watching documentaries, and listening to music"]],
    [r"(.*skills|.*abilities|.*tools)", ["Pandas, NumPy, statistical analysis, SQL"]],
    [r"(.*experience)", ["I help implement solutions that empower businesses and create data flows"]],
    [r"(.*about|.*interest)", ["You are a developer working on Python-based projects, including advanced mathematical calculators, Flask web applications with MySQL integration, and collaborative work in Google Colab."]]
]

# Create the chatbot instance
chatbot = Chat(data, reflections)

# Streamlit UI setup
st.title("Chatbot with Streamlit")
st.write("Welcome to the chatbot! Type 'exit' to end the chat.")

# Session state to maintain chat history
if "history" not in st.session_state:
    st.session_state["history"] = []

# Get user input
user_input = st.text_input("You:", "")

# Process the user's input and generate a response
if user_input:
    if user_input.lower() == "exit":
        bot_response = "I am gone. Goodbye!"
    else:
        bot_response = chatbot.respond(user_input)
        if bot_response is None:
            bot_response = "Sorry, I didn't understand that. Could you rephrase?"

    # Display the bot's response immediately below the input
    st.write(f"**Bot:** {bot_response}")

    # Append user input and bot response to the history
    st.session_state["history"].append(("You", user_input))
    st.session_state["history"].append(("Bot", bot_response))

# Display the chat history in the sidebar
with st.sidebar:
    st.write("### Chat History")
    for sender, message in st.session_state["history"]:
        st.write(f"**{sender}:** {message}")


