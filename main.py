import calendar

# 年と月を設定
year = 2024
month = 2

# TextCalendar クラスのインスタンスを作成
cal = calendar.TextCalendar(calendar.SUNDAY)

# 指定された年と月のカレンダーを表示
cal_str = cal.formatmonth(year, month)

print(cal_str)
