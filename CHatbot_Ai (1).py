import streamlit as st
from openai import OpenAI

st.title("Week 3 – Simple Chatbot 💬")
st.write("This is a minimal chatbot using the OpenAI API and Streamlit.")

# ENTER API KEY MANUALLY

api_key = st.text_input(
    "Enter your OpenAI API Key:",
    type="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",
    help="Your key will not be stored. Used only for this session."
)

if not api_key:
    st.warning("Please enter your API key to continue.")
    st.stop()

client = OpenAI(api_key=api_key)


# CHAT HISTORY INIT
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a friendly TA for Embedded AI & Robotics students."}
    ]


#SHOW CHAT HISTORY
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


#  USER INPUT

user_input = st.chat_input("Ask something about Arduino, sensors, or AI:")

if user_input:
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    #  OPENAI API CALL (FIXED)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=st.session_state["messages"]
            )

            reply = response.choices[0].message.content
            st.markdown(reply)

    # Add assistant reply to history
    st.session_state["messages"].append({"role": "assistant", "content": reply})
