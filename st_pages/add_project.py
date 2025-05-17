import re
import streamlit as st

st.title("Add Github Project")

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

st.subheader("Enter your Github Project URL")
title = st.text_input("Repo URL")

if title:
    if is_valid_github_repo(title):
        st.session_state.projects[title] = title
        st.success(f"Project added!")
    else:
        st.error("Invalid GitHub repository URL. Please enter a valid URL.")

st.markdown("""
### Added Projects

"""
)
for idx, item in enumerate(st.session_state.projects, start=1):
    st.write(f"{idx}. {item}")
