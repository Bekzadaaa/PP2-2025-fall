from datetime import datetime, timedelta
date1=datetime.now()
date2=datetime(2025, 2, 12, 14 , 10, 0)
diff=(date1-date2).total_seconds()
print(diff)