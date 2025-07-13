import re
import streamlit as st
from src.backend import add_github_project
import os

st.header("Add Github Project")


def is_valid_github_repo(url: str) -> bool:
    """
    Validates if the given URL is a valid GitHub repository URL.

    Examples of valid URLs:
    - https://github.com/user/repo
    - http://github.com/user/repo
    - https://www.github.com/user/repo
    - git@github.com:user/repo.git
    - https://github.com/user/repo.git
    """
    pattern = re.compile(
        r"^(?:https?://|git@)(?:www\.)?github\.com[/:]([\w.-]+)/([\w.-]+)(?:\.git)?/?$"
    )
    return bool(pattern.match(url))


if "projects" not in st.session_state:
    st.session_state.projects = {}
    dirs = os.listdir("data")
    for item in dirs:
        with open(f"data/{item}/name.txt", "r") as f:
            full_repo_name = f.read().strip()
            repo_url = f"https://github.com/{full_repo_name}"
            st.session_state.projects[repo_url] = full_repo_name


st.subheader("Enter your Github Project URL")
title = st.text_input("Repo URL")

if title:
    if is_valid_github_repo(title):
        st.session_state.projects[title] = title
        add_github_project(title)
        st.success("Project added!")
    else:
        st.error("Invalid GitHub repository URL. Please enter a valid URL.")

st.markdown("""
### Added Projects
""")
for idx, item in enumerate(st.session_state.projects, start=1):
    st.write(f"{idx}. {item}")
