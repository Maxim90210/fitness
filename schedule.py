from datetime import datetime, timedelta

def generate_time_intervals(start_time, end_time, interval_minutes=15):
    intervals = []
    current_time = start_time
    while current_time < end_time:
        next_time = current_time + timedelta(minutes=interval_minutes)
        intervals.append((current_time.time(), next_time.time()))
        current_time = next_time
    return intervals

def mark_schedule_intervals(intervals, occupied_times):
    schedule = []
    for interval in intervals:
        start_interval = datetime.combine(datetime.today(), interval[0])
        end_interval = datetime.combine(datetime.today(), interval[1])
        is_occupied = False
        for occupied in occupied_times:
            start_occupied = datetime.strptime(occupied[0], '%H:%M')
            end_occupied = datetime.strptime(occupied[1], '%H:%M')
            if (start_occupied < end_interval and end_occupied > start_interval):
                is_occupied = True
                break
        schedule.append((interval, 'Occupied' if is_occupied else 'Free'))
    return schedule

# Приклад використання
work_start = datetime.strptime('08:00', '%H:%M')
work_end = datetime.strptime('20:00', '%H:%M')
occupied_times = [('09:00', '10:30'), ('13:00', '14:15'), ('16:45', '17:15')]

intervals = generate_time_intervals(work_start, work_end)
schedule = mark_schedule_intervals(intervals, occupied_times)

for time_slot, status in schedule:
    print(f"{time_slot[0]} - {time_slot[1]}: {status}")
