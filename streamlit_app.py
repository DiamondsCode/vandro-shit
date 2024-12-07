import streamlit as st

st.title("YouTube Statistics")

st.write("""
    write a description here or some shit
""")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to section:", ["Section 1", "Section 2", "Section 3", "Section 4"])

if page == "Section 1":
    st.image("https://picsum.photos/800/400", caption="describe the photo by text here", use_column_width=True)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.11111111111
    """)

elif page == "Section 2":
    st.image("https://picsum.photos/800/401", caption="describe the photo by text here", use_column_width=True)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.222222222222
    """)

elif page == "Section 3":
    st.image("https://picsum.photos/800/402", caption="describe the photo by text here", use_column_width=True)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.33333333333
    """)

elif page == "Section 4":
    st.image("https://picsum.photos/800/403", caption="describe the photo by text here", use_column_width=True)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.444444444444444
    """)
