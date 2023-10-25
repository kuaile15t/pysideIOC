#!/usr/bin/python3
# coding: utf-8
from framework.application import Application


def main():
    app = Application()
    app.run(welcome=1, welmsg='welcome...')


if __name__ == '__main__':
    main()


