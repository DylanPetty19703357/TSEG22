from flask import Flask, request
import os
import librosa
from machinelearning_helper import *

BackEnd = Flask(__name__) # Define Flask env
 
#http://192.168.0.1/analyseSong&song=file
# Accepts HTTP POST requests from the client. Requires a 'file' within the header. 
@BackEnd.route("/analyseSong", methods = ['POST'])
def analyseSong():
	if request.method == 'POST':  
		File = request.files['file']  
		FileName = File.filename
		if FileName != '':
			File_Ext = os.path.splittext(FileName)[1]
			if File_Ext != ".ogg": # Ensure the file is only an .ogg - abort any other file types.
				abort(415)
				return "415 - Restricted File Type"
		File.save(File.filename)
    # Execute functions within the Machine learning python files
		SongFeatures = features(FileName)
		Prediction = predict(SongFeatures)
		return Prediction # Return prediction or error
		

#/pollResults&id=112344
# This was removed due to issues with celery. Now returns HTTP 410, Gone.
@BackEnd.route("/pollResults", methods = ['GET'])
def pollResults(id):
	abort(410)
	return 410

# Deploy
if __name__ == "__main__":
    BackEnd.run(host='0.0.0.0', port=5000)
