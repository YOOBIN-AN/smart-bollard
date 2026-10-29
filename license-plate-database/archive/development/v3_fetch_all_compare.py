import mysql.connector
from mysql.connector import Error

def connect_to_database():
    """MySQL 데이터베이스에 연결하는 함수"""
    try:
        connection = mysql.connector.connect(
            host='localhost',            # 데이터베이스 서버 주소
            database='bolla',            # 데이터베이스 이름
            user='root',                 # 사용자 이름
            password='********'     # 비밀번호
        )
        if connection.is_connected():
            print("MySQL 데이터베이스에 성공적으로 연결되었습니다.")
            return connection
    except Error as e:
        print(f"연결 오류: {e}")
        return None

def fetch_plate_info(cursor):
    """번호판 정보를 가져오는 함수"""
    query = "SELECT license_plate FROM plate"  # 적절한 테이블 이름을 사용
    cursor.execute(query)
    return cursor.fetchall()

def check_plate_match(plate_info_list, recognized_text):
    """번호판 정보와 인식된 텍스트가 일치하는지 확인하는 함수"""
    for license_plate, in plate_info_list:
        if license_plate == recognized_text:
            print(f"일치하는 번호판 발견: {license_plate}")
            return True
    print("일치하는 번호판이 없습니다.")
    return False

def main():
    # 데이터베이스 연결
    connection = connect_to_database()
    if connection is None:
        return

    cursor = connection.cursor()

    # 번호판 정보 가져오기
    plate_info_list = fetch_plate_info(cursor)

    # 인식된 텍스트 (예: 외부에서 제공된 텍스트)
    recognized_text = "인식된번호판정보".replace(' ', '')  # 예시 텍스트

    # 번호판 정보와 인식된 텍스트 비교
    check_plate_match(plate_info_list, recognized_text)

    # 연결 종료
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
