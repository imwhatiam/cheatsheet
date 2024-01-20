import random
import time

TOTAL_DAYS = 200  # 一共有多少天的股票价格
X_DAYS_NEW_HIGH = 99  # 百日新高：确认当天是不是比过去 99 天的价格都高。

# 对一只股票，随机生成股票价格
STOCK_PRICE_LIST = list()
for i in range(TOTAL_DAYS):
    int_part = random.randint(5, 20)
    float_part = round(random.random(), 2)
    total = round(int_part + float_part, 2)
    STOCK_PRICE_LIST.append(total)

# 暴力解法
start_time = time.time()

res = list()
for day in range(X_DAYS_NEW_HIGH, TOTAL_DAYS):

    # 求出过去99天的最大值
    max_price = max(STOCK_PRICE_LIST[day - X_DAYS_NEW_HIGH:day])
    if STOCK_PRICE_LIST[day] > max_price:
        res.append(day)

end_time = time.time()
time_cost = end_time - start_time

# 优化方法
lian_start_time = time.time()


def get_top_price_date(current_date, last_x_days):

    max_price = max(STOCK_PRICE_LIST[current_date - last_x_days:current_date])
    for index, value in enumerate(STOCK_PRICE_LIST[:current_date]):
        if value == max_price:
            top_price_date = index

    return top_price_date


lian_res = []
top_price_date = get_top_price_date(X_DAYS_NEW_HIGH, X_DAYS_NEW_HIGH)

for date in range(X_DAYS_NEW_HIGH, TOTAL_DAYS):

    if date - top_price_date == X_DAYS_NEW_HIGH + 1:
        top_price_date = get_top_price_date(date, X_DAYS_NEW_HIGH)

    if STOCK_PRICE_LIST[date] > STOCK_PRICE_LIST[top_price_date]:
        top_price_date = date
        lian_res.append(date)

lian_end_time = time.time()
lian_time_cost = lian_end_time - lian_start_time


print("总计有股票价格天数：%d，记录每只股票价格创 %d天 新高的日期".center(20) % (TOTAL_DAYS, X_DAYS_NEW_HIGH + 1))
print("暴力方法，新高第x天 ", res)
print("lian法，新高第x天 ", lian_res)

effidency = round(time_cost/lian_time_cost, 2)
print("暴力方法用时：%f" % time_cost)
print("lian方法耗时：%f" % lian_time_cost)
print("效率提升%s倍" % effidency)
