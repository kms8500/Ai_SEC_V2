# AI_SEC_V2
## 인공지능솔루션 적대적공격 위협 분석 AI보안 전문가   
### 1. 인공지능 분야 : 선형회귀  (Boston Housing Regression)
####  데이터 - 보스턴 주택 평균가격  
####  <데이터 정의>
<pre>
    CRIM 도시별 1인당 범죄율  
    ZN: 25,000제곱피트(약 2만 5천 제곱피트) 이상 면적의 주거용 토지 비율  
    INDUS: 도시별 비소매업용 에이커(약 1,000에이커) 비율  
    CHAS: 찰스 강 더미 변수(= 해당 구역이 강 경계에 있는 경우 1, 그렇지 않은 경우 0)  
    NOX: 일산화질소 농도(1,000만 분의 1)  
    RM: 가구당 평균 방 개수  
    AGE: 1940년 이전에 지어진 자가 주택 비율  
    DIS: 보스턴 5개 고용 센터까지의 가중 거리  
    RAD: 방사형 고속도로 접근성 지수  
    TAX: 1만 달러당 재산세 전액 세율  
    PTRATIO: 도시별 교사-학생 비율  
    B 1000(Bk - 0.63)^2, 여기서 Bk는 도시별 흑인 비율  
    LSTAT: 인구 하위 계층 비율(%)

    정답 :MEDV: 자가 주택의 중간 가격(1,000달러대)    
</pre>
####  <개발 도구>
<pre>   google Colab editor, Keras tensorflow, numpy, matplotlib </pre>  
#### <훈련순서>  
<pre>
     1. 데이터 수집  
     2. 데이터 분석  
     3. 데이터 전처리  
     4. 순차모델 구성  
     5. 훈련결과 시각화  
     6. 정확률 시각화  
     7. 정확률 수치화  
</pre>

### 2. 프로젝트 : 다중선형회귀  (가상화폐 가격예측 실전 분석)
####  데이터 - 현재시간의 가상화폐 데이터 200여개 추출 및 시계열 데이터 변환 
####  <데이터 정의>
<pre>
    time_step(간격)별 최고가
    time_step(간격)별 최저가
    time_step(간격)별 현재가
</pre>
####  <개발 kit>
<pre>   개발언어 : python 3.9
        개발도구 : jupyter notebook, pycharm GUI, python 3.9
        주요라이브러리 : tensorflow 2.10, falsk 3.12 scikit-learn 1.6.1 keras 2.10.0 numpy1.26.4 matplot 3.9.4

</pre>  

#### <Package Structure>  
<pre>
    Crypto_Coin_Service_02 
	root directory : ai_service, static, templates
	root file : Web_Service_AI.py (Web Routing) 
</pre>

#### <directory structure>  
   ai_service 
<pre>
      - coin_config 저장된 모델과 에러율 및 스케일러
	  - Crypto_Coin_Predict.py (모델 예측 관련 서비스)
	  - Crypto_Coin_Service.py (미들웨어 서버와 연동되는 서비스)
	  - Crypto_Coin_Train.py (데이터 전처리와 모델 생성 및 훈련 저장)
</pre>
    Static
<pre>
      - chart (훈련결과 그래프 저장)
	  - css (client service 화면 서식)
	  - js (client service 화면 컨트롤러)
	  - img (client service 요구 이미지)
</pre>
    templates
<pre>
	  - html (client service 화면 구조)
</pre>

#### <훈련순서>  
<pre>
     1. 데이터 수집  
     2. 데이터 분석  
     3. 데이터 전처리  
     4. 순차모델 구성  
     5. 훈련결과 시각화  
     6. 정확률 시각화  
     7. 정확률 수치화 
     8. 예측함수 작성
     9. 웹서비스연동 모듈
     10. 웹서버
     11. 클라이언트 구현
</pre>
