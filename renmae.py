import os

# Replace this with your audio folder path
AUDIO_ROOT = r"C:\Users\Bidur Siwakoti\OneDrive\Desktop\breathe-now-audio\breathe-now-audio"

# Allowed audio extensions
AUDIO_EXTENSIONS = {'.mp3', '.wav', '.ogg', '.m4a', '.flac'}

def rename_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext in AUDIO_EXTENSIONS and " " in filename:
                old_path = os.path.join(root, filename)
                new_filename = filename.replace(" ", "_")
                new_path = os.path.join(root, new_filename)
                
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {filename} → {new_filename}")
                except Exception as e:
                    print(f"Error renaming {filename}: {e}")

if __name__ == "__main__":
    rename_files_in_directory(AUDIO_ROOT)
