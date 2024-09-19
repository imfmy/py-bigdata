import re

import pandas as pd

# def clean_data(value):
#     try:
#         return value.encode('unicode_escape').decode('utf-8')
#     except UnicodeDecodeError:
#         return ''
def remove_special_characters(value):
    # 使用正则表达式移除特定范围的字符
    return pd.Series(value).replace(to_replace=[r'[\000-\010]', r'[\013-\014]', r'[\016-\037]'], value='', regex=True).iloc[0]


def csv2xlsx(input_file, output_file=None):
    if output_file is None:
        output_file = input_file.replace('.csv', '.xlsx')
    df = pd.read_csv(input_file, delimiter=',', na_filter=False)  # 如果是tsv文件，将delimiter参数设置为'\t'
    # df = df.applymap(remove_special_characters)
    df = df.astype(str)
    df.to_excel(output_file, index=False,na_rep='', float_format="%.2f")
    print(f'{input_file} done')


def tsv2xlsx(input_file, output_file):
    df = pd.read_csv(input_file, delimiter='\t', na_filter=False)  # 如果是tsv文件，将delimiter参数设置为'\t'
    df = df.astype(str)
    df.to_excel(output_file, index=False)
    print(f'{input_file} done')


if __name__ == '__main__':
    input_file = './qushu_files/qushu_entity_shop_part1.csv'
    csv2xlsx(input_file)
