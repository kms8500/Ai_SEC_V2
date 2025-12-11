
#저장된 모델의 예측값 출력
import os
from movie_review.Naver_NLP_Train import MAX_TOKENS
import matplotlib.pyplot as plt
import pickle
import numpy as np
from konlpy.tag import Okt
import re

PATH=r"movie_review/"
#PATH=r"./"
import tensorflow as tf
print(tf.__version__)
#모델생성
model = None
MAX_TOKENS=0
MAX_LEN=0
VOCAB=None
#가중치 셋팅
#print(model.get_weights()[:5])
print("😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘")
if os.path.exists(f"{PATH}config/nlp_model.keras"):
    configs = None
    with open(f"{PATH}config/config","rb") as fp:
        configs = pickle.load(fp)
    print(configs)
    MAX_TOKENS=configs["max_tokens"]
    MAX_LEN=configs["max_len"]
    print(configs)
    VOCAB = configs["vocab"]
    print(os.path.exists(f"{PATH}config/nlp_model.keras"))
    model=tf.keras.models.load_model(
        f"{PATH}config/nlp_model.keras")
    model.summary()
    plt.show()
    #레이어 이름도 동일해야합니다.
    #model.load_weights(f"{PATH}config/naver_move_npl.weights.h5")
    #print(model.get_weights()[:5])
#사전설정
tv = tf.keras.layers.TextVectorization(
    max_tokens=MAX_TOKENS,#사전크기
    output_mode='int',
    pad_to_max_tokens=True,
    output_sequence_length=MAX_LEN,#전체문장의 길이, 자동패딩과 스피릿
)
tv.set_vocabulary(VOCAB)
def get_userData(user_data):# 이 영화는 너무 재밌어
    # 정규식 전환, 불용어처리/형태소분류, 숫자변환(Tokenizer-vocab)
    reg_han = r"[^\sㄱ-ㅎ가-힣]"
    user_data = re.sub(reg_han,"",user_data)
    #user_data.replace(to_replace=reg_han, regex=True, inplace=True, value="")
    if not user_data :
        print("좀 더 명확한 입력을 해주세요")
    stopword = ["에서", "은", "는", "이", "가", "이다", "하다", "들", "좀", "걍", "도", "요",
                "흠", "에게", "나다", "데", "있다", "해도", "에", "의", "을", "를", "다", "한",
                "것", "내", "그", "나"]
    # 나중에 단어 출현 횟수에 따라 의미없는 단어는 추가하여 다시 제거를 하는게 좋다.
    print("한글 형태소 분리 실행")
    okt = Okt()
    x_user = []
    token_word = okt.morphs(user_data, stem=True)  # 리턴값 : 단어 리스트
    x_user.append(" ".join([w for w in token_word if not w in stopword]))
    x_user = np.array(x_user)
    return x_user
def vocab_process(x_user):
    global tv
    return tv(x_user)
def predict_userdata(x_user):
    global model
    return model.predict(x_user)
if __name__=="__main__":
    x_user = get_userData("영화 너무너무 재밌네 개나 줘버려")
    x_user = vocab_process(x_user)
    print(predict_userdata(x_user))

