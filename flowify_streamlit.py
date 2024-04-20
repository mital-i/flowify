import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""") 

def main():
  uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
  # ... rest of your app logic using the uploaded_file object
  if uploaded_file is not None:
    filename = uploaded_file.name
    file_type = uploaded_file.type
    file_size = uploaded_file.size
    st.write(f"Filename: {filename}")
    st.write(f"File type: {file_type}")
    st.write(f"File size: {file_size} bytes")
  
if __name__ == "__main__":
  main()
