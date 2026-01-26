import streamlit as st

def render_overview():
    """Page 1: Project Overview - Problem Statement & Motivation"""
    
    st.markdown("""
    <div class="card">
    <h2>🎯 Problem Statement</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Medical professionals spend **hours analyzing medical images** to identify diseases. 
    Current diagnostic processes are:
    
    - ⏱️ **Time-consuming** - Manual review of hundreds of images
    - 👨‍⚕️ **Dependent on expertise** - Diagnosis quality varies by radiologist experience
    - 🌍 **Unevenly distributed** - Expert radiologists unavailable in many regions
    - 😓 **Prone to fatigue** - Long hours of concentration lead to errors
    """)
    
    st.markdown("""
    <div class="card">
    <h2>💡 Solution: AI-Based Medical Image Analysis</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    We built a **Convolutional Neural Network (CNN)** that:
    
    - ⚡ **Processes images instantly** - Diagnosis in milliseconds
    - 🎯 **Maintains consistency** - Same accuracy across all images
    - 🌐 **Scales globally** - Can be deployed anywhere
    - 📊 **Provides confidence scores** - Shows certainty of predictions
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
        <h3>❌ Manual Diagnosis</h3>
        <p><strong>Time:</strong> 15-30 min per case</p>
        <p><strong>Cost:</strong> High (expert required)</p>
        <p><strong>Availability:</strong> Limited</p>
        <p><strong>Consistency:</strong> Variable</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
        <h3>✅ AI-Based Diagnosis</h3>
        <p><strong>Time:</strong> < 1 second</p>
        <p><strong>Cost:</strong> One-time training</p>
        <p><strong>Availability:</strong> Always accessible</p>
        <p><strong>Consistency:</strong> 100% consistent</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
    <h2>🎓 Why This Project?</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Before building a model, we clearly defined the problem and objective.**
    
    This project demonstrates:
    
    1. **Problem Understanding** - Why AI is necessary
    2. **Data-Driven Approach** - Quality data leads to better models
    3. **Iterative Development** - Failures teach us how to improve
    4. **Complete ML Lifecycle** - Not just predictions, but the entire journey
    5. **Real-World Relevance** - Addressing actual healthcare challenges
    
    Each subsequent page explains one aspect of this journey.
    """)
    
    st.markdown("""
    <div class="card">
    <h2>🚀 The ML Lifecycle Journey</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ```
    Problem Definition
           ↓
    Data Collection & Preprocessing
           ↓
    Model Architecture Design
           ↓
    Model Training & Tuning
           ↓
    Experiments & Failure Analysis ⭐ (Most Important!)
           ↓
    Evaluation & Metrics
           ↓
    Live Prediction & Deployment
           ↓
    Future Improvements
    ```
    
    **Key Insight:** The intelligence of the system is built through every step above, 
    not just the final prediction stage.
    """)
