import streamlit as st
from dotenv import load_dotenv

load_dotenv()
st.title("Ragify Github Discussions")

# st.markdown("""
# ### Welcome to the Github Discussions Ragify App!
# This is the home page :)
# ### Features
# - Add Github Project
# - Do Q&A
# """)

pg = st.navigation(["welcome.py", "add_project.py", "q_and_a.py"])
pg.run()
