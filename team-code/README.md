[← 프로젝트 메인](../README.md)

# team-code

대회 당시 전체 시스템을 실행한 팀 코드입니다. 번호판 인식부터 볼라드 제어까지 이 코드로 동작합니다.  
`client.py`의 `connect_to_database()` · `compare_license_plate()`와 `database.sql`은 안유빈이 작성했고, 나머지는 팀 공동 코드입니다.  
코드의 Wi-Fi 이름 · 비밀번호와 DB 비밀번호는 `YOUR_SSID` · `YOUR_PASSWORD` · `********`로 바꿔 두었습니다.

### 파일 구성

PC(`client.py`)가 ESP8266에서 초음파 거리를 받고, ESP32-CAM 사진으로 번호판을 인식해 DB와 비교한 뒤, ESP8266에 볼라드 · LED · 소리 제어를 요청합니다.

| 파일 | 실행 위치 | 내용 | 작성 |
|---|---|---|---|
| [`client.py`](client.py) | PC (Python) | 초음파 거리 확인 → 번호판 인식 → DB 비교 → 상태별 볼라드 · LED · 멜로디 · 부저 제어 | 공동 (DB 함수: 안유빈) |
| [`database.sql`](database.sql) | MySQL | 등록 차량 DB 생성 ([`sql/database.sql`](../license-plate-database/sql/database.sql)과 같은 파일) | 안유빈 |
| [`ESP8266/ESP8266.ino`](ESP8266/ESP8266.ino) | ESP8266 | `/distance` · `/move_servo` · `/control_led` · 멜로디 · 부저 HTTP 서버 | 공동 |
| [`CameraWebServer/`](CameraWebServer/) | ESP32-CAM | `/capture`로 사진을 제공하는 카메라 웹 서버 (ESP32 CameraWebServer 예제 기반) | 공동 |

### 핀 배치 (ESP8266)

| 장치 | 핀 |
|---|---|
| 초음파 센서 Trig · Echo | D0 · D1 |
| LED 빨강 · 노랑 · 초록 | D2 · D5 · D6 |
| 서보 1 · 2 | D3 · D4 |
| 멜로디 IC 1 (딩동) · 2 (엘리제를 위하여) | D7 · D8 |
| 부저 | D9 |
