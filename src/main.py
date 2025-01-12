import os
from qr_class import QR  

def main():
    
    text = "Scan me"
    link = "https://www.youtube.com/"


    qr_generator = QR(text, link, name="myqr")

    output_dir = os.path.join(os.getcwd(), "output")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "myqr.png")
    qr_generator.create_qr_with_text(output_file=output_file)

    print(f"QR code with text saved to: {output_file}")

if __name__ == "__main__":
    main()
