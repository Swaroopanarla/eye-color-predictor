import streamlit as st
import pandas as pd
from model import EyeModel

# Page settings
st.set_page_config(page_title="Eye Color Predictor", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
/* Background */
body {
    background: linear-gradient(135deg, #0f172a, #1e3c72);
}

/* Main container */
.main {
    background-color: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
}

/* Title */
.title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    color: #e2e8f0;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #cbd5f5;
    margin-bottom: 30px;
}

/* Card style (FIXED COLOR ✅) */
.card {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    color: white;
    padding: 15px;
    border-radius: 12px;
    margin: 10px 0;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}

/* Card title */
.card b {
    font-size: 18px;
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOAD DATA ----------
data = pd.read_csv("eye_dataset.csv")

# ---------- TITLE ----------
st.markdown('<div class="title">👁️ Eye Color Country Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Analyze global eye color distribution and predictions 🌍</div>', unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.header("🔍 Filters")

regions = ["All"] + list(data["region"].unique())
selected_region = st.sidebar.selectbox("Select Region", regions)

if selected_region == "All":
    filtered_data = data
else:
    filtered_data = data[data["region"] == selected_region]

# ---------- MAIN INPUT ----------
eye = st.selectbox("🎯 Select Eye Color", filtered_data['eye_color'].unique())

col1, col2 = st.columns(2)

# ---------- TABLE ----------
with col1:
    st.subheader("📊 Countries with this Eye Color")

    result = filtered_data[filtered_data['eye_color'] == eye]

    if not result.empty:
        st.dataframe(result, use_container_width=True)
    else:
        st.warning("No data found")

# ---------- METRICS ----------
with col2:
    st.subheader("📈 Insights")

    if not result.empty:
        avg_percentage = int(result["percentage"].mean())
        total_people = int(result["population_with_eye_color"].sum())

        st.metric("🌍 Avg Percentage", f"{avg_percentage}%")
        st.metric("👥 Total Population", f"{total_people:,}")

# ---------- PREDICTION ----------
st.subheader("🤖 Prediction")

if st.button("🔮 Predict Country"):
    model = EyeModel(data.copy())
    model.train()

    pred = model.predict(eye)

    st.success(f"🌍 Predicted Country: {pred}")

# ---------- SIMILAR COUNTRIES ----------
st.subheader("🔗 Similar Countries")

if not result.empty:
    for i, row in result.iterrows():
        st.markdown(f"""
        <div class="card">
        <b>{row['country']}</b><br><br>
        👁️ Eye Color: {row['eye_color']}<br>
        📊 {row['percentage']}% population<br>
        🌍 Similar: {row['resembles_countries']}
        </div>
        """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.caption("🚀 BTech Final Year Project | Eye Color Analysis System")