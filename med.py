import streamlit as st
import ollama
import google.generativeai as genai
import datetime

# Configure API Key for Google Gemini
GEMINI_API_KEY = "AIzaSyB_KI4oSauqEPcuacCM97U_kNdtqelOckk"
genai.configure(api_key=GEMINI_API_KEY)

# Initialize Ollama client (assuming it's running locally)
client = ollama.Client(host='http://localhost:11434')

# Configure Streamlit App
st.set_page_config(page_title="Health Guardian: AI Wellness Assistant", page_icon="🩺")

# System Prompt for Health Assistant
HEALTH_ASSISTANT_PROMPT = """
You are Health Guardian, an AI assistant focused on user well-being. 
- Provide **mental health tips** and **reminders** to drink water and eat on time.
- Respond only to health-related queries. If a user asks an irrelevant question, politely decline to answer.
- Be concise, friendly, and supportive.
"""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm Health Guardian, your AI wellness assistant. How can I support your well-being today?"}
    ]

# Chat Interface
st.title("Health Guardian: AI Wellness Assistant 🩺")
st.caption("Caring for Your Health, One Reminder at a Time")

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input for health-related queries
if prompt := st.chat_input("Ask me about mental health, wellness tips, or reminders..."):

    # Define allowed topics
    allowed_keywords = ["mental health", "stress", "anxiety", "sleep", "water", "food", "exercise", "reminder"]

    if any(keyword in prompt.lower() for keyword in allowed_keywords):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            response = client.chat(
                model='meditron:latest',
                messages=[{"role": "system", "content": HEALTH_ASSISTANT_PROMPT}] + st.session_state.messages,
                stream=True
            )

            for chunk in response:
                if chunk['message']['content']:
                    full_response += chunk['message']['content']
                    message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})
    else:
        st.warning("I can only assist with health and wellness topics.")

# Reminder System
st.sidebar.header("Reminders")
reminder_type = st.sidebar.selectbox("Choose a reminder:", ["Drink Water", "Eat Food", "Take a Break"])
reminder_time = st.sidebar.time_input("Set Reminder Time:")

if "reminders" not in st.session_state:
    st.session_state.reminders = []

if st.sidebar.button("Set Reminder"):
    st.session_state.reminders.append((reminder_type, reminder_time))
    st.sidebar.success(f"Reminder set for {reminder_type} at {reminder_time.strftime('%I:%M %p')}")

# Display upcoming reminders
if st.session_state.reminders:
    st.sidebar.subheader("Upcoming Reminders")
    for r_type, r_time in st.session_state.reminders:
        st.sidebar.write(f"⏰ {r_type} at {r_time.strftime('%I:%M %p')}")

# Footer Disclaimer
st.markdown(
    "<div style='text-align: center; font-size: 12px; color: gray;'>⚠️ Disclaimer: This AI provides general health tips and reminders but does not replace professional medical advice.</div>",
    unsafe_allow_html=True
)
