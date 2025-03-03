import os

def check_path(path):
    if os.path.exists(path):
        print("The specified path exists.")
        print("Directory portion:", os.path.dirname(path))
        print("Filename portion:", os.path.basename(path))
    else:
        print("The specified path does not exist.")

def main():
    path = input("Enter the path to check: ")
    check_path(path)

if __name__ == "__main__":
    main()
