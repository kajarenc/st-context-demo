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


"----------------------------"

st.write("**Setting a new header or cookie should return an error**")
st.code(
    """
    st.context.headers["New-Header"] = "newheader"
    """
)
st.context.headers["New-Header"] = "newheader"
