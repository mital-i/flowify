import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")

def main():
  uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
  # ... rest of your app logic using the uploaded_file object
  
if __name__ == "__main__":
  main()