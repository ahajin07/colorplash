import sys
import os
import shutil
from PIL import Image, ImageOps

# Function adapted from DeOldify colorizer
def colorize_image(source_path, results_path, render_factor=35):
    """
    Colorizes a grayscale image using the DeOldify model.
    
    Parameters:
    - source_path: Path to the source image to be colorized
    - results_path: Directory to save the results
    - render_factor: Quality factor for the colorization (higher is better but slower)
    
    Returns:
    - grayscale_path: Path to the grayscale version of the image
    - colorized_path: Path to the colorized output image
    """
    try:
        # Add DeOldify to path
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'DeOldify')))
        
        from deoldify import device
        from deoldify.device_id import DeviceId
        from deoldify.visualize import get_image_colorizer
        
        device.set(device=DeviceId.CPU)  # Set to GPU0 if you have CUDA
        
        # Ensure the input image is grayscale before colorization
        with Image.open(source_path) as img:
            # Convert to grayscale
            grayscale_img = ImageOps.grayscale(img)
            # Save the grayscale image as the new source
            grayscale_path = os.path.join(results_path, 'grayscale_' + os.path.basename(source_path))
            grayscale_img.save(grayscale_path)
        
        # Use the grayscale image for colorization
        colorizer = get_image_colorizer(artistic=True)
        result_path = colorizer.plot_transformed_image(
            grayscale_path,
            render_factor=render_factor,
            display_render_factor=False,
            results_dir=results_path
        )
        
        # Rename the output file to match our expected naming convention
        filename = os.path.basename(source_path)
        new_filename = os.path.join(results_path, 'colorized_' + filename)
        
        # Delete the file if it already exists
        if os.path.exists(new_filename):
            os.remove(new_filename)
        
        # Copy the file to the new location with the expected name
        shutil.copy2(result_path, new_filename)
        
        # Return both the grayscale and colorized paths
        return grayscale_path, new_filename
    except Exception as e:
        print(f"Error in colorize_image: {e}")
        raise 