def generate_all_11_digit_numbers():
    numbers = set()  # 使用集合来存储唯一的数字组合

    # 第1位固定为1
    first_digit = "1"

    # 第2、3位从3到9中选择
    second_third_digits = [str(i) for i in range(3, 10)]

    # 生成符合规则的8位数字
    def generate_8_digits():
        results = []

        # AAAAAAAA
        for i in range(10):
            results.append(str(i) * 8)

        # AAAABBBB
        for i in range(10):
            for j in range(10):
                results.append(str(i) * 4 + str(j) * 4)

        # ABCDABCD
        for i in range(0, 7):  # 0到6是为了保证ABCD可以是连续的数字
            abcd = ''.join(str(i + j) for j in range(4))
            results.append(abcd * 2)

        # 0000000A 前7位相同，最后1位不同
        for i in range(10):
            for j in range(10):
                results.append(str(i) * 7 + str(j))

        return results

    eight_digit_combinations = generate_8_digits()

    # 组合所有可能的11位数字
    for second in second_third_digits:
        for third in second_third_digits:
            prefix = first_digit + second + third
            for suffix in eight_digit_combinations:
                numbers.add(prefix + suffix)  # 使用集合去重

    return numbers

# 生成所有符合规则的11位数字
all_numbers = generate_all_11_digit_numbers()

# 保存结果到文件
with open("all_11_digit_numbers.txt", "w") as file:
    for number in sorted(all_numbers):  # 按照字典序排序
        file.write(number + "\n")

# 打印一些示例
for number in list(all_numbers)[:10]:
    print(number)

# 打印总数
print(f"Total numbers generated: {len(all_numbers)}")
