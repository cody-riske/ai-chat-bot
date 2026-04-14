from functions.get_files_info import get_files_info

def test():
    result = get_files_info("calculator", "lorem.txt")
    print("Result for lorem directory")
    print(result)
    
    result = get_files_info("calculator", "main.py")
    print("Result for current directory:")
    print(result)

    result = get_files_info("calculator", "pkg/calculator.py")
    print("Result for 'pkg/calculator' directory:")
    print(result)

    result = get_files_info("calculator", "/bin/cat")
    print("Result for '/bin/cat' directory:")
    print(result)

    result = get_files_info("calculator", "pkg/does_not_exist.py")
    print("Result for 'pkg/does_not_exist' directory:")
    print(result)


if __name__ == "__main__":
    test()