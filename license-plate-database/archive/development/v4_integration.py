import mysql.connector

def bring():
    recognized_text = '154러 7070'

    def connect_to_database():
        # MySQL 데이터베이스 연결 설정
        conn = mysql.connector.connect(
            host='localhost',        # MySQL 서버 호스트 이름
            user='root',    # MySQL 사용자 이름
            password='********',# MySQL 사용자 비밀번호
            database='bolla' # 사용할 데이터베이스 이름
        )
        return conn

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

    # 인식된 번호판 데이터 가져오기
    recognized_plate = recognized_text.replace(' ', '')

    # 데이터베이스 연결 및 번호판 비교
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
    bring()