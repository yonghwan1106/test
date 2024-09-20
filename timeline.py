import streamlit as st

st.markdown("""
<style>
.timeline-item {
    border-left: 2px solid #4CAF50;
    padding-left: 20px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

def timeline(items):
    for i, item in enumerate(items):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.write(f"### 단계 {i+1}")
        with col2:
            st.write(f"### {item['title']}")
            for task in item['tasks']:
                st.write(f"- {task}")
        if i < len(items) - 1:
            st.write("---")

def main():
    st.title("가이드라인 구현 타임라인")

    timeline_data = [
        {
            "title": "기획 및 팀 구성",
            "tasks": [
                "프로젝트 계획 수립",
                "전문가 팀 구성",
                "유관 기관 협력 체계 구축"
            ]
        },
        {
            "title": "데이터 수집 및 모델 개발",
            "tasks": [
                "기상 및 농업 데이터 수집",
                "AI 기반 예측 모델 개발",
                "작물별 최적 조건 DB 구축"
            ]
        },
        {
            "title": "시스템 구축 및 시범 운영",
            "tasks": [
                "의사결정 지원 시스템 개발",
                "시범 농가 선정 및 적용",
                "사용자 피드백 수렴"
            ]
        },
        {
            "title": "전면 도입 및 지속적 개선",
            "tasks": [
                "전체 농가 대상 서비스 확대",
                "지속적인 데이터 업데이트",
                "시스템 고도화"
            ]
        }
    ]

    timeline(timeline_data)

if __name__ == "__main__":
    main()
