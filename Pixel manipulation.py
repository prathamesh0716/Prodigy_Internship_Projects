from PIL import Image

def encrypt_image(image_path, output_path):
    img = Image.open(image_path)
    data = list(img.getdata())
    encrypted_data = [(r ^ 255, g ^ 255, b ^ 255) for r, g, b in data]  # Invert colors
    img.putdata(encrypted_data)
    img.save(output_path)
    print("✅ Image encrypted and saved to", output_path)

def decrypt_image(image_path, output_path):
    encrypt_image(image_path, output_path)  # Reuse the same function

# Use the image you uploaded
encrypt_image("sample.jpg", "encrypted.jpg")
decrypt_image("encrypted.jpg", "decrypted.jpg")
