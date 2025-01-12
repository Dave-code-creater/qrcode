import qrcode
import os
from utils.write_text_to_image import write_text_to_image
class QR:
    def __init__(self, text:str, link:str, name: str="myqr", path=None, ver=1, size = 15, border=5):
        self.qr = qrcode.QRCode(version=ver, box_size = size, border=border)
        self.data = link
        self.path = os.getcwd() + (path if path else '')
        self.name = name
        self.text = text

    def create_qr_with_text(self, output_file: str) -> None:
        # Generate QR Code
        self.qr.add_data(self.data)
        qr_image = self.qr.make_image(fill_color="black", back_color="white")
        
        # Save QR Code before adding text
        qr_image.save(os.path.join(self.path, self.name + '.png'))
        
        # Add text to QR Code image
        write_text_to_image(input_file=os.path.join(self.path, self.name + '.png'), text=self.text, output_file=output_file)

def main():
    myqr = QR( "Scan me", "https://www.youtube.com/", name="myqr")
    myqr.create_qr_with_text(output_file=os.path.join(myqr.path, "myqr.png"))


if __name__ == "__main__":
    main()
    