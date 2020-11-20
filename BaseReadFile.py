# -*- coding: utf-8 -*-#

# Name:         基础文件读写服务类（以后有新增的文件读写方法都往这里面写）
# Description:
# Author:       gongzhao
# Date:         2020/9/25
import urllib

import xlrd as xlrd
import xlwt as xlwt


def read_txt_file(file_name):
    content = []
    f = open(file_name, "r")
    lines = f.readlines()
    for line in lines:
        content.append(line.strip())
    return content


def read_excel_file(file_name, sheet_name, row_value_list, skip_first_line=True):
    """

    :param file_name: 文件名
    :param sheet_name: excel文件 页码名称
    :param row_value_list: excel 行名称
    :param skip_first_line: 是否跳过第一行（如果第一行为行名称，则需要跳过，否则不需要）
    """
    result = []
    data = xlrd.open_workbook(file_name)
    table = data.sheet_by_name(sheet_name)
    for row_num in range(table.nrows):
        if row_num == 0 and skip_first_line:
            continue
        row_value = table.row_values(row_num)
        line_value = {}
        for index in range(len(row_value)):
            if "oss" in str(row_value[index]):
                line_value[row_value_list[index]] = urllib.parse.unquote(row_value[index])
            else:
                line_value[row_value_list[index]] = row_value[index]
        result.append(line_value)
    return result


def write_excel_file(file_name, row_value_list, read_content, sheet_name="sheet1"):
    """

    :param file_name: excel 文件名
    :param row_value_list: 列名
    :param read_content: 带写入的内容 list
    :param sheet_name: 页签名称
    """
    write_book = xlwt.Workbook()
    sheet = write_book.add_sheet(sheet_name)
    for i in range(len(read_content) + 1):
        if i == 0:
            for row_index in range(len(row_value_list)):
                sheet.write(i, row_index, row_value_list[row_index])
        else:
            for row_index in range(len(row_value_list)):
                sheet.write(i, row_index, read_content[i - 1][row_value_list[row_index]])
    write_book.save(file_name)


if __name__ == '__main__':
    row_val_list = ["type", "app_name", "openid", "unionid"]
    content = read_excel_file("data.xlsx", "data", row_val_list, True)
    print(len(content))
    row_val_list = ["type", "app_name", "unionid"]
    write_excel_file("hello.xlsx", row_val_list, content)
