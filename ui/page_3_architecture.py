import streamlit as st

def render_architecture():
    """Page 3: System Architecture – DiffusionGenMed Pipeline"""

    st.markdown("""
    <div class="card">
        <h2>⚙️ System Architecture – DiffusionGenMed</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **“Prediction is not a single step.  
    It is the result of data engineering, generative modeling, and deep learning.”**

    This architecture explains how **synthetic medical image generation**
    is integrated with **rare disease classification**.
    """)

    # ================= PIPELINE =================
    st.markdown("""
    <div class="card">
        <h3>📋 End-to-End Processing Pipeline</h3>
    </div>
    """, unsafe_allow_html=True)

    # CSS for pipeline
    st.markdown("""
    <style>
        .pipeline-container {
            display: flex;
            flex-direction: column;
            gap: 16px;
            margin: 20px 0;
        }
        
        .pipeline-step {
            background: linear-gradient(135deg, rgba(0, 153, 255, 0.1), rgba(0, 217, 255, 0.1));
            border-left: 4px solid #0099ff;
            border-radius: 12px;
            padding: 16px;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        
        .pipeline-step:hover {
            border-left-color: #0066cc;
            background: linear-gradient(135deg, rgba(0, 153, 255, 0.15), rgba(0, 217, 255, 0.15));
            box-shadow: 0 8px 20px rgba(0, 153, 255, 0.2);
        }
        
        .step-number {
            font-weight: 700;
            color: #0099ff;
            font-size: 18px;
            margin-bottom: 8px;
        }
        
        .step-title {
            font-weight: 600;
            color: #f8fafc;
            font-size: 16px;
            margin-bottom: 8px;
        }
        
        .step-details {
            color: #cbd5e1;
            font-size: 14px;
            line-height: 1.6;
        }
        
        .arrow {
            text-align: center;
            color: #0099ff;
            font-size: 20px;
            margin: 8px 0;
        }
    </style>
    """, unsafe_allow_html=True)

    # Pipeline HTML
    st.markdown("""
    <div class="pipeline-container">
        <div class="pipeline-step">
            <div class="step-number">① Data Source</div>
            <div class="step-title">Input Collection</div>
            <div class="step-details">
                • Public Datasets (NIH)<br>
                • Hospital Data (Anonymized)
            </div>
        </div>
        <div class="arrow">⬇️</div>
        <div class="pipeline-step">
            <div class="step-number">② Data Preprocessing</div>
            <div class="step-title">Standardization & Preparation</div>
            <div class="step-details">
                • DICOM → PNG/JPEG<br>
                • Normalization<br>
                • Resizing (224×224)<br>
                • Dataset Organization
            </div>
        </div>
        <div class="arrow">⬇️</div>
        <div class="pipeline-step">
            <div class="step-number">③ Synthetic Image Generation</div>
            <div class="step-title">Generative Modeling</div>
            <div class="step-details">
                • Stable Diffusion Model<br>
                • LoRA Fine-Tuning<br>
                • ControlNet Guidance<br>
                • Text Prompts
            </div>
        </div>
        <div class="arrow">⬇️</div>
        <div class="pipeline-step">
            <div class="step-number">④ Dataset Augmentation</div>
            <div class="step-title">Data Enrichment</div>
            <div class="step-details">
                • Real + Synthetic Images<br>
                • Balanced Training Data
            </div>
        </div>
        <div class="arrow">⬇️</div>
        <div class="pipeline-step">
            <div class="step-number">⑤ Disease Classification</div>
            <div class="step-title">Model Training</div>
            <div class="step-details">
                • ResNet / EfficientNet<br>
                • Vision Transformer (ViT)
            </div>
        </div>
        <div class="arrow">⬇️</div>
        <div class="pipeline-step">
            <div class="step-number">⑥ Evaluation & Validation</div>
            <div class="step-title">Performance Assessment</div>
            <div class="step-details">
                • Accuracy, Precision<br>
                • Recall, F1-score<br>
                • SSIM Analysis
            </div>
        </div>
        <div class="arrow">⬇️</div>
        <div class="pipeline-step">
            <div class="step-number">⑦ Output Layer</div>
            <div class="step-title">Deployment Ready</div>
            <div class="step-details">
                • Trained Model<br>
                • Synthetic Dataset<br>
                • Performance Report
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ================= MODULE DETAILS =================
    st.markdown("""
    <div class="card">
        <h3>🧠 Core System Modules</h3>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Synthetic Image Generation Module**
        - Uses Stable Diffusion
        - Learns distribution of medical images
        - Generates realistic rare disease samples
        - Preserves anatomical structure
        """)

    with col2:
        st.markdown("""
        **Disease Classification Module**
        - CNN-based models (ResNet / EfficientNet)
        - Vision Transformer for global context
        - Outputs disease probability score
        """)

    # ================= DATA FLOW =================
    st.markdown("""
    <div class="card">
        <h3>📊 Data Flow Explanation</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    | Stage | Description |
    |------|-------------|
    | Data Source | Collects real medical images |
    | Preprocessing | Converts & standardizes images |
    | Diffusion Model | Generates synthetic images |
    | Augmentation | Combines real + synthetic data |
    | Classifier | Learns disease-specific patterns |
    | Evaluation | Measures accuracy & realism |
    | Output | Deployable model & dataset |
    """)

    # ================= FEATURE LEARNING =================
    st.markdown("""
    <div class="card">
        <h3>🎯 Learning & Generalization Strategy</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    1. **Diffusion Model Learning**
       - Learns medical image structure
       - Generates diverse disease variations

    2. **Augmented Training**
       - Reduces class imbalance
       - Improves generalization

    3. **Classifier Learning**
       - CNN captures local pathology
       - ViT captures global context

    4. **Evaluation Feedback**
       - Confirms synthetic data usefulness
    """)

    # ================= MODES =================
    st.markdown("""
    <div class="card">
        <h3>🔁 Dual Operating Modes</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **Mode 1: Synthetic Data Generation**
    - Input: Text prompts / disease conditions
    - Output: Synthetic medical images
    - Used for research and data augmentation

    **Mode 2: Disease Classification**
    - Input: Real medical image
    - Output: Disease probability & diagnosis
    - Used as clinical decision support
    """)

    # ================= JUSTIFICATION =================
    st.info("""
    **Why This Architecture?**

    - Rare diseases suffer from data scarcity
    - Diffusion models generate high-quality medical images
    - Augmented data improves classifier robustness
    - Dual-mode design supports both research and diagnosis

    This architecture transforms **data scarcity into a solvable problem**.
    """)
