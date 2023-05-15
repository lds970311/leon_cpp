# coding:utf-8
# time: 2023/5/14
# author: evan
# python excel操作
import xlrd
import xlsxwriter


class ExcelHandler:
    def __init__(self, path):
        self.path = path

    def read_data(self):
        e = xlrd.open_workbook(self.path)
        sheet = e.sheet_by_index(0)
        print(f'总行数：{sheet.nrows}, 总列数： {sheet.ncols}')
        print("cotent: ...")
        for row in sheet.get_rows():
            for col in row:
                print(col.value, end="\t")
            print()

    def write_data(self):
        book = xlsxwriter.Workbook(self.path)
        sheet = book.add_worksheet('goods')
        meta_data = ['商品名称', '价格', '库存', '类别']
        goods1 = ['iPhone14', 9999, 10, 'iPhone']
        for index, data in enumerate(meta_data):
            sheet.write(0, index, data)
        for index, data in enumerate(goods1):
            sheet.write(1, index, data)

        book.close()

    def add_chart(self):
        excel = xlsxwriter.Workbook(self.path)

        book1 = excel.add_worksheet('学生等级')
        data = [
            ['优秀', '良好', '中', '差'],
            [1100, 2000, 1000, 900]
        ]

        book1.write_column('A1', data[0])
        book1.write_column('B1', data[1])

        chart = excel.add_chart({'type': 'column'})
        chart.add_series({
            'categories': '=学生等级!$A1:$A4',
            'values': '=学生等级!$B1:$B4',
            'name': '成绩占比'
        })
        chart.set_title({'name': '成绩占比图表'})
        book1.insert_chart('A10', chart)

        excel.close()


if __name__ == '__main__':
    excel = ExcelHandler('./doc/study.xlsx')
    # excel.read_data()
    # excel.write_data()
    excel.add_chart()
