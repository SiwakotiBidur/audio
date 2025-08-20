import os
import json
import urllib.parse  # <-- New import

base_url = "https://raw.githubusercontent.com/SiwakotiBidur/audio/main"
local_root = "C:/Users/Bidur Siwakoti/OneDrive/Desktop/breathe-now-audio/breathe-now-audio"

raw_urls = []

for root, _, files in os.walk(local_root):
    for file in files:
        if file.endswith(".mp3"):
            rel_path = os.path.relpath(os.path.join(root, file), local_root)
            rel_path = rel_path.replace("\\", "/")
            encoded_path = urllib.parse.quote(rel_path)  # <-- Encode path properly
            raw_urls.append(f"{base_url}/{encoded_path}")

with open("raw-audio-urls.json", "w") as f:
    json.dump(raw_urls, f, indent=2)

print(f"✅ Total files: {len(raw_urls)}. Spaces handled. Saved to raw-audio-urls.json")
