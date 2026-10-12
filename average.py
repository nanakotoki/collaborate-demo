import sys

def main():
    args = sys.argv[1:]

    total = 0
    count = 0

    for arg in args:
        total = total + float(arg)
        count = count + 1

    if count > 0:
        avg = total / count
        print(f"平均数为: {avg}")
    else:
        print("未输入任何数字。")

if __name__ == "__main__":
    main()