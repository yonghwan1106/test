import streamlit as st
import graphviz

def create_tree():
    # Graphviz 객체 생성
    graph = graphviz.Digraph()
    graph.attr(rankdir='LR')

    # 노드 추가
    graph.node('root', '작물별 맞춤형 재배 가이드라인')
    
    graph.node('rice', '미곡')
    graph.node('rice1', '강수량 증가 대응')
    graph.node('rice2', '고온 스트레스 관리')

    graph.node('potato', '서류')
    graph.node('potato1', '과다 강수 대비 배수 관리')
    graph.node('potato2', '병해충 예방')

    graph.node('common', '공통')
    graph.node('common1', '기상 예측 정보 활용')
    graph.node('common2', '농가 규모별 전략')

    # 엣지 추가
    graph.edge('root', 'rice')
    graph.edge('rice', 'rice1')
    graph.edge('rice', 'rice2')

    graph.edge('root', 'potato')
    graph.edge('potato', 'potato1')
    graph.edge('potato', 'potato2')

    graph.edge('root', 'common')
    graph.edge('common', 'common1')
    graph.edge('common', 'common2')

    return graph

st.title('작물별 맞춤형 재배 가이드라인')

# 트리 생성 및 표시
tree = create_tree()
st.graphviz_chart(tree)
