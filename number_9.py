def one():
    emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
              'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
              'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
              'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
              'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
              'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
    a = [f"{name}@{key}" for key, value in emails.items() for name in value]
    a.sort()
    return a


def two():
    a = [i ** 3 for i in range(1, 11)]
    return a


def main():
    print("Number №1")
    print("\n".join(one()))
    print("\nNumber №2\n")
    print(two())


if __name__ == "__main__":
    main()