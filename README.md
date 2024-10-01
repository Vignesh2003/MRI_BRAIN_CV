

---

# **Brain MRI Metastasis Segmentation Assignment**

## **Project Overview**

This project demonstrates proficiency in computer vision techniques by implementing two deep learning architectures, **Nested U-Net (U-Net++)** and **Attention U-Net**, for brain MRI metastasis segmentation. The goal is to identify and segment brain metastases in MRI scans, compare the performance of the two models, and build a web application to interactively showcase the segmentation results.

## **Dataset**
- **Dataset Link**: [Brain MRI Metastasis Dataset](https://dicom5c.blob.core.windows.net/public/Data.zip)
- **Description**: The dataset contains brain MRI images and their corresponding metastasis segmentation masks.
- **Preprocessing**: Images are enhanced using CLAHE (Contrast Limited Adaptive Histogram Equalization) for better metastasis visibility.
- **Train-Test Split**: The dataset is split into 80% training and 20% testing.

---

## **Architectures**

### **1. Nested U-Net (U-Net++)**
The U-Net++ architecture builds on the original U-Net by introducing nested and dense skip pathways. This allows the model to better capture the context of the image, improving segmentation precision for small metastases.

- **Key Features**:
  - Multiple skip connections
  - Enhanced segmentation performance with dense upsampling layers
  - Better at capturing fine details in metastasis regions

### **2. Attention U-Net**
Attention U-Net enhances the U-Net architecture by incorporating attention mechanisms to focus the model on the most important features in the MRI images. This helps reduce irrelevant information and improves the segmentation quality for metastases.

- **Key Features**:
  - Attention gates that highlight relevant regions
  - Reduces false positives by focusing on key metastasis regions
  - Better overall accuracy and specificity for metastasis detection

---

## **Project Workflow**

### **1. Data Preprocessing**
- **CLAHE (Contrast Limited Adaptive Histogram Equalization)** is applied to enhance metastasis visibility.
- The MRI images are **normalized** to [0, 1] range.
- **Data augmentation** is performed using rotations, zooming, and flipping to create more diverse training samples.

### **2. Model Training**
- Both **Nested U-Net** and **Attention U-Net** models were trained on the preprocessed dataset.
- The **Dice Score** is used as the primary evaluation metric to measure the segmentation accuracy of both models.

### **3. Evaluation**
- The models are evaluated based on their performance on the test set, and the **Dice Score** is computed for each.

### **4. Web Application**
- A web application was developed to showcase the segmentation results.
  - **Backend**: A FAST API serves the best performing model for metastasis segmentation.
  - **Frontend**: A Streamlit interface allows users to upload MRI images and view segmentation results interactively.

---

## **Model Training and Evaluation**

### **Dice Score**
The **Dice Score** is the main evaluation metric for this task. It measures the overlap between the predicted segmentation mask and the ground truth. The formula for the Dice Score is:

\[ Dice = \frac{2 \cdot |A \cap B|}{|A| + |B|} \]

Where `A` is the ground truth mask and `B` is the predicted mask.

### **Training Hyperparameters**
- **Optimizer**: Adam
- **Loss Function**: Binary Cross-Entropy
- **Epochs**: 50
- **Batch Size**: 8
- **Learning Rate**: 0.001

### **Results**
The models were evaluated on the test set, and the following Dice Scores were obtained:

| Model            | Dice Score (Test Set) |
|------------------|-----------------------|
| Nested U-Net++    | **0.89**              |
| Attention U-Net   | **0.92**              |

### **Model Comparison**
- **Attention U-Net** slightly outperformed **Nested U-Net** in terms of Dice Score due to its ability to focus on relevant features using the attention mechanism.
- **Nested U-Net** performed well but struggled with fine-grained metastasis details compared to Attention U-Net.

---

## **How to Set Up and Run the Project**

### **Prerequisites**
- Python 3.7+
- Required libraries: TensorFlow, Keras, OpenCV, FastAPI, Streamlit, scikit-learn, and other standard Python libraries.
  
### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/brain-mri-metastasis-segmentation.git
cd brain-mri-metastasis-segmentation
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Download the Dataset**
Download the dataset from [this link](https://dicom5c.blob.core.windows.net/public/Data.zip) and extract it into the `data/` folder.

### **4. Train the Models**
Run the script to train both models:
```bash
python train.py
```

### **5. Run the Web Application**

#### Start the FAST API Backend
```bash
uvicorn app:app --reload
```

#### Start the Streamlit Frontend
```bash
streamlit run app.py
```

Now, open your browser and go to `http://localhost:8501` to use the web app. Upload a brain MRI image to view the segmentation results.

---

## **Directory Structure**
```
brain-mri-metastasis-segmentation/
│
├── data/                   # Dataset folder (place the images here)
├── models/                 # Trained models
├── notebooks/              # Jupyter notebooks for model experimentation
├── src/
│   ├── preprocessing.py    # Data preprocessing and augmentation code
│   ├── models.py           # Model architecture definitions (Nested U-Net, Attention U-Net)
│   ├── train.py            # Training script
│   ├── evaluation.py       # Model evaluation script
│   ├── app.py              # Streamlit app code
│   └── app_backend.py      # FastAPI backend code
├── README.md               # This file
└── requirements.txt        # Python dependencies
```

---

## **Challenges and Solutions**

### **Challenges in Brain Metastasis Segmentation**
1. **Small metastases** are difficult to detect and segment.
2. **Class imbalance** between background and metastasis regions.
3. **MRI noise** and inconsistent image quality across patients.

### **Solutions**
1. Applied **attention mechanisms** in Attention U-Net to help focus on smaller regions of interest.
2. Used **data augmentation** to create a more balanced dataset and improve model generalization.
3. **CLAHE preprocessing** helped enhance the visibility of metastases by improving contrast in the images.

---

## **Potential Improvements**
1. **Multimodal MRI data**: Incorporating multiple MRI modalities (e.g., T1, T2, FLAIR) could provide richer information for segmentation.
2. **3D U-Net**: Moving to 3D models could better capture volumetric information from MRI scans.
3. **Further model optimization**: Fine-tuning hyperparameters, experimenting with different loss functions, and training on larger datasets can potentially improve performance.

---

## **Conclusion**
In this project, we implemented and compared **Nested U-Net** and **Attention U-Net** architectures for brain MRI metastasis segmentation. Attention U-Net performed slightly better, achieving a higher Dice Score due to its ability to focus on key metastasis regions. The project is wrapped up with an interactive web application built using **FAST API** and **Streamlit** to showcase the segmentation results.

---

## **Video Demonstration**
A video demonstration of the Streamlit UI can be found [here](#).

---

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides a structured and detailed guide for anyone looking to understand and run your project, including setup, code usage, results, and future work. Make sure to adjust specific values (such as URLs, Dice Scores, etc.) based on your actual project results.