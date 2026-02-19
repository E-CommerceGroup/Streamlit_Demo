import streamlit as st
import os
from pathlib import Path

def render_architecture():
    """Page 3: System Architecture – DiffusionGenMed Pipeline"""

    st.markdown("""
    <div class="card">
        <h2>⚙️ System Architecture – DiffusionGenMed</h2>
    </div>
    """, unsafe_allow_html=True)

    # Get the project root directory
    project_root = Path(__file__).parent.parent
    svg_file_path = project_root / "System Architecture.drawio (1).svg"
    
    # Display SVG Architecture Diagram
    if svg_file_path.exists():
        with open(svg_file_path, "r", encoding="utf-8") as f:
            svg_content = f.read()
        
        # Display SVG in container
        html_content = f"""
        <div style="background: #1a1a1a; border: 2px solid rgba(0, 153, 255, 0.3); border-radius: 16px; padding: 24px; margin: 20px 0;">
            <div style="width: 100%; overflow: auto; border: 1px solid #333333; border-radius: 12px; background: #1a1a1a; max-height: 600px; display: flex; justify-content: center; align-items: flex-start;">
                {svg_content}
            </div>
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
    else:
        st.error(f"❌ Architecture diagram not found at: {svg_file_path}")

    st.divider()

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

