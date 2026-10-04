# 🤖 Rule-Based Chatbot

A simple and interactive **Rule-Based Chatbot** built with Python and Flask.  
The chatbot uses predefined rules and keyword matching to understand user messages and generate suitable responses.

live demo https://rule-based-chatbot-io83.onrender.com/

## 🚀 Features

- 💬 Interactive chatbot
- 🧠 Rule-based response system
- 🔍 Keyword-based message analysis
- 📊 Text statistics
- 🎨 Modern responsive web interface
- ⚡ Fast Flask backend
- 🌐 Ready for deployment on Render
- 📱 Responsive design for desktop and mobile

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **HTML5**
- **CSS3**
- **JavaScript**
- **Rule-Based NLP**

## 📂 Project Structure

```text
Rule-Based-Chatbot/
│
├── app.py
├── chatbot.py
├── rules.py
├── text_analyzer.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/abinayasai05-boop/Rule-Based-Chatbot.git
```

### 2. Open the project

```bash
cd Rule-Based-Chatbot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 💬 Example

### User

```text
Hello
```

### Chatbot

```text
Hello! 👋 How can I help you today?
```

Other example questions:

```text
What can you do?
Who are you?
How does this chatbot work?
Tell me about the project
Help
Thank you
Bye
```

## 🧠 How It Works

The chatbot follows a simple rule-based NLP pipeline:

```text
User Input
    ↓
Text Processing
    ↓
Keyword Matching
    ↓
Rule Detection
    ↓
Predefined Response
    ↓
Chatbot Output
```

Unlike generative AI chatbots, this project uses predefined rules and responses. This makes the system simple, predictable, and easy to understand.

## 📊 Text Analysis

The project can analyze user input and provide information such as:

- Word count
- Character count
- Sentence count
- Average word length
- Longest word
- Frequently used keywords

## 🌐 Deployment

This application can be deployed using platforms such as **Render**.

For Render, use:

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
gunicorn app:app
```

Make sure `gunicorn` is included in `requirements.txt`.

## 🔮 Future Enhancements

- 🎤 Speech input
- 🔊 Text-to-speech
- 😊 Sentiment analysis
- 🌍 Multilingual support
- 💾 Chat history
- 🤖 Advanced NLP
- 📈 Conversation analytics
- 🔐 User authentication

## 🎯 Project Objective

The main objective of this project is to demonstrate how a **rule-based Natural Language Processing system** can process user input, identify predefined patterns, and generate appropriate responses through a web-based chatbot.

## 👩‍💻 Author

**Abinaya Sai**

GitHub:  
https://github.com/abinayasai05-boop

## 📄 License

This project is created for educational and academic purposes.
