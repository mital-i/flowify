import pathlib
import google.generativeai as genai
import PIL.Image

def authenticate():
    GOOGLE_API_KEY='AIzaSyAHXrT0Bo4bqDtWDTGZSsWp_e4m3cpo9yQ'
    genai.configure(api_key=GOOGLE_API_KEY) 

def fetch_songs():
    img = PIL.Image.open('beach.jpeg')
    model = genai.GenerativeModel('gemini-pro-vision')

    response = model.generate_content(["Analyze the setting, emotions, and vibe of the image. Suggest ten songs that match the energy and feeling of the image.", img], stream=True)
    response.resolve()

    text = response.text

    for line in text:
        print(line)

def run():
    authenticate()
    songs = fetch_songs()

run()