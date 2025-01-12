from setuptools import setup, find_packages

setup(
    name="qrCode",
    version="0.1.0",
    description="A Python project to generate QR codes and add text to them.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="youremail@example.com",
    license="MIT",
    packages=find_packages(where="src"), 
    package_dir={"": "src"},
    install_requires=[
        "qrcode>=8.0.0",
        "Pillow>=11.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    entry_points={
        "console_scripts": [
            "qr-code-generator=src.main:main", 
        ]
    }
)
