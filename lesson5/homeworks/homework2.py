def main():
    try:
        num = int(input("Number greater than 10: "))
        if num <= 10:
            raise Exception("The number should be greater than 10.")
    except ValueError:
        print("ValueError: the input should be an integer.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
