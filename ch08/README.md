# Algorithmic Trading for Quantitative Strategies



-----------------


## 8장 주요 내용
딥러닝을 활용한 데이터 분석.

 - [CNN](https://github.com/quant4junior/algoTrade/tree/master/ch08/8.1%20CNN%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EC%BA%94%EB%93%A4%EC%B0%A8%ED%8A%B8%20%EC%98%88%EC%B8%A1%EB%B6%84%EC%84%9D)

 - [RNN](https://github.com/quant4junior/algoTrade/tree/master/ch08/8.2%20RNN%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EC%A3%BC%EA%B0%80%20%EB%B0%A9%ED%96%A5%EC%84%B1%20%EB%B6%84%EB%A5%98%20%EC%98%88%EC%B8%A1)

 - [AutoEncoder](https://github.com/quant4junior/algoTrade/tree/master/ch08/8.3%20%EC%98%A4%ED%86%A0%EC%9D%B8%EC%BD%94%EB%8D%94%EB%A5%BC%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EC%A3%BC%EA%B0%80%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%83%9D%EC%84%B1)


 ## 아나콘다를 이용한 환경 설정 방법.


* 파이썬 3.6버전 가상환경 만들기.
```sh
(base)conda create -n py36 python=3.6
```
* 가상환경 활성화
```sh
(base)activate py36
```

* 패키지 설치하기.
```sh
(py36) pip install -r requirements.txt
```

* (TIP) 패키지 내보내기.

```sh
(py36) pip freeze > requirements.txt
```

## 사용하는 딥러닝 버전.

 - tensorflow==1.15.0
 - Keras==2.2.4



## 참고.

 - [Using Deep Learning Neural Networks and Candlestick Chart Representation to Predict Stock Market](https://github.com/jason887/Using-Deep-Learning-Neural-Networks-and-Candlestick-Chart-Representation-to-Predict-Stock-Market)
 - [Application of Deep Learning to Algorithmic Trading](http://cs229.stanford.edu/proj2017/final-reports/5241098.pdf)
 - [Autoencoders for the compression of stock market time series](https://towardsdatascience.com/autoencoders-for-the-compression-of-stock-market-data-28e8c1a2da3e)
 
