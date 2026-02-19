import streamlit as st
import pandas as pd
from PIL import Image
import datetime

from backend.models.model_predictor import predict_image
from utils.confidence_utils import confidence_label, get_confidence_message
from utils.image_utils import generate_mock_gradcam
from utils.pdf_generator import generate_pdf_report


# =========================================================
# MAIN PAGE
# =========================================================

def render_prediction():
    """Live Prediction Page – REAL MODEL INFERENCE (Colab-Aligned)"""

    # ---------------- STATE ----------------
    if "history" not in st.session_state:
        st.session_state.history = []

    st.markdown("""
    <div class="card">
        <h2>🖼️ Live Prediction – Clinical Decision Support</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **This page runs the trained deep learning model (5-class classification).**  
    Predictions and confidence values are produced directly by the model.
    """)

    uploaded_file = st.file_uploader(
        "Upload CT / MRI / X-ray Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")

        col1, col2 = st.columns([1, 1])

        # ---------------- IMAGE PREVIEW ----------------
        with col1:
            st.image(
                image,
                caption="Uploaded Medical Image",
                width=320
            )

        with col2:
            st.markdown("""
            **Image Ready for Inference**
            - Input Size: 224 × 224
            - Color Mode: RGB
            - Model: ResNet-18 (5-Class CNN)
            """)
            run = st.button("🚀 Run Prediction")

        # ---------------- RUN INFERENCE ----------------
        if run:
            with st.spinner("Running AI inference..."):
                result = predict_image(image)

            if not result.get("is_brain", True):
                st.error(result["message"])
                st.metric("Validation Confidence", f"{result['confidence']:.2%}")
                return

            predicted_class = result["prediction"]
            confidence = result["confidence"]        # 0–1
            probabilities = result["probabilities"]
            conf_level = confidence_label(confidence)

            # Save history
            record = {
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "image_name": uploaded_file.name,
                "prediction": predicted_class,
                "confidence": confidence,
                "confidence_level": conf_level,
            }
            st.session_state.history.append(record)

            # ---------------- RESULTS ----------------
            st.markdown("""
            <div class="card">
                <h3>📊 Prediction Result</h3>
            </div>
            """, unsafe_allow_html=True)

            # Custom styling for results
            col_res1, col_res2, col_res3 = st.columns([1, 1, 1])
            
            with col_res1:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, rgba(0, 153, 255, 0.1), rgba(0, 217, 255, 0.1)); border-left: 4px solid #0099ff; border-radius: 12px; padding: 16px; text-align: center;">
                    <div style="color: #64748b; font-size: 12px; margin-bottom: 8px;">Predicted Disease</div>
                    <div style="color: #0099ff; font-size: 24px; font-weight: bold;">{predicted_class}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col_res2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(34, 197, 94, 0.05)); border-left: 4px solid #22c55e; border-radius: 12px; padding: 16px; text-align: center;">
                    <div style="color: #64748b; font-size: 12px; margin-bottom: 8px;">Confidence</div>
                    <div style="color: #22c55e; font-size: 24px; font-weight: bold;">{confidence:.2%}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col_res3:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(168, 85, 247, 0.05)); border-left: 4px solid #a855f7; border-radius: 12px; padding: 16px; text-align: center;">
                    <div style="color: #64748b; font-size: 12px; margin-bottom: 8px;">Confidence Level</div>
                    <div style="color: #a855f7; font-size: 24px; font-weight: bold;">{conf_level}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("")
            
            # Probability visualization with smaller chart
            prob_df = pd.DataFrame({
                "Disease Class": list(probabilities.keys()),
                "Confidence Score": list(probabilities.values())
            })
            
            # Create a more compact chart
            st.markdown("**Confidence Scores by Disease Class**")
            
            chart_col1, chart_col2 = st.columns([2, 1])
            with chart_col1:
                st.bar_chart(
                    prob_df.set_index("Disease Class"),
                    height=280,
                    use_container_width=True
                )
            
            with chart_col2:
                st.markdown("**Scores**")
                for disease, score in probabilities.items():
                    st.markdown(f"• {disease}: **{score:.2%}**")

            # ---------------- GRAD-CAM (Mock) ----------------

            # ---------------- CLINICAL INTERPRETATION ----------------

            # ---------------- PDF REPORT ----------------
            st.markdown("""
            <div class="card">
                <h3>📄 Generate Report</h3>
            </div>
            """, unsafe_allow_html=True)

            # Generate PDF buffer (assumed function)
            pdf_buffer = generate_pdf_report(record)

            # Custom button styling (NEW COLOR THEME: Purple → Pink Gradient)
            st.markdown("""
            <style>
                .download-btn {
                    display: flex;
                    justify-content: center;
                    margin: 24px 0;
                }

                /* Target Streamlit download button */
                div.stDownloadButton > button {
                    background: linear-gradient(135deg, #7b2ff7, #f107a3) !important;
                    color: #ffffff !important;
                    border: none !important;
                    padding: 14px 36px !important;
                    font-size: 16px !important;
                    font-weight: 600 !important;
                    border-radius: 10px !important;
                    cursor: pointer !important;
                    transition: all 0.35s ease !important;
                    box-shadow: 0 6px 20px rgba(123, 47, 247, 0.45) !important;
                }

                div.stDownloadButton > button:hover {
                    background: linear-gradient(135deg, #5f1eea, #c8007a) !important;
                    box-shadow: 0 10px 30px rgba(193, 0, 122, 0.55) !important;
                    transform: translateY(-4px) scale(1.02) !important;
                }

                div.stDownloadButton > button:active {
                    transform: translateY(0px) scale(0.98) !important;
                    box-shadow: 0 4px 12px rgba(123, 47, 247, 0.35) !important;
                }
            </style>
            <div class="download-btn">
            """, unsafe_allow_html=True)

            # Centered button using columns
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                st.download_button(
                    label="📥 Download PDF Report",
                    data=pdf_buffer,
                    file_name="AI_Prediction_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

            st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- HISTORY ----------------
    st.markdown("""
    <div class="card">
        <h3>📜 Prediction History</h3>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.history:
        st.dataframe(
            pd.DataFrame(st.session_state.history),
            use_container_width=True
        )
    else:
        st.info("No predictions made yet.")

    # ---------------- DISCLAIMER ----------------
    st.info("""
    **Disclaimer:**  
    This AI system is a clinical decision-support tool.  
    Final diagnosis must always be confirmed by a qualified medical professional.
    """)
