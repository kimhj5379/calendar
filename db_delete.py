import sqlite3
from datetime import datetime

conn = sqlite3.connect('event-calendar-main/db.sqlite3')
cursor = conn.cursor()

event_id = 3  # 삭제할 일정의 ID

cursor.execute("DELETE FROM calendarapp_event WHERE id = ?", (event_id,))

conn.commit()
conn.close()

print("🗑️ 일정 완전 삭제 완료!")