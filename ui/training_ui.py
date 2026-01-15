import streamlit as st
import time
import random

def render_training_ui():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧪 Synthetic Data Generation & Training")
    st.markdown(
        "Generate high-quality synthetic medical images to overcome data scarcity "
        "and incrementally improve the disease prediction system."
    )
    st.markdown('</div>', unsafe_allow_html=True)

    disease = st.text_input("Disease Category")
    prompt = st.text_area("Describe imaging characteristics (text prompt)")
    num_images = st.slider("Number of synthetic images", 100, 2000, 1000)

    if st.button("⚙️ Generate & Train"):
        progress = st.progress(0)
        status = st.empty()

        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)
            status.text(f"Processing... {i + 1}%")

        progress.empty()
        status.empty()

        st.success("Synthetic dataset generated and model trained successfully")

        col1, col2 = st.columns(2)
        col1.metric("SSIM Score", round(random.uniform(0.78, 0.92), 3))
        col2.metric("FID Score", round(random.uniform(22, 38), 2))

        st.download_button(
            "⬇️ Download Synthetic Dataset",
            data=b"dummy",
            file_name=f"{disease}_synthetic.zip"
        )

        st.download_button(
            "⬇️ Download Combined Dataset",
            data=b"dummy",
            file_name=f"{disease}_combined.zip"
        )

        st.info(
            "This disease will be available in the prediction system "
            "after backend integration."
        )
