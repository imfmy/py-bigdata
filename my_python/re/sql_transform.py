import re
import string
from re import Match

# SparkSQL与PrestoSQL的相同功能的函数，普通转换
normal_tran_dict = {
    # 数组是否包含某个元素
    "array_contains": "contains",
    # 计算数组、字典的长度
    "size": "cardinality",
    # 当前日期
    "current_date()": "current_date",
    # unix_timestamp转为时间: from_unixtime()好像一样

    # 安全等于
    "<=>": " is not distinct from ",

}
# SparkSQL与PrestoSQL的相同功能的函数，需要复杂转换
special_tran_dict = {
    # 聚合去重
    "collect_set": {"pre": "array_except(array_distinct(array_agg(", "post": ")),array[null])"},
    # 加减月份
    "add_months": ""
}


def rp_space(m: Match):
    # print(m)
    if m:
        return ' ' * len(m.group())


# 将忽略的字符串转换为等长的空格
def text_lite(text: string):
    res1 = re.sub(r'\'[^\']+\'|\"[^\"]+\"', rp_space, text)
    res2 = re.sub(r'--.+(?=\n)', rp_space, res1)
    return res2


# 统计所有括号对的位置
def find_parentheses(text):
    count = 0
    l_stack = []
    start = -1
    inside_quotation = False
    parentheses = {}
    for i in range(len(text)):
        c = text[i]
        # if c in ("'", '"'):
        #     inside_quotation = not inside_quotation
        # 如果发现左括号，则括号总数加一，左括号栈进栈，并记录次序与位置
        if c == '(':
            count += 1
            l_stack.append((count, i))
        # 如果发现右括号，则左括号栈出栈，并记录次序与位置
        elif text[i] == ')':
            if l_stack:
                l = l_stack.pop()
                parentheses[l[0]] = (l[1], i + 1, i - l[1] + 1)
            else:
                raise IndexError(f"括号()异常，第{i}位置的左括号匹配不到右括号")
    return parentheses


# 查找第n个括号及里面的内容
def find_nth_parentheses(text: string, n: int):
    parentheses = find_parentheses(text)
    l = len(parentheses)
    if n <= len(parentheses):
        res = text[parentheses[n][0]:parentheses[n][1]]
        return res
    else:
        raise IndexError(f"你输入的括号数{n}大于总括号数{len(parentheses)}")


# 查找子串在文本text中第n次出现的位置
def find_nth_occurrence(text, char, n):
    start_index = -1
    for i in range(n):
        start_index = text.find(char, start_index + 1)
        if start_index == -1:
            break
    return start_index


if __name__ == '__main__':
    with open('example1.sql', 'r') as file:
        # 读取原始文本
        content_org = file.read()
        content_res = content_org
        # 简化原始文本（为了确定复杂替换的位置）：将注释与单/双引号内的东西换为同长度的空字符，统一转小写
        content_lite = text_lite(content_org).lower()
        # 查找collect_set第一个出现的索引
        print("首先进行特殊替换：")
        for k, v in special_tran_dict.items():

            rp_num = content_lite.count(k)
            if rp_num > 0:
                print(f"需替换 {k} {rp_num} 次")
                i = 1
                while i <= rp_num:
                    # 全文查询 k 第i次出现的位置
                    k_pos = find_nth_occurrence(content_lite, k, i)
                    # 查询 k 后第一个括号内的内容
                    bracket_content = find_nth_parentheses(content_org[k_pos:], 1)
                    bracket_content_len = find_parentheses(content_org[k_pos:])[1][2]
                    # 将要被替换的内容
                    k_bracket_content = content_org[k_pos:k_pos + len(k) + bracket_content_len]
                    # 如果 有 k 且括号内内容不为空，则进行替换
                    if k_pos != -1 and bracket_content:
                        old1 = f"{k_bracket_content}"
                        new1 = f"{special_tran_dict[f'{k}']['pre']}{bracket_content}{special_tran_dict[f'{k}']['post']}"
                        print(f"第{i}次替换 {k} ，将 {old1} 替换为 {new1}")
                        ptn = re.escape(old1)
                        content_res = re.sub(ptn, new1, content_res, flags=re.IGNORECASE)
                        # print(content_res)
                    i = i + 1
        # print(content_res)
        print("进行简单替换")
        for k, v in normal_tran_dict.items():
            es_k = re.escape(k)
            temp_ptn = re.compile(fr'((?<=\s)|(?<=\b)){es_k}(?=\b|\s)', re.IGNORECASE)
            print(temp_ptn)
            rp_num2 = len(re.findall(temp_ptn, content_lite))
            if rp_num2 > 0:
                content_res = re.sub(temp_ptn, f"{v}", content_res)
                print(f"将 {k} 替换为 {v} ，共 {rp_num2} 次")
        print(content_res)
