from datetime import datetime, timedelta, timezone

# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
now = datetime.now()  # 获取当前datetime
dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime

# 我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
# 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp

t = dt.timestamp()  # 把datetime转换为timestamp
dt1 = datetime.fromtimestamp(t)  # 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()   本地时间

dt2 = datetime.utcfromtimestamp(t)  # 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()   UTC时间

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')  # 2015-06-01 18:19:59

# datetime转换为str
now.strftime('%a, %b %d %H:%M')  # Mon, May 05 16:28

# datetime加减
dt3 = now - timedelta(days=1)
dt4 = now + timedelta(hours=10)
dt5 = now + timedelta(days=2, hours=12)

# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00

# 时区转换 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  # 拿到UTC时间，并强制设置时区为UTC+0:00:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  # astimezone()将转换时区为北京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))  # astimezone()将转换时区为东京时间:
