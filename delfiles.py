import glob
import os

def main():
    for file in glob.glob('./*/*/arq.del'):
        os.remove(file)

    for file in glob.glob('./*/arq.del'):
        os.remove(file)

if __name__ == "__main__":
    main()