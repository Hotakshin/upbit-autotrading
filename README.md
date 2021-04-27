# upbit-autotrading

by 유튜브 조코딩 채널

pyupbit 라이브러리를 활용하여 upbit 거래소에서 비트코인 자동매매를 하는 코드입니다.
파일 구성
test.py : 잔고 조회 
backtest.py : 백테스팅 코드
bestK.py : 가장 좋은 k 값을 찾는 코드 
bitcoinAutoTrade.py : 변동성 돌파 전략 비트코인 자동매매 코드
참고 문헌: https://wikidocs.net/book/1665
Ubuntu 서버 명령어
(*추가)한국 기준으로 서버 시간 설정: sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
현재 경로 상세 출력: ls -al
경로 이동: cd 경로
vim 에디터로 파일 열기: vim bitcoinAutoTrade.py
vim 에디터 입력: i
vim 에디터 저장: :wq!
패키지 목록 업데이트: sudo apt update
pip3 설치: sudo apt install python3-pip
pip3로 pyupbit 설치: pip3 install pyupbit
백그라운드 실행: nohup python3 bitcoinAutoTrade.py > output.log &
실행되고 있는지 확인: ps ax | grep .py
프로세스 종료(PID는 ps ax | grep .py를 했을때 확인 가능): kill -9 PID
