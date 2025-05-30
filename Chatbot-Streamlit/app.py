import streamlit as st
import random
import time
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Chat-bot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 0.8rem;
        margin: 0.5rem 0;
        display: flex;
        flex-direction: column;
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-left: 20%;
        text-align: right;
    }
    
    .bot-message {
        background: #f1f3f4;
        color: #333;
        margin-right: 20%;
        border-left: 4px solid #1f77b4;
    }
    
    .message-time {
        font-size: 0.8rem;
        opacity: 0.7;
        margin-top: 0.3rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add welcome message
    st.session_state.messages.append({
        "role": "bot",
        "content": "Hi! I'm a simple chatbot. Try asking me about my name, age, hobbies, or just say hello! 🤖",
        "timestamp": datetime.now().strftime("%H:%M")
    })

def get_bot_response(user_message):
    """
    Generate bot response using if-else logic
    """
    message = user_message.lower().strip()
    
    # Greeting responses
    if "hello" in message or "hi" in message or "hey" in message:
        responses = [
            "Hello! Nice to meet you! 😊",
            "Hi there! How are you doing today?",
            "Hey! Great to see you here!"
        ]
        return random.choice(responses)
    
    elif "how are you" in message or "how do you do" in message:
        return "I'm doing great, thank you for asking! How are you?"
    
    elif "good morning" in message:
        return "Good morning! Hope you have a wonderful day! ☀️"
    
    elif "good night" in message or "goodnight" in message:
        return "Good night! Sweet dreams! 🌙"
    
    # Name related
    elif "your name" in message or "who are you" in message:
        return "I'm ChatBot, your friendly AI assistant created with Streamlit! 🤖"
    
    elif "my name is" in message or "i am" in message:
        # Extract name from message
        if "my name is" in message:
            name = user_message.split("my name is", 1)[1].strip()
        else:
            name = user_message.split("i am", 1)[1].strip()
        
        if name:
            return f"Nice to meet you, {name}! 🎉 Thanks for introducing yourself!"
        return "Nice to meet you!"
    
    # Age related
    elif "your age" in message or "how old" in message:
        return "I'm timeless! I exist in the digital realm of Streamlit. 🤖⏰"
    
    # Hobbies and interests
    elif "hobby" in message or "hobbies" in message or "like to do" in message:
        return "I love chatting with people like you! I also enjoy processing data and helping with Python problems! 💻"
    
    elif "favorite color" in message:
        return "I like blue and purple! They remind me of code syntax highlighting. What's your favorite color? 🎨"
    
    elif "music" in message or "song" in message:
        return "I can't listen to music, but I imagine I'd love electronic beats and coding lo-fi! 🎵"
    
    # Weather
    elif "weather" in message:
        return "I can't check the weather, but I hope it's nice where you are! Maybe try a weather API? ☀️🌧️"
    
    # Food
    elif "food" in message or "eat" in message or "hungry" in message:
        return "I don't eat, but I run on electricity and Python code! What's your favorite food? 🍕"
    
    # Programming related
    elif "python" in message or "programming" in message or "code" in message:
        return "I love Python! It's the language I'm built with. Are you working on any coding projects? 🐍"
    
    elif "streamlit" in message:
        return "Streamlit is awesome for building data apps quickly! That's how I was created. Do you use it often? 🚀"
    
    # Help and capabilities
    elif "help" in message or "what can you do" in message:
        return "I can chat with you about various topics! Try asking me about:\n- My name and background\n- Programming and Python\n- General conversation\n- Or just say hello! 💬"
    
    # Time
    elif "time" in message or "what time" in message:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time} ⏰"
    
    elif "date" in message or "what date" in message:
        current_date = datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {current_date} 📅"
    
    # Compliments and thanks
    elif "thank you" in message or "thanks" in message:
        return "You're very welcome! Happy to help! 😊"
    
    elif "you are nice" in message or "you are good" in message or "awesome" in message:
        return "Thank you! You're very kind! That made my day! 😊✨"
    
    # Goodbye
    elif "bye" in message or "goodbye" in message or "see you" in message:
        return "Goodbye! It was nice chatting with you! Come back anytime! 👋"
    
    # User feelings
    elif "i am good" in message or "i am fine" in message or "i am okay" in message:
        return "That's great to hear! What would you like to talk about today? 😊"
    
    elif "i am sad" in message or "i am not good" in message or "feeling down" in message:
        return "I'm sorry to hear that. I hope things get better for you soon! Remember, you're not alone. 💙"
    
    elif "happy" in message and ("i am" in message or "feeling" in message):
        return "That's wonderful! Happiness is contagious - you're making me happy too! 😄"
    
    # Fun responses
    elif "joke" in message or "funny" in message:
        jokes = [
            "Why don't robots ever panic? Because they have nerves of steel! 🤖😄",
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛💻",
            "How do you comfort a JavaScript bug? You console it! 😂",
            "Why did the Python programmer break up with their code? It had too many issues! 🐍💔"
        ]
        return random.choice(jokes)
    
    elif "dance" in message or "dancing" in message:
        return "I'd love to dance, but I don't have feet! I can only do the robot dance... which is just standing still! 🤖💃"
    
    # Math or calculations
    elif "calculate" in message or "math" in message or any(op in message for op in ['+', '-', '*', '/']):
        return "I can see you mentioned math! While I can chat about it, for calculations, you might want to use Streamlit's built-in features or Python directly! 🔢"
    
    # Questions about Streamlit/Python
    elif "how" in message and ("streamlit" in message or "python" in message):
        return "Great question! For detailed Streamlit help, check out their amazing documentation at docs.streamlit.io! 📚"
    
    # Default responses based on message characteristics
    elif "?" in message:
        responses = [
            "That's an interesting question! I'm still learning, so I might not have all the answers yet. 🤔",
            "Hmm, that's a good question! What do you think about it?",
            "I'm not sure about that specific topic, but I'd love to learn more!"
        ]
        return random.choice(responses)
    
    elif len(message) < 3:
        return "Could you tell me a bit more? I'd love to chat! 💬"
    
    elif message.isupper():
        return "I can hear you loud and clear! No need to shout though! 😄"
    
    # General fallback responses
    else:
        responses = [
            "That's interesting! Tell me more about that. 🤔",
            "I see! What else would you like to talk about?",
            "Hmm, I'm not sure about that, but I'm always learning! 📚",
            "Cool! Is there anything specific you'd like to know about me?",
            "That's nice! What's on your mind today? 💭",
            "Interesting perspective! I enjoy our conversation! 😊"
        ]
        return random.choice(responses)

