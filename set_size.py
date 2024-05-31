import os
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def resize_images_in_folder(folder_path, output_folder_path, size):
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
        
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    print(len(image_files))
    total_files = len(image_files)
    logging.info(f"Found {total_files} images to resize.")
    
    for i, filename in enumerate(image_files):
        try:
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            img = img.resize(size, Image.ANTIALIAS)
            
            output_path = os.path.join(output_folder_path, filename)
            img.save(output_path)
            
            if (i + 1) % 100 == 0 or i + 1 == total_files:
                logging.info(f"Processed {i + 1}/{total_files} images")
                
        except Exception as e:
            logging.error(f"Failed to process {filename}: {e}")

# Example usage
input_folder = '/home/huy/data1tb/Restormer/SR_restormer/data/SR/test/rain'
output_folder = '/home/huy/data1tb/Restormer/SR_restormer/data/SR/test/rain'
new_size = (300, 300)  # New size in pixels

resize_images_in_folder(input_folder, output_folder, new_size)
