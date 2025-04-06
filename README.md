# 🧠 VoiceFlow - Your Smart Voice Assistant 🤖

**VoiceFlow** is a personalized, voice-enabled chatbot assistant powered by [Google Gemini 2.0 Flash](https://ai.google.dev/), with a sleek [Streamlit](https://streamlit.io/) interface. It understands your voice, responds intelligently with spoken feedback, and remembers the context of your conversation during the session.

> 🎤 Ask questions with your voice, 💬 get helpful answers, and 👨‍💻 enjoy a customized assistant made for **Manjil Budhathoki**.

---

## ✨ Features

- 🎙️ **Voice Input**: Talk to your assistant using your microphone.
- 🧠 **Gemini LLM Integration**: Uses Gemini 2.0 Flash via Google’s Generative AI API.
- 🗣️ **Voice Output**: The assistant reads out its response using `pyttsx3`.
- 💬 **Typing Animation**: Assistant replies appear with smooth typing effects.
- 🧍 **Personalized Greeting**: Recognizes and greets **Manjil** on load.
- 📜 **Chat History**: Maintains session memory in a friendly chat layout.
- 🔐 **Environment-secured API key** using `.env`.

---

## 📷 Preview

Here's a quick look at the Manjil AI interface:

![Manjil AI Screenshot](screenshot.png)

---

## 🛠️ Tech Stack

| Tool/Library          | Purpose                       |
| --------------------- | ----------------------------- |
| `streamlit`           | Frontend UI                   |
| `streamlit_chat`      | Chat-style display            |
| `google-generativeai` | Gemini model API              |
| `SpeechRecognition`   | Voice input (speech-to-text)  |
| `pyttsx3`             | Voice output (text-to-speech) |
| `python-dotenv`       | Secure API key loading        |
| `pyaudio`             | Mic input support             |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/manjil-ai.git
cd VoiceFlow
```


### 2. Install required packages

```bash
pip install -r requirements.txt
```

> 🧪 If `pyaudio` gives issues:

- On Linux:

```bash
sudo apt install portaudio19-dev
```

- On Windows:

```bash
pip install pipwin
pipwin install pyaudio
```

### 3. Add your `.env` file

In the root directory, create a `.env` file with:

```
GEMINI_API_KEY=your_google_generative_ai_key_here
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## 🧠 Project Structure

```
VoiceFlow/
├── app.py                # Main Streamlit app
├── .env                  # Gemini API key (you add this)
├── requirements.txt      # Python dependencies
├── screenshot.png        # UI preview
└── README.md             # You're reading it!
```

---

## 🙋 FAQ

**Q: Can I use this assistant with my own Gemini API key?**  
A: Absolutely! Just add your key to the `.env` file.

**Q: Does it save chat history permanently?**  
Not yet — but that can be added with a logging system or database.

**Q: Can I change the assistant’s personality or behavior?**  
Yes! You can customize the system prompt in the code.

---

## 🙌 Credits

Made with ❤️ by [Manjil Budhathoki](https://github.com/yourusername)

Inspired by Gemini AI, Streamlit, and all things voice-enabled.

---

## 🛡 License

This project is licensed under the **MIT License** – feel free to use, remix, and share with credit.

---

## ⭐ Like This Project?

Consider giving it a ⭐ on GitHub or sharing it with friends who love AI, chatbots, or voice tech!

```

---

Let me know if you want:
- A version with badges (e.g., GitHub stars, Python version)
- Deployment instructions (like for Streamlit Cloud or Hugging Face Spaces)
- A `CONTRIBUTING.md` for open-source collab
```
