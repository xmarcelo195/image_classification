import glob

path = r'D:\\PycharmProjects\\Review\\image_classification\\images\\998.jpg'

# teste se função vai dar certo


def get_name(path):
    print(path)
    photo = path.split('\\')[-1]
    return photo


name = get_name(path)
print(name)
