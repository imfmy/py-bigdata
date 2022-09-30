#!/usr/bin/env /usr/bin/python3
# -*- coding:utf-8 -*-
import json
import re



def get_price(desc: str) -> float or None:
    """
    通过product_price_desc取值，汇率计算如下：
    "US $" -> 6.79
    "JPY ¥" -> 0.0628
    "CNY ¥" -> 1.0
    "HK $" -> 0.87
    "€" -> 7.84
    "EUR" -> 7.84
    "$" ->  6.79
    其他->1，
    针对原始价格是区间值，按取计算后的最小值,小数点保留后两位
    """
    price = None
    matched = None
    if desc:
        matched = re.match(r'([^\d.]*)([\d.]+)', desc)
    if matched:
        g1 = matched.group(1)
        ori = float(matched.group(2))
        if g1 == 'US $':
            price = round(ori * 6.79, 2)
        elif g1 == 'JPY ¥':
            price = round(ori * 0.0628, 2)
        elif g1 == 'CNY ¥':
            price = round(ori * 1.0, 2)
        elif g1 == 'HK $':
            price = round(ori * 0.87, 2)
        elif g1 == '€' or g1 == 'EUR':
            price = round(ori * 7.84, 2)
        elif g1 == '$':
            price = round(ori * 6.79, 2)
        else:
            price = round(ori, 2)
    return price