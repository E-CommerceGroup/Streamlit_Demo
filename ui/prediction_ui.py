import streamlit as st
from backend.mock_predictor import MockPredictionEngine
from utils.confidence import get_confidence

def render_prediction_ui():

    # ---------- STATE ----------
    if "engine" not in st.session_state:
        st.session_state.engine = MockPredictionEngine()

    if "run_prediction" not in st.session_state:
        st.session_state.run_prediction = False

    if "file_uploaded" not in st.session_state:
        st.session_state.file_uploaded = False

    # ---------- HEADER CARD ----------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔍 AI-Powered Disease Prediction")
    st.markdown("Upload a medical image to identify rare diseases using AI.")
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- FILE UPLOADER ----------
    uploaded_file = st.file_uploader(
        "Upload MRI / CT / X-ray Image",
        type=["png", "jpg", "jpeg"],
        disabled=st.session_state.file_uploaded
    )

    if uploaded_file:
        st.session_state.file_uploaded = True

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(uploaded_file, use_container_width=True)

        with col2:
            if st.button("🚀 Run Prediction"):
                st.session_state.run_prediction = True

            if st.session_state.run_prediction:
                with st.spinner("Running AI inference..."):
                    results = st.session_state.engine.predict(uploaded_file)

                max_prob = max(results.values())
                confidence = get_confidence(max_prob)

                st.success("Prediction Complete")

                for disease, prob in results.items():
                    st.metric(disease, f"{prob * 100:.2f}%")

                st.info(f"Confidence Level: {confidence}")

                if confidence == "Low":
                    st.warning(
                        "The image does not match known disease patterns. "
                        "Please add this disease using the Training section."
                    )
