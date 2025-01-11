import sys

from file_converter import FileConverter


def main():
    fileConverter = FileConverter(sys.argv)
    fileConverter.execute()


if __name__ == "__main__":
    main()

