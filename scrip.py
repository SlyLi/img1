import os


def read_dictory(path):
    for f_name in os.listdir(path):
        print('![](https://cdn.jsdelivr.net/gh/slyli/img1/wallpaper/%s)'%f_name)


if __name__ == "__main__":
    path = './wallpaper'
    read_dictory(path)