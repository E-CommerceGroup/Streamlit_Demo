import streamlit as st
import pandas as pd
from PIL import Image
import datetime

from backend.inference import predict_image, _load_model, _get_transform, _get_device
from backend.gradcam.gradcam import generate_real_gradcam

from utils.confidence_utils import confidence_label, get_confidence_message
from utils.pdf_generator import generate_pdf_report


# =========================================================
# MAIN PAGE
# =========================================================

def render_prediction():
    """Live Prediction Page – REAL MODEL INFERENCE + REAL Grad-CAM"""

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
    Predictions and explainability (Grad-CAM) are generated from the trained CNN.
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

            r1, r2 = st.columns(2)
            with r1:
                st.metric("Predicted Disease", predicted_class)
            with r2:
                st.metric("Confidence", f"{confidence:.2%}")

            # Probability bar chart
            st.bar_chart(
                pd.DataFrame({
                    "Class": list(probabilities.keys()),
                    "Probability": list(probabilities.values())
                }).set_index("Class")
            )

            # ---------------- REAL GRAD-CAM ----------------
            st.markdown("""
            <div class="card">
                <h3>🔥 Grad-CAM Visualization (Model Explainability)</h3>
            </div>
            """, unsafe_allow_html=True)

            gradcam_img = None
            try:
                model = _load_model()
                transform = _get_transform()
                device = _get_device()

                class_idx = list(probabilities.keys()).index(predicted_class)

                gradcam_img = generate_real_gradcam(
                    model=model,
                    image_pil=image,
                    transform=transform,
                    device=device,
                    class_idx=class_idx
                )
            except Exception:
                gradcam_img = None

            g1, g2 = st.columns(2)
            with g1:
                st.image(image, caption="Original Image", width=280)
            with g2:
                if gradcam_img is not None:
                    st.image(gradcam_img, caption="Grad-CAM Overlay", width=280)
                else:
                    st.info("Grad-CAM could not be generated.")

            # ---------------- CLINICAL INTERPRETATION ----------------
            if conf_level == "High":
                st.success(get_confidence_message(conf_level))
            elif conf_level == "Moderate":
                st.warning(get_confidence_message(conf_level))
            else:
                st.error(get_confidence_message(conf_level))

            # ---------------- PDF REPORT ----------------
            pdf_buffer = generate_pdf_report(record)
            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_buffer,
                file_name="AI_Prediction_Report.pdf",
                mime="application/pdf"
            )

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
