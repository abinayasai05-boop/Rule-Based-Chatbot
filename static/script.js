const input = document.getElementById("messageInput");
const chatArea = document.getElementById("chatArea");
const sendButton = document.getElementById("sendButton");


function handleKey(event) {

    if (event.key === "Enter" && !event.shiftKey) {

        event.preventDefault();

        sendMessage();
    }
}


function useSuggestion(text) {

    input.value = text;

    input.focus();

    sendMessage();
}


function addMessage(text, sender) {

    const message = document.createElement("div");

    message.className = `message ${sender}`;

    const content = document.createElement("div");

    content.className = "message-content";

    content.textContent = text;

    message.appendChild(content);

    chatArea.appendChild(message);

    chatArea.scrollTop = chatArea.scrollHeight;
}


function showAnalysis(data) {

    document.getElementById("words").textContent =
        data.words;

    document.getElementById("characters").textContent =
        data.characters;

    document.getElementById("sentences").textContent =
        data.sentences;

    document.getElementById("vowels").textContent =
        data.vowels;

    document.getElementById("consonants").textContent =
        data.consonants;

    document.getElementById("sentiment").textContent =
        data.sentiment;

    document.getElementById("intent").textContent =
        data.intent;

    document.getElementById("confidence").textContent =
        data.confidence + "%";

    document.getElementById("analysisStatus").textContent =
        "Analysis complete";

    const keywordContainer =
        document.getElementById("keywords");

    keywordContainer.innerHTML = "";

    if (data.keywords && data.keywords.length > 0) {

        data.keywords.forEach(keyword => {

            const span = document.createElement("span");

            span.className = "keyword";

            span.textContent = keyword;

            keywordContainer.appendChild(span);
        });

    } else {

        keywordContainer.innerHTML =
            '<span class="keyword-empty">None</span>';
    }
}


async function sendMessage() {

    const message = input.value.trim();

    if (!message) {
        return;
    }

    addMessage(message, "user");

    input.value = "";

    input.disabled = true;

    sendButton.disabled = true;


    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        if (!response.ok) {

            throw new Error("Server error");

        }


        const data = await response.json();


        addMessage(data.response, "bot");


        showAnalysis(data.analysis);


    } catch (error) {

        addMessage(
            "Sorry, I couldn't process your message. Please make sure the Flask server is running.",
            "bot"
        );

        console.error(error);

    } finally {

        input.disabled = false;

        sendButton.disabled = false;

        input.focus();
    }
}


function clearChat() {

    chatArea.innerHTML = `

        <div class="welcome">

            <div class="welcome-icon">
                🤖
            </div>

            <h2>Hello! I'm TSA Bot 👋</h2>

            <p>
                I'm a rule-based NLP chatbot. Ask me something,
                and I'll analyze your text and respond using
                predefined rules.
            </p>

            <div class="welcome-cards">

                <button onclick="useSuggestion('Hello')">
                    <span>👋</span>
                    <strong>Say Hello</strong>
                    <small>Test greeting rules</small>
                </button>

                <button onclick="useSuggestion('What is NLP?')">
                    <span>🧠</span>
                    <strong>Ask about NLP</strong>
                    <small>Test knowledge rules</small>
                </button>

                <button onclick="useSuggestion('I am very happy today')">
                    <span>😊</span>
                    <strong>Test Sentiment</strong>
                    <small>Analyze your emotion</small>
                </button>

            </div>

        </div>
    `;


    document.getElementById("words").textContent = "0";
    document.getElementById("characters").textContent = "0";
    document.getElementById("sentences").textContent = "0";
    document.getElementById("vowels").textContent = "0";
    document.getElementById("consonants").textContent = "0";
    document.getElementById("sentiment").textContent = "—";
    document.getElementById("intent").textContent = "—";
    document.getElementById("confidence").textContent = "—";

    document.getElementById("analysisStatus").textContent =
        "Waiting for input";

    document.getElementById("keywords").innerHTML =
        '<span class="keyword-empty">None</span>';
}