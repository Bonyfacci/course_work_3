# course_work_3
Платонов Сергей - Курсовая карбота №3
Стек технологий:
colorama==0.4.6
coverage==7.2.6
exceptiongroup==1.1.1
iniconfig==2.0.0
packaging==23.1
pluggy==1.0.0
pytest==7.3.1
pytest-cov==4.1.0
tomli==2.0.1
Для запуска необходимо:
создать виртуальное окружение
pip install -r requirements.txt
Чтобы сгенерировать отчет о покрытии необходимо:
pytest --cov src --cov-report term-missing
