#!/usr/bin/env python3

__author__ = "Nathan Harriss"
__version__ = "0.0.1"

import sys
import argparse
import pyperclip


def main(args):
    """ Main entry point of the app """

    if args.filepath is not None:
        print("Copying file text...")
        try:
            with open(args.filepath, 'r') as f:
                text = f.read()
        except (FileNotFoundError, PermissionError) as e:
            print(e)
            sys.exit(1)
    elif args.text is not None:
        print("Copying string...")
        text = args.text
    else:
        parser.print_help()
        sys.exit(0)

    # Save text to clipboard
    pyperclip.copy(text)
    print("Text saved to clipboard")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--text", action="store", dest="text", help="clip text from string")
    parser.add_argument("-f", "--filepath", action="store", dest="filepath", help="clip text from a file")
    parser.add_argument("--version", action="version", version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
