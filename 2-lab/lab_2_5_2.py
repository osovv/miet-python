import os

def main():
    ext = input("Enter the file extension: ")
    count = 0

    for root, dirs, files in os.walk('./example'):
        for file in files:
            _, file_extension = os.path.splitext(file)
            if file_extension == ext:
                count += 1

    print(f"Result: {count} files with {ext} extension")



if __name__ == '__main__':
    main()
