import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from PIL import Image, ImageDraw, ImageFont

def create_plot():
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
    ax.scatter(rice_data["precipitation"], rice_data["production"], label="Rice", color="blue")
    ax.scatter(potato_data["precipitation"], potato_data["production"], label="Potato", color="green")
    
    ax.set_xlabel("Precipitation (mm)")
    ax.set_ylabel("Production (ton)")
    ax.set_title("Relationship between Precipitation and Crop Production")
    ax.legend()

    # 그래프를 이미지로 저장
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    return Image.open(img_buf)

def add_korean_text(image, text, position, font_size=20, color=(0, 0, 0)):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
    draw.text(position, text, font=font, fill=color)

def main():
    st.set_page_config(page_title="강수량과 작물 생산량의 관계", layout="wide")
    
    # 영어로 된 그래프 생성
    plot_image = create_plot()
    
    # 한글 텍스트 추가
    add_korean_text(plot_image, "강수량과 작물 생산량의 관계", (150, 10), font_size=30)
    add_korean_text(plot_image, "강수량 (mm)", (400, 550), font_size=20)
    add_korean_text(plot_image, "생산량 (톤)", (10, 250), font_size=20, color=(0, 0, 0))
    add_korean_text(plot_image, "미곡", (750, 100), font_size=16, color=(0, 0, 255))
    add_korean_text(plot_image, "서류", (750, 130), font_size=16, color=(0, 128, 0))
    
    # 이미지 표시
    st.image(plot_image, use_column_width=True)

if __name__ == "__main__":
    main()
