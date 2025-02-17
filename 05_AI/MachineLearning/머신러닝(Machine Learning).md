# 머신러닝(Machine Learning)

규칙 기반 전문가 시스템(Rule-based Expert System)으로 지능형 애플리케이션을 만드는데 한계가 있었다.

결정에 필요한 로직이 바뀌면 시스템을 다시 개발해야했고, 로직을 설계하려면 그 분야 전문가들 수준의 지식이 필요했던것.

머신러닝은 사람이 생각하는 대로 로직을 짤 필요가 없기 때문에 규칙으로 표현하기 어려운 것들을 학습하는데 아주 좋다.

- **지도학습(Supervised Learning)**  : 이미 알려진 사례를 바탕으로 일반화된 모델을 만들어 결정 프로세스를 자동화 하는것.  입력값에 대한 기대되는 출력을 반복적으로 입력해 알고리즘을 학습시킨다. 학습된 알고리즘은 사람의 도움 없이도 입력값에 대해 적절한 출력을 만들 수 있다.입력과 출력데이터가 충분해야 하고 데이터가 없다면 데이터셋을 만드는데 시간이 많이 소요된다.분석하기에도 좋고 성능을 측정하기도 쉽다.

  ex)

  - 영상 이미지 기반의 종양판단
  - 손글씨로 쓴 숫자를 인식하는 것
  - 신용카드 거래내역 학습을 기반으로 한 의심되는 거래 감지

- **비지도학습(Unsupervised learning)** : 입력은 주어지지만 출력은 제공하지 않고 학습시키는 방법. 성공사례는 많지만 이해하거나 평가하기 쉽지않다. 
  - 글의 주제 구분
  - 고객 취향을 분석해 비슷한 그룹으로 묶기
  - 비정상적인 웹사이트 접근 탐지

머신러닝에서는 하나의 개체 혹을 행을 **샘플(Sample)** 또는 **데이터 포인트(Data Point)** 라고 한다. 샘플이 속성, 열을 **특성(Feature)** 이라고 한다.

  