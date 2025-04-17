# ColorSplash

A Flask web application that colorizes black and white images using DeOldify.

## Features

- Upload black and white images
- Automatically colorize images using AI
- View both the original and colorized versions

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/YOUR_USERNAME/colorplash.git
   cd colorplash
   ```

2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Download the DeOldify model file (ColorizeArtistic_gen.pth) and place it in the models directory.

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000`

3. Upload a black and white image and see the colorized result

## Technologies Used

- Flask
- DeOldify
- Python
- HTML/CSS 