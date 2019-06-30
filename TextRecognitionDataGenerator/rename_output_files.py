import os 
import glob
import sys
from PIL.Image import Image

def main():
    files = [f for f in glob.glob('./out/*.jpg')]
    for i, f in enumerate(files):
        middle_path = f.split('.')[1]
        os.rename(f, f'./out/{i}.jpg')
        os.rename(f'.{middle_path}.xml', f'./out/{i}.xml')

if __name__ == '__main__':
    main()