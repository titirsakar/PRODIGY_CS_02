from PIL import Image

def process_image(image_path, output_path, key):
    try:
        # Open the image file
        img = Image.open(image_path)
        # Convert image to RGB mode to access pixel colors cleanly
        img = img.convert('RGB')
        
        # Load the pixel data into memory
        pixels = img.load()
        width, height = img.size

        # Go through every single pixel row by row, column by column
        for x in range(width):
            for y in range(height):
                # Extract individual Red, Green, and Blue values
                r, g, b = pixels[x, y]
                
                # Perform a basic mathematical operation (XOR) using the key
                # This scrambles the colors for encryption, and unscrambles them for decryption
                encrypted_r = r ^ key
                encrypted_g = g ^ key
                encrypted_b = b ^ key
                
                # Write the modified pixel back into the image
                pixels[x, y] = (encrypted_r, encrypted_g, encrypted_b)
        
        # Save the new manipulated image
        img.save(output_path)
        print(f"\nSuccess! Saved image to: {output_path}")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

def main():
    print("\n=== Simple Image Encryption Tool ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Choose an option (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice!")
        return

    # Prompt user for filenames
    input_file = input("Enter the source image filename (e.g., test.png): ")
    output_file = input("Enter the output image filename (e.g., encrypted.png): ")
    
    # Simple numerical key for the mathematical pixel shifting
    try:
        key = int(input("Enter an encryption key (a number between 1 and 255): "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if choice == '1':
        print("\nEncrypting image...")
        process_image(input_file, output_file, key)
    elif choice == '2':
        print("\nDecrypting image...")
        process_image(input_file, output_file, key)

if __name__ == "__main__":
    main()