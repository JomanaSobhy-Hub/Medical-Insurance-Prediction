
import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MediSure AI | Insurance Predictor",
    page_icon="✚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return joblib.load("best_insurance_model.pkl")

model = load_model()

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #102A43;
    --navy-light: #173F5F;
    --teal: #12A89D;
    --teal-dark: #07877F;
    --bg: #F3F7FA;
    --muted: #6B7C8F;
    --border: #E2EAF0;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 5% 5%, rgba(18,168,157,.08), transparent 25%),
        var(--bg);
    color: var(--navy);
}

.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    display: none;
}

/* Header */
.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 0 24px;
}

.brand-icon {
    width: 46px;
    height: 46px;
    border-radius: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 26px;
    font-weight: 800;
    background: linear-gradient(135deg, #12A89D, #087E8B);
    box-shadow: 0 8px 22px rgba(18,168,157,.24);
}

.brand-name {
    font-size: 23px;
    font-weight: 800;
    color: #102A43;
    letter-spacing: -0.8px;
}

.brand-name span {
    color: #12A89D;
}

.brand-caption {
    font-size: 11px;
    color: #7B8B9A;
    letter-spacing: 1.6px;
    text-transform: uppercase;
}

/* Hero */
.hero {
    position: relative;
    overflow: hidden;
    padding: 42px 44px;
    border-radius: 28px;
    background: linear-gradient(120deg, #102A43 0%, #173F5F 66%, #087E8B 120%);
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 18px 45px rgba(16,42,67,.13);
}

.hero:after {
    content: "";
    position: absolute;
    width: 280px;
    height: 280px;
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 50%;
    right: -65px;
    top: -110px;
    box-shadow: 0 0 0 35px rgba(255,255,255,.025),
                0 0 0 70px rgba(255,255,255,.025);
}

.eyebrow {
    display: inline-block;
    background: rgba(18,168,157,.18);
    color: #8CF1E6;
    border: 1px solid rgba(140,241,230,.25);
    padding: 7px 13px;
    border-radius: 50px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.2px;
    margin-bottom: 18px;
}

.hero h1 {
    color: white;
    font-size: clamp(30px, 4vw, 46px);
    font-weight: 800;
    line-height: 1.18;
    letter-spacing: -1.5px;
    margin: 0 0 15px;
}

.hero h1 span {
    color: #6EE7D8;
}

.hero p {
    color: #D1E0EB;
    max-width: 650px;
    font-size: 15px;
    line-height: 1.9;
    margin-bottom: 22px;
}

.hero-note {
    color: #D8F8F4;
    font-size: 12px;
    font-weight: 600;
}

/* Section headings */
.section-kicker {
    color: #0B938B;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    margin-bottom: 7px;
}

.section-title {
    color: #102A43;
    font-size: 27px;
    font-weight: 800;
    letter-spacing: -.7px;
    margin-bottom: 7px;
}

.section-subtitle {
    color: #718096;
    font-size: 14px;
    line-height: 1.8;
    margin-bottom: 22px;
}

/* Form card */
[data-testid="stForm"] {
    background: white;
    border: 1px solid #E2EAF0;
    border-radius: 22px;
    padding: 26px 28px 22px;
    box-shadow: 0 10px 35px rgba(16,42,67,.045);
}

[data-testid="stWidgetLabel"] p {
    color: #29465E !important;
    font-weight: 600 !important;
    font-size: 13px !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    border-radius: 11px !important;
    border-color: #DCE6ED !important;
    background: #FBFDFE !important;
}

div[data-baseweb="input"] input {
    color: #102A43 !important;
}

div[data-baseweb="select"] * {
    color: #102A43;
}

div[data-baseweb="input"]:focus-within,
div[data-baseweb="select"]:focus-within {
    border-color: #12A89D !important;
    box-shadow: 0 0 0 2px rgba(18,168,157,.1);
}

/* Primary button */
.stButton > button,
[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(100deg, #12A89D, #07877F);
    color: white;
    border: none;
    border-radius: 12px;
    min-height: 49px;
    font-size: 14px;
    font-weight: 700;
    transition: all .2s ease;
    box-shadow: 0 7px 18px rgba(18,168,157,.18);
}

.stButton > button:hover,
[data-testid="stFormSubmitButton"] > button:hover {
    color: white;
    border: none;
    transform: translateY(-2px);
    box-shadow: 0 10px 22px rgba(18,168,157,.27);
}

/* Result */
.result-card {
    background: linear-gradient(145deg, #FFFFFF, #F1FBF9);
    border: 1px solid #CFECE7;
    border-radius: 23px;
    padding: 28px;
    box-shadow: 0 12px 35px rgba(16,42,67,.05);
    margin-top: 20px;
}

.result-label {
    color: #07877F;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.4px;
}

.result-price {
    color: #102A43;
    font-size: clamp(34px, 4vw, 48px);
    font-weight: 800;
    letter-spacing: -1.6px;
    margin: 13px 0 8px;
}

.result-caption {
    color: #6B7C8F;
    font-size: 13px;
    line-height: 1.8;
}

.result-badge {
    display: inline-block;
    background: #DDF7F0;
    color: #087E70;
    border-radius: 30px;
    padding: 7px 11px;
    font-size: 11px;
    font-weight: 700;
    margin-top: 12px;
}

.info-card {
    background: #102A43;
    color: white;
    border-radius: 20px;
    padding: 24px;
    margin-top: 20px;
}

.info-card h3 {
    color: white;
    font-size: 18px;
    margin: 0 0 10px;
}

.info-card p {
    color: #CBD8E3;
    font-size: 13px;
    line-height: 1.9;
}

.info-point {
    padding: 11px 0;
    border-bottom: 1px solid rgba(255,255,255,.12);
    color: #E4EEF5;
    font-size: 13px;
}

.info-point:last-child {
    border-bottom: none;
}

/* Footer */
.footer {
    text-align: center;
    color: #8293A4;
    font-size: 11px;
    padding-top: 35px;
    line-height: 2;
}

hr {
    border-color: #E2EAF0;
}

/* Responsive */
@media (max-width: 700px) {
    .hero {
        padding: 30px 24px;
        border-radius: 20px;
    }
    [data-testid="stForm"] {
        padding: 18px 15px;
    }
    .section-title {
        font-size: 23px;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="brand">
    <div class="brand-icon">✚</div>
    <div>
        <div class="brand-name">MediSure <span>AI</span></div>
        <div class="brand-caption">Intelligent Insurance Insights</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
hero_left, hero_right = st.columns([1.65, 1])

with hero_left:
    st.markdown("""
    <div class="hero">
        <div class="eyebrow">✦ &nbsp; SMARTER HEALTHCARE ESTIMATES</div>
        <h1>Clarity for your<br><span>healthcare costs.</span></h1>
        <p>
            Make more informed decisions with an intelligent estimate
            of medical insurance charges, powered by machine learning.
        </p>
        <div class="hero-note">
            ✓ &nbsp; Simple inputs &nbsp;&nbsp; ✓ &nbsp; Instant estimate
        </div>
    </div>
    """, unsafe_allow_html=True)

with hero_right:
    st.markdown("""
    <div style="
        height:100%;
        min-height:285px;
        margin-bottom:28px;
        padding:32px 27px;
        border-radius:28px;
        background:linear-gradient(145deg,#E3F7F4,#FFFFFF 75%);
        border:1px solid #D5ECE9;
        display:flex;
        flex-direction:column;
        justify-content:center;
        box-shadow:0 18px 45px rgba(16,42,67,.05);
    ">
        <div style="
            width:65px;height:65px;border-radius:21px;
            background:#D0F2EC;color:#087E8B;
            display:flex;align-items:center;justify-content:center;
            font-size:34px;margin-bottom:22px;
        ">♙</div>
        <div style="font-size:11px;font-weight:800;letter-spacing:1.5px;color:#07877F;">
            PERSONALIZED INSIGHTS
        </div>
        <div style="font-size:25px;line-height:1.3;font-weight:800;color:#102A43;margin-top:10px;">
            Your profile.<br>Your estimate.
        </div>
        <div style="font-size:13px;line-height:1.9;color:#6B7C8F;margin-top:12px;">
            Explore an estimate based on the information you provide.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- MAIN CONTENT ----------------
left, right = st.columns([1.5, 1], gap="large")

with left:
    st.markdown("""
    <div class="section-kicker">01 — YOUR PROFILE</div>
    <div class="section-title">Personalize your estimate</div>
    <div class="section-subtitle">
        Fill in the details below to calculate your estimated charges.
    </div>
    """, unsafe_allow_html=True)

    with st.form("insurance_form"):
        st.markdown("##### Personal details")

        c1, c2 = st.columns(2)

        with c1:
            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=30,
                help="Age in years"
            )
            sex = st.selectbox(
                "Sex",
                ["female", "male"],
                format_func=lambda x: x.capitalize()
            )
            bmi = st.number_input(
                "Body Mass Index (BMI)",
                min_value=10.0,
                max_value=70.0,
                value=25.0,
                step=0.1,
                help="Enter your BMI value"
            )

        with c2:
            children = st.number_input(
                "Number of Children",
                min_value=0,
                max_value=10,
                value=0
            )
            smoker = st.selectbox(
                "Smoking Status",
                ["no", "yes"],
                format_func=lambda x: "Non-smoker" if x == "no" else "Smoker"
            )
            region = st.selectbox(
                "Region",
                ["northeast", "northwest", "southeast", "southwest"],
                format_func=lambda x: x.replace("_", " ").title()
            )

        st.markdown("---")
        submitted = st.form_submit_button(
            "Calculate My Estimate  →",
            use_container_width=True
        )

with right:
    st.markdown("""
    <div class="section-kicker">02 — YOUR RESULTS</div>
    <div class="section-title">Estimate overview</div>
    <div class="section-subtitle">
        Your predicted annual insurance charges will appear here.
    </div>
    """, unsafe_allow_html=True)

    if submitted if "submitted" in locals() else False:
        pass

    # Result area is updated after form submission
    if "prediction" not in st.session_state:
        st.markdown("""
        <div class="result-card">
            <div class="result-label">ESTIMATED ANNUAL CHARGES</div>
            <div class="result-price">— — —</div>
            <div class="result-caption">
                Your estimate will appear here after you complete
                your profile and calculate.
            </div>
            <div class="result-badge">✦ &nbsp; Powered by Machine Learning</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <h3>✦ &nbsp; How it works</h3>
        <p>
            MediSure AI uses a trained machine learning model to
            estimate medical insurance charges from the profile details.
        </p>
        <div class="info-point">01 &nbsp; Enter your profile information</div>
        <div class="info-point">02 &nbsp; Run the prediction model</div>
        <div class="info-point">03 &nbsp; Review your estimated charges</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- HANDLE PREDICTION ----------------
if submitted:
    customer_data = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }])

    # Keep feature engineering consistent with training
    customer_data["age_bmi"] = (
        customer_data["age"] * customer_data["bmi"]
    )
    customer_data["smoker_num"] = (
        customer_data["smoker"].map({"yes": 1, "no": 0})
    )
    customer_data["age_smoker"] = (
        customer_data["age"] * customer_data["smoker_num"]
    )
    customer_data["bmi_smoker"] = (
        customer_data["bmi"] * customer_data["smoker_num"]
    )
    customer_data["bmi_category"] = pd.cut(
        customer_data["bmi"],
        bins=[0, 18.5, 25, 30, float("inf")],
        labels=["Underweight", "Normal", "Overweight", "Obese"],
        right=False
    )

    prediction = float(model.predict(customer_data)[0])
    st.session_state["prediction"] = prediction

    st.rerun()

# Show result after rerun
if "prediction" in st.session_state:
    with right:
        st.markdown(f"""
        <div class="result-card">
            <div class="result-label">ESTIMATED ANNUAL CHARGES</div>
            <div class="result-price">${st.session_state["prediction"]:,.2f}</div>
            <div class="result-caption">
                Estimated annual medical insurance charges based on your
                submitted profile.
            </div>
            <div class="result-badge">✓ &nbsp; Prediction completed</div>
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    <b style="color:#29465E;">MediSure AI</b> &nbsp; · &nbsp;
    Medical Insurance Cost Prediction<br>
    This estimate is for educational purposes only and is not an actual
    insurance quote or medical advice.
</div>
""", unsafe_allow_html=True)
