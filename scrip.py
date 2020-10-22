import os


def read_dictory(path):
    for f_name in os.listdir(path):
        print(f_name)


if __name__ == "__main__":
    path = './wallpapper'