from flask import Flask, redirect,url_for, request, render_template, jsonify
import pickle
import pafy
import os
import subprocess
from pydub import AudioSegment 
from pydub.utils import make_chunks

app=Flask(__name__)
## Load the model
model = pickle.load(open('mlmodel.pkl', 'rb'))

@app.route('/')
def home():
    name=""
    return render_template("home.html", transcription=name)

@app.route('/', methods=['POST'])
def transcribe():
    #Getting URL from frontend
    url = request.form['url']
    
    #downloading audio
    video = pafy.new(url)
    audiostreams = video.audiostreams
    for a in audiostreams:
        if(a.extension == "m4a"):
            a.download()
            
    #Converting audio from m4a to mp3
    for i in os.listdir("./"):
        if i.endswith('.m4a'):
            CurrentFileName = i
            FinalFileName = 'audio.mp3'
            subprocess.call(['ffmpeg', '-i', f'{CurrentFileName}', f'{FinalFileName}'])
            os.remove("./"+i)

    #Splitting audio into 30 sec file for transcription
    myaudio = AudioSegment.from_file("audio.mp3", "mp3") 
    chunk_length_ms = 30000 # pydub calculates in millisec 
    chunks = make_chunks(myaudio,chunk_length_ms) #Make chunks of one sec 
    for i, chunk in enumerate(chunks): 
        chunk_name = './testing/' +"{0}.mp3".format(i) 
        print ("exporting", chunk_name) 
        chunk.export(chunk_name, format="mp3")
    
    #Transcripting the audio files
    audioFiles = os.listdir('testing/')
    transcript = ""
    model = pickle.load(open('mlmodel.pkl', 'rb'))
    for files in audioFiles:
        audio = 'testing/'+files
        result = model.transcribe(audio,fp16=False)
        transcript+=result['text']
    
    #Removing the files from directory
    for i in os.listdir("./testing/"):
        os.remove("./testing/"+i)
    os.remove("./"+"audio.mp3")
    
    print(transcript)
    return render_template("home.html", transcription="Transcription is : {}".format(transcript))

    
@app.route("/<usr>")
def user(usr):
    audioFiles = os.listdir('testing/')
    transcript = ""
    for files in audioFiles:
        model = pickle.load(open('mlmodel.pkl', 'rb'))
        audio = 'testing/'+files
        result = model.transcribe(audio,fp16=False)
        transcript+=result['text']
    print(transcript)
    return f"<h1>{transcript}</h1>"

if __name__=="__main__":
    app.run(debug=True)