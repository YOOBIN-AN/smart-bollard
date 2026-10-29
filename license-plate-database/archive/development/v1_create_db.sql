CREATE DATABASE bola;				# 데이터베이스 생성

USE bola;							# 데이터베이스 선택 ; 사용

CREATE TABLE license_plates (
    id INT AUTO_INCREMENT PRIMARY KEY,			# id : 1st column, int : 1열의 자료형, auto_increment : 열 자동 증가
    license_plate VARCHAR(20) NOT NULL,			# varchar(20) : 가변길이 문자열 ; 최대 20자
    plate_type ENUM('장애인', '전기차') NOT NULL	# 입력은 '장애인' / '전기차' 만 가능 !
);

INSERT INTO license_plates (license_plate, plate_type)		# 임의 데이터 생성
VALUES
    ('12가1234', '장애인'),
    ('34나5678', '전기차'),
    ('56다8910', '장애인'),
    ('55구1601', '전기차')
    ('154러7070','장애인');
