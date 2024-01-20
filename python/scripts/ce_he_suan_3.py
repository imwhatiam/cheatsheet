import time
import math
import random
import itertools

interval_day_list = random.sample(range(2, 100), 5)
interval_day_list = sorted(interval_day_list)

# [3, 4, 5, 7, 8]
print(interval_day_list)

all_date_list = []
for interval_day in interval_day_list:
    all_date_list.append([0] * (interval_day-1) + [1])

# [[0, 0, 1],
#  [0, 0, 0, 1],
#  [0, 0, 0, 0, 1],
#  [0, 0, 0, 0, 0, 0, 1],
#  [0, 0, 0, 0, 0, 0, 0, 1]]
# pprint(all_date_list)

print("\n遍历方法")

start_time = time.time()

index = 0
result = 0

for count in [1, 2, 3]:

    while result != count:

        total_count = 0
        for date_list in all_date_list:
            total_count += date_list[index % len(date_list)]

        if total_count == 3:
            result += 1

        index += 1

    print("遍历方法，第 {} 次三人同时做得天数: {}".format(count, index))

print("耗时：")
print(time.time() - start_time)


# 数学方法
def get_result(interval_day_list, number):

    sub_list = list(itertools.combinations(interval_day_list, number))
    print("{}{}子集: \n{}".format(number, number, sub_list))

    result = []
    for value in sub_list:

        index = 0
        a = value[index]
        while index + 2 <= number:
            a = math.lcm(a, value[index + 1])
            index += 1

        result.append(a)

    new_result = []
    for item in result:
        new_result.append(item)
        new_result.append(item * 2)
        new_result.append(item * 3)

    new_result = set(new_result)
    new_result = sorted(new_result)
    return new_result


print("\n数学方法")

start_time = time.time()

number = 3
result_3 = get_result(interval_day_list, number)
print("{}{}子集的最小公倍数，及每个最小公倍数均乘以 2 和 3\n{}\n".format(number, number, result_3))

number = 4
result_4 = get_result(interval_day_list, number)
print("{}{}子集的最小公倍数，及每个最小公倍数均乘以 2 和 3 \n{}\n".format(number, number, result_4))

number = 5
result_5 = get_result(interval_day_list, number)
print("{}{}子集的最小公倍数，及每个最小公倍数均乘以 2 和 3 \n{}\n".format(number, number, result_5))

print("从33子集中，去掉也在 44 或 55 子集中的数字，即可得出结果")
final_result = list(set(result_3) - set(result_4) - set(result_5))
print(sorted(final_result))

print("耗时：")
print(time.time() - start_time)
