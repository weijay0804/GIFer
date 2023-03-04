from PIL import Image
from typing import List
from PIL.PngImagePlugin import PngImageFile

def convert_to_gif(input_file: List[str], output_path: str, *args, **kw):

    if kw.get("speed"):
        speed = kw.get("speed")
    
    else:
        speed = 2

    images: List[PngImageFile] = []

    for file in input_file:
        images.append(Image.open(file))

    if len(input_file) > 1:
        images[0].save(
            fp = output_path,
            format="gif",
            append_images = images[1:],
            save_all=True,
            duration = speed * 1000,
            loop = 0
        )

    else:
        images[0].save(
            fp = output_path,
            format="gif",
            save_all=True,
            duration = speed * 1000,
            loop = 0
        )