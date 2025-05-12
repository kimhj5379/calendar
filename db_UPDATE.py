import sqlite3
from datetime import datetime

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()


event_id = 3  # 수정할 일정의 ID
new_title = "수정된 일정 제목"
new_description = "수정된 설명입니다."
new_updated_at = datetime.now()

cursor.execute("""
    UPDATE calendarapp_event
    SET title = ?, description = ?, updated_at = ?
    WHERE id = ?
""", (new_title, new_description, new_updated_at, event_id))

conn.commit()
conn.close()

print("✅ 일정 수정 완료!")