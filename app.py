import streamlit as st
from roadmap_generator import generate_roadmap
from quiz_generator import generate_quiz
from mentor_chat import ask_mentor
from youtube_search import get_videos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from database import save_progress, get_progress
from recommender import recommend_topics


st.set_page_config(
    page_title="AI Learning Copilot",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
}
h1, h2, h3 {
    color: #1f77b4;
}
.main {
    padding: 2rem;
}
.big-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='big-title'>🚀 AI Learning Copilot</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Personalized AI Learning Roadmaps</div>",
    unsafe_allow_html=True
)

st.divider()

with st.sidebar:
    st.header("⚙️ Settings")

    page = st.radio(
        "Navigation",
        [
            "Roadmap",
            "Mentor",
            "Quiz",
            "Resources",
            "Dashboard",
            "Recommendations"
        ]
    )

    level = st.selectbox(
        "Skill Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    duration = st.selectbox(
        "Learning Duration",
        [
            "1 Week",
            "1 Month",
            "3 Months",
            "6 Months"
        ]
    )

# ─── Roadmap Page ───────────────────────────────────────────────────────────
if page == "Roadmap":
    col1, col2 = st.columns(2)

    with col1:
        topic = st.text_input(
            "🎯 What do you want to learn?"
        )

    with col2:
        goal = st.text_input(
            "🏆 Career Goal (Optional)"
        )

    if st.button("Generate Roadmap", use_container_width=True):
        with st.spinner("Generating AI Roadmap..."):
            prompt = f"""
            Topic: {topic}

            Skill Level: {level}

            Duration: {duration}

            Career Goal: {goal}

            Generate:

            1. Learning Roadmap
            2. Weekly Plan
            3. Important Topics
            4. Projects To Build
            5. Interview Preparation Topics

            Format properly.
            """

            roadmap = generate_roadmap(prompt)

            st.success("Roadmap Generated Successfully!")
            st.markdown(roadmap)

# ─── Mentor Page ─────────────────────────────────────────────────────────────
if page == "Mentor":
    st.subheader("🤖 AI Mentor")

    question = st.text_area(
        "Ask any question"
    )

    if st.button("Ask Mentor"):
        with st.spinner("Thinking..."):
            answer = ask_mentor(question)
            st.markdown(answer)

# ─── Quiz Page ───────────────────────────────────────────────────────────────
if page == "Quiz":
    st.subheader("📝 AI Quiz Generator")

    quiz_topic = st.text_input(
        "Enter topic for quiz"
    )

    if st.button("Generate Quiz"):
        quiz = generate_quiz(quiz_topic)
        st.markdown(quiz)

# ─── Resources Page ──────────────────────────────────────────────────────────
if page == "Resources":
    st.subheader("📚 Recommended Websites")

    st.markdown("- LearnCpp")
    st.markdown("- GeeksforGeeks")
    st.markdown("- W3Schools")
    st.markdown("- FreeCodeCamp")

    st.divider()

    st.subheader("🎥 Recommended Videos")

    video_topic = st.text_input(
        "Topic for Videos"
    )

    if st.button("Get Videos"):
        videos = get_videos(video_topic)

        for video in videos:
            title = video["snippet"]["title"]
            thumbnail = video["snippet"]["thumbnails"]["high"]["url"]
            video_id = video["id"]["videoId"]
            url = f"https://www.youtube.com/watch?v={video_id}"

            st.image(thumbnail)
            st.markdown(f"### {title}")
            st.markdown(url)
            st.divider()

# ─── Dashboard Page ──────────────────────────────────────────────────────────
if page == "Dashboard":
    st.subheader("📊 Learning Dashboard")

    data = get_progress()

    total_topics = len(data)

    if total_topics > 0:
        scores = [row[2] for row in data]
        avg_score = sum(scores) / len(scores)
    else:
        avg_score = 0

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Topics Learned",
            total_topics
        )

    with col2:
        st.metric(
            "Average Score",
            f"{avg_score:.1f}%"
        )

    with col3:
        st.metric(
            "Records Saved",
            len(data)
        )

    st.subheader("📋 Progress History")
    st.dataframe(data)

    if len(data) > 0:
        df = pd.DataFrame(
            data,
            columns=[
                "ID",
                "Topic",
                "Score",
                "Date"
            ]
        )

        st.subheader("📈 Learning Progress")
        st.line_chart(df["Score"])

    st.divider()

    if st.button("Save Test Progress"):
        save_progress("Python", 85)
        st.success("Progress Saved!")

# ─── Recommendations Page ────────────────────────────────────────────────────
if page == "Recommendations":
    st.subheader("🧠 AI Recommendations")

    rec_topic = st.text_input(
        "Enter completed topic"
    )

    if st.button("Get Recommendations"):
        recs = recommend_topics(rec_topic)

        for item in recs:
            st.success(item)