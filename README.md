## Youtube Transcriber

YouTube Transcriber is a web application that transcribes YouTube videos into text. It is built with Python, Flask.

The transcriber uses the **Audio-wizard** model that I trained based on [deep-speech-2](https://arxiv.org/abs/1512.02595) paper.

You can find more details about the model [here.](https://github.com/Msparihar/deep-speech-2) 

To use the application, simply enter the URL of the YouTube video you want to transcribe and click the "Transcribe" button. The application will then generate a transcript of the video, which you can then download or copy and paste into another document.

YouTube Transcriber is a useful tool for anyone who wants to make their YouTube videos more accessible to a wider audience, or who needs to transcribe YouTube videos for research or other purposes.

**Here are some of the benefits of using YouTube Transcriber:**

* Make your YouTube videos more accessible to viewers with hearing disabilities
* Improve the SEO of your YouTube videos by making them easier to search for
* Create transcripts of your YouTube videos for blogging, research, or other purposes
* Easily share transcripts of your YouTube videos on social media or other websites

**Try YouTube Transcriber today and see how easy it is to transcribe your YouTube videos into text!**

### Software and Tools Requirements

1. [Github Account](https://github.com/)
2. [Heroku Account](https://heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

### Step 1: Create a new environment
```
conda create -p venv python==3.10 -y
```

### Step 2: Activate Environment
```
conda activate venv/
```

### Step 3: Install dependencies
```
pip install -r requirements.txt
```

### Step 4: Run the application
```
flask run app.py
```
