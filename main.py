from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'files/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'mcs_csta'



@app.route("/",methods=['GET'])
def main_page():
    return render_template('index.html')



@app.route("/upload_image",methods=['POST','GET'])
def catch_file():

    
    if request.method == "POST":

        if request.files:


            file = request.files['file_jas']
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    

    


    return redirect('/')
   





app.run()