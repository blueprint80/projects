duration = int(input())
seconds = duration % 60
minutes = duration // 60
hours = minutes // 60
days = hours // 24

if 60 >= duration >= 0:
    print(duration, "сек")
elif 60 ** 2 >= duration > 60:
    print(minutes, "мин.", seconds, "сек.")
elif 3600 * 24 >= duration > 3600:
    print(hours, "ч.", minutes % 60, "мин.", seconds, "сек.")
elif 3600 * 24 * 31 >= duration > 3600 * 24:
    print(days, "д.", hours % 24, "ч.", minutes % 60, "мин.", seconds, "сек.")
