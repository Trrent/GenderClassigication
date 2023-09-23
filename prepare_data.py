import os

base_path = 'data'
for dir in ['man', 'woman']:
    path = os.path.join(base_path, dir)
    counter = 10000
    for file in os.listdir(path):
        new_name = f"{counter}.{file.split('.')[-1]}"
        if file.endswith('.png'):
            os.remove(os.path.join(path, file))
        else:
            os.rename(os.path.join(path, file), os.path.join(path, new_name))
            counter += 1