import streamlit as st

# Set the title of the Streamlit app
st.title("YouTube Statistics")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to section:", ["Section 1", "Section 2", "Section 3", "Section 4"])

# Section 1
if page == "Section 1":
    st.image("biden-medium.png", caption="describe the photo by text here", use_column_width=True, height=450)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.
    """)

# Section 2
elif page == "Section 2":
    st.image("biden-medium.png", caption="describe the photo by text here", use_column_width=True, height=450)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.
    """)

# Section 3
elif page == "Section 3":
    st.image("biden-medium.png", caption="describe the photo by text here", use_column_width=True, height=450)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.
    """)

# Section 4
elif page == "Section 4":
    st.image("biden-medium.png", caption="describe the photo by text here", use_column_width=True, height=450)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.
    """)
