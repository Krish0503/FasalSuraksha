import os
import subprocess
import urllib.request
import gdown

def download_from_google_drive(file_id, destination):
    """Download file from Google Drive"""
    try:
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, destination, quiet=False)
        return True
    except Exception as e:
        print(f"Google Drive download failed: {e}")
        return False

def download_model():
    model_path = "models/plant_disease_recog_model_pwp.keras"
    
    # Check if model file exists and is valid
    if os.path.exists(model_path):
        file_size = os.path.getsize(model_path)
        if file_size > 1000000:  # > 1MB means it's the real file
            print(f"✓ Model file exists and is valid ({file_size} bytes)")
            return True
    
    print("⚠ Model file missing or invalid. Downloading...")
    os.makedirs("models", exist_ok=True)
    
    # Option 1: Google Drive (recommended)
    google_drive_id = os.getenv('GOOGLE_DRIVE_MODEL_ID')
    if google_drive_id:
        print(f"Downloading from Google Drive (ID: {google_drive_id})...")
        if download_from_google_drive(google_drive_id, model_path):
            print("✓ Model downloaded from Google Drive")
            return True
    
    # Option 2: Direct URL (Cloudflare R2, Dropbox, etc.)
    model_url = os.getenv('MODEL_URL')
    if model_url:
        try:
            print(f"Downloading from {model_url}...")
            urllib.request.urlretrieve(model_url, model_path)
            print("✓ Model downloaded from URL")
            return True
        except Exception as e:
            print(f"✗ Download from URL failed: {e}")
    
    # Option 3: Git LFS (fallback)
    try:
        print("Trying git lfs pull...")
        subprocess.run(["git", "lfs", "pull"], check=True)
        if os.path.exists(model_path) and os.path.getsize(model_path) > 1000000:
            print("✓ Git LFS pull successful")
            return True
    except Exception as e:
        print(f"✗ Git LFS failed: {e}")
    
    print("\n❌ Model download failed!")
    print("\nTo fix this, set one of these environment variables:")
    print("  GOOGLE_DRIVE_MODEL_ID - Google Drive file ID (easiest)")
    print("  MODEL_URL - Direct download URL")
    return False

if __name__ == "__main__":
    success = download_model()
    if not success:
        exit(1)

