import sqlite3

conn = sqlite3.connect('event-calendar-main/db.sqlite3')  # Django 프로젝트 루트에 있는 DB 파일
cursor = conn.cursor()

# 예: 일정(Event) 테이블에서 모든 데이터 가져오기
cursor.execute("SELECT * FROM calendarapp_event")  # 앱 이름과 모델명 조합
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


# import sqlite3

# conn = sqlite3.connect('event-calendar-main/db.sqlite3')
# cursor = conn.cursor()

# # 테이블 구조 확인
# cursor.execute("PRAGMA table_info(calendarapp_event)")
# columns = cursor.fetchall()

# for col in columns:
#     print(col)

# conn.close()
