import os
import subprocess

def download_model():
    model_path = "models/plant_disease_recog_model_pwp.keras"
    
    # Check if model file exists and is valid (not just LFS pointer)
    if os.path.exists(model_path):
        file_size = os.path.getsize(model_path)
        # LFS pointer files are tiny (< 1KB), real model is ~200MB
        if file_size > 1000000:  # > 1MB means it's the real file
            print(f"Model file exists and is valid ({file_size} bytes)")
            return True
    
    print("Model file missing or is LFS pointer. Attempting to download...")
    
    try:
        # Try to pull LFS files
        subprocess.run(["git", "lfs", "pull"], check=True)
        print("Git LFS pull successful")
        return True
    except Exception as e:
        print(f"Git LFS pull failed: {e}")
        print("Please ensure the model file is properly committed or use an alternative hosting solution")
        return False

if __name__ == "__main__":
    download_model()
