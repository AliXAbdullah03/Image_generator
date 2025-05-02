from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import os

def generate_background(theme, style, output_path="output.png"):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    print("🚀 Loading Stable Diffusion model...")
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5", 
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        revision="fp16" if device == "cuda" else None
    )
    pipe = pipe.to(device)

    prompt = f"Background, {theme}, {style}, no text, 8k resolution, ultra realistic, professional, minimalistic"
    print(f"🎯 Prompt: {prompt}")

    with torch.autocast(device) if device == "cuda" else torch.no_grad():
        image = pipe(prompt).images[0]

    # Save the image
    image.save(output_path)
    print(f"✅ Background saved to {output_path}")

if __name__ == "__main__":
    theme = input("Enter the theme (e.g., Modern Tech): ")
    style = input("Enter the style (e.g., Minimalistic blue and white): ")
    output_path = "background_output.png"

    generate_background(theme, style, output_path)
