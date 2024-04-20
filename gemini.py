import google.generativeai as genai

def authenticate():
    GOOGLE_API_KEY='AIzaSyAHXrT0Bo4bqDtWDTGZSsWp_e4m3cpo9yQ'
    genai.configure(api_key=GOOGLE_API_KEY) 

def generate_response():
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Write a story about a magic backpack.")
    print(response.text)

def run():
    authenticate()
    generate_response()

run()