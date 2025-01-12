# QR Code Generator with Text

This Python project generates QR codes with customizable text. It allows you to create a QR code that can link to any URL and overlay custom text on the QR code image.

## Features

- Generate QR codes with any URL.
- Add custom text to the QR code image.
- Output QR code image is saved in an `output` folder.

## Installation

### Prerequisites

- Python 3.7 or higher.
- `pip` (Python package installer).

### Steps

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/qrCode.git
    cd qrCode
    ```

2. Install the required dependencies:

    If you are using `poetry` (recommended):

    ```bash
    poetry install
    ```

    Or use `pip` to install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Install dependencies manually:

    ```bash
    pip install qrcode[pil] Pillow
    ```

## Usage

To generate a QR code with text, run the `main.py` script:

```bash
python src/main.py
