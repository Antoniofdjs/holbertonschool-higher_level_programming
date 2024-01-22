#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    list_str = dir(hidden_4)

    for _ in range(0, len(list_str)):
        string = list_str[_]
        if string[:2] != "__" != string[-2:]:
            print(string)
