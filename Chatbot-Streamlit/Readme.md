# 🤖 Simple Streamlit Chatbot

A user-friendly chatbot built with Streamlit using basic if-else logic for conversational AI. This project demonstrates how to create an interactive chat interface with Python and Streamlit.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.0+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Features

- **Interactive Chat Interface**: Clean and modern UI with custom CSS styling
- **Real-time Conversations**: Instant responses with typing indicators
- **Persistent Chat History**: Messages saved during the session
- **Comprehensive Responses**: Handles 20+ different conversation topics
- **Emoji Support**: Engaging responses with emojis
- **Responsive Design**: Works on desktop and mobile devices
- **Easy to Extend**: Simple if-else structure for adding new responses

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository** (or download the files):
   ```bash
   git clone <your-repo-url>
   cd streamlit-chatbot
   ```

2. **Install required packages**:
   ```bash
   pip install streamlit
   ```

3. **Run the application**:
   ```bash
   streamlit run chatbot.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📁 Project Structure

```
streamlit-chatbot/
│
├── chatbot.py          # Main application file
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (optional)
```

## 🎯 How It Works

The chatbot uses a simple but effective if-else logic structure to process user input and generate appropriate responses:

```python
def get_bot_response(user_message):
    message = user_message.lower().strip()
    
    if "hello" in message or "hi" in message:
        return "Hello! Nice to meet you! 😊"
    elif "your name" in message:
        return "I'm ChatBot, your friendly AI assistant!"
    # ... more conditions
```

### Conversation Topics Handled:

- ✅ **Greetings**: Hello, hi, good morning, good night
- ✅ **Personal Information**: Name, age, hobbies, interests
- ✅ **Programming Topics**: Python, Streamlit, coding
- ✅ **Time & Date**: Current time and date queries
- ✅ **Emotions**: User feelings and mood
- ✅ **Entertainment**: Jokes and fun responses
- ✅ **Help & Guidance**: Bot capabilities and instructions
- ✅ **Farewells**: Various goodbye phrases
- ✅ **Fallback Responses**: Default answers for unrecognized input

## 💬 Example Conversations

```
You: Hello!
Bot: Hello! Nice to meet you! 😊

You: What's your name?
Bot: I'm ChatBot, your friendly AI assistant created with Streamlit! 🤖

You: Tell me a joke
Bot: Why don't robots ever panic? Because they have nerves of steel! 🤖😄

You: My name is Alice
Bot: Nice to meet you, Alice! 🎉 Thanks for introducing yourself!
```

## 🎨 Customization

### Adding New Responses

To add new conversation topics, simply extend the `get_bot_response()` function:

```python
elif "your new topic" in message:
    return "Your custom response here!"
```

### Styling

Modify the CSS in the `st.markdown()` section to change colors, fonts, and layout:

```python
st.markdown("""
<style>
    .user-message {
        background: your-custom-color;
    }
</style>
""", unsafe_allow_html=True)
```

### Random Responses

Add variety by using random responses:

```python
responses = [
    "Response option 1",
    "Response option 2",
    "Response option 3"
]
return random.choice(responses)
```

## 📚 Key Components

### Session State Management
```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

### Message Display
```python
for message in st.session_state.messages:
    # Display user and bot messages with styling
```

### Input Handling
```python
user_input = st.text_input("Type your message:")
if send_button and user_input:
    # Process and respond to user input
```

## 🛠️ Technical Details

- **Framework**: Streamlit
- **Language**: Python 3.7+
- **Styling**: Custom CSS with HTML markdown
- **State Management**: Streamlit session state
- **Response Logic**: If-else conditional statements
- **UI Components**: Text input, buttons, containers, sidebar

## 🔧 Configuration Options

### Optional: Create requirements.txt
```
streamlit>=1.0.0
```

### Environment Variables
No environment variables required for basic functionality.

## 📱 Usage Tips

1. **Try Different Phrases**: The bot recognizes many variations of common phrases
2. **Ask Questions**: Use question words like "what", "how", "when"
3. **Share Information**: Tell the bot your name or feelings
4. **Clear History**: Use the sidebar button to start fresh
5. **Case Insensitive**: Type in any case - the bot understands both

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Add your improvements to the if-else logic
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Contribution Ideas:
- Add more conversation topics
- Implement sentiment analysis
- Add user preferences storage
- Create themed chat modes
- Integrate with external APIs

## 🐛 Troubleshooting

### Common Issues:

**Problem**: Streamlit not found
```bash
# Solution: Install streamlit
pip install streamlit
```

**Problem**: Port already in use
```bash
# Solution: Use different port
streamlit run chatbot.py --server.port 8502
```

**Problem**: CSS not loading
```bash
# Solution: Check unsafe_allow_html=True is set
```

## 📈 Future Enhancements

- [ ] Add conversation memory across sessions
- [ ] Implement natural language processing
- [ ] Add voice input/output capabilities
- [ ] Create different personality modes
- [ ] Add multi-language support
- [ ] Integrate with databases for persistent storage
- [ ] Add user authentication
- [ ] Implement conversation analytics

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Created with ❤️ using Streamlit

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing framework
- Python community for excellent documentation
- Open source contributors for inspiration

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Look through existing issues in the repository
3. Create a new issue with detailed description
4. Join the Streamlit community forums

---

**Happy Chatting! 🤖💬**

*Built with Python and Streamlit - Simple, Effective, and Fun!*