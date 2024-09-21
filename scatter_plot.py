import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy import stats

# 데이터 준비
rice_data = pd.DataFrame([
    {"precipitation": 1204, "production": 12802},
    {"precipitation": 1082, "production": 10814},
    {"precipitation": 1548, "production": 10688},
    {"precipitation": 1570, "production": 9250},
    {"precipitation": 1802, "production": 9001},
    {"precipitation": 1392, "production": 12611},
    {"precipitation": 1529, "production": 11165},
])

potato_data = pd.DataFrame([
    {"precipitation": 1204, "production": 29342},
    {"precipitation": 1082, "production": 27763},
    {"precipitation": 1548, "production": 27808},
    {"precipitation": 1570, "production": 29148},
    {"precipitation": 1802, "production": 17272},
    {"precipitation": 1392, "production": 25716},
    {"precipitation": 1529, "production": 26726},
])

def create_regression_line(data):
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['precipitation'], data['production'])
    line = slope * data['precipitation'] + intercept
    return line, r_value**2

def main():
    st.title("Relationship between Precipitation and Crop Production")

    # 대화형 요소: 작물 선택
    crops = st.multiselect(
        "Select crops to display",
        ["Rice", "Potato"],
        default=["Rice", "Potato"]
    )

    # 그래프 생성
    fig = go.Figure()

    if "Rice" in crops:
        rice_line, rice_r2 = create_regression_line(rice_data)
        fig.add_trace(go.Scatter(
            x=rice_data['precipitation'], y=rice_data['production'],
            mode='markers', name='Rice', marker=dict(color='blue', size=10)
        ))
        fig.add_trace(go.Scatter(
            x=rice_data['precipitation'], y=rice_line,
            mode='lines', name=f'Rice Trend (R²: {rice_r2:.3f})', line=dict(color='blue', dash='dash')
        ))

    if "Potato" in crops:
        potato_line, potato_r2 = create_regression_line(potato_data)
        fig.add_trace(go.Scatter(
            x=potato_data['precipitation'], y=potato_data['production'],
            mode='markers', name='Potato', marker=dict(color='green', size=10)
        ))
        fig.add_trace(go.Scatter(
            x=potato_data['precipitation'], y=potato_line,
            mode='lines', name=f'Potato Trend (R²: {potato_r2:.3f})', line=dict(color='green', dash='dash')
        ))

    fig.update_layout(
        xaxis_title="Precipitation (mm)",
        yaxis_title="Production (ton)",
        legend_title="Crop Type",
        width=800,
        height=600
    )

    st.plotly_chart(fig)

    # 분석 및 결론
    st.subheader("Analysis:")
    st.write("""
    1. The scatter plot shows the relationship between precipitation and crop production for rice and potatoes.
    2. Trend lines (dashed) indicate the general direction of the relationship for each crop.
    3. R² values show how well the trend lines fit the data (closer to 1 means a better fit).
    """)

    st.subheader("Conclusions:")
    st.write("""
    - Rice production seems less affected by precipitation changes (flatter trend line).
    - Potato production shows a more pronounced negative correlation with precipitation.
    - Higher precipitation levels appear to have a more detrimental effect on potato yields compared to rice.
    - These insights can inform agricultural strategies and crop selection based on expected precipitation levels.
    """)

if __name__ == "__main__":
    main()
