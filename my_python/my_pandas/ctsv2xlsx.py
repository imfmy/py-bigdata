import pandas as pd

input_file='my_python\\my_pandas\\file\\csv2xlsxtest.csv'
# input_file='my_python\\my_pandas\\file\\tsv2xlsxtest.tsv'
input_fil1 = 'my_python\\my_pandas\\file\\20240201_071118_01423_w8hvn.csv'
output_fil1 = 'my_python\\my_pandas\\file\\20240201_071118_01423_w8hvn.xlsx'
# 读取csv或tsv文件
df = pd.read_csv(input_fil1, delimiter=',',na_filter=False)  # 如果是tsv文件，将delimiter参数设置为'\t'

# 将单元格格式设置为字符串类型
df = df.astype(str)
# df.replace('nan', '', inplace=True)

# 将数据保存为xlsx文件
df.to_excel(output_fil1, index=False)
