# CRM - система рекламной компании

## Эта CRM-система предназначена для автоматизации процессов привлечения клиентов, обработки обращений и составления контрактов. 
Она поможет вашему бизнесу улучшить взаимодействие с клиентами, оптимизировать маркетинговые кампании и упростить процесс управления контрактами.


## Основные функции
- Ведение учета предлагаемых компанией услуг
- Запуск и завершение рекламных кампаний
- Учет потенциальных клиентов, заинтересованных в конкретной рекламной кампании
- Перевод клиентов из статуса «потенциальные» в статус «активные» при составлении контрактов на сотрудничество


## Технологии
- Backend: Python, Django
- Frontend: [HTML, CSS]
- База данных: [PostgreSQL]


## Установка и запуск

### Требования
- Python 3.9.6
- Другие зависимости, перечисленные в `requirements.txt`


### Уствнока
1. Клонируйте репозиторий:
  git clone https://github.com/Bawkan/CRM-system
2. Установите необходимые зависимости:
  pip instal requiremets.txt
3. Настройте базу данных:
  python manage.py makemigrations
  python manage.py migrate
4. Создайте суперпользователя:
  python manage.py createsuperuser


### Запуск
Запустите сервер разработки:
  python manage.py runserver

Перейдите по адресу http://localhost:8000 в вашем браузере.
