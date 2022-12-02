def main():
    file_reader()


def file_reader():
    with open('day1/input.txt') as f:
        lines = f.read().splitlines()
        print(lines)

if __name__ == '__main__':
    main()
