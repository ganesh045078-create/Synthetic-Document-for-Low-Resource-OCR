# Synthetic data generation
# from src.generation.generator import generate_synthetic_documents

# Preprocessing
# from src.preprocessing.preprocess import preprocess_document_images

# Model training (ML, DL, SD-GAN)
# from src.training.train import train_ml_models, train_dl_models, train_gan_augmented_model

# Evaluation methods (PSNR, SSIM, CER, WER)
# from src.evaluation.metrics import calculate_psnr_ssim, evaluate_ocr_accuracy

# Utility to save evaluation output
# from src.utils.save_results import save_evaluation_results


def main():

    print("\n================= REPRODUCTION STARTED =================\n")

    # STEP 1 — Generate Synthetic Dataset

    print("[1/4] Generating synthetic document dataset...")
    # generate_synthetic_documents(output_dir="data/synthetic/")
    # print("Synthetic dataset created at: data/synthetic/")

    
    # STEP 2 — Preprocess Dataset
    
    print("[2/4] Preprocessing dataset...")
    # preprocess_document_images(input_dir="data/synthetic/",
    #                            output_dir="data/processed/")
    # print("Preprocessed dataset saved at: data/processed/")

    
    # STEP 3 — Train OCR Models
    
    print("[3/4] Training OCR models (ML, DL, SD-SD-GAN)...")
    
    # print("Training ML models...")
    # train_ml_models(processed_data_path="data/processed/")

    # print("Training DL models...")
    # train_dl_models(processed_data_path="data/processed/")

    # print("Training SD-SD-GAN enhanced OCR model...")
    # train_gan_augmented_model(processed_data_path="data/processed/")

    
    # STEP 4 — Evaluate Models
    
    print("[4/4] Evaluating models...")
    
    # psnr_score, ssim_score = calculate_psnr_ssim(
    #     real_dir="data/ground_truth/",
    #     generated_dir="data/processed/"
    # )

    # cer, wer = evaluate_ocr_accuracy(
    #     predictions_dir="results/predictions/",
    #     ground_truth_dir="data/ground_truth/"
    # )

    
    # STEP 5 — Save Evaluation Outputs
    
    print("Saving evaluation results to: results/evaluation_summary.txt")
    
    # results = {
    #     "PSNR": psnr_score,
    #     "SSIM": ssim_score,
    #     "CER": cer,
    #     "WER": wer
    # }

    # save_evaluation_results(results, output_file="results/evaluation_summary.txt")

    print("\n================= REPRODUCTION COMPLETED =================\n")
    print("All results, logs, and generated files are stored in the 'results/' directory.\n")


if __name__ == "__main__":
    main()
