import streamlit as st
import pandas as pd

def render_dataset():
    """Page 2: Dataset Insights – Detailed Medical Dataset Analysis"""

    # ================= HEADER =================
    st.markdown("""
    <div class="card">
        <h2>📊 Dataset Insights & Analysis</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **“In medical deep learning, the dataset defines the ceiling of model performance.”**

    This project uses **curated and balanced medical imaging datasets**
    focused on **rare neurological disorders**, where data scarcity and imbalance
    are major challenges.
    """)

    # ================= DATASET ORIGIN =================
    st.markdown("""
    <div class="card">
        <h3>📁 Dataset Origin & Motivation</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    - Medical imaging data collected from **publicly available, research-grade datasets**
    - Focused on **rare neurological diseases**, which are often underrepresented
    - Includes both **Disease** and **Normal** brain images
    - Designed to simulate **real-world clinical decision challenges**
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

    st.dataframe(pd.DataFrame(disease_info), width='stretch')

    # ================= DATASET SIZE =================
    st.markdown("""
    <div class="card">
        <h3>📦 Dataset Size Summary</h3>
    </div>
    """, unsafe_allow_html=True)

    size_data = {
        "Disease": [
            "Moyamoya + IVH",
            "Neurofibromatosis Type 1",
            "Optic Glioma",
            "Tuberous Sclerosis"
        ],
        "Training Images": [1208, 1342, 692, 928],
        "Validation Images": [260, 288, 150, 200],
        "Testing Images": [260, 290, 150, 200],
        "Total Images": [1728, 1920, 992, 1328]
    }

    df_size = pd.DataFrame(size_data)
    st.dataframe(df_size, width='stretch')

    st.markdown("""
    ✔ Each dataset is **class-balanced**  
    ✔ Equal number of **Disease** and **Normal** images  
    ✔ Enables unbiased performance evaluation
    """)

    # ================= CLASS BALANCE =================
    st.markdown("""
    <div class="card">
        <h3>⚖️ Class Balance Strategy</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **Why balancing was necessary:**
    - Rare diseases naturally have fewer samples
    - Imbalanced data causes biased predictions
    - Model may learn to predict only the majority class

    **Balancing Approach Used:**
    - Equal disease and normal samples per split
    - Stratified splitting across train/validation/test
    - Augmentation applied selectively during training
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

    st.dataframe(pd.DataFrame(img_props), width='stretch')

    # ================= PREPROCESSING =================
    st.markdown("""
    <div class="card">
        <h3>🧹 Data Preprocessing Pipeline</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    The following preprocessing steps were applied **before model training**:

    1. **Image Resizing** – Standardized all images to 224 × 224  
    2. **Normalization** – Pixel intensities scaled to improve convergence  
    3. **Noise Filtering** – Removed low-quality or corrupted scans  
    4. **Label Verification** – Ensured correct disease annotation  
    5. **Stratified Splitting** – Maintained class balance across splits  
    """)

    # ================= STATISTICAL OBSERVATIONS =================
    st.markdown("""
    <div class="card">
        <h3>📌 Key Dataset Observations</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    - Rare disease datasets are **small but complex**
    - High inter-class similarity increases classification difficulty
    - Small dataset size increases risk of overfitting
    - Motivated the use of augmentation and regularization
    """)

    # ================= LINK TO FAILURE PAGE =================
    st.info("""
    **Important Insight:**  
    Even with balanced data, early experiments showed overfitting and poor generalization.
    These issues and their solutions are discussed in detail in the
    **Experiments & Failures** section.
    """)
