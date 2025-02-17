# 선형회귀(Linear Regression)

- 지도학습의 한 종류
- Regression중 가장 간단한 방법
- 결과값이 실수로 나옴
- x -> y의 관계를 가지고 예측

### 수식

##### (선형회귀)Linear Regression

- 선형 회귀의 결과값은 실수로 나타나며 input 값에 대해 다음과 같은 선형 함수로 나타낼 수 있다.

  <img src="https://render.githubusercontent.com/render/math?math=y(x)=w^Tx %2B \epsilon">

  <img src="https://render.githubusercontent.com/render/math?math=w^T">의 기울기를 가지고 <img src="https://render.githubusercontent.com/render/math?math=\epsilon">의 절편을 가진다.

- 이 때, <img src="https://render.githubusercontent.com/render/math?math=\epsilon">(the residual error)은 Gaussian distribution을 따른다고 가정하면

  <img src="https://render.githubusercontent.com/render/math?math=p(y|\theta) = \mathcal{N}(y|u(x), \sigma^2(x))">

- where

  <img src="https://render.githubusercontent.com/render/math?math=u(x) = w^Tx = w_0 %2B w_1x">

##### Modeling non-linear relationships

- Simply Take

  <img src="https://render.githubusercontent.com/render/math?math=p(y|x, \theta) = \mathcal{N}(y|w^Tx, \sigma^2)">

- and replace <img src="https://render.githubusercontent.com/render/math?math=x"> with some non-linear function of the inputs

  <img src="https://render.githubusercontent.com/render/math?math=p(y|x, \theta) = \mathcal{N}(y|w^T\phi(x), \epsilon^2)">	ex) <img src="https://render.githubusercontent.com/render/math?math=\phi(x) = x^2, \phi(x) = 2x %2B 3x^2">

  this is called the basis function expansion.

  이 경우에도 여전히 Linear Regression 이라고 불린다. 왜냐하면 Parameter <img src="https://render.githubusercontent.com/render/math?math=w">에 대해 선형이기 때문이다. <img src="https://render.githubusercontent.com/render/math?math=w(x %2B x^2) = wx %2B wx^2"> 라는 의미.

- Polynomial Regression

  <img src="https://render.githubusercontent.com/render/math?math=x, x^2, x^n...">

- Multivariate linear regression

  <img src="https://render.githubusercontent.com/render/math?math=w_0 %2B w_1x_1 %2B w_2x_2, w_0 %2B w_1x_1 %2B w_2x_2 %2B w_3x_1^2 %2B w_4x_2^2 ...">

##### Maximum likelihood estimation(MLE)

- Using MLE, arguments  <img src="https://render.githubusercontent.com/render/math?math=\theta"> can be computed by

  <img src="https://render.githubusercontent.com/render/math?math=$arg \space \space max \space\space logp(D|\theta)=\sum_{i=1}^N logp(y_i|x_i, \theta)$">

- if we plug in the Gaussian formulation

  <img src="https://render.githubusercontent.com/render/math?math=$p(y|x, \theta) = \mathcal{N}(y|w^Tx, \sigma^2)$">

  and put it into the log likelihood above, we get

  <img src="https://render.githubusercontent.com/render/math?math=$=\sum_{i=1}^N log[(\frac{1}{2\pi\sigma^2})^{\frac{1}{2}}exp(-\frac{1}{2\sigma^2}(y_i-w^Tx_i)^2)]$">

  <img src="https://render.githubusercontent.com/render/math?math=$=-\frac{N}{2}log(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1}^N(y_i - w^Tx_i)^2$">

  and **Negative log likelihood (NLL)** is

  <img src="https://render.githubusercontent.com/render/math?math=$\frac{N}{2}log(2\pi\sigma^2) %2B \frac{1}{2\sigma^2}\sum_{i=1^N}(y_i - w^Tx_i)^2$">

  

- To **minimize NLL**, we minimize this term

  <img src="https://render.githubusercontent.com/render/math?math=$\sum_{i=1}^N(y_i - w^Tx_i)^2$">

  called **residual sum of squares(RSS)**

- RSS를 통해 NLL을 최소화 하는 것이 가장 최적화된 regression이 된다.

##### Ridge Regression

- MLE can overfit

  - For linear regression, this means the weight can become large

  - We can encourage the weights to be small by putting a zero-mean Gaussian prior on the weights

    <img src="https://render.githubusercontent.com/render/math?math=- l_2">**Regularization**(<img src="https://render.githubusercontent.com/render/math?math=\lambda||w||^2">를 이용하는 Regularzation)

- Zero-mean Gaussian prior on the weights

  <img src="https://render.githubusercontent.com/render/math?math=$p(w) = \prod_j \mathcal{N}(w_j|0, \tau^2)$">

- MAP estimation problem

  $argmax \sideset{}{_{i=1}^Nlog(y_i|w_0 +w^Tx_i, \sigma^2)}\sum + \sideset{}{j_i^D logN(w_j|0, \tau^2)}\sum$

  <img src="https://render.githubusercontent.com/render/math?math=$argmax \sum_{i=1}^N log\mathcal{N}(y_i|w_0 %2B w^Tx_i, \sigma^2) %2B \sum_{j_i}^D logN(w_j|0, \tau^2)$">

- Compare with the MLE problem

  <img src="https://render.githubusercontent.com/render/math?math=$arg \space \space max \space\space logp(D|\theta)=\sum_{i=1}^N logp(y_i|x_i, \theta)$">

- To solve the MAP estimation, minimize

  <img src="https://render.githubusercontent.com/render/math?math=$J(w) = \frac{1}{N}\sum_{i=1}^N (y_i-(w_0+w^Tx_i))^2 %2B \lambda||w||_2^2$">

- Compare with NLL Before

  <img src="https://render.githubusercontent.com/render/math?math=$\sum_{i=1}^N(y_i - w^Tx_i)^2$">

- So the first term of ridge regression is same as NLL, and the second term is the complexity penalty (when <img src="https://render.githubusercontent.com/render/math?math=\lambda > 0" >)

- Corresponding solution is

  <img src="https://render.githubusercontent.com/render/math?math=$\hat{w}_{ridge} = (\lambda I_D %2B X^TX)^{-1}X^Ty$" >

  <img src="https://render.githubusercontent.com/render/math?math=$\hat{w}_{OLS} = (X^TX)^{-1}X^Ty$" >

- Regularization effects of big data

  - 데이터가 많아질 수록 Regularization 효과를 볼 수있다.
  - = 그래프가 부드러워짐

#### Regression 모델 평가하기

- test case와 past case의 오차 정도를 본다.
  - 둘다 너무 오차가 크다.
    - 모델 설계가 잘못
  - n이 작을 때 past case에 대해 오차가 적고 test case에 대해 약간의 오차를 보인다. n이 커질 수록 개선된다.
    - 설계 잘했다
  - n이 작을때 past case에 대해 오차가 거의없고 test case에 대해 큰 오차를 보인다. n이 커질수록 개선되지만 그래프가 가파르다.
    - Overfitting 이다.
    - = 불필요하게 complex
    - 하지만 n이 커지면 어느정도 유효한 모델이다.
  - n이 적당히 커졌음에도 past case에 대해서만 오차가적고 test case에 대해 오차가 크다.
    - 심하게 Overfitting 되어서 유효하지 않은 모델이다.