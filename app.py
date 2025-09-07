import streamlit as st
from myapp import run_app  # Comes from private repo

def main():
    st.title("Welcome to My Streamlit App")
    run_app.run_app()

if __name__ == "__main__":
    main()
