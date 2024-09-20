import React from 'react';
import { Tree } from 'react-tree-graph';

const data = {
  name: '작물별 맞춤형 재배 가이드라인',
  children: [
    {
      name: '미곡',
      children: [
        { name: '강수량 증가 대응' },
        { name: '고온 스트레스 관리' }
      ]
    },
    {
      name: '서류',
      children: [
        { name: '과다 강수 대비 배수 관리' },
        { name: '병해충 예방' }
      ]
    },
    {
      name: '공통',
      children: [
        { name: '기상 예측 정보 활용' },
        { name: '농가 규모별 전략' }
      ]
    }
  ]
};

const ClimateAdaptiveGuideline = () => (
  <div style={{ width: '100%', height: '300px' }}>
    <Tree
      data={data}
      height={300}
      width={400}
      svgProps={{
        transform: 'rotate(90)'
      }}
      textProps={{
        transform: 'rotate(-90)'
      }}
    />
  </div>
);

export default ClimateAdaptiveGuideline;
