# coding:utf-8
# time: 2023/5/14
# author: evan

import pdfkit
from pydocx import PyDocX


def web_to_pdf():
    pdfkit.from_url('https://www.google.com', './google.pdf')


def word_to_html(path):
    html = PyDocX.to_html(path)
    f = open('./leon.html', 'w')
    f.write(html)
    f.close()
    pdfkit.from_file('leon.html', 'leon.pdf')


if __name__ == '__main__':
    # web_to_pdf()
    word_to_html('./doc/简历1.docx')
