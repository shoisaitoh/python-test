import streamlit as st

st.title("練習用アプリです")
st.caption("これはshoisaitohの練習用アプリです")

with st.form(key="profile_form"):
    # textbox
    name = st.text_input("お名前")
    address = st.text_input("ご住所")

    age_category = st.radio("年齢層", ("子ども（18歳未満）", "大人（18歳以上）"))
    # 複数選択
    hobby = st.multiselect(
        "趣味", ("スポーツ", "読書", "料理", "プログラミング", "釣り", "映画")
    )

    # button
    submit_btn = st.form_submit_button("送信")
    # cancel_btn = st.button("キャンセル")
    if submit_btn:
        st.text(f"ようこそ！{name}さん！")
