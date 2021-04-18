import importlib


if __name__ == '__main__':
    module = importlib.import_module('UserFile')
    print(module.if_new_message)
    print(module.ID)
