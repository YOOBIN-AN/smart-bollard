"""스마트 볼라드 — 번호판 데이터베이스 연동 모듈

팀 원본 client.py 에서 데이터베이스 연결 · 번호판 비교 부분만 분리한 코드입니다.
원본: https://github.com/Yunseo-Cho/2024ESWContest_free_1090

원본과 달라진 점
- DB 접속 정보를 코드에 직접 쓰지 않고 환경변수로 받음
- stream_video() 안에 있던 "후보 번호판 목록 → DB 비교" 부분을 check_plates() 로 분리

사용 예
    export BOLLA_DB_PASSWORD=...
    python src/plate_db.py 55구1601
"""

import os
import sys

import mysql.connector


def connect_to_database():
    """MySQL 서버에 접속해 bolla 데이터베이스 연결을 반환"""
    conn = mysql.connector.connect(
        host=os.getenv("BOLLA_DB_HOST", "localhost"),
        user=os.getenv("BOLLA_DB_USER", "root"),
        password=os.getenv("BOLLA_DB_PASSWORD", ""),
        database=os.getenv("BOLLA_DB_NAME", "bolla"),
    )
    return conn


def compare_license_plate(conn, recognized_plate):
    """license_plates 테이블에 인식된 번호판이 있으면 True, 없으면 False"""
    cursor = conn.cursor()
    query = "SELECT * FROM license_plates WHERE license_plate = %s"
    cursor.execute(query, (recognized_plate,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def check_plates(plates):
    """OCR 후보 번호판 목록 중 DB와 일치하는 첫 번호판을 반환 (없으면 None)

    원본 stream_video() 의 DB 비교 부분과 같은 동작:
    한 프레임에서 형식에 맞는 후보가 여러 개 나오면 하나라도 일치하는지 확인
    """
    conn = connect_to_database()
    try:
        if not conn.is_connected():
            print("Database connection failed")
            return None
        for plate in plates:
            if compare_license_plate(conn, plate):
                print(f"번호판 {plate}이(가) 데이터베이스와 일치합니다.")
                return plate
        return None
    finally:
        conn.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python src/plate_db.py <번호판> [<번호판> ...]")
        sys.exit(1)

    matched = check_plates(sys.argv[1:])
    print("등록 차량" if matched else "미등록 차량")
