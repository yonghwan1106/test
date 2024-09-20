import streamlit as st
import pandas as pd
import plotly.express as px

def main():
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

    # 데이터 합치기
    data = pd.concat([rice_data, potato_data])

    # 산점도 생성
    fig = px.scatter(data, x="precipitation", y="production", color="crop",
                     labels={"precipitation": "강수량 (mm)", 
                             "production": "생산량 (톤)", 
                             "crop": "작물"},
                     title="강수량과 작물 생산량의 관계")

    # 그래프 표시
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
