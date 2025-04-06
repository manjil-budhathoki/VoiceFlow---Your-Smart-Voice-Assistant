import streamlit as st
from streamlit_chat import message
import google.generativeai as genai
from dotenv import load_dotenv
import os
import speech_recognition as sr
import pyttsx3
import time

# -------------------- SETUP --------------------
# Load Gemini API key securely from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Initialize Gemini 2.0 model (flash version)
model = genai.GenerativeModel("gemini-2.0-flash")

# Page config
st.set_page_config(page_title="VoiceFlow - Your Smart Voice Assistant 🤖")
st.title("🧠 VoiceFlow Gemini Assistant")
st.caption("Crafted with ❤️ by Manjil himself.")

# -------------------- Initialize Chat Memory --------------------
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------- Greeting Section --------------------
if "greeted" not in st.session_state:
    st.success("👋 Hello Manjil! I’m your assistant. Ask me anything or tap the mic 🎤.")
    st.session_state.greeted = True

# -------------------- Voice Input Function --------------------
def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        st.info("🎙️ Listening... Speak now...")
        audio = recognizer.listen(source, timeout=5)
    try:
        text = recognizer.recognize_google(audio)
        st.success(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        st.warning("Couldn't understand your voice.")
    except sr.RequestError as e:
        st.error(f"Speech recognition failed: {e}")
    return None

# -------------------- Voice Output Function --------------------
def speak_reply(reply):
    engine = pyttsx3.init()
    engine.say(reply)
    engine.runAndWait()

# -------------------- Chat History Display --------------------
for msg in st.session_state.messages:
    message(msg["content"], is_user=(msg["role"] == "user"))

# -------------------- Voice Chat Input --------------------
if st.button("🎤 Speak Now"):
    spoken_text = recognize_speech_from_mic()
    if spoken_text:
        st.session_state.messages.append({"role": "user", "content": spoken_text})
        message(spoken_text, is_user=True)

        # Get LLM response
        response = st.session_state.chat.send_message(spoken_text)
        reply = response.text

        # Typing animation
        placeholder = st.empty()
        typed_text = ""
        for char in reply:
            typed_text += char
            placeholder.markdown(typed_text)
            time.sleep(0.01)
        placeholder.empty()

        # Save & display response
        st.session_state.messages.append({"role": "assistant", "content": reply})
        message(reply, is_user=False)

        # Speak the response
        speak_reply(reply)

# -------------------- Text Chat Input --------------------
text_input = st.chat_input("Type your message...")
if text_input:
    st.session_state.messages.append({"role": "user", "content": text_input})
    message(text_input, is_user=True)

    # Get LLM response
    response = st.session_state.chat.send_message(text_input)
    reply = response.text

    # Typing animation
    placeholder = st.empty()
    typed_text = ""
    for char in reply:
        typed_text += char
        placeholder.markdown(typed_text)
        time.sleep(0.01)
    placeholder.empty()

    # Save & display response
    st.session_state.messages.append({"role": "assistant", "content": reply})
    message(reply, is_user=False)

    # Speak the response
    speak_reply(reply)
