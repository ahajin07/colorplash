import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from colorizer_utils import colorize_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MODEL_PATH'] = 'models/ColorizeArtistic_gen.pth'
app.secret_key = 'some_secret_key'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('models', exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if not os.path.exists(app.config['MODEL_PATH']):
        flash('Model file not found. Please download the ColorizeArtistic_gen.pth model file and place it in the models directory.')
        return render_template('index.html', model_missing=True)
        
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Now colorize_image returns both the grayscale path and colorized path
            grayscale_path, colorized_path = colorize_image(filepath, app.config['UPLOAD_FOLDER'])
            
            # Extract just the filenames from the paths
            grayscale_filename = os.path.basename(grayscale_path)
            colorized_filename = os.path.basename(colorized_path)
            
            return render_template('index.html', 
                                  input_image=filename, 
                                  grayscale_image=grayscale_filename,
                                  output_image=colorized_filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
