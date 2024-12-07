import streamlit as st

# Set the title of the Streamlit app
st.title("YouTube Statistics")

# Add a description
st.write("""
    Welcome to the YouTube Statistics page! Here, you will find optimal statistics and tips to help you maximize 
    the performance of your YouTube content. We'll provide insights into the best practices for video optimization, 
    audience engagement, and much more.
""")

# First image and description
st.image("https://picsum.photos/800/400", caption="Optimal Video Quality", use_column_width=True)
st.write("""
    **Optimal Video Quality:** High-resolution videos attract more views and engagement. Aim for at least 1080p 
    resolution to ensure the best quality for your audience.
""")

# Second image and description
st.image("https://picsum.photos/800/401", caption="Audience Engagement", use_column_width=True)
st.write("""
    **Audience Engagement:** Engaging with your audience through comments, polls, and calls to action in videos 
    increases your video's visibility and viewer retention.
""")

# Third image and description
st.image("https://picsum.photos/800/402", caption="Video Thumbnails", use_column_width=True)
st.write("""
    **Video Thumbnails:** Custom thumbnails with clear and enticing visuals can significantly improve your click-through rate.
    Always use high-quality and relevant thumbnails to attract more viewers.
""")

# Fourth image and description
st.image("https://picsum.photos/800/403", caption="Consistency is Key", use_column_width=True)
st.write("""
    **Consistency is Key:** Uploading regularly helps build an audience and improves your chances of being recommended
    by YouTube's algorithm. Stick to a consistent schedule for maximum impact.
""")
