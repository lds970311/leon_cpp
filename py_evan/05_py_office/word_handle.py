# coding:utf-8
# time: 2023/5/13
# author: evan
import glob
import os

from docx import Document


def read_word_paragraph():
    doc = Document('./doc/文本.docx')
    # for p in doc.paragraphs:
    # print(p.text)
    for tab in doc.tables:
        for row in tab.rows:
            for cell in row.cells:
                print(cell.text, end=' ')
            print()


class ReadDoc:
    def __init__(self, path):
        self.doc = Document(path)
        self.p_text = ''
        self.table_text = ''
        self.get_paragraph()
        self.get_table()

    def get_paragraph(self):
        for p in self.doc.paragraphs:
            self.p_text += p.text + '\n'

    def get_table(self):
        for table in self.doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    self.table_text += cell.text
                self.table_text += '\n'


def cv_filter(path, target):
    """
    简历筛选
    :return:
    """
    res = []

    result = glob.glob(path)
    for i in result:
        if os.path.isfile(i):
            if i.endswith(".docx"):
                doc = ReadDoc(i)
                p_text = doc.p_text
                p_table = doc.table_text

                for t in target:
                    if t not in p_text and t not in p_table:
                        break
                else:
                    res.append(i)

    return res


if __name__ == '__main__':
    # read_word_paragraph()
    path = os.path.join(os.getcwd(), 'doc', '*')
    l = cv_filter(path, ['python'])
    print(l)
    print(len(l))
