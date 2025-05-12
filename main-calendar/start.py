import os
import subprocess

# 프로젝트 생성
# subprocess.run(["django-admin", "startproject", "mysite"])
# os.chdir("mysite")

os.chdir("event-calendar-main")

# requirements.txt 설치
subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

subprocess.run(["python", "manage.py", "makemigrations"])
subprocess.run(["python", "manage.py", "migrate"])

# 처음 실행할때만
# subprocess.run(["python", "manage.py", "createsuperuser"])

# 서버 실행
subprocess.run(["python", "manage.py", "runserver"])