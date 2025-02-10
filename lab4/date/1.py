from datetime import datetime, timedelta
date=datetime.now()
new_date=date-timedelta(days=5)
print("Дата 5 дней назад:", new_date.strftime("%Y-%m-%d"))