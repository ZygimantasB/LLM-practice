import ollama
import shutil
from pathlib import Path
import os

# Define the directory containing the images
images_dir = Path('F:\\Python GitHub ZygimantasB\\LLM-practice\\AI agent\\images')

# Define target directories for 'drugs' and 'guns'
drugs_dir = Path('F:\\Python GitHub ZygimantasB\\LLM-practice\\AI agent\\images\\drugs')
guns_dir = Path('F:\\Python GitHub ZygimantasB\\LLM-practice\\AI agent\\images\\guns')

# Ensure target directories exist
drugs_dir.mkdir(parents=True, exist_ok=True)
guns_dir.mkdir(parents=True, exist_ok=True)

# List all image files in the directory
image_files = list(images_dir.glob('*'))  # Adjust pattern as needed to match specific image types

for image_path in image_files:
    try:
        # Analyze the image using ollama
        res = ollama.chat(
            model='llava:13b',
            messages=[{
                'role': 'user',
                'content': 'Classify this image. Does this image contain a gun, drugs, or is it unrelated? Provide a '
                           'single classification: "gun", "drugs", or "unrelated". You can use only one word',
                'images': [str(image_path)]
            }]
        )

        # Extract the message content
        message_content = res['message']['content'].strip().lower()
        print(message_content)

        # Copy the image to the respective folder based on the content
        if 'drugs' in message_content:
            target_path = drugs_dir / image_path.name
            if not target_path.exists():
                shutil.copy(image_path, target_path)
                print(f"Image copied to {target_path}")
            else:
                print(f"Image already exists in {target_path}")
        elif 'gun' in message_content:
            target_path = guns_dir / image_path.name
            if not target_path.exists():
                shutil.copy(image_path, target_path)
                print(f"Image copied to {target_path}")
            else:
                print(f"Image already exists in {target_path}")

    except PermissionError as e:
        print(f"PermissionError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
