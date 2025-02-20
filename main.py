from Functions.functions import *


def main():
    connection = Main("https://escueladirecta-blog.blogspot.com/", "title")
    connection.extract()

if __name__ == "__main__":
    main()
    