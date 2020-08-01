import argparse
import src.ocr
import src.bounding_box
import src.search


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file', help='path to image file you want to extract text from')
    parser.add_argument(
        '-v', '--view', action='store_true', help='Shows the boundaries around the text')
    parser.add_argument(
        '-s', '--search', help='Search for the paticular Regular Expression in Image.')

    args = parser.parse_args()

    if(args.view):
        try:
            src.bounding_box.main(args.file)
        except:
            print(
                'boundary_box.py : Dependency Error : Tesseract Version > 3.05 required.')

    if(args.search):
        try:
            src.search.main(args.file, args.search)
        except:
            print('search.py : Dependency Error : Tesseract Version > 3.05 required.')

    src.ocr.main(args.file)


if __name__ == '__main__':
    main()
