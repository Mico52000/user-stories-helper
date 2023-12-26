import streamlit as st
from backend.core import run_llm
from streamlit_chat import message




st.header("User Stories Helper Bot")

prompt = st.text_input("prompt", placeholder="What are we building today?")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []
if "bot_response_history" not in st.session_state:
    st.session_state["bot_response_history"] = []
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


if prompt:
    ## with notation allows for the spinner to dissapear after code inside is finished
    with st.spinner("Generating Response"):
        generated_response = run_llm(
            query=prompt, chat_history=st.session_state["chat_history"]
        )


        formatted_response = (
            f'{generated_response["response"]} \n \n '
        )
        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["bot_response_history"].append(formatted_response)
        st.session_state["chat_history"].append((prompt, generated_response["response"]))
        st.session_state["prompt"] = ""

if st.session_state["bot_response_history"]:
    for prompt, response in zip(
        st.session_state["user_prompt_history"],
        st.session_state["bot_response_history"],
    ):
        message(prompt, is_user=True)
        message(response)
