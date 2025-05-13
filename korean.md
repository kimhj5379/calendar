

# calendar
[https://github.com/sajib1066/event-calendar]프로젝트를 바탕으로 제작했음을 밝힙니다.

requirements.txt, makemigrations, and migrate은 start.py를 실행하면 자동으로 모두 설치 및 작동하게 설계되어있습니다. 만약 처음 작동할 때에는, start.py에 있는 subprocess.run(["python", "manage.py", "createsuperuser"])를 재활성화 시키기바랍니다.

## Description
GPT 기반 코드 검토를 통해 자동 생성된 GitHub 포트폴리오입니다.
이는 GPT가 코드를 확인 후 코드리뷰하는 방식이라 내용이 정확하지 않습니다.
혹시 문제있으면 Issues에 올려주시기 바랍니다.

이 코드는 GPT가 Tools를 가지고 일정을 추가, 제거, 수정 모두 가능하게 제작되었습니다.
gpt제어 리포는 따로 올리겠습니다.
## Project Contents
- 파이썬 파일 수: 46
- 텍스트 데이터: 1

## How to Run
```
git clone https://github.com/kimhj5379/calendar.git
cd main-calendar
python start.py
```
