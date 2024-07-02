from pathlib import Path
import ollama
from ollama._types import ResponseError

images_dir = Path(r'F:\Python GitHub ZygimantasB\LLM-practice\AI agent\images')

def analyze_image(image_path):
    try:
        res = ollama.chat(
            # model='llama3:70b', # Bad for this task
            # model='gemma2:27b', # Bad for this task
            model='llava:13b',  # Average for this task
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
    result = analyze_image(image_path)
    if result == 'guns':
        print(f"Image {image_path} contains guns.")
    elif result == 'drugs':
        print(f"Image {image_path} contains drugs.")
    elif result == 'none':
        print(f"Image {image_path} does not contain guns or drugs.")
