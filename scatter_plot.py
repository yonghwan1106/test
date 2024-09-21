import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

def main():
    st.set_page_config(page_title="강수량과 작물 생산량의 관계", layout="wide")
    st.title("강수량과 작물 생산량의 관계")

    # 데이터 준비
    rice_data = pd.DataFrame([
        {"precipitation": 1204, "production": 12802, "crop": "미곡"},
        {"precipitation": 1082, "production": 10814, "crop": "미곡"},
        {"precipitation": 1548, "production": 10688, "crop": "미곡"},
        {"precipitation": 1570, "production": 9250, "crop": "미곡"},
        {"precipitation": 1802, "production": 9001, "crop": "미곡"},
        {"precipitation": 1392, "production": 12611, "crop": "미곡"},
        {"precipitation": 1529, "production": 11165, "crop": "미곡"},
    ])

    potato_data = pd.DataFrame([
        {"precipitation": 1204, "production": 29342, "crop": "서류"},
        {"precipitation": 1082, "production": 27763, "crop": "서류"},
        {"precipitation": 1548, "production": 27808, "crop": "서류"},
        {"precipitation": 1570, "production": 29148, "crop": "서류"},
        {"precipitation": 1802, "production": 17272, "crop": "서류"},
        {"precipitation": 1392, "production": 25716, "crop": "서류"},
        {"precipitation": 1529, "production": 26726, "crop": "서류"},
    ])

    # 그래프 생성
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(rice_data["precipitation"], rice_data["production"], label="미곡", color="blue")
    ax.scatter(potato_data["precipitation"], potato_data["production"], label="서류", color="green")
    
    ax.set_xlabel("강수량 (mm)")
    ax.set_ylabel("생산량 (톤)")
    ax.set_title("강수량과 작물 생산량의 관계")
    ax.legend()

    # 그래프 표시
    st.pyplot(fig)

if __name__ == "__main__":
    main()
