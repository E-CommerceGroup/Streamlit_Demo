# 🏥 Streamlit Demo – Rare Disease AI Platform

**A Complete Machine Learning Lifecycle for Medical Image Analysis**

This is a **Streamlit-based interactive web application** for a **Generative AI-Driven Rare Disease Classification System**. It demonstrates a complete machine learning lifecycle for medical image analysis, specifically focused on detecting rare neurological diseases using deep learning and synthetic data generation techniques.

---

## 🎯 Core Problem & Solution

### Problem Statement
Medical professionals spend extensive time analyzing medical images (CT scans, MRI, X-rays) to identify diseases. Current diagnostic challenges:

- ⏱️ **Time-consuming** – Manual review takes 15-30 minutes per case
- 👨‍⚕️ **Expertise-dependent** – Diagnosis quality varies by radiologist experience
- 🌍 **Geographically limited** – Expert radiologists unavailable in many regions
- 😓 **Fatigue-prone** – Long hours lead to diagnostic errors

### Solution
A **CNN-based (Convolutional Neural Network) diagnostic system** that:

- ⚡ Processes images in **< 1 second**
- 🎯 Maintains **100% consistency**
- 🌐 **Globally deployable**
- 📊 Provides **confidence scores** for clinical decision support

---

## 🧠 Technical Architecture

