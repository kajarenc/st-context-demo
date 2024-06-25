import streamlit as st

st.header("Headers")

headers = st.context.headers
cookies = st.context.cookies

for key, value in headers.items():
    st.write(key)
    st.code(value)

st.write("-------")
st.header("Cookies")

for cookie_key, cookie_value in cookies.items():
    st.write(cookie_key)
    st.code(cookie_value)

st.write("------")

st.write(st.context.headers["User-Agent"])
st.write(st.context.headers.get("user-agent"))
st.write(st.context.headers.get_all("USER-AGENT"))

st.write(st.context.headers.get_all("MISSING-HEADER"))
