import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
# num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
# num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

# indices = np.linspace(0, 1, num_points)
# theta = 2 * np.pi * num_turns * indices
# radius = indices

# x = radius * np.cos(theta)
# y = radius * np.sin(theta)

# df = pd.DataFrame({
#     "x": x,
#     "y": y,
#     "idx": indices,
#     "rand": np.random.randn(num_points),
# })

# st.altair_chart(alt.Chart(df, height=700, width=700)
#     .mark_point(filled=True)
#     .encode(
#         x=alt.X("x", axis=None),
#         y=alt.Y("y", axis=None),
#         color=alt.Color("idx", legend=None, scale=alt.Scale()),
#         size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#     ))

# st.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

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


st.sidebar.title("What to do")
app_mode = st.sidebar.selectbox("Choose the app mode",
    ["Show instructions", "Upload file", "Show the source code"])
if app_mode == "Show instructions":
    st.sidebar.success('To continue select "Upload file".')
elif app_mode == "Show the source code":
    readme_text.empty()
    st.code(get_file_content_as_string("streamlit_app.py"))
elif app_mode == "Upload file":  # Changed this line
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
            # print(uploaded_file)
            st.write("You selected the file:", uploaded_file.name)