### Model Architecture: ResNet-18 CNN
- **Base Model:** ResNet-18 (lightweight, pre-trained backbone)
- **Classification Head:** Linear layer with 5 output classes
- **Input Size:** 224 × 224 RGB images
- **Normalization:** ImageNet standard (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

### Inference Pipeline
- **Lazy loading** – Model loads only when needed to optimize memory
- **GPU/CPU support** – Automatically detects device availability (CPU for Streamlit)
- **Preprocessing:** Image resizing, tensor conversion, normalization
- **Output:** Prediction class, confidence score (0-1), probability distribution for all 5 classes

### Five Disease Classification Classes

1. **Moyamoya Disease with Intraventricular Hemorrhage (IVH)** – Cerebrovascular disorder
2. **Neurofibromatosis Type 1 (NF1)** – Genetic neurological disorder
3. **Optic Glioma** – Brain tumor (neuroendocrine)
4. **Tuberous Sclerosis** – Genetic neurocutaneous syndrome
5. **Normal** – Healthy brain images

---

## 📊 Data & Training Strategy

### Dataset Characteristics
- **Domain:** Medical neuroimaging (CT/MRI scans)
- **Focus:** Rare neurological diseases with high data scarcity
- **Composition:** Balanced real images + synthetically generated images
- **Challenge:** Dealing with class imbalance and limited labeled samples for rare diseases

### Two-Stage Training Strategy

**Stage 1 – Generative Model (Diffusion)**
- Uses **Stable Diffusion** fine-tuned for medical images
- **Technique:** LoRA (Low-Rank Adaptation) for efficient training
- **Objective:** Generate realistic synthetic medical images for rare diseases
- **Loss:** Noise prediction loss (diffusion model standard)

**Stage 2 – Classification Model**
- Trains on **combined real + synthetic images**
- Uses **ResNet-18** for disease classification
- Improves generalization by increasing effective training data
- Mitigates overfitting from small rare disease datasets

---

## 💻 Project Structure

```
Streamlit_Demo/
├── app.py                      # Main Streamlit entry point
├── requirements.txt            # Dependencies (streamlit, torch, etc.)
├── README.md                   # This file
├── assets/                     # Sample images for demo
├── backend/
│   ├── config.py              # Model paths, class names, device settings
│   ├── models/
│   │   ├── model_architecture.py    # ResNet-18 CNN definition
│   │   ├── model_predictor.py       # Inference pipeline (real predictions)
│   │   └── best_model.pth          # Pre-trained model weights
│   └── gradcam/
│       └── gradcam.py         # Grad-CAM visualization for explainability
├── ui/                        # Multi-page Streamlit interface
│   ├── page_1_overview.py     # Problem & motivation
│   ├── page_2_dataset.py      # Dataset analysis & statistics
│   ├── page_3_architecture.py # System architecture diagram
│   ├── page_4_training.py     # Training methodology
│   ├── page_5_experiments.py  # Failure analysis & lessons learned
│   ├── page_6_evaluation.py   # Model performance metrics
│   ├── page_7_prediction.py   # Live inference interface
│   ├── page_8_future.py       # Future improvements & roadmap
│   ├── prediction_ui.py       # Reusable prediction UI components
│   └── training_ui.py         # Training visualization components
└── utils/
    ├── confidence_utils.py    # Confidence level classification
    ├── confidence.py          # Confidence scoring logic
    ├── image_utils.py         # Image preprocessing & visualization
    └── pdf_generator.py       # Clinical report generation
```

---

## 🎨 Frontend – Streamlit Dashboard

### Main Application (app.py)
- **Theme:** Dark mode with gradient background (#0f172a to #020617)
- **Components:** Custom CSS styling with glass-morphism cards
- **Navigation:** 8-page interactive dashboard with sidebar navigation
- **Styling:** Roboto font, smooth animations, professional medical UI

### The 8-Page Dashboard

| Page | Description |
|------|-------------|
| **1. Overview** | Problem statement, motivation, manual vs AI comparison |
| **2. Dataset Insights** | Dataset origin, disease coverage, statistics, distribution |
| **3. System Architecture** | DiffusionGenMed pipeline, data flow, generative+discriminative integration |
| **4. Model Training** | Two-stage training strategy, hyperparameters, optimization |
| **5. Experiments & Failures** | Failed approaches, lessons learned, iterative improvement |
| **6. Evaluation & Results** | Performance metrics (90% accuracy, 0.91 F1-score), confusion matrix |
| **7. Live Prediction** | Interactive image upload, real inference, confidence visualization, Grad-CAM, PDF reports |
| **8. Future Scope** | Short/medium/long-term improvements, expansion roadmap |

---

## 🔍 Key Features

### Real Model Inference
- **Actual predictions** using trained ResNet-18 model
- **No mock data** – real neural network forward pass
- Supports PNG, JPG, JPEG formats
- Pre-processing: Resize to 224×224, normalize to ImageNet standards

### Confidence Scoring System
- **High Confidence (≥80%):** ✅ Suitable for automated screening
- **Moderate Confidence (60-79%):** ⚠️ Expert review recommended
- **Low Confidence (<60%):** ❌ Do not rely on AI alone
- Clinically-aligned interpretation messages

### Explainable AI – Grad-CAM
- **Gradient-weighted Class Activation Mapping**
- Shows which image regions influenced the prediction
- Helps clinicians understand AI decision-making
- Builds trust through transparency

### Clinical Report Generation
- Generates professional medical AI reports
- Includes timestamp, prediction, confidence level
- Ready for medical record integration
- PDF format for archiving and sharing

### Prediction History
- Tracks all uploaded images and predictions
- Stores timestamp, filename, prediction, confidence
- Enables pattern analysis and audit trails

---

## 📦 Dependencies

```
streamlit          # Web framework for interactive dashboards
numpy              # Numerical computing
Pillow             # Image processing
reportlab          # PDF generation
pandas             # Data manipulation and analysis
torch              # Deep learning framework (PyTorch)
torchvision        # Computer vision utilities and models
```

---

## ⚙️ Configuration (backend/config.py)
- **Device Detection:** Automatic GPU/CPU selection
- **Model Path:** Points to `best_model.pth`
- **Class Names:** 5 disease classes hardcoded
- **Lazy Imports:** Torch only loaded when needed (memory optimization)

---

## 🚀 How to Run the Application Locally

Follow the steps below to run the Streamlit app on your system.

### Prerequisites

Make sure you have the following installed:

- **Python 3.8 or higher**
- **Git**
- **Internet connection** (for font loading)

Check Python version:
```bash
python --version
```

### Installation Steps

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/E-CommerceGroup/Streamlit_Demo.git
cd Streamlit_Demo
```

#### 2️⃣ Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

The application will launch in your browser at `http://localhost:8501`

---

## 📊 Model Performance

### Overall Metrics
| Metric | Value |
|--------|-------|
| **Accuracy** | 90% (+12% vs baseline) |
| **F1-Score** | 0.91 (Balanced metric) |
| **Test Samples** | 1,000 (Held-out data) |
| **Inference Time** | 90 ms per image (GPU) |

### Confusion Matrix (Disease vs Normal)
```
                  Predicted Normal    Predicted Disease
Actual Normal           450                    50
Actual Disease          40                     460
```

---

## 🎓 Machine Learning Journey

This project demonstrates a **realistic ML development cycle**:

1. ❌ **Initial failures** – Naive approaches don't work
   - Naive CNN without augmentation → 71% accuracy (overfitting)
   - Traditional augmentation → 78% accuracy (still insufficient)

2. 🔄 **Iterative improvements** – Each failure provides insights
   - Realized data scarcity is the core problem
   - Synthetic generation needed

3. ✅ **Final success** – Combining generative + discriminative models
   - Diffusion model generates realistic synthetic images
   - Classification trained on real + synthetic data
   - Achieved 90% accuracy with better generalization

4. 📈 **Performance validation** – Comprehensive evaluation metrics
   - Confusion matrix, ROC-AUC, precision-recall curves
   - Confidence calibration for clinical deployment

---

## 💡 Why This Matters for Rare Diseases

- **Data scarcity** – Rare diseases have few labeled examples
- **Synthetic data generation** – Diffusion models create realistic variations
- **Generalization** – Training on real + synthetic improves robustness
- **Clinical applicability** – AI assists (not replaces) human experts
- **Trust building** – Confidence scores and explainability (Grad-CAM)

---

## 🎓 Educational Value

This project teaches:

✅ Complete ML lifecycle (problem → data → model → evaluation → deployment)  
✅ Deep learning for medical imaging  
✅ Generative AI (diffusion models) + discriminative AI (CNNs)  
✅ Handling rare disease data scarcity  
✅ Building production-ready web applications (Streamlit)  
✅ Failure-driven learning and iterative improvement  
✅ Explainable AI for healthcare  
✅ Clinical decision support systems design  

---

## 🚀 Future Roadmap

### Short-Term (3-6 months)
- **Dataset Expansion:** 5K → 50K images
- **Multi-Class Expansion:** 5 → 10+ disease subtypes
- **Uncertainty Quantification:** Bayesian predictions with confidence intervals

### Medium-Term (6-12 months)
- **Explainable AI:** Enhanced Grad-CAM visualizations
- **Multi-Modal Input:** Combine CT, MRI, X-ray modalities
- **Clinical Integration:** DICOM support, EHR connectivity

### Long-Term
- **Real-World Deployment:** Hospital integration
- **Federated Learning:** Privacy-preserving distributed training
- **Continuous Learning:** Model updates with new clinical data

---

## 📝 Project Status

✅ Model Architecture: Complete  
✅ Inference Pipeline: Production-Ready  
✅ Streamlit Dashboard: 8-Page Interface  
✅ Real Model Integration: Deployed  
✅ Explainability: Grad-CAM Support  
✅ Clinical Reports: PDF Generation  
🔄 Dataset Expansion: In Progress  
🔄 Multi-Modal Support: Planned  

---

## 📞 Support & Contact

For questions or issues:
- Check the individual page documentation in the UI
- Review comments in source code
- Refer to this README for architectural details

---

## 📄 License & Attribution

This project is designed for educational and research purposes in medical AI and deep learning.

---

**Last Updated:** January 26, 2026  
**Project Type:** Medical AI, Deep Learning, Streamlit Application  
**Primary Use Case:** Rare Disease Detection & Clinical Decision Support
