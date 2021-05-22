from datetime import datetime

today = datetime.now().strftime('%d-%m-%Y %H:%M:%S/%p')
date, time = today.split()
print(date)
print(time)
