import streamlit as st
from utils.utils import set_background
set_background("demo/asset/background_picture.png")

st.title("🎮 Twitch Content Recommendation System")

st.markdown("""
    ## About the Project
    This recommendation system helps users discover Twitch content based on their preferences.
    The system analyzes user behavior and provides personalized recommendations for games, streams, and videos.""")
    
st.markdown("""
    ## Key Features
    - Personalized game recommendations
    - User preference tracking
    - Real-time Twitch data integration
    """)

st.markdown("## System Architecture")
st.image("demo/asset/System_Architecture.png", caption="System Architecture Diagram")

st.markdown("## Technology Stack")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Frontend**\n- React")

with col2:
    st.markdown("**Backend**\n- Java\n- Spring Boot\n- MySQL\n- Twitch API")

with col3:
    st.markdown("**Deployment**\n - AWS EC2\n- Docker\n - AppRunner" )