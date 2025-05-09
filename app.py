import streamlit as st

# Page settings
st.set_page_config(page_title="VentPal – Mental Health Chatbot", page_icon="🧠")

# App title and intro
st.title("🧠 VentPal")
st.caption("Your confidential mental health companion.")

# Clear conversation button
if st.button("🗑️ Clear Conversation"):
    st.session_state.messages = []
    st.experimental_rerun()

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show welcome message if it's the first visit
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown("🌿 Hello. I'm **VentPal**, your mental health support chatbot.\n\nYou can talk to me about how you're feeling. This space is private and safe.")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box for user message
user_prompt = st.chat_input("How are you feeling today?")

# Process user message
if user_prompt:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Placeholder assistant response
    assistant_reply = "💬 I'm here for you. Would you like to talk more about that?"
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

# Footer
st.markdown("---")
st.markdown("📘 *This chatbot is for educational purposes only and is not a substitute for professional mental health support.*")
