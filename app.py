import os
from flask import Flask, render_template, request, redirect
from flask import make_response
import requests
from flask import flash, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.basename('static')
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/upload', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # check if a file is selected
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # check if the file type is allowed
        if not allowed_file(file.filename):
            flash('File type not allowed')
            return redirect(request.url)
        # if file type is there and allowed
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("file %s uploaded succesfully" %file.filename)
            return redirect(url_for('uploads',
                                    filename=filename))

    return render_template('index.html')




if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
