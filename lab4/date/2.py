from datetime import datetime, timedelta
today=datetime.now()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)
print("Сегодня:",today.strftime("%y-%m-%d"))
print("Вчера:",yesterday.strftime("%y-%m-%d"))
print("Завтра:",tomorrow.strftime("%y-%m-%d"))