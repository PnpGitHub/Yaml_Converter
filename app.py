import streamlit as st
from fallback_converter import convert_with_basic_mapper

st.set_page_config(page_title="GitLab → GitHub YAML Converter (Offline)", layout="centered")
st.title("🔧 Offline GitLab CI → GitHub Actions YAML Converter")

gitlab_yaml = st.text_area("Paste your `.gitlab-ci.yml` below")

if st.button("Convert"):
    if not gitlab_yaml.strip():
        st.warning("Please paste a GitLab YAML first.")
    else:
        result = convert_with_basic_mapper(gitlab_yaml)
        st.code(result, language="yaml")
        st.download_button("Download GitHub YAML", result, file_name="github_actions.yml")
