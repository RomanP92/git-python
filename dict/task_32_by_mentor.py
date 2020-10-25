from collections import defaultdict, Counter


def calc_words_1():
    words_count = defaultdict(int)
    for word in input().lower().split():
        words_count[word] += 1
    for item in words_count.items():
        print(item[0], item[1])


def calc_words_2():
    words_count = Counter(input().lower().split())
    [print(item[0], item[1]) for item in words_count.items()]


def calc_words_3():
    words_count = Counter(input().lower().split())
    for item in words_count.items():
        print(item[0], item[1])


if __name__ == "__main__":
    # a aa abC aa ac abc bcd a
    print("Example 1:")
    calc_words_1()
    print("Example 2:")
    calc_words_2()
    print("Example 3:")
    calc_words_3()
