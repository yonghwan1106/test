import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.set_page_config(page_title="Relationship between Precipitation and Crop Production", layout="wide")
    
    # Data preparation
    rice_data = pd.DataFrame([
        {"precipitation": 1204, "production": 12802, "crop": "Rice"},
        {"precipitation": 1082, "production": 10814, "crop": "Rice"},
        {"precipitation": 1548, "production": 10688, "crop": "Rice"},
        {"precipitation": 1570, "production": 9250, "crop": "Rice"},
        {"precipitation": 1802, "production": 9001, "crop": "Rice"},
        {"precipitation": 1392, "production": 12611, "crop": "Rice"},
        {"precipitation": 1529, "production": 11165, "crop": "Rice"},
    ])
    potato_data = pd.DataFrame([
        {"precipitation": 1204, "production": 29342, "crop": "Potato"},
        {"precipitation": 1082, "production": 27763, "crop": "Potato"},
        {"precipitation": 1548, "production": 27808, "crop": "Potato"},
        {"precipitation": 1570, "production": 29148, "crop": "Potato"},
        {"precipitation": 1802, "production": 17272, "crop": "Potato"},
        {"precipitation": 1392, "production": 25716, "crop": "Potato"},
        {"precipitation": 1529, "production": 26726, "crop": "Potato"},
    ])

    # Create graph
    fig, ax = plt.subplots(figsize=(8, 8))  # Square shape
    ax.scatter(rice_data["precipitation"], rice_data["production"], label="Rice", color="blue")
    ax.scatter(potato_data["precipitation"], potato_data["production"], label="Potato", color="green")
    
    ax.set_xlabel("Precipitation (mm)")
    ax.set_ylabel("Production (ton)")
    ax.set_title("Relationship between Precipitation and Crop Production")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Adjust plot limits for better visualization
    ax.set_xlim(1000, 1900)
    ax.set_ylim(5000, 32000)

    # Streamlit application
    st.title("Relationship between Precipitation and Crop Production")
    
    # Display graph
    st.pyplot(fig)
    
    # The rest of your code remains the same
    # ...

if __name__ == "__main__":
    main()
