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
        results = set()  # 使用集合来自动去重

        # AAAAAAAA
        for i in range(10):
            results.add(str(i) * 8)

        # AAAABBBB
        for i in range(10):
            for j in range(10):
                if i != j:  # 确保前后部分不同
                    results.add(str(i) * 4 + str(j) * 4)

        # ABCDABCD
        for i in range(0, 7):  # 0到6是为了保证ABCD可以是连续的数字
            abcd = ''.join(str((i + j) % 10) for j in range(4))  # 确保数字在0-9范围内
            results.add(abcd * 2)

        # 前7位相同，最后1位不同
        for i in range(10):
            for j in range(10):
                if i != j:  # 确保前7位和最后1位不同
                    results.add(str(i) * 7 + str(j))

        return results

    eight_digit_combinations = generate_8_digits()

    # 组合所有可能的11位数字
    for second in second_digits:
        for third in third_digits:
            prefix = first_digit + second + third
            for suffix in eight_digit_combinations:
                numbers.add(prefix + suffix)

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
