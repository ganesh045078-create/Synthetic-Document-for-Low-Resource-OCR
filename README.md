Title: Generative AI for Synthetic Document Creation for Low-Resource OCR
Description: In this paper, we introduce a generative AI–driven framework that precisely targets one of the major bottlenecks towards the development of reliable OCR systems: the absence or rarity of annotated datasets in low-resource languages. Central to our approach is a Synthetic Document Generation Pipeline, driven by the SD-SD-GAN, capable of generating high-quality artificial document images that closely resemble real scanned pages.
            The process starts with the collection of a base corpus of text samples in the target low-resource language. These are then arranged randomly into document layouts, including various fonts, background textures, noise patterns, distortions, and artifacts such as blur, ink bleed, creases, shadows, and compression noise. The SD-SD-GAN captures the real structure and visual characteristics of actual documents and generates them with realistic variations. The result of this process is the creation of larger, more diverse, and more complex datasets without requiring manual ground-truth annotation.
            These synthesized images are combined with the available real data and processed through a complete OCR training pipeline. The codebase includes the steps of preprocessing, data augmentation routines, GAN-based data generation, conventional Machine Learning and Deep Learning models for classifying OCR, and a full evaluation framework. The performance of the models is evaluated using OCR metrics such as CER and WER, as well as image quality metrics like PSNR and SSIM.
            The repository includes all algorithms and source code, dataset generation procedures, and a reproduction script that can regenerate the whole experimental workflow starting from the creation of synthetic data up to model evaluation for scientific reproducibility. Comparison experiments include:
            - ML models versus DL models versus SD-GAN–augmented models
            Ablation studies comparing performance with and without synthetic data, and with different enhancement components These results clearly indicate that incorporating GAN-generated synthetic documents significantly improves the performance of OCR for low-resource languages, thereby successfully testing the efficiency of generative AI in data-scarce domains.
Dataset: The study uses a hybrid dataset consisting of synthetic document images generated using SD-GAN and real document samples from external sources. Synthetic images include paired ground-truth text            
Code Information: All source code for synthetic data generation, preprocessing, model training, and evaluation is provided in the src/ directory. The repository includes scripts for SD-GAN–based synthetic document creation, OCR model training (ML, DL, and GAN-augmented), and evaluation metrics. A reproduction script (reproduction_script.py) is included to fully replicate the experiments and results presented in the study.
Usage Instructions:Install all dependencies using: pip install -r requirements.txt
                    Place any external datasets (if used) inside the `data/external/` directory.
                    To reproduce the full pipeline—including synthetic data generation, preprocessing, training, and evaluation—run: python reproduction_script.py
Requirements
This project requires Python 3.x and the packages listed in `requirements.txt`.  
Key libraries include:
- numpy
- pandas
- opencv-python
- scikit-learn
- scikit-image
- tqdm
- tensorflow or torch
Methodology
The implemented workflow consists of the following steps:
1. Generating synthetic document images using the SD-GAN pipeline.
2. Preprocessing both real and synthetic document images.
3. Training OCR models using ML, DL, and GAN-augmented architectures.
4. Evaluating performance using CER, WER, PSNR, and SSIM metrics.
5. Performing comparative analysis (ML vs DL vs SD-GAN) and ablation studies.
6. Citations
If you use this repository, please cite:
[Your Name], "Generative AI for Synthetic Document Creation for Low-Resource OCR", 2025.
Also cite any external datasets used in this work using their official DOI/URL.

 



            
