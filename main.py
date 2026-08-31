import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def optimize_images():
    folder_path = filedialog.askdirectory(title="Select Image Folder")
    if not folder_path:
        return
    
    output_folder = os.path.join(folder_path, "optimized_webp")
    os.makedirs(output_folder, exist_ok=True)
    
    count = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            img_path = os.path.join(folder_path, filename)
            try:
                img = Image.open(img_path)
                name, _ = os.path.splitext(filename)
                output_path = os.path.join(output_folder, f"{name}.webp")
                
                img.save(output_path, "WEBP", quality=80)
                count += 1
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                
    messagebox.showinfo("Success", f"Successfully converted {count} images to WebP!\nFolder: {output_folder}")

root = tk.Tk()
root.title("Bulk WebP Optimizer Pro")
root.geometry("400x220")

label = tk.Label(root, text="Bulk WebP & Image Optimizer", font=("Arial", 12, "bold"))
label.pack(pady=20)

btn = tk.Button(root, text="Select Folder & Convert", command=optimize_images, bg="#28a745", fg="white", font=("Arial", 11), padx=10, pady=5)
btn.pack(pady=10)

root.mainloop()
