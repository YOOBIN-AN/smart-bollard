[← DB 구축 · 연동](../README.md)

# archive

최종 코드([`sql/database.sql`](../sql/database.sql) · [`src/plate_db.py`](../src/plate_db.py))에 이르기까지의 버전별 코드와 SQL입니다.  
코드의 DB 비밀번호는 모두 `********`로 가렸습니다.

### 1단계 · DB 생성과 비교 테스트

MySQL 설치 → `bola` DB · `license_plates` 테이블 생성 → 고정 번호판으로 일치 확인 → Raspberry Pi로 이전

| 버전 | 날짜 | 파일 | 변경 내용 |
|:-:|---|---|---|
| v1 | 2024.08.08 | [`v1_db_compare.py`](development/v1_db_compare.py) | MySQL 연결 테스트 + 고정 번호판(`34나5678`)으로 일치 여부 확인 |
| v1 | 2024.08.13 | [`v1_create_db.sql`](development/v1_create_db.sql) | `bola` DB · `license_plates` 테이블 최초 생성, 임의 번호판 5개 삽입 |
| v1-1 | 2024.08.13 | [`v1-1_sqlite_template.py`](development/v1-1_sqlite_template.py) | SQLite 기반 비교 방식 검토용 템플릿 (최종 미사용) |
| v2 | 2024.08.14 | [`v2_reset_db.sql`](development/v2_reset_db.sql) | `DROP ... IF EXISTS`로 반복 실행 가능하게 변경, DB 이름 `bolla`로 통일 |

### 2단계 · OCR 결과 연동과 통합

실제 OCR 출력으로 테스트 → 비교 방식 정리 → 함수 단위로 나눠 `client.py`에 통합

| 버전 | 날짜 | 파일 | 변경 내용 |
|:-:|---|---|---|
| v3 | 2024.08.18 | [`v3_fetch_all_compare.py`](development/v3_fetch_all_compare.py) | 전체 번호판을 가져와 Python에서 비교하는 방식 시도, `try/except` 연결 오류 처리 |
| v3-1 | 2024.08.18 | [`v3-1_ocr_text_compare.py`](development/v3-1_ocr_text_compare.py) | 실제 OCR 출력(`154러 7070`) 공백 제거 후 SQL 조회 방식으로 정리 |
| v4 | 2024.09.02 | [`v4_integration.py`](development/v4_integration.py) | 통합용 함수 구조로 정리, 시연 PC 환경 접속 정보 적용 |
| v4 | 2024.09.02 | [`v4_database.sql`](development/v4_database.sql) | 시연용 등록 차량 14대 (최종본은 `23가4568` 추가로 15대) |

v3처럼 전체 목록을 가져와 Python에서 비교하면 등록 차량이 늘수록 매번 모든 행을 읽어야 해서, v3-1부터는 SQL `WHERE`로 일치하는 행만 찾는 방식을 최종으로 채택했습니다.
