from PIL import Image, ImageDraw, ImageFont

def write_text_to_image(input_file:str, text: str="Scan me", font_path:str=None, font_size: int=50, rows: int=-8,output_file:str=None) -> None:
    try:
        img = Image.open(input_file)
        draw = ImageDraw.Draw(img)

        if font_path:
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.load_default()

        img_width, img_height = img.size

        text_width = draw.textlength(text, font_size=font_size)
        text_height = font_size * rows

        x = (img_width - text_width) // 2  
        y = (img_height - text_height) // 2 

        draw.text((x, y), text, fill="black", font_size = font_size)
        img.save(output_file)
        
    except OSError :
        raise("File not found")


def main():
    write_text_to_image(
        "/home/code/Server/Python/tools/qrCode/src/myqr.png",

    )
if __name__ == "__main__":
    main()
