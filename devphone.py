#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def generate_all_11_digit_numbers():
    numbers = set()  # 使用集合来自动去重

    # 第1位固定为1
    first_digit = "1"

    # 第2位从3到9中选择
    second_digits = [str(i) for i in range(3, 10)]
    
    # 第3位从0到9中选择
    third_digits = [str(i) for i in range(10)]

    # 生成符合规则的8位数字
    def generate_8_digits():
        results = set()

        # AAAAAAAA
        results.update(str(i) * 8 for i in range(10))

        # AAAABBBB
        results.update(str(i) * 4 + str(j) * 4 for i in range(10) for j in range(10) if i != j)

        # ABCDABCD
        results.update(''.join(str((i + j) % 10) for j in range(4)) * 2 for i in range(7))

        # 前7位相同，最后1位不同
        results.update(str(i) * 7 + str(j) for i in range(10) for j in range(10) if i != j)

        # AAABBBCC
        results.update(str(i) * 3 + str(j) * 3 + str(k) * 2 for i in range(10) for j in range(10) for k in range(10) if i != j and j != k)

        return results

    eight_digit_combinations = generate_8_digits()

    # 组合所有可能的11位数字
    for second in second_digits:
        for third in third_digits:
            prefix = first_digit + second + third
            
            # 处理 ABCABCABCCC 的情况
            numbers.add(prefix * 3 + prefix[2] * 2)
            
            # 添加其他8位组合
            numbers.update(prefix + suffix for suffix in eight_digit_combinations)

    return numbers

# 生成所有符合规则的11位数字
all_numbers = generate_all_11_digit_numbers()

# 保存结果到文件
with open("all_11_digit_numbers.txt", "w") as file:
    for number in all_numbers:
        file.write(number + "\n")

# 打印一些示例
for number in list(all_numbers)[:20]:
    print(number)

# 打印总数
print(f"Total unique numbers generated: {len(all_numbers)}")
