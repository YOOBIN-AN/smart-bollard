'''MySQL 데이터베이스 연결'''

import mysql.connector

def connect_to_database():
    # MySQL 데이터베이스 연결 설정
    conn = mysql.connector.connect(
        host='localhost',        # MySQL 서버 호스트 이름
        user='root',    # MySQL 사용자 이름
        password='********',# MySQL 사용자 비밀번호
        database='bola' # 사용할 데이터베이스 이름
    )
    return conn

# 연결 테스트
conn = connect_to_database()
if conn.is_connected():
    print("Database connection successful")
else:
    print("Database connection failed")
conn.close()


'''인식된 번호판 데이터 비교'''

def get_recognized_plate():
    # 예시: YOLO 모델을 사용하여 번호판 인식 결과를 반환
    # 실제 코드에서는 YOLO 모델을 호출하고 결과를 받아와야 함
    recognized_plate = "34나5678"  # 예시 결과
    return recognized_plate

def compare_license_plate(conn, recognized_plate):
    cursor = conn.cursor()

    # 데이터베이스에서 번호판 조회
    query = "SELECT * FROM license_plates WHERE license_plate = %s"
    cursor.execute(query, (recognized_plate,))

    # 결과 가져오기
    result = cursor.fetchone()
    cursor.close()

    if result:
        return True, result
    else:
        return False, None

def main():
    # 인식된 번호판 데이터 가져오기
    recognized_plate = get_recognized_plate()
    print(f"Recognized license plate: {recognized_plate}")

    # 연결 및 번호판 비교
    conn = connect_to_database()
    if conn.is_connected():
        print("Database connection successful")
        match, data = compare_license_plate(conn, recognized_plate)
        if match:
            print("번호판이 일치합니다:", data)
        else:
            print("번호판이 일치하지 않습니다.")
    else:
        print("Database connection failed")
    conn.close()

if __name__ == "__main__":
    main()
