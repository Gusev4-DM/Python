if __name__ == "__main__":
    from sys import argv

    with open("bakery.csv", "a", encoding="utf-8") as f:
        print(f'{round(float(argv[1].replace(",", ".")), 3)}', file=f)

