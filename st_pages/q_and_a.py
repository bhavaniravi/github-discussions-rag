import streamlit as st
from backend import get_answer

st.title("Do RAG based Q&A")

def response_generator(prompt):
    return get_answer(st.session_state.selected_project.split('/')[-1], prompt)

if "projects" not in st.session_state:
    st.session_state.projects = {}
    st.session_state.selected_project = ""

selected_project = st.selectbox(
    "Which Github project do you wanna query on?",
    st.session_state.projects.keys(),
)
st.session_state.selected_project = selected_project



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type in your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # response = st.write_stream(response_generator())
        response = st.write(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
