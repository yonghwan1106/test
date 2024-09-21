import streamlit as st
import pandas as pd
import plotly.express as px

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

    data = pd.concat([rice_data, potato_data])

    # Create graph
    fig = px.scatter(data, x="precipitation", y="production", color="crop",
                     labels={"precipitation": "Precipitation (mm)", 
                             "production": "Production (ton)", 
                             "crop": "Crop Type"},
                     title="Relationship between Precipitation and Crop Production")

    # Streamlit application
    st.title("Relationship between Precipitation and Crop Production")
    
    # Display graph
    st.plotly_chart(fig, use_container_width=True)
    
    # Add legend explanation
    st.markdown("**Legend:**")
    st.markdown("- Rice: Blue")
    st.markdown("- Potato: Red")
    
    # Add axis explanation
    st.markdown("**X-axis:** Precipitation (mm)")
    st.markdown("**Y-axis:** Production (ton)")

    # Add analysis
    st.subheader("Analysis:")
    st.write("""
    1. Rice production seems to have a slight negative correlation with precipitation. As precipitation increases, there's a slight tendency for rice production to decrease.
    
    2. Potato production shows a more pronounced negative correlation with precipitation. There's a clear trend of decreasing potato production as precipitation increases.
    
    3. The highest potato production occurs at lower precipitation levels (around 1200-1400 mm), while the lowest production is at the highest precipitation level (around 1800 mm).
    
    4. Rice production appears more stable across different precipitation levels compared to potato production.
    
    5. The data suggests that excessive precipitation might be more detrimental to potato crops than to rice crops in this region.
    """)

    st.subheader("Conclusions:")
    st.write("""
    - Potato farming in this region might benefit from better drainage systems to manage high precipitation levels.
    - Rice farming appears more resilient to precipitation changes, but there's still a slight negative impact from increased rainfall.
    - For both crops, but especially for potatoes, it might be beneficial to develop varieties that are more tolerant to high precipitation.
    - Agricultural policies and support systems should consider these precipitation-production relationships when planning for climate change adaptation.
    """)

if __name__ == "__main__":
    main()
