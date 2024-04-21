import json
import google.generativeai as genai
import PIL.Image
from dotenv import load_dotenv
import os

def authenticate():
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')
    if api_key is None:
        raise ValueError("API_KEY environment variable not set!")

    genai.configure(api_key=api_key) 

def fetch_songs():
    img = PIL.Image.open('beach.jpeg')
    img_model = genai.GenerativeModel('gemini-pro-vision')

    img_response = img_model.generate_content(["Analyze the setting, emotions, and vibe of the image. Suggest ten songs that match the energy and feeling of the image. Output only the names and artists of the songs in this format: Song -> Artist", img], stream=True)
    img_response.resolve()

    model = genai.GenerativeModel('gemini-pro')

    songs = model.generate_content(f"""Given this string: '{img_response.text}', parse and output just the songs and artist names and store it into a dictionary. The json format must store the songs and artist names as strings with double quotes. Sample output format: {{
                                                "Some Beach": ["Blake Shelton"],
                                                "Soak Up the Sun": ["Sheryl Crow"],
                                                "Island in the Sun": ["Weezer"],
                                                "Walking on Sunshine": ["Katrina", "The Waves"],
                                                "Here Comes the Sun": ["The Beatles"],
                                                "Good Vibrations": ["The Beach Boys"],
                                                "California Gurls": ["Katy Perry"],
                                                "Summer Nights": ["Olivia Newton-John", "John Travolta"],
                                                "Dancing Queen": ["ABBA"],
                                                "Don't Stop Me Now": ["Queen"]
                                            }}""").text 
    start_idx = songs.index('{')
    end_idx =  songs.index('}')

    dict_obj = songs[start_idx:end_idx+1]
    song_to_artist = json.loads(dict_obj)

    return song_to_artist