import streamlit as st
import pandas as pd

def render_dataset():
    """Page 2: Dataset Insights – Real + Synthetic Medical Dataset Analysis"""

    # ================= HEADER =================
    st.markdown("""
    <div class="card">
        <h2>📊 Dataset Insights & Analysis</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **“In medical deep learning, the dataset defines the ceiling of model performance.”**

    This project uses a **hybrid dataset strategy**, combining:
    - **Limited real medical images**, and
    - **High-quality synthetic images generated using Diffusion + LoRA**

    This combination directly addresses **rare disease data scarcity**
    while maintaining **clinical realism and class balance**.
    """)

    # ================= DATASET ORIGIN =================
    st.markdown("""
    <div class="card">
        <h3>📁 Dataset Origin & Motivation</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    - Real medical images collected from **public, research-grade datasets**
    - Focused on **rare neurological disorders**
    - Includes both **Disease** and **Normal** brain scans
    - Real datasets alone were **insufficient for reliable model training**

    🔑 **Key Decision:**  
    Synthetic images were introduced **only to augment training data**,
    not to replace real clinical data.
    """)

    # ================= DISEASE COVERAGE =================
    st.markdown("""
    <div class="card">
        <h3>🧠 Diseases Included in the Study</h3>
    </div>
    """, unsafe_allow_html=True)

    disease_info = {
        "Disease Name": [
            "Moyamoya Disease with Intraventricular Hemorrhage (IVH)",
            "Neurofibromatosis Type 1 (NF1)",
            "Optic Glioma",
            "Tuberous Sclerosis"
        ],
        "Disease Category": [
            "Cerebrovascular Disorder",
            "Genetic Neurological Disorder",
            "Brain Tumor",
            "Genetic Neurocutaneous Syndrome"
        ],
        "Rarity Level": [
            "Very Rare",
            "Rare",
            "Rare",
            "Rare"
        ]
    }

    st.dataframe(pd.DataFrame(disease_info), width="stretch")

    # ================= DATASET SIZE (REAL + SYNTHETIC) =================
    st.markdown("""
    <div class="card">
        <h3>📦 Dataset Size (Real + Synthetic Combination)</h3>
    </div>
    """, unsafe_allow_html=True)

    size_data = {
        "Disease": [
            "Moyamoya + IVH",
            "Neurofibromatosis Type 1",
            "Optic Glioma",
            "Tuberous Sclerosis"
        ],
        "Real Images": [ 480, 432, 332, 248],
        "Synthetic Images": [ 480, 432, 332, 248],
        "Total": [960, 864, 664, 496]

    }

    df_size = pd.DataFrame(size_data)
    st.dataframe(df_size, width="stretch")

    st.markdown("""
    ✔ Synthetic images were generated **only for training and validation**  
    ✔ Test sets primarily contain **real medical images**  
    ✔ Prevents data leakage and inflated performance metrics
    """)

    # ================= WHY SYNTHETIC IMAGES =================
    st.markdown("""
    <div class="card">
        <h3>🧪 Why Synthetic Images Were Required</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **Challenges with real data alone:**
    - Extremely limited rare disease samples
    - Severe overfitting during early experiments
    - Poor generalization on unseen images

    **Role of synthetic images:**
    - Increase dataset diversity
    - Improve representation of rare disease patterns
    - Stabilize model training
    - Reduce variance and overfitting
    """)

    # ================= CLASS BALANCE =================
    st.markdown("""
    <div class="card">
        <h3>⚖️ Class Balance Strategy</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **Balancing principles followed:**
    - Equal number of Disease and Normal samples
    - Synthetic images added **only to minority classes**
    - Stratified splitting across train / validation / test

    ⚠️ Synthetic images were **never blindly oversampled**
    to avoid bias toward generated patterns.
    """)

    # ================= IMAGE CHARACTERISTICS =================
    st.markdown("""
    <div class="card">
        <h3>🔍 Medical Image Characteristics</h3>
    </div>
    """, unsafe_allow_html=True)

    img_props = {
        "Attribute": [
            "Imaging Modality",
            "Image Resolution",
            "File Format",
            "Color Encoding",
            "Bit Depth",
            "Average File Size"
        ],
        "Description": [
            "CT and MRI Brain Scans",
            "224 × 224 pixels",
            "PNG / JPG",
            "RGB",
            "8-bit",
            "50–200 KB"
        ]
    }

    st.dataframe(pd.DataFrame(img_props), width="stretch")

    # ================= PREPROCESSING =================
    st.markdown("""
    <div class="card">
        <h3>🧹 Data Preprocessing Pipeline</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    The following preprocessing steps were applied **uniformly to real and synthetic images**:

    1. Image resizing to 224 × 224  
    2. Pixel normalization  
    3. Removal of low-quality scans  
    4. Label verification  
    5. Stratified dataset splitting  
    """)

    # ================= KEY OBSERVATIONS =================
    st.markdown("""
    <div class="card">
        <h3>📌 Key Dataset Observations</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    - Real-only datasets were insufficient for deep learning
    - Synthetic images significantly improved class representation
    - Balanced datasets led to stable training curves
    - Motivated the final Diffusion + Classification pipeline
    """)

    # ================= TRANSITION =================
    st.info("""
    **Important Insight:**  
    Even after balancing with synthetic data, multiple experiments were conducted
    to verify realism, avoid leakage, and ensure clinical relevance.

    These experiments — including failures and corrections — are discussed in detail
    in the **Experiments & Failure Analysis** section.
    """)
