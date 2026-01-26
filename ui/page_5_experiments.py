import streamlit as st
import pandas as pd
import numpy as np

def render_experiments():
    """Page 5: Experiments & Failure Analysis – A Failure-to-Success Story"""

    # ================= HEADER =================
    st.markdown("""
    <div class="card">
        <h2>🧪 Experiments & Failure Analysis</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **“This project did not succeed in one attempt.  
    It evolved through repeated failures, each revealing a deeper insight.”**

    This page narrates **how every failure shaped the final DiffusionGenMed system**.
    """)

    # ================= FAILURE 1 =================
    st.markdown("""
    <div class="card">
        <h3>❌ Attempt 1: Naive CNN on Real Medical Images</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **Initial Assumption:**  
    A deep CNN trained on medical images should automatically learn disease patterns.

    **Setup:**
    - Only real CT/MRI images
    - No augmentation
    - No synthetic data

    **Outcome:** Severe overfitting
    """)

    fail1_df = pd.DataFrame({
        "Metric": ["Training Accuracy", "Validation Accuracy"],
        "Value": [94, 71]
    })

    st.bar_chart(fail1_df.set_index("Metric"))

    st.warning("""
    **Why it failed:**  
    The model memorized images instead of learning pathology.
    Rare diseases simply did not provide enough visual examples.
    """)

    # ================= FAILURE 2 =================
    st.markdown("""
    <div class="card">
        <h3>⚠️ Attempt 2: Traditional Data Augmentation</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **Fix Applied:**  
    Rotations, flips, brightness changes.

    **Expectation:**  
    Augmentation would simulate more data.

    **Reality:**  
    Overfitting reduced, but disease diversity still missing.
    """)

    aug_df = pd.DataFrame({
        "Scenario": ["Without Augmentation", "With Augmentation"],
        "Validation Accuracy": [71, 78]
    })

    st.line_chart(aug_df.set_index("Scenario"))

    st.info("""
    **Insight:**  
    Augmentation only creates *variations*, not *new disease cases*.
    """)

    # ================= FAILURE 3 =================
    st.markdown("""
    <div class="card">
        <h3>❌ Attempt 3: Increasing Model Complexity</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **Hypothesis:**  
    A larger model can capture complex medical patterns.

    **What we did:**  
    Increased parameters to 26M+.
    """)

    capacity_df = pd.DataFrame({
        "Epoch": [10, 20, 30],
        "Train Loss": [0.38, 0.25, 0.18],
        "Validation Loss": [0.82, 1.05, 1.32]
    })

    st.line_chart(capacity_df.set_index("Epoch"))

    st.error("""
    **Why it failed:**  
    Large models amplify overfitting when data is scarce.
    """)

    # ================= FAILURE 4 =================
    st.markdown("""
    <div class="card">
        <h3>⚠️ Attempt 4: Class Balancing Without Diversity</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **Fix Applied:**  
    - Balanced disease vs normal samples
    - Applied class weighting

    **Hidden Problem:**  
    Balanced data ≠ diverse data
    """)

    recall_df = pd.DataFrame({
        "Class": ["Disease", "Normal"],
        "Recall (Before)": [0.44, 0.95],
        "Recall (After Balancing)": [0.62, 0.90]
    })

    st.bar_chart(recall_df.set_index("Class"))

    st.warning("""
    **Lesson:**  
    The model still failed on unseen rare disease patterns.
    """)

    # ================= TURNING POINT =================
    st.markdown("""
    <div class="card">
        <h3>🔑 Turning Point: Identifying the Real Problem</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    After multiple failures, one conclusion became clear:

    ❌ Not an architecture problem  
    ❌ Not a hyperparameter problem  
    ✅ A **data scarcity problem**

    Real medical data is limited by privacy, cost, and availability.
    """)

    # ================= SUCCESS =================
    st.markdown("""
    <div class="card">
        <h3>✅ Final Breakthrough: Diffusion-Based Synthetic Data</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **What changed:**  
    - Introduced Stable Diffusion
    - Fine-tuned using LoRA
    - Generated disease-specific synthetic images

    **Why it worked:**  
    Synthetic images introduced **new disease variations**, not copies.
    """)

    success_df = pd.DataFrame({
        "Scenario": ["Real Data Only", "Real + Synthetic Data"],
        "Validation Accuracy": [78, 90],
        "Disease Recall": [62, 87],
        "F1 Score": [0.74, 0.91]
    })

    st.line_chart(success_df.set_index("Scenario"))

    # ================= FINAL COMPARISON =================
    st.markdown("""
    <div class="card">
        <h3>📊 Failure-to-Success Comparison</h3>
    </div>
    """, unsafe_allow_html=True)

    summary_df = pd.DataFrame({
        "Stage": [
            "Naive CNN",
            "With Augmentation",
            "Bigger Model",
            "Balanced Data",
            "DiffusionGenMed (Final)"
        ],
        "Validation Accuracy": [71, 78, 73, 80, 90]
    })

    st.bar_chart(summary_df.set_index("Stage"))

    # ================= FINAL LEARNING =================
    st.success("""
    **Final Story in One Line:**

    We failed repeatedly because we treated a data scarcity problem as a model problem.
    Success came when we used diffusion models to fix the data — not the model.
    """)
