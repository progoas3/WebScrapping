from Functions.functions import *


def main():
    connection = Main("https://httpbin.org/basic-auth/user/pass")
    connection.pr()

if __name__ == "__main__":
    main()
    