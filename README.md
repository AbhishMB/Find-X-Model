# **Batch OCR Processing with EasyOCR**

This repository contains code to perform batch Optical Character Recognition (OCR) using EasyOCR and other supporting libraries for image processing and GPU acceleration. The notebook is designed to process a batch of images, extract text, and use various tools like spacy and torch to enhance the performance and usability of the OCR output.

## Features
* Batch OCR Processing: Utilizes EasyOCR to perform OCR on a batch of images.
* Image Preprocessing: Employs OpenCV (cv2) for preprocessing images, improving OCR accuracy.
* GPU Support: Leverages torch to utilize GPU acceleration (NVIDIA CUDA) for faster processing.
* Progress Tracking: Uses tqdm to display progress bars during batch processing.
* Text Postprocessing: Includes functionality to clean and organize OCR-extracted text using spacy and regular expressions.
  
## Requirements
* Python 3.x
* The following Python libraries:
  * pandas
  * opencv-python
  * numpy
  * easyocr
  * spacy
  * tqdm
  * torch
    
You can install the required packages using the following command:

bash
Copy code

pip install pandas opencv-python numpy easyocr spacy tqdm torch

Usage
Clone the repository:

bash
Copy code

git clone https://github.com/your-username/your-repo.git

cd your-repo

Open the Jupyter notebook: Launch Jupyter and open the batch.ipynb file to begin working with the notebook.

Run the notebook: The notebook is structured into cells that execute the following steps:

Import necessary libraries.
Check GPU availability and CUDA support.
Load and preprocess images.
Perform OCR on the batch of images using EasyOCR.
Post-process the extracted text (cleaning, formatting, etc.).
GPU Support
This project supports GPU acceleration via PyTorch. The notebook will automatically check if a CUDA-enabled GPU is available and utilize it if possible. This significantly speeds up the OCR process when working with large image datasets.

License
This project is licensed under the MIT License.

