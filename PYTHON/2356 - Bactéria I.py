while True:
    try:
        d = input()
        s = input()
        if "ACGT" in d or "ACGT" in s:
            print("Resistente")
        else:
            print("Nao resistente")

    except EOFError:
        break