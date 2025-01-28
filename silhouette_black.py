import sys
from PIL import Image, ImageOps, ImageFilter

def convert_to_silhouette(input_image_path, output_image_path_pattern, threshold_values, blur_radius=2):
    # Load the image
    image = Image.open(input_image_path)

    # Convert palette images with transparency to RGBA
    if image.mode == 'P' or image.mode == 'LA':
        image = image.convert('RGBA')

    # Convert the image to grayscale
    grayscale = ImageOps.grayscale(image)
    
    # Apply Gaussian blur to smooth the edges
    blurred = grayscale.filter(ImageFilter.GaussianBlur(blur_radius))
    
    for threshold_value in threshold_values:
        # Threshold the image to create a binary (black and white) image
        # The silhouette will be black (0) on a white (255) background
        silhouette = blurred.point(lambda x: 0 if x > threshold_value else 255, '1')

        # Generate the output file path
        output_image_path = output_image_path_pattern.format(threshold_value=threshold_value)
        
        # Save the result
        silhouette.save(output_image_path)

# Example usage
input_image_path = sys.argv[1]
output_image_path_pattern = "Silhouette_{threshold_value}.png"
threshold_values = [10, 20, 30, 50, 75, 100, 150, 200]  # List of threshold values to generate different outputs

convert_to_silhouette(input_image_path, output_image_path_pattern, threshold_values)
