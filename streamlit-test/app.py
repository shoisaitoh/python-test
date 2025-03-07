import streamlit as st

st.title("練習用アプリです")
st.caption("これはshoisaitohの練習用アプリです")

with st.form(key="profile_form"):
    # textbox
    name = st.text_input("お名前")
    address = st.text_input("ご住所")

    # button
    submit_btn = st.form_submit_button("送信")
    # cancel_btn = st.button("キャンセル")
    if submit_btn:
        st.text(f"ようこそ！{name}さん！")
