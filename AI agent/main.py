from pathlib import Path
import shutil
import ollama
from ollama._types import ResponseError

images_dir = Path(r'F:\Python GitHub ZygimantasB\LLM-practice\AI agent\images')
drugs_dir = Path(r'F:\Python GitHub ZygimantasB\LLM-practice\AI agent\drugs')
guns_dir = Path(r'F:\Python GitHub ZygimantasB\LLM-practice\AI agent\guns')

drugs_dir.mkdir(parents=True, exist_ok=True)
guns_dir.mkdir(parents=True, exist_ok=True)

def analyze_image(image_path):
    try:
        res = ollama.chat(
            model='llava:13b',  # Model average for this task
            messages=[{
                'role': 'user',
                'content': 'Describe this image',
                'images': [image_path]
            }]
        )

        if 'message' in res:
            description = res['message']['content']
            if 'gun' in description:
                return 'guns'
            elif 'drugs' in description:
                return 'drugs'
        return 'none'
    except ResponseError as e:
        print(f"Unsupported image format for {image_path}: {e}")
        return 'unsupported format'

image_paths = []
for extension in ['*.png', '*.jpg', '*.jpeg', '*.gif']:
    image_paths.extend(images_dir.glob(extension))

for image_path in image_paths:
    if image_path.stat().st_size < 10 * 1024:  # Skip images smaller than 10KB
        print(f"Skipping {image_path}, file size is smaller than 10KB.")
        continue

    result = analyze_image(image_path)

    if result == 'drugs':
        print(f"Image {image_path} contains drugs. Copying to drugs folder.")
        shutil.copy(image_path, drugs_dir)
    elif result == 'guns':
        print(f"Image {image_path} contains guns. Copying to guns folder.")
        shutil.copy(image_path, guns_dir)
    elif result == 'none':
        print(f"Image {image_path} does not contain guns or drugs.")
