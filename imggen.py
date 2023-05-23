import openai
import requests
import os

openai.api_key = "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"

def generate_image_from_text(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256",
        response_format="url",
    )

    image_url = response["data"][0]["url"]
    image_data = requests.get(image_url).content

    filename = prompt.replace(" ", "_") + ".png"
    with open(filename, "wb") as f:
        f.write(image_data)

    return filename

image_file = generate_image_from_text("IIT Kanpur")
print(f"Image saved to {image_file}")