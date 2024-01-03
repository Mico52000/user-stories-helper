import streamlit as st
from backend.core import run_llm
from streamlit_chat import message




st.header("User Stories Helper Bot")


# Define buttons
mixtral_button = st.button("mixtral")
gpt35_button = st.button("GPT 3.5 Turbo")
gpt4_button = st.button("GPT 4")




if 'selected_llm_option' not in st.session_state:
    st.session_state['selected_llm_option'] = None
if 'model_status_message' not in st.session_state:
    st.session_state['model_status_message'] = 'Choose your model'

if mixtral_button:
    st.session_state['model_status_message'] = 'you are now chatting with  mixtral'
    st.session_state['selected_llm_option'] = 1
elif gpt35_button:
    st.session_state['model_status_message'] = 'you are now chatting with gpt 3.5'
    st.session_state['selected_llm_option'] = 2
elif gpt4_button:
    st.session_state['model_status_message'] = 'you are now chatting with gpt 4'
    st.session_state['selected_llm_option'] = 3

st.text(st.session_state['model_status_message'])

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
            query=prompt,
            selected_llm_option= st.session_state['selected_llm_option']
        )



        formatted_response = (
            f'{generated_response["response"]} \n \n '
        )
        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["bot_response_history"].append(formatted_response)
        st.session_state["chat_history"].append((prompt, generated_response["response"]))
        st.session_state["prompt"] = ""

if st.session_state["bot_response_history"]:
    for i,(prompt, response) in enumerate(zip(
        st.session_state["user_prompt_history"],
        st.session_state["bot_response_history"],
    )):
        message(prompt, is_user=True, key=f"user_message_{i}")
        message(response, key=f"bot_message_{i}")
