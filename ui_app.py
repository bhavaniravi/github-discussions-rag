import streamlit as st

# Title
st.title("Github Discussions Ragify")

# st.markdown("""
# ### Welcome to the Github Discussions Ragify App!
# This is the home page :)
# ### Features
# - Add Github Project
# - Do Q&A
# """)

pg = st.navigation(["st_pages/welcome.py", "st_pages/add_project.py", "st_pages/q_and_a.py"])
pg.run()