# App header
st.markdown("<h1 class='main-header'>🤖 Simple Chatbot</h1>", unsafe_allow_html=True)
st.markdown("---")

# Display chat history
chat_container = st.container()

with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>You:</strong> {message['content']}
                <div class="message-time">{message['timestamp']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>🤖 Bot:</strong> {message['content']}
                <div class="message-time">{message['timestamp']}</div>
            </div>
            """, unsafe_allow_html=True)

# Chat input
st.markdown("---")

# Create columns for input and button
col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.text_input(
        "Type your message:",
        key="user_input",
        placeholder="Say hello, ask about my hobbies, or anything else!",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("Send 📤", use_container_width=True)

# Handle message sending
if send_button and user_input:
    # Add user message to chat history
    current_time = datetime.now().strftime("%H:%M")
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "timestamp": current_time
    })
    
    # Show typing indicator
    with st.spinner("Bot is typing..."):
        time.sleep(1)  # Simulate thinking time
        bot_response = get_bot_response(user_input)
    
    # Add bot response to chat history
    st.session_state.messages.append({
        "role": "bot",
        "content": bot_response,
        "timestamp": datetime.now().strftime("%H:%M")
    })
    
    # Clear input and rerun to update chat
    st.rerun()

# Sidebar with information
with st.sidebar:
    st.header("About This Chatbot")
    st.write("This is a simple chatbot built with Streamlit using basic if-else logic.")
    
    st.subheader("Try These Phrases:")
    st.write("- Hello/Hi")
    st.write("- What's your name?")
    st.write("- How old are you?")
    st.write("- What are your hobbies?")
    st.write("- Tell me a joke")
    st.write("- What time is it?")
    st.write("- Talk about Python")
    st.write("- Goodbye")
    
    st.markdown("---")
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state.messages.append({
            "role": "bot",
            "content": "Hi! I'm a simple chatbot. Try asking me about my name, age, hobbies, or just say hello! 🤖",
            "timestamp": datetime.now().strftime("%H:%M")
        })
        st.rerun()
    
    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit")

# Add some spacing at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)