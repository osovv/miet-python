from lib_list import split_by_lambda

def count_operations(data: list[int]) -> int:
    def helper(a: list[int]) -> int:
        if not(any(a)):
            return 0
        
        segments = split_by_lambda(a, lambda x: x == 0)

        mins = [min(s) for s in segments]

        k = sum(mins)

        new_segments = list(map(
            lambda xy: list(map(lambda el: el - xy[1], xy[0])),
            zip(segments, mins)
        ))

        return k + sum(map(helper, new_segments))

    return helper(data)


def main():
    data = [int(x) for x in input("Enter a list: ").split()]
    return count_operations(data)


if __name__ == '__main__':
    main()
