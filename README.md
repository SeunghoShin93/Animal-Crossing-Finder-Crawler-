# Animal Crossing Finder (Crawler)

## 프로젝트 소개

닌텐도 스위치 동물의 숲 에디션을 파는 쇼핑몰을 크롤링하여 재고 여부를 알려줍니다.



## 개발 배경

### 닌텐도 스위치 동물의 숲 에디션이 갖고 싶었다. 

그러나 수요에 비해 공급은 터무니 부족했고, 정해진 시간에 물량을 푸는 오픈 마켓은 대기자가 너무 많다.

게릴라 성으로 갑자기 물건을 푸는 사이트에 기대해야하는 상황이지만,

하루종일 새로고침만 누르고 있을 순 없는 노릇이기에 직접 사용하기 위해 개발했다.



## Getting Started

- pip upgrade
- pip install -r requirements.txt
- 사용하는 chrome 버전에 맞춰 chromedriver 다운로드 - https://chromedriver.chromium.org/downloads



## 기술 스택

- Selenium
- pygame



## 동작 원리

- `python ds_finder.py` 로 실행

- 사이트 별 재고 풀리는 걸 캐치
  - pygame의 mixer로 음악을 재생하여 사용자에게 구매 가능 여부를 알린다.
  - 콘솔에 재고가 풀린 사이트를 print
  - 사용자는 알림을 듣고 콘솔을 보고 재빠르게 해당 사이트에서 구매
- 재고 없음 미 변동시
  - 크롤링 과정 반복
- `ctrl+l` 명령어로 끄지 않는 이상 상기 과정 반복

## 지원하는 사이트 목록

- 소프라노
- 조이트론 스토어 (네이버 스마트 스토어)
- 엔엔마켓

- cjmall (분리)
  - 인질
  - 단품 

2020-05-15 13:11 기준 5개