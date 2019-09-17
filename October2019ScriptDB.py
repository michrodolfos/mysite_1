from main.models import Calendar, SuggestedCalendar
from django.utils import timezone
from datetime import datetime, timedelta

initial_datetime = datetime(2019, 10, 1, 10)
temp_datetime = initial_datetime

increment_time = timedelta(minutes=20)
revert_time = timedelta(hours=-4)
increment_day = timedelta(days=1)

for w in range (0, 4):
        for d in range (0, 4):
                x = Calendar(schedule=temp_datetime)
                y = SuggestedCalendar(schedule=temp_datetime)
                x.save()
                y.save()
                for t in range (0, 12):
                        temp_datetime += increment_time
                        x = Calendar(schedule=temp_datetime)
                        y = SuggestedCalendar(schedule=temp_datetime)
                        x.save()
                        y.save()
                        if t==11:
                                temp_datetime += increment_day
                temp_datetime += revert_time
        temp_datetime += increment_day
        temp_datetime += increment_day
        temp_datetime += increment_day
                
