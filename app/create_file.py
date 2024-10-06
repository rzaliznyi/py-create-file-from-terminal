import os
import sys
import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Directory {path} created successfully!")


def create_file(path: str) -> None:
    file_exists = os.path.exists(path)

    with open(path, "a") as file:
        if not file_exists:
            print(f"File '{path}' created successfully.")
        else:
            print(f"Appending to existing file '{path}'.")

        # Додаємо запис часу всередині блоку with
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        d_index = args.index("-d") + 1
        directories = []

        while d_index < len(args) and args[d_index] != "-f":
            directories.append(args[d_index])
            d_index += 1

        if directories:
            dir_path = os.path.join(*directories)
            create_directory(dir_path)
        else:
            print("No directory specified after '-d' flag.")
            return

    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args):
            file_name = args[f_index]

            if "-d" in args:
                dir_path = os.path.join(*directories)
                file_path = os.path.join(dir_path, file_name)
            else:
                file_path = file_name

            create_file(file_path)
        else:
            print("No file specified after '-f' flag.")
            return
    else:
        print("You need to specify a file with '-f' flag.")


if __name__ == "__main__":
    main()
