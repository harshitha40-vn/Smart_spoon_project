
# import streamlit as st
# from food_recognition.model import predict_food
# from market_analysis.analysis import load_data, plot_preferences, sodium_impact,analyze_awareness_interest,summarize_salt_opinion
# from sentiment_analysis.sentiment import load_feedback, analyze_sentiment

# st.title("Smart Spoon Software Simulation")

# # --- Food Recognition ---
# st.header("🍽️ Food Recognition")
# img = st.file_uploader("Upload food image")
# if img:
#     with open("temp.jpg", "wb") as f: f.write(img.read())
#     result = predict_food("temp.jpg")
#     st.success(f"Predicted Food: {result}")

# # --- Market Analysis ---
# st.header("📊 Market Analysis")
# df = load_data()
# plot_preferences(df)
# st.image("market_analysis/pref_chart.png")

# st.subheader("Awareness & Interest in Smart Spoon")
# aware, interest = analyze_awareness_interest(df)
# st.write("**Awareness of tech:**")
# st.bar_chart(aware)
# st.write("**Interest in device:**")
# st.bar_chart(interest)

# st.subheader("Taste Satisfaction (Low Sodium Diet)")
# st.write(sodium_impact(df))

# st.subheader("General Salt Usage Perception")
# st.write(summarize_salt_opinion(df))


# # --- Sentiment ---
# st.header("💬 Sentiment Analysis")
# feedback = load_feedback()
# results = analyze_sentiment(feedback)
# st.dataframe(results)
# st.bar_chart(results['sentiment'])
import streamlit as st
from food_recognition.model import predict_food
from market_analysis.analysis import (
    load_data,
    plot_preferences,
    sodium_impact,
    analyze_awareness_interest,
    summarize_salt_opinion
)
from sentiment_analysis.sentiment import load_feedback, analyze_sentiment

# Set page config
st.set_page_config(page_title="Smart Spoon AI Dashboard", layout="centered")
st.markdown("""
    <style>
    
        
        .stButton>button {
            color: white;
            background-color: #003366;
            border-radius: 5px;
            padding: 0.5em 1em;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #005599;
            transition: 0.3s;
        }
    </style>
""", unsafe_allow_html=True)
import base64

def set_background_with_overlay(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()

    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), 
                        url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)

set_background_with_overlay("background.jpeg")


# Header
st.markdown("<h1 style='text-align: center; color: #003366;'>Smart Spoon - AI Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Button Navigation ---
col1, col2, col3 = st.columns(3)
page = None
with col1:
    if st.button("Food Recognition"):
        page = "food"
with col2:
    if st.button("Market Research"):
        page = "market"
with col3:
    if st.button("Sentiment Analysis"):
        page = "sentiment"

st.markdown("<hr>", unsafe_allow_html=True)

# ===============================
# 🍽️ Food Recognition
# ===============================
if page == "food":
    st.subheader("Food Recognition")
    st.write("Upload an image of food. The AI model will try to identify the dish.")

    img = st.file_uploader("Upload Food Image", type=["jpg", "jpeg", "png"])
    
    if img:
        with open("temp.jpg", "wb") as f:
            f.write(img.read())
        result = predict_food("temp.jpg")
        st.image("temp.jpg", caption="Uploaded Image", use_column_width=True)
        st.success(f"Predicted Food: {result}")

        corrected = st.selectbox("Optional: Correct the prediction", [result, "Dosa", "Idli", "Sambar", "Rasam", "Other"])
        st.write(f"Final Label: {corrected}")

# ===============================
# 📊 Market Research
# ===============================
elif page == "market":
    st.subheader("Market Research Analysis")
    st.write("Insights based on responses from participants on taste preferences and Smart Spoon concept.")

    df = load_data()
    plot_preferences(df)
    st.image("market_analysis/pref_chart.png", caption="Dining Frequency")

    st.write("### Awareness & Interest")
    aware, interest = analyze_awareness_interest(df)
    st.write("Tech Awareness:")
    st.bar_chart(aware)
    st.write("Interest in Device:")
    st.bar_chart(interest)

    st.write("### Satisfaction with Low Sodium Options")
    st.write(sodium_impact(df))

    st.write("### Salt Preference Opinion")
    st.write(summarize_salt_opinion(df))

# ===============================
# 💬 Sentiment Analysis
# ===============================
elif page == "sentiment":
    st.subheader("Sentiment Analysis")
    st.write("Analyzing user feedback using NLP to understand satisfaction and areas of improvement.")

    feedback = load_feedback()
    results = analyze_sentiment(feedback)

    st.dataframe(results)

    st.write("Sentiment Scores")
    st.bar_chart(results.set_index('user'))
