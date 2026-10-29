recognized_text = '55구 1601'
recognized_text = recognized_text.replace(' ', '')

import sqlite3

def check_text_in_db(recognized_text, db_file='your_database.db'):
    # SQLite 데이터베이스에 연결
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # 테이블명과 검색할 컬럼명을 지정
    table_name = 'your_table_name'  # 데이터베이스에 실제 테이블명을 사용
    column_name = 'your_column_name'  # 검색할 컬럼명을 사용

    # 쿼리문을 작성
    query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = ?"
    
    # 쿼리 실행 및 결과 가져오기
    cursor.execute(query, (recognized_text,))
    count = cursor.fetchone()[0]

    # 연결 종료
    conn.close()

    # 결과 반환
    if count > 0:
        return "일치한다"
    else:
        return "일치하지 않는다"

result = check_text_in_db(recognized_text)
print(result)
