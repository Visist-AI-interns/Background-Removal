import streamlit as st

def main():
    st.title("Video File Upload")
    
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov", "mkv", "flv", "wmv"])
    
    if uploaded_file is not None:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        
        # Display file details
        st.write("File details:")
        st.write({
            "Filename": uploaded_file.name,
            "File Type": uploaded_file.type,
            "File Size": uploaded_file.size,
        })

if __name__ == "__main__":
    main()