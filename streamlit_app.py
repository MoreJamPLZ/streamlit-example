import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


# if st.button('Upload File'):
#     uploaded_file = st.file_uploader("Choose a file")
#     print(uploaded_file)
#     if uploaded_file is not None:
#         # print(uploaded_file)
#         st.write("You selected the file:", uploaded_file.name)

# # Once we have the dependencies, add a selector for the app mode on the sidebar.
# st.sidebar.title("What to do")
# app_mode = st.sidebar.selectbox("Choose the app mode",
#     ["Show instructions", "Upload file", "Show the source code"])
# if app_mode == "Show instructions":
#     st.sidebar.success('To continue select "Upload file".')
# elif app_mode == "Show the source code":
#     readme_text.empty()
#     st.code(get_file_content_as_string("streamlit_app.py"))
# elif app_mode == "Run the app":
#     readme_text.empty()
#     run_the_app()

# # This is the main app app itself, which appears when the user selects "Run the app".
# def run_the_app():
#     if 'clicked' not in st.session_state:
#         st.session_state.clicked = False
    
#     def set_clicked():
#         st.session_state.clicked = True
    
#     st.button('Upload File', on_click=set_clicked)
#     if st.session_state.clicked:
#         uploaded_file = st.file_uploader("Choose a file")
#         print(uploaded_file)
#         if uploaded_file is not None:
#             # print(uploaded_file)
#             st.write("You selected the file:", uploaded_file.name)


# Placeholder for readme_text
readme_text = st.empty()

# Once we have the dependencies, add a selector for the app mode on the sidebar.
st.sidebar.title("What to do")
app_mode = st.sidebar.selectbox("Choose the app mode",
    ["Show instructions", "Upload file", "Show the source code"])
if app_mode == "Show instructions":
    st.sidebar.success('To continue select "Upload file".')
# elif app_mode == "Show the source code":
#     readme_text.empty()
#     # st.code(get_file_content_as_string("streamlit_app.py"))
else app_mode == "Upload file":
    readme_text.empty()
    run_the_app()

# This is the main app itself, which appears when the user selects "Upload file".
def run_the_app():
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False
    
    def set_clicked():
        st.session_state.clicked = True
    
    st.button('Upload File', on_click=set_clicked)
    if st.session_state.clicked:
        uploaded_file = st.file_uploader("Choose a file")
        print(uploaded_file)
        if uploaded_file is not None:
            st.write("You selected the file:", uploaded_file.name)
