import streamlit as st

st.header("st.context demo app", divider="rainbow")

with st.echo():
    st.write(st.context)
    "----------------------------"
    st.write(st.context.cookies)
    "----------------------------"
    st.write(st.context.headers)
    "----------------------------"
    st.write(st.context.headers["User-Agent"])
    "----------"
    st.write(st.context.headers.get("User-Agent"))
    "----------"
    st.write(st.context.headers.get_all("User-Agent"))

# st.context.headers["User-Agent"] = "blablbalbla"
