import sqlite3
from datetime import datetime

conn = sqlite3.connect('event-calendar-main/db.sqlite3')
cursor = conn.cursor()

data = (
    1,        # is_active (True/1)
    0,        # is_deleted (False/0)
    datetime.now(),  # created_at
    datetime.now(),  # updated_at
    '직접 삽입한 일정입니다.',  # description
    '2025-05-20 09:00:00',  # start_time
    '2025-05-20 10:00:00',  # end_time
    1,        # user_id
    '예시 일정 제목'         # title
)

cursor.execute("""
    INSERT INTO calendarapp_event (
        is_active, is_deleted, created_at, updated_at,
        description, start_time, end_time, user_id, title
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", data)

conn.commit()
conn.close()
print("✅ 일정 추가 완료")
