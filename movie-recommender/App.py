import streamlit as st
from data_processor import NetflixRecommender

def add_netflix_logo():
    st.markdown("""
        <style>
        .netflix-logo {
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        </style>
        <div style="text-align: center;">
            <h1 style="color: #E50914; font-size: 48px; font-weight: bold; margin-bottom: 20px;" class="netflix-logo">
                NETFLIX
            </h1>
        </div>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Netflix Recommender", page_icon="🎬", layout="wide")
    recommender = NetflixRecommender()
    all_shows = recommender.get_all_shows()
    add_netflix_logo()
    st.write("""
        <div style="text-align: center; color: #808080; margin-bottom: 30px;">
            <h2>Find your next favorite show!</h2>
            <p>Select a show you like, and we'll recommend similar ones.</p>
        </div>
    """, unsafe_allow_html=True)
    selected_show = st.selectbox(
        "Select a show you like",
        ["Choose a show..."] + all_shows
    )
    if selected_show != "Choose a show...":
        show_info = recommender.get_show_info(selected_show)
        st.subheader(f"🎬 {show_info['title']}")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"**Type:** {show_info['type']}")
        with col2:
            st.write(f"**Year:** {show_info['year']}")
        with col3:
            st.write(f"**Rating:** {show_info['rating']}")
        st.write(f"**Genres:** {show_info['genres']}")
        st.write(f"**Description:** {show_info['description']}")
        if st.button("Get Similar Shows", type="primary"):
            with st.spinner("Finding similar shows..."):
                recommendations = recommender.get_similar_shows(selected_show)
                st.subheader("🎯 Similar Shows")
                for _, show in recommendations.iterrows():
                    with st.expander(f"🎬 {show['title']} ({show['type']})"):
                        st.write(f"**Genres:** {show['listed_in']}")
                        st.write(f"**Description:** {show['description']}")

if __name__ == "__main__":
    main() 