#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  ┌───┐   ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┐
  │Esc│   │ F1│ F2│ F3│ F4│ │ F5│ F6│ F7│ F8│ │ F9│F10│F11│F12│ │P/S│S L│P/B│  ┌┐    ┌┐    ┌┐
  └───┘   └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┘  └┘    └┘    └┘
  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐ ┌───┬───┬───┐ ┌───┬───┬───┬───┐
  │~ `│! 1│@ 2│# 3│$ 4│% 5│^ 6│& 7│* 8│( 9│) 0│_ -│+ =│ BacSp │ │Ins│Hom│PUp│ │N L│ / │ * │ - │
  ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤ ├───┼───┼───┤ ├───┼───┼───┼───┤
  │ Tab │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │{ [│} ]│ | \ │ │Del│End│PDn│ │ 7 │ 8 │ 9 │   │
  ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴─────┤ └───┴───┴───┘ ├───┼───┼───┤ + │
  │ Caps │ A │ S │ D │ F │ G │ H │ J │ K │ L │: ;│" '│ Enter  │               │ 4 │ 5 │ 6 │   │
  ├──────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴────────┤     ┌───┐     ├───┼───┼───┼───┤
  │ Shift  │ Z │ X │ C │ V │ B │ N │ M │< ,│> .│? /│  Shift   │     │ ↑ │     │ 1 │ 2 │ 3 │   │
  ├─────┬──┴─┬─┴──┬┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤ ┌───┼───┼───┐ ├───┴───┼───┤ E││
  │ Ctrl│    │Alt │         Space         │ Alt│    │    │Ctrl│ │ ← │ ↓ │ → │ │   0   │ . │←─┘│
  └─────┴────┴────┴───────────────────────┴────┴────┴────┴────┘ └───┴───┴───┘ └───────┴───┴───┘

  Code is far away from bug with the keyboard protecting.

  Author: yangrui
  Created at: 2019/11/21 18:19
  Software: PyCharm
  Description: user-defined function for spark sql.
  return type：udf返回值类型，要添加@udf注解。例如：@udf(returnType=ArrayType(StringType()))
                                                IntegerType()、StringType()
                不添加注解，默认返回值类型为StringType()类型。
"""
import datetime
import json
import re
import time

import diff_match_patch as dmp_module
import jieba
from pyspark.sql.functions import udf
from pyspark.sql.types import *


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def get_json_date_int(column, column2):
    if column:
        datas_tmp = json.loads(column)
        datas = []
        for i in datas_tmp:
            if i:
                datas.append(i)
        if 'alter_formatted' in column2 or 'alter_info' in column2:
            for data in datas:
                if 'altDate' in data:
                    if data['altDate'] != '' and data['altDate'] != '-':
                        if 'AM' in str(data['altDate']) or 'PM' in str(data['altDate']):
                            dates = datetime.datetime.strptime(data['altDate'], '%b %d, %Y %H:%M:%S %p')
                            data['altDate'] = int(dates.timestamp()) * 1000
                        else:
                            if 'T' in str(data['altDate']) and not is_number(data['altDate']):
                                dates = datetime.datetime.strptime(data['altDate'], '%Y-%m-%dT%H:%M:%S')
                                data['altDate'] = int(dates.timestamp()) * 1000
                            else:
                                data['altDate'] = int(data['altDate'])
                    elif data['altDate'] == '' or data['altDate'] == '-':
                        data['altDate'] = None

        elif 'shareholder' in column2:
            for data in datas:
                if 'ACCONDATE' in data:
                    if data['ACCONDATE'] != '' and data['ACCONDATE'] != '-' and data['ACCONDATE']:
                        if data['ACCONDATE'] == 'null':
                            data['ACCONDATE'] = None
                        else:
                            data['ACCONDATE'] = int(data['ACCONDATE'])
                    elif data['ACCONDATE'] == '' or data['ACCONDATE'] == '-':
                        data['ACCONDATE'] = None
                if 'SUBCONDATE' in data:
                    if data['SUBCONDATE'] != '' and data['SUBCONDATE'] != '-' and data['SUBCONDATE']:
                        if data['SUBCONDATE'] == 'null':
                            data['SUBCONDATE'] = None
                        else:
                            data['SUBCONDATE'] = int(data['SUBCONDATE'])
                    elif data['SUBCONDATE'] == '' or data['SUBCONDATE'] == '-':
                        data['SUBCONDATE'] = None
                if 'detail' in data:
                    details = data['detail']
                    if 'subDetails' in details:
                        for subDetail in details['subDetails']:
                            if 'conDate' in subDetail:
                                if subDetail['conDate'] != '' and subDetail['conDate'] != '-':
                                    subDetail['conDate'] = int(subDetail['conDate'])
                                elif subDetail['conDate'] == '' or subDetail['conDate'] == '-':
                                    subDetail['conDate'] = None
                    if 'aubDetails' in details:
                        for aubDetails in details['aubDetails']:
                            if 'conDate' in aubDetails:
                                if aubDetails['conDate'] != '' and aubDetails['conDate'] != '-':
                                    aubDetails['conDate'] = int(aubDetails['conDate'])
                                elif aubDetails['conDate'] == '' or aubDetails['conDate'] == '-':
                                    aubDetails['conDate'] = None
        elif 'be_invest' in column2:
            for data in datas:
                if 'ACCONDATE' in data:
                    if data['ACCONDATE'] != '' and data['ACCONDATE'] != '-' and data['ACCONDATE']:
                        if data['ACCONDATE'] == 'null':
                            data['ACCONDATE'] = None
                        else:
                            data['ACCONDATE'] = int(data['ACCONDATE'])
                    elif data['ACCONDATE'] == '' or data['ACCONDATE'] == '-':
                        data['ACCONDATE'] = None
                if 'SUBCONDATE' in data:
                    if data['SUBCONDATE'] != '' and data['SUBCONDATE'] != '-' and data['SUBCONDATE']:
                        if data['SUBCONDATE'] == 'null':
                            data['SUBCONDATE'] = None
                        else:
                            data['SUBCONDATE'] = int(data['SUBCONDATE'])
                    elif data['SUBCONDATE'] == '' or data['SUBCONDATE'] == '-':
                        data['SUBCONDATE'] = None
        elif 'invest' in column2 or 'branch_info' in column2:
            for data in datas:
                if 'branch_info' in column2:
                    if 'REGCAP' in data:
                        if data['REGCAP'] == "":
                            data['REGCAP'] = None
                        else:
                            if data['REGCAP']:
                                data['REGCAP'] = float(data['REGCAP'])
                if 'ESDATE' in data:
                    if 'ESDATE' in data:
                        if data['ESDATE'] != '' and data['ESDATE'] != '-' and data['ESDATE']:
                            if '-' in str(data['ESDATE']):
                                if not is_number(data['ESDATE']):
                                    if 'T' in data['ESDATE']:
                                        dates = datetime.datetime.strptime(data['ESDATE'], '%Y-%m-%dT%H:%M:%S')
                                        data['ESDATE'] = int(dates.timestamp()) * 1000
                                    else:
                                        dates = datetime.datetime.strptime(data['ESDATE'], '%Y-%m-%d')
                                        data['ESDATE'] = int(dates.timestamp()) * 1000
                            else:
                                data['ESDATE'] = int(data['ESDATE'])
                        elif data['ESDATE'] == '' or data['ESDATE'] == '-':
                            data['ESDATE'] = None
        return json.dumps(datas, ensure_ascii=False)
    return column


def get_json_length(column):
    if column:
        columns = json.loads(column)
        return len(columns)
    return 0


def get_inv_invest(column1, column2, column3):
    names = set([])
    if column1:
        be_invests = json.loads(column1)
        for be_invest in be_invests:
            if 'INV' in be_invest:
                if str(be_invest['INV']) != '':
                    names.add(str(be_invest['INV']))
    if column2:
        key_persons = json.loads(column2)
        for key_person in key_persons:
            if 'name' in key_person:
                if str(key_person['name']) != '':
                    names.add(str(key_person['name']))
    if column3:
        names.add(str(column3))
    list_name = list(names)
    return ','.join(list_name)


@udf(returnType=ArrayType(StringType()))
def get_json_string_list(column):
    if column:
        return json.loads(column)
    return None


@udf(returnType=ArrayType(StringType()))
def get_ent_alter_details(column, column2):
    if column:
        ent_alters = []
        name_values = str(column2).split('&')
        alter_items = json.loads(column)
        name_values_dict = {}
        for name_value in name_values:
            name_values_dict[name_value.split('$')[1]] = name_value.split('$')[0]
        if len(alter_items) > 0:
            for alter_item in alter_items:
                ent_alter = []
                if 'item' in alter_item:
                    if alter_item['item'] in str(column2):
                        ent_alter.append(name_values_dict[alter_item['item']])
                        if 'alterDate' in alter_item:
                            ent_alter.append(str(alter_item['alterDate']))
                        else:
                            alter_item['alterDate'] = None
                        ent_alters.append("&".join(ent_alter))
        if len(ent_alters) > 0:
            return ent_alters
    return ['false&false']


def get_alter_item(column, es_date):
    alter_infos = []
    if column:
        if 'altItem_CN' in str(column):
            alterinfos = json.loads(column)
            distinct_dict = {}
            for alterinfo in alterinfos:
                if alterinfo:
                    if ('altAf' not in alterinfo) and ('altBe' not in alterinfo):
                        continue
                    if ('altAf' in alterinfo and (alterinfo['altAf'] == '' or alterinfo['altAf'] == None)) and (
                            'altBe' in alterinfo and (alterinfo['altBe'] == '' or alterinfo['altBe'] == None)):
                        continue
                    if 'altDate' not in alterinfo:
                        continue
                    if alterinfo['altDate'] == 0 or (alterinfo['altDate'] is None) or alterinfo['altDate'] == '' or \
                            alterinfo[
                                'altDate'] == '-':
                        continue
                    if 'AM' in str(alterinfo['altDate']) or 'PM' in str(alterinfo['altDate']):
                        dates = datetime.datetime.strptime(alterinfo['altDate'], '%b %d, %Y %H:%M:%S %p')
                        alterinfo['altDate'] = int(dates.timestamp()) * 1000
                    elif 'T' in str(alterinfo['altDate']) and not is_number(alterinfo['altDate']):
                        dates = datetime.datetime.strptime(alterinfo['altDate'], '%Y-%m-%dT%H:%M:%S')
                        alterinfo['altDate'] = int(dates.timestamp()) * 1000
                    if int(alterinfo['altDate']) > (int(time.time()) * 1000):
                        continue
                    if es_date != '' and es_date is not None:
                        if int(alterinfo['altDate']) < int(es_date):
                            continue
                    alter_info = {}
                    if 'altItem_CN' in alterinfo:
                        if '-' != alterinfo['altItem_CN'] and len(alterinfo['altItem_CN']) > 0:
                            alter_info['altItemOrigina'] = alterinfo['altItem_CN']
                            altitem_cn = ''
                            if '（' in alterinfo['altItem_CN']:
                                altitem_cn = str(alterinfo['altItem_CN'].split('（')[0])
                            elif '(' in alterinfo['altItem_CN']:
                                altitem_cn = str(alterinfo['altItem_CN'].split('(')[0])
                            else:
                                altitem_cn = alterinfo['altItem_CN']
                            if ('范围' in altitem_cn) or ('项目' in altitem_cn):
                                alter_info['item'] = '经营范围变更'
                            elif ('地址' in altitem_cn) or ('省' in altitem_cn) or (
                                    '县' in altitem_cn) or ('村' in altitem_cn) or (
                                    '乡' in altitem_cn) or ('住所' in altitem_cn) or (
                                    '场所' in altitem_cn) or ('经营地' in altitem_cn):
                                alter_info['item'] = '企业地址变更'
                            elif ('资本' in altitem_cn) or ('总额' in altitem_cn):
                                alter_info['item'] = '注册资本变更'
                            elif '名称' in altitem_cn:
                                alter_info['item'] = '公司名称变更'
                            elif ('增照' in altitem_cn) or ('补照' in altitem_cn) or (
                                    '换照' in alterinfo['altItem_CN']):
                                alter_info['item'] = '增、补、换照'
                            elif '期限' in altitem_cn:
                                alter_info['item'] = '期限变更(经营期限、营业期限、驻在期限变更)'
                            elif '日期' in altitem_cn:
                                alter_info['item'] = '日期变更'
                            elif ('章程' in altitem_cn) or ('备案' in altitem_cn):
                                alter_info['item'] = '章程备案变更'
                            elif ('出资' in altitem_cn) or ('投资' in altitem_cn):
                                alter_info['item'] = '投资人变更(包括出资额、出资方式、出资日期、投资人名称等)'
                            elif ('执照' in altitem_cn) or ('许可' in altitem_cn) or (
                                    '审批' in altitem_cn) or ('证' in altitem_cn):
                                alter_info['item'] = '证件变更'
                            elif ('号码' in altitem_cn) or ('联系' in altitem_cn) or (
                                    '邮政' in altitem_cn) or ('联络' in altitem_cn):
                                alter_info['item'] = '联系方式变更'
                            elif ('机关' in altitem_cn) or ('机构' in altitem_cn) or (
                                    '工商' in altitem_cn) or ('单位' in altitem_cn) or (
                                    '监管' in altitem_cn) or ('部门' in altitem_cn):
                                alter_info['item'] = '监管机构变更'
                            elif ('人' in altitem_cn) or ('代表' in altitem_cn) or (
                                    '者' in altitem_cn) or ('股东' in altitem_cn) or (
                                    '董事' in altitem_cn) or ('经理' in altitem_cn):
                                alter_info['item'] = '负责人变更(法定代表人、负责人、首席代表、合伙事务执行人等变更)'
                            elif '股' in altitem_cn:
                                alter_info['item'] = '股权变更'
                            else:
                                alter_info['item'] = '其他变更'
                            if 'altDate' in alterinfo:
                                # alt_date = alterinfo['altDate']
                                # if len(str(alt_date)) == 10:
                                #     alt_date = alt_date * 1000
                                # elif len(str(alt_date)) > 13:
                                #     alt_date = int(str(alt_date)[0:13])
                                # dateArray = datetime.datetime.fromtimestamp(alt_date / 1000)
                                # otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
                                if 'AM' in str(alterinfo['altDate']) or 'PM' in str(alterinfo['altDate']):
                                    dates = datetime.datetime.strptime(alterinfo['altDate'], '%b %d, %Y %H:%M:%S %p')
                                    alter_info['alterDate'] = int(dates.timestamp()) * 1000
                                elif 'T' in str(alterinfo['altDate']) and not is_number(alterinfo['altDate']):
                                    dates = datetime.datetime.strptime(alterinfo['altDate'], '%Y-%m-%dT%H:%M:%S')
                                    alter_info['alterDate'] = int(dates.timestamp()) * 1000
                                else:
                                    if alterinfo['altDate'] != '':
                                        alter_info['alterDate'] = int(alterinfo['altDate'])
                                    else:
                                        alter_info['alterDate'] = alterinfo['altDate']
                            else:
                                continue
                            if 'altBe' in alterinfo:
                                alter_info['alterBefore'] = str(alterinfo['altBe']).replace('<em>', '').replace('</em>',
                                                                                                                '').replace(
                                    ';',
                                    '|').replace(
                                    '；', '|')
                            else:
                                alter_info['alterBefore'] = ''
                            if 'altAf' in alterinfo:
                                alter_info['alterAfter'] = str(alterinfo['altAf']).replace('<em>', '').replace('</em>',
                                                                                                               '').replace(
                                    ';',
                                    '|').replace(
                                    '；', '|')
                            else:
                                alter_info['alterAfter'] = ''
                            if 'item' in alter_info:
                                if '注册资本变更' in alter_info['item']:
                                    if 'alterAfter' in alter_info:
                                        if ('+' in alter_info['alterAfter']) or ('-' in alter_info['alterAfter']):
                                            alter_before_num = alter_info['alterAfter'].replace('<em>', '').replace(
                                                '</em>',
                                                '')
                                            alter_info['alterAfter'] = alter_before_num.split('(')[0]
                            else:
                                continue
                            if alter_info['alterBefore'] == '' and alter_info['alterAfter'] == '':
                                continue
                            # if '企业地址变更' not in alter_info['item']:
                            if len(alter_info['alterBefore']) > 0 or len(alter_info['alterAfter']) > 0:
                                alter_dict = diff_alter_info(alter_info['alterBefore'], alter_info['alterAfter'])
                                if alter_dict:
                                    if 'alterBefore' in alter_dict:
                                        alter_info['alterBefore'] = alter_dict['alterBefore']
                                    if 'alterAfter' in alter_dict:
                                        alter_info['alterAfter'] = alter_dict['alterAfter']
                                    del alter_dict
                            alter_info_dumps = json.dumps(alter_info, ensure_ascii=False)
                            if alter_info_dumps not in distinct_dict:
                                alter_infos.append(alter_info)
                                distinct_dict[alter_info_dumps] = ''
    if len(alter_infos) > 0:
        return json.dumps(alter_infos, ensure_ascii=False)
    return None


def insertionSort(arr, flag):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr[flag]


def get_diff_alter_info(column):
    if column:
        alterinfos = json.loads(column)
        num = 500
        if len(alterinfos) > num:
            alter_dates = []
            alterinfos_new = []
            for alterinfo in alterinfos:
                if 'altDate' in alterinfo:
                    alter_dates.append(alterinfo['altDate'])
            alter_date_flag = insertionSort(alter_dates, num - 1)
            for alterinfo in alterinfos:
                if 'altDate' in alterinfo:
                    if alterinfo['altDate'] >= alter_date_flag and len(alterinfos_new) < num:
                        alterinfos_new.append(alterinfo)
                    elif len(alterinfos_new) >= num:
                        break
            return json.dumps(alterinfos_new, ensure_ascii=False)
    return column


def diff_alter_info(str1, str2):
    """
        自定义 diff算法: 标记出变化的字符
        :param str1：变更前
        :param str2：变更后
        :return: 不同的标红，返回 dict类型
    """
    if str1 or str2:
        alter_dict = {}
        dmp = dmp_module.diff_match_patch()
        diff = dmp.diff_main(str1, str2)
        str3 = ''
        str4 = ''
        for i in diff:
            if i[0] == 0:
                str3 = str3 + i[1]
                str4 = str4 + i[1]
            if i[0] == -1:
                sp1 = i[1]
                if len(sp1) > 0:
                    str3 = str3 + '<em>%s</em>' % sp1
            elif i[0] == 1:
                sp2 = i[1]
                if len(sp2) > 0:
                    str4 = str4 + '<em>%s</em>' % sp2
        alter_dict['alterBefore'] = str3
        alter_dict['alterAfter'] = str4
        del str1
        del str2
        return alter_dict
    return None


@udf(returnType=ArrayType(StringType()))
def get_json_string_list(column):
    if column:
        return json.loads(column)
    return None


def get_industry_backstepping(column, flag):
    if column:
        industry_list = [("农业", "A 01"), ("林业", "A 02"), ("畜牧业", "A 03"), ("渔业", "A 04"), ("农、林、牧、渔专业及辅助性活动", "A 05"),
                         ("煤炭开采和洗选业", "B 06"), ("石油和天然气开采业", "B 07"), ("黑色金属矿采选业", "B 08"), ("有色金属矿采选业", "B 09"),
                         ("非金属矿采选业", "B 10"), ("开采专业及辅助性活动", "B 11"), ("其他采矿业", "B 12"), ("农副食品加工业", "C 13"),
                         ("食品制造业", "C 14"), ("酒、饮料和精制茶制造业", "C 15"), ("烟草制品业", "C 16"), ("纺织业", "C 17"),
                         ("纺织服装、服饰业", "C 18"), ("皮革、毛皮、羽毛及其制品和制鞋业", "C 19"), ("木材加工和木、竹、藤、棕、草制品业", "C 20"),
                         ("家具制造业", "C 21"), ("造纸和纸制品业", "C 22"), ("印刷和记录媒介复制业", "C 23"), ("文教、工美、体育和娱乐用品制造业", "C 24"),
                         ("石油、煤炭及其他燃料加工业", "C 25"), ("化学原料和化学制品制造业", "C 26"), ("医药制造业", "C 27"), ("化学纤维制造业", "C 28"),
                         ("橡胶和塑料制品业", "C 29"), ("非金属矿物制品业", "C 30"), ("黑色金属冶炼和压延加工业", "C 31"), ("有色金属冶炼和压延加工业", "C 32"),
                         ("金属制品业", "C 33"), ("通用设备制造业", "C 34"), ("专用设备制造业", "C 35"), ("汽车制造业", "C 36"),
                         ("铁路、船舶、航空航天和其他运输设备制造业", "C 37"), ("电气机械和器材制造业", "C 38"), ("计算机、通信和其他电子设备制造业", "C 39"),
                         ("仪器仪表制造业", "C 40"), ("其他制造业", "C 41"), ("废弃资源综合利用业", "C 42"), ("金属制品、机械和设备修理业", "C 43"),
                         ("电力、热力生产和供应业", "D 44"), ("燃气生产和供应业", "D 45"), ("水的生产和供应业", "D 46"), ("房屋建筑业", "E 47"),
                         ("土木工程建筑业", "E 48"), ("建筑安装业", "E 49"), ("建筑装饰、装修和其他建筑业", "E 50"), ("批发业", "F 51"),
                         ("零售业", "F 52"), ("铁路运输业", "G 53"), ("道路运输业", "G 54"), ("水上运输业", "G 55"), ("航空运输业", "G 56"),
                         ("管道运输业", "G 57"), ("多式联运和运输代理业", "G 58"), ("装卸搬运和仓储业", "G 59"), ("邮政业", "G 60"),
                         ("住宿业", "H 61"), ("餐饮业", "H 62"), ("电信、广播电视和卫星传输服务", "I 63"), ("互联网和相关服务", "I 64"),
                         ("软件和信息技术服务业", "I 65"), ("货币金融服务", "J 66"), ("资本市场服务", "J 67"), ("保险业", "J 68"),
                         ("其他金融业", "J 69"), ("房地产业", "K 70"), ("租赁业", "L 71"), ("商务服务业", "L 72"), ("研究和试验发展", "M 73"),
                         ("专业技术服务业", "M 74"), ("科技推广和应用服务业", "M 75"), ("水利管理业", "N 76"), ("生态保护和环境治理业", "N 77"),
                         ("公共设施管理业", "N 78"), ("土地管理业", "N 79"), ("居民服务业", "O 80"), ("机动车、电子产品和日用产品修理业", "O 81"),
                         ("其他服务业", "O 82"), ("教育", "P 83"), ("卫生", "Q 84"), ("社会工作", "Q 85"), ("新闻和出版业", "R 86"),
                         ("广播、电视、电影和录音制作业", "R 87"), ("文化艺术业", "R 88"), ("体育", "R 89"), ("娱乐业", "R 90"),
                         ("中国共产党机关", "S 91"), ("国家机构", "S 92"), ("人民政协、民主党派", "S 93"), ("社会保障", "S 94"),
                         ("群众团体、社会团体和其他成员组织", "S 95"), ("基层群众自治组织及其他组织", "S 96"), ("国际组织", "T 97")]
        if flag == '1':
            for i in industry_list:
                if column in str(i):
                    industry_phy = i[1].split(' ')[0]
                    return industry_phy
        if flag == '2':
            for i in industry_list:
                if column in str(i):
                    industry_big = i[0]
                    return industry_big
    return None


def get_reomve_bracket(column):
    n = str(column).find('（')
    n2 = str(column).find('）')
    for i in range(n, n2 + 1):
        print(i)
        front = str(column)[:n]
        back = str(column)[n + 1:]
        column = front + back
    return column


def get_ent_name_2_firm(results, column2, result_all):
    if results and column2:
        regions = []
        citys = []
        districts = []
        st = []
        s1 = column2.split('*')  # 获得省市县组合list  江西_萍乡-鹰潭-宜春-新余 新建_乌鲁木齐-
        for i in range(0, len(s1)):
            region = s1[i].split('_')[0]
            regions.append(region)  # 获得省
            citys2 = s1[i].split('_')[1].split('-')
            for j in range(0, len(citys2)):
                citys.append(citys2[j])  # 获得市
            districts2 = s1[i].split('_')[2].split('#')
            for k in range(0, len(districts2)):
                districts.append(districts2[k])  # 获得县区
        st.append(str(region) + '&' + str(citys2) + '&' + str(districts2))
        removes = []

        for i in range(0, len(results)):
            result = results[i]
            prefix = result
            if len(result) > 1:
                prefix_res = prefix.replace('省', '').replace('市', '')
                if prefix in str(regions):
                    removes.append(prefix)
                    continue
                if prefix_res in str(regions):
                    removes.append(prefix)
                    continue
                if prefix in str(citys):
                    removes.append(prefix)
                    continue
                if prefix_res in str(citys):
                    removes.append(prefix)
                    continue
                if prefix in str(districts):
                    if i > 0:
                        if results[i - 1] in str(removes):
                            removes.append(prefix)
                            continue
                    else:
                        removes.append(prefix)
                        continue
                prefix_res = prefix
                if '中国' == prefix or '中國' == prefix or '香港' == prefix:
                    removes.append(prefix)
                    continue
                if ('乡' in prefix or '镇' in prefix or '村' in prefix or '区' in prefix or '市' in prefix) and len(
                        prefix) <= 2 and i >= 1:
                    removes.append(results[i - 1])
                    removes.append(results[i])
                    continue
                if len(prefix) > 1:
                    prefix = prefix.replace('市', '').replace('区', '').replace('县', '')
                    if ('镇' in prefix or '村' in prefix) and ('农村' not in prefix):
                        removes.append(prefix_res)
                        continue
                    if prefix + '市' in str(districts):
                        if i > 0:
                            if results[i - 1] in str(removes):
                                removes.append(prefix_res)
                                continue
                        else:
                            removes.append(prefix_res)
                            continue
                    if prefix + '区' in str(districts):
                        if i > 0:
                            if results[i - 1] in str(removes):
                                removes.append(prefix_res)
                                continue
                        else:
                            removes.append(prefix_res)
                            continue
                    if prefix + '县' in str(districts):
                        if i > 0:
                            if results[i - 1] in str(removes):
                                removes.append(prefix_res)
                                continue
                        else:
                            removes.append(prefix_res)
                            continue
                    if '保税区' == prefix:
                        removes.append(prefix_res)
                        continue
                    if prefix == '市':
                        removes.append(prefix_res)
                        continue
        res = []
        for result in results:
            if result not in str(removes):
                res.append(result)
        for i in range(0, len(res)):
            if res[i] == '市':
                continue
            if len(res[i]) == 4:
                return res[i]
            if (len(res) - 1) >= i + 1:
                if len(str(res[i]) + str(res[i + 1])) == 4:
                    if res[i] + res[i + 1] in result_all:
                        return res[i] + res[i + 1]
                    else:
                        return res[i]
                elif len(res[i] + res[i + 1]) > 4:
                    return res[i]
                else:
                    if (len(res) - 1) >= i + 2:
                        if len(res[i] + res[i + 1] + res[i + 2]) == 4:
                            if res[i] + res[i + 1] + res[i + 2] in result_all:
                                return res[i] + res[i + 1] + res[i + 2]
                            else:
                                return res[i] + res[i + 1]
                        elif len(res[i] + res[i + 1] + res[i + 2]) > 4:
                            if res[i] + res[i + 1] in result_all:
                                return res[i] + res[i + 1]
                            else:
                                return res[i]
                        else:
                            if (len(res) - 1) >= i + 3:
                                if len(res[i] + res[i + 1] + res[i + 2] + res[i + 3]) == 4:
                                    if res[i] + res[i + 1] + res[i + 2] + res[i + 3] in result_all:
                                        return res[i] + res[i + 1] + res[i + 2] + res[i + 3]
                                    else:
                                        return res[i] + res[i + 1] + res[i + 2]
                                elif len(res[i] + res[i + 1] + res[i + 2] + res[i + 3]) > 4:
                                    if res[i] + res[i + 1] + res[i + 2] in result_all:
                                        return res[i] + res[i + 1] + res[i + 2]
                                    else:
                                        if res[i] + res[i + 1] in result_all:
                                            return res[i] + res[i + 1]
                                        else:
                                            return res[i]
                                else:
                                    if res[i] + res[i + 1] + res[i + 2] in result_all:
                                        return res[i] + res[i + 1] + res[i + 2]
                                    else:
                                        if res[i] + res[i + 1] in result_all:
                                            return res[i] + res[i + 1]
                                        else:
                                            return res[i]
                            else:
                                if res[i] + res[i + 1] in result_all:
                                    return res[i] + res[i + 1]
                                else:
                                    return res[i]
                    else:
                        if res[i] + res[i + 1] in result_all:
                            return res[i] + res[i + 1]
                        else:
                            return res[i]
            else:
                return res[i]


def get_ent_name_short_jieba(column1, column2):
    """
    param:column1:公司名，column2:省市区拼接
    return:返回商号
    """
    result = column1
    if column1:
        if '（' in column1:
            result = get_reomve_bracket(column1)
        removes = ['建材部', '经济开发公司', '上海事务所', '批发部', '海军东海舰队', '上海代表处', '宾馆', '加工', '销售部', '大兴安岭', '地方', '马达加斯加',
                   '第五研究设计院华中分院', '昌吉州分行', '分理处', '职工', '家属', '生产组', '国营', '汾西新科店', '招待所', '烟代表处', '东莞代表处', '股份公司',
                   '於陵大厦', '驻', '乌鲁木齐代表处', '常州分行健身路分理处', '北京代表处', '海外管理公司', '门市部', '美国', '公司', '义乌代表处', '郑州销售处',
                   '哈尔滨代表处', '韩国', '安亭', '昌西', '红石林业局', '巴基斯坦', '湘西自治州', '伊犁', '中国', '香港', '有限公司', '配件厂', '咨询有限公司',
                   '管理有限公司', '经营部', '手套厂', '分社', '经纪有限公司', '股份清新专卖店', '专卖店',
                   '技术服务开发公司',
                   '服务开发公司', '加工厂', '服务有限公司', '专业合作社', '发展有限公司', '饭店',
                   '有限公司', '有限责任公司', '分公司', '种植场', '服务部', '商贸店', '商贸行', '欢乐海岸', '服装厂', '工作室'
            , '经销处', '服务站', '商行', '大药房', '勘察院', '制品', '商场', '百货店', '包子店', '代理点']
        removes = ['伊犁', '中国', '股份有限公司', '有限公司', '有限责任公司', '股份公司', '分公司', '分厂', '种植场', '批发部', '招待所', '经营部', '合伙企业',
                   '加工厂', '厂']
        removes = ['伊犁', '中国', '股份有限公司', '有限公司', '有限责任公司', '股份公司', '分公司', '分厂', '种植场', '批发部', '招待所', '经营部', '合伙企业',
                   '加工厂', '厂']
        words = ['中国石油', '太平鸟', '双路', '皖西南', '财务', '南华仪器', '咨询', '大药房', '大数据', '长盛', '浴霸']
        for i in words:
            jieba.add_word(i)
        del_words = ['慕田峪长城', '财务咨询', '上海浦东新区', '商讯', '华为技术有限公司', '市长', '四川长虹', '科技开发', '商务信息', '排名', '中国移动通信集团',
                     '浦东发展银行', '石油化工', '富萊雅國際']
        for i in del_words:
            jieba.del_word(i)
        participles = jieba.lcut(result, cut_all=False, HMM=True)
        res = get_ent_name_2_firm(participles, column2, result)
    return res


def get_annals_info(column, column2, column3):
    if column:
        annsocsecinfo = json.loads(column)
        annals_info = {}
        if not column2:
            column2 = ''
        annals_info['report_year'] = column2
        baseInfo = ''
        if column3:
            baseInfo = json.loads(column3)
        if len(baseInfo) > 0 and 'addr' in baseInfo:
            annals_info['geo_address'] = baseInfo['addr']
        if 'so110' in annsocsecinfo:
            annals_info['ann_soc_sec_info'] = annsocsecinfo['so110']
        else:
            annals_info['ann_soc_sec_info'] = ''
        if len(annals_info) > 0:
            return json.dumps(annals_info, ensure_ascii=False)
    return None


def get_key_persons(column):
    if column:
        key_persons = json.loads(column)
        key_persons_new = []
        for key_person in key_persons:
            key_person_new = {}
            if 'NAME' in key_person and 'POSITION' in key_person:
                key_person_new['name'] = key_person['NAME']
                key_person_new['position_cn'] = key_person['POSITION']
                key_persons_new.append(key_person_new)
        if len(key_persons_new) > 0:
            return json.dumps(key_persons_new, ensure_ascii=False)
    return None


def get_be_invest(column):
    if column:
        be_invests = json.loads(column)
        be_invests_new = []
        for be_invest in be_invests:
            be_invest_new = {}
            if 'INV' in str(be_invest) and 'INVTYPE' in str(be_invest):
                if 'INV' in be_invest:
                    be_invest_new['inv'] = be_invest['INV']
                else:
                    be_invest_new['inv'] = ''
                if 'INVTYPE' in str(be_invest):
                    be_invest_new['invtype'] = be_invest['INVTYPE']
                else:
                    be_invest_new['invtype'] = ''
                if 'LISUBCONAM' in str(be_invest):
                    be_invest_new['lisubconam'] = be_invest['LISUBCONAM']
                else:
                    be_invest_new['lisubconam'] = ''
                if 'LIACCONAM' in str(be_invest):
                    be_invest_new['liacconam'] = be_invest['LIACCONAM']
                else:
                    be_invest_new['liacconam'] = ''
                if 'INSTO' in be_invest:
                    be_invest_new['insto'] = be_invest['INSTO']
                else:
                    be_invest_new['insto'] = ''
                be_invests_new.append(be_invest_new)
        if len(be_invests_new) > 0:
            return json.dumps(be_invests_new, ensure_ascii=False)
    return None


def get_branch_info(column, column2):
    if column:
        branch_infos = json.loads(column)
        branch_infos_new = []
        brpcps = ''
        if column2:
            brpcps = json.loads(str(column2))
        for branch_info in branch_infos:
            branch_info_new = {}
            if 'PID' in branch_info:
                branch_info_new['pid'] = branch_info['PID']
                if branch_info['PID'] in str(brpcps):
                    for brpcp in brpcps:
                        if 'br_pid' in brpcp and brpcp['br_pid'] in branch_info['PID']:
                            if 'legal_person_desc' in str(brpcp):
                                branch_info_new['legal_person_desc'] = brpcp['legal_person_desc']
                            if 'reg_cap' in str(brpcp):
                                branch_info_new['reg_cap'] = brpcp['reg_cap']
                            break
            else:
                branch_info_new['pid'] = ''
            if 'ENTNAME' in branch_info:
                branch_info_new['br_name'] = branch_info['ENTNAME']
            else:
                branch_info_new['br_name'] = ''
            if 'TYPE' in branch_info:
                branch_info_new['branch_type'] = branch_info['TYPE']
            else:
                branch_info_new['branch_type'] = ''
            if 'ESDATE' in branch_info:
                branch_info_new['es_date'] = branch_info['ESDATE']
            else:
                branch_info_new['es_date'] = ''
            if 'legal_person_desc' not in str(branch_info_new):
                branch_info_new['legal_person_desc'] = ''
            if 'reg_cap' not in str(branch_info_new):
                branch_info_new['reg_cap'] = ''
            branch_infos_new.append(branch_info_new)
        if len(branch_infos_new) > 0:
            return json.dumps(branch_infos_new, ensure_ascii=False)
    return None


def get_invest(column, column2, column3):
    if column:
        invests = json.loads(column)
        insrs = ''
        if column2:
            insrs = json.loads(column2)
        invests_new = []
        for invest in invests:
            invest_new = {}
            if 'PID' in invest:
                invest_new['pid'] = invest['PID']
                if invest['PID'] in str(insrs) and 'insto' not in invest_new:
                    for insr in insrs:
                        if insr['in_pid'] in invest['PID']:
                            if 'geo_address' in insr:
                                invest_new['geo_address'] = insr['geo_address']
                            # 计算出资比例be_invests
                            if 'be_invest' in insr:
                                be_invests = insr['be_invest']
                                if be_invests and len(be_invests) > 0 and 'insto' not in invest_new:
                                    for be_invest in be_invests:
                                        if 'INV' in be_invest:
                                            if be_invest['INV'] in column3:  # 当前公司
                                                if 'INSTO' in be_invest:
                                                    invest_new['insto'] = be_invest['INSTO']
                                                    break
                                else:
                                    break
            else:
                invest_new['pid'] = ''
            if 'ENTNAME' in invest:
                invest_new['ent_name'] = invest['ENTNAME']
            else:
                invest_new['ent_name'] = ''
            if 'geo_address' not in str(invest_new):
                invest_new['geo_address'] = ''
            if 'LEGALPERSON' in invest:
                invest_new['legal_person_desc'] = invest['LEGALPERSON']
            else:
                invest_new['legal_person_desc'] = ''
            if 'ESDATE' in invest:
                invest_new['es_date'] = invest['ESDATE']
            else:
                invest_new['es_date'] = ''
            if 'insto' not in str(invest_new):
                invest_new['insto'] = ''
            if 'geo_address' not in str(invest_new):
                invest_new['geo_address'] = ''
            invests_new.append(invest_new)
        if len(invests_new) > 0:
            return json.dumps(invests_new, ensure_ascii=False)
    return None


def get_base_info_json(column1, column2, column3):
    dicts = {}
    dicts['br_pid'] = column1
    dicts['legal_person_desc'] = column2
    if column3:
        dicts['reg_cap'] = float(column3)
    else:
        dicts['reg_cap'] = None
    return json.dumps(dicts, ensure_ascii=False)


@udf(returnType=ArrayType(StringType()))
def get_list_pids(column):
    if column:
        branch_infos = json.loads(column)
        pids = []
        for branch_info in branch_infos:
            if 'PID' in branch_info:
                pids.append(branch_info['PID'])
        if len(pids) > 0:
            return pids
    return None


def get_base_info_be_invest_json(column1, column2, column3):
    dicts = {}
    dicts['in_pid'] = column1
    dicts['geo_address'] = column2
    if column3:
        dicts['be_invest'] = json.loads(column3)
    else:
        dicts['be_invest'] = None
    return json.dumps(dicts, ensure_ascii=False)


@udf(returnType=ArrayType(StringType()))
def get_pids(column):
    """
    param column:[{"PID":"72b240d870b346b2b75c6a17fa9ce838","name":"肖庆新"},{"PID":"520fa90bb863d7ec3e3008b4f9af3d44","name":"于思源"},{"PID":"a73813ca1da57b90cee3b71eb3aa556c","name":"天安财产保险股份有限公司濮阳中心支公司"},{"PID":"5d246b978571659885bb22b8d83133cc","name":"高俊阁"}]
    return:b0089cb868ad52789f26d9659fe61387&82c4305c6f9334eb39e3fbbb89370897
    """
    pids = []
    if column:

        if 'PID' in str(column):
            inp_dict = json.loads(str(column))
            for dict in inp_dict:
                pid = dict.get('PID', '1')
                if pid != '1':
                    pids.append(pid)
        # return '&'.join(pids)
    return pids


@udf(returnType=ArrayType(IntegerType()))
def get_tag(column):
    tags = []
    if column:
        for i in range(len(column)):
            if column[i] == 10:
                tags.append(10)
            elif column[i] == 11:
                tags.append(11)
            elif column[i] == 4:
                tags.append(4)
            elif column[i] == 13:
                tags.append(13)
            elif column[i] == 14:
                tags.append(14)
            elif column[i] == 15:
                tags.append(15)
            elif column[i] == 16:
                tags.append(16)
            elif column[i] == 17:
                tags.append(17)
            elif column[i] == 18:
                tags.append(18)
            elif column[i] == 19:
                tags.append(19)
            elif column[i] == 20:
                tags.append(20)
            elif column[i] == 21:
                tags.append(21)
            elif column[i] == 22:
                tags.append(22)
            elif column[i] == 23:
                tags.append(23)
            elif column[i] == 3:
                tags.append(3)
            elif column[i] == 25:
                tags.append(25)
    return tags


def get_string_json_len(column):
    if column:
        return len(json.loads(column))
    return 0


def is_pure_number(number):
    """
    判断是否是纯数字，不能带任何其他符号，只能是数字
    """
    if number:
        sub_str = re.sub("[0-9]", "", number)
        if sub_str == '':
            return True
    return False


def get_privoce_code(un_cid, reg_no):
    if un_cid:
        if len(un_cid) == 18:
            tmp_un = un_cid[2:8]
            if is_pure_number(tmp_un):
                return tmp_un
    if reg_no:
        if len(reg_no) == 15:
            tmp_re = reg_no[0:6]
            if is_pure_number(tmp_re):
                return tmp_re


def get_tag_tmp(column, flag):
    if column:
        tags = []
        map_tag = [(10, '科技型中小企业'), (11, '民营科技企业'), (4, '瞪羚企业'), (13, '专精特精企业')
            , (14, '企业技术中心'), (15, '科技小巨人企业'), (16, '雏鹰企业'), (17, '专精特精小巨人企业'),
                   (18, '众创空间'), (19, '科技企业孵化器'), (20, '技术创新示范企业')
            , (21, '隐形冠军企业'), (22, '技术先进型服务企业'), (23, '牛羚企业'), (3, '独角兽企业'),
                   (25, '创新型企业')]
        map_tag = dict(map_tag)
        tag_code = [
            ('500强', '003-001'), ('民营科技企业', '004-01'), ('专精特精小巨人企业', '004-02'), ('科技企业孵化器', '004-03'),
            ('雏鹰企业', '004-04'), ('牛羚企业', '004-05'), ('专精特精企业', '004-06'), ('隐形冠军企业', '004-07'), ('科技型中小企业', '004-08'),
            ('创新型企业', '004-09'), ('技术创新示范企业', '004-10'), ('科技小巨人企业', '004-11'), ('技术先进型服务企业', '004-12'),
            ('独角兽企业', '004-13'), ('瞪羚企业', '004-14'), ('企业技术中心', '004-15'), ('众创空间', '004-16')]
        tag_code = dict(tag_code)
        for i in column:
            i = int(i)
            if i == 2 and flag == '2':
                # tags.append(tag_code['500强'])
                return tag_code['500强']
                pass
            if i in map_tag:
                tags.append(tag_code[map_tag[i]])
        if len(tags) > 0 and flag != '2':
            return json.dumps(tags, ensure_ascii=False)


def alter_info_repetition(alter_infos):
    if alter_infos:
        # alter_infos=json.loads(alter_infos)
        alter_info_dicts = {}
        alter_info_news = []
        for i in alter_infos:
            if i:
                alter_info = json.dumps(i, ensure_ascii=False)
                if alter_info not in alter_info_dicts:
                    alter_info_dicts[alter_info] = ''
                    alter_info_news.append(i)
        if len(alter_info_news) > 0:
            return alter_info_news


def is_contain_chinese_num_letter(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    check_str = str(check_str)
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
        if u'\u0030' <= ch <= u'\u9fff':
            return True
    return False


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


def is_noe_number(uchar):
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False


def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False


def is_other(uchar):
    """判断是否非汉字，数字和英文字符"""
    if not (is_chinese(uchar) or is_noe_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False


def format_alter_info_name(column):
    if column:
        column = column.replace('(', '（').replace(')', '）').replace('!', '！').replace('?', '？').replace('\'',
                                                                                                        '‘').replace(
            ';', '；').replace('<em>', '').replace('</em>', '')
        alters = json.loads(column)
        for alter_info in alters:
            if alter_info:
                if 'altItem_CN' in alter_info:
                    if alter_info['altItem_CN']:
                        if isinstance(alter_info['altItem_CN'], str):
                            altItem_CN = alter_info['altItem_CN'].lstrip().replace(',', '，').replace(':', '：').replace(
                                '"',
                                '”').replace(
                                '\'', '‘')
                            alter_info['altItem_CN'] = altItem_CN
                            if len(altItem_CN) >= 1:
                                # 判断是否包含字母数字中文
                                sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "",
                                                 str(altItem_CN))
                                if sub_str:
                                    tmp = altItem_CN[0: 1]
                                    if is_other(tmp):
                                        if '（' != tmp and '\'' != tmp and '“' != tmp and '"' != tmp and '’' != tmp and '《' != tmp and '〈' != tmp and '［' != tmp and '｛' != tmp and '【' != tmp and '〖' != tmp:
                                            alter_info['altItem_CN'] = altItem_CN[1:]
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                continue
        for alter_info in alters:
            if alter_info:
                if 'altBe' in alter_info and alter_info['altBe'] and isinstance(alter_info['altBe'], str):
                    altBe = alter_info['altBe'].lstrip().replace(',', '，').replace(':', '：').replace('"', '”').replace(
                        '\'',
                        '‘')
                    alter_info['altBe'] = altBe
                    if len(altBe) >= 1:
                        # 判断是否包含字母数字中文
                        sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", str(altBe))
                        if sub_str:
                            if len(altBe) > 2:
                                if altBe[0:3] == 'em>':
                                    alter_info['altBe'] = alter_info['altBe'][3:]
                            tmp = altBe[0:1]
                            if is_other(tmp):
                                if '（' != tmp and '\'' != tmp and '”' != tmp and '"' != tmp and '‘' != tmp and '《' != tmp and '〈' != tmp and '［' != tmp and '｛' != tmp and '【' != tmp and '〖' != tmp:
                                    alter_info['altBe'] = altBe[1:]
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
        for alter_info in alters:
            if alter_info:
                if 'altAf' in alter_info and alter_info['altAf'] and isinstance(alter_info['altAf'], str):
                    altAf = alter_info['altAf'].lstrip().replace(',', '，').replace(':', '：').replace('"', '”').replace(
                        '\'',
                        '‘')
                    alter_info['altAf'] = altAf
                    if len(altAf) >= 1:
                        if len(altAf) > 2:
                            if altAf[0:3] == 'em>':
                                alter_info['altAf'] = alter_info['altAf'][3:]
                        # 判断是否包含字母数字中文
                        sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", str(altAf))
                        if sub_str:
                            tmp = altAf[0:1]
                            if is_other(tmp):
                                if '（' != tmp and '\'' != tmp and '“' != tmp and '"' != tmp and '’' != tmp and '《' != tmp and '〈' != tmp and '［' != tmp and '｛' != tmp and '【' != tmp and '〖' != tmp:
                                    alter_info['altAf'] = altAf[1:]
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
        alters = alter_info_repetition(alters)
        if alters and len(alters) > 0:
            return json.dumps(alters, ensure_ascii=False)
        else:
            return None


def ent_status_transition(ent_status, ent_status_desc):
    tmp_status = [('存续', '1'), ('在营', '1'), ('开业', '1'), ('在册', '1'), ('在业', '1'), ('正常', '1'),
                  ('吊销', '2'), ('撤销', '2'), ('注销', '3'), ('迁出', '4'), ('迁入', '5'), ('清算', '7'),
                  ('停业', '8'), ('其他', '9')]
    tmp_status_code = [('存续', '001-01'), ('正常', '001-02'), ('开业', '001-03'), ('在业', '001-04'), ('在营', '001-05'),
                       ('在册', '001-06'),
                       ('吊销', '001-07'), ('撤销', '001-08'), ('注销', '001-09'), ('迁入', '001-10'), ('迁出', '001-11'),
                       ('停业', '001-12'), ('清算', '001-13')
        , ('其他', '001-14'), ('歇业', '001-15'), ('责任关闭', '001-16')]
    ent_status_map = dict(tmp_status)
    tmp_status_code = dict(tmp_status_code)
    if ent_status and ent_status_desc:
        for (key, value) in ent_status_map.items():
            if str(ent_status) == value and key in ent_status_desc:
                return tmp_status_code[key]
    else:
        return None


def group_name_desc_transition(column):
    if column:
        group_name_descs = [('展览馆协会', '008-001'), ('电路板行业协会', '008-002'), ('翻译协会', '008-003'), ('工程咨询协会', '008-004'),
                            ('广交会', '008-005'), ('消防协会', '008-006'), ('文化用品行业协会', '008-007'), ('律师协会', '008-008'),
                            ('中国船舶集团', '008-009'), ('中国华能集团', '008-010'), ('中国中信集团', '008-011'), ('中国中化集团', '008-012'),
                            ('北京建工集团山西建设', '008-013'), ('中国中钢集团', '008-014'), ('中国医药集团', '008-015'),
                            ('中国新时代控股集团', '008-016'), ('中国兵器装备集团', '008-017'), ('中国五矿集团', '008-018'),
                            ('中国建筑集团', '008-019'), ('中国信达资产集团', '008-020'), ('中铁城建集团', '008-021'),
                            ('江西省天然气集团', '008-022'), ('机械学院研究总院集团', '008-023'), ('天津能源集团', '008-024'),
                            ('中国建银投资集团', '008-025'), ('中国通用技术集团', '008-026'), ('招商局集团', '008-027'),
                            ('中国石油化工集团', '008-028'), ('中国宝武钢铁集团', '008-029'), ('亚泰集团', '008-030'),
                            ('中国华融资产集团', '008-031'), ('中国信息通信科技集团', '008-032'), ('中光学集团', '008-033'),
                            ('湖南江滨机器集团', '008-034'), ('中国长江三峡集团', '008-035'), ('中国出版集团', '008-036'),
                            ('中国银河金融集团', '008-037'), ('中国冶金地质集团', '008-038'), ('中轻集团', '008-039'),
                            ('国家电力投资集团', '008-040'), ('机械科学研究总院集团', '008-041'), ('中国检验认证集团', '008-042'),
                            ('浙建集团', '008-043'), ('中国太平保险集团', '008-044'), ('宝钢工程技术集团', '008-045'),
                            ('矿冶科技集团', '008-046'), ('江苏省国信集团', '008-047'), ('中国航空集团', '008-048'),
                            ('中国诚通控股集团', '008-049'), ('中国国际工程咨询集团', '008-050'), ('中国旅游集团', '008-051'),
                            ('中铁建工集团', '008-052'), ('中国农业发展集团', '008-053'), ('四川能投集团', '008-054'), ('华润集团', '008-055'),
                            ('甘肃省电力投资集团', '008-056'), ('国机集团', '008-057'), ('中国铁路物资集团', '008-058'),
                            ('陕西延长石油集团', '008-059'), ('中国林业集团', '008-060'), ('中国交通建设集团', '008-061'),
                            ('大屯煤电集团', '008-062'), ('通号工程局集团', '008-063'), ('中国电力建设集团', '008-064'),
                            ('中国工商银行集团', '008-065'), ('南光集团', '008-066'), ('中国民航信息集团', '008-067'),
                            ('中国长城资产集团', '008-068'), ('北京建工集团', '008-069'), ('中国第一汽车集团', '008-070'),
                            ('中国华录集团', '008-071'), ('中国航天科工集团', '008-072'), ('中国钢研科技集团', '008-073'),
                            ('中国电子信息产业集团', '008-074'), ('中国石化集团', '008-075'), ('国投集团', '008-076'),
                            ('中国华电集团', '008-077'), ('交通银行集团', '008-078'), ('山东能源集团', '008-079'), ('市政建设集团', '008-080'),
                            ('中国航空工业集团', '008-081'), ('新兴际华集团', '008-082'), ('中国电建集团', '008-083'),
                            ('中铁大桥勘探设计院集团', '008-084'), ('中国农业银行集团', '008-085'), ('北京市政路桥集团', '008-086'),
                            ('国家能源投资集团', '008-087'), ('中国机械工业集团', '008-088'), ('中国远洋海运集团', '008-089'),
                            ('中国宝武集团', '008-090'), ('中国建筑科学集团', '008-091'), ('中国化学工程集团', '008-092'),
                            ('中国兵器工业集团', '008-093'), ('中国航空发动机集团', '008-094'), ('中国铁道建筑集团', '008-095'),
                            ('国家开发投资集团', '008-096'), ('中国核工业集团', '008-097'), ('中国能源建设集团', '008-098'),
                            ('中国普天信息产业集团', '008-099'), ('中国铁路工程集团', '008-100'), ('中国航天科技集团', '008-101'),
                            ('中国电子科技集团', '008-102'), ('中国光大集团', '008-103'), ('国家电网集团', '008-104'),
                            ('中国黄金集团', '008-105'), ('中国有色矿业集团', '008-106'), ('中国中煤能源集团', '008-107')]
        group_name_descs = dict(group_name_descs)
        if column in group_name_descs:
            return group_name_descs[column]


def stock_type_transition(column):
    if column:
        stock_types = [('新四板', '006-07'), ('新三板', '006-06'), ('创业板', '006-05'), ('中小板', '006-04'), ('A股', '006-01'),
                       ('科创板', '006-03')]
        stock_types = dict(stock_types)
        if column in stock_types:
            return stock_types[column]
        pass


def json_array_marge(column):
    if column:
        columns = column.split('&')
        data_all = []
        for i in columns:
            if '[' in i:
                data_all = data_all + json.loads(i)
            elif i:
                data_all.append(i)
        if len(data_all) > 0:
            return json.dumps(data_all, ensure_ascii=False)


def marge_flads(column1, column2):
    lists = []
    if column1:
        lists.append(column1)
    if column2:
        lists.append(column2)
    if len(lists) > 0:
        return json.dumps(lists, ensure_ascii=False)


def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    if check_str:
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
    return False


def is_chinese_all_str(string):
    """
    检查整个字符串是否为中文
    Args:
        string (str): 需要检查的字符串,包含空格也是False
    Return
        bool
    """
    for chart in string:
        if chart < u'\u4e00' or chart > u'\u9fff':
            return False

    return True


if __name__ == '__main__':
    print(is_contain_chinese("AA在"))
    # print(get_privoce_code('91.21090474710317','912.10904747103'))
    # print(capital_rate('123.1香港万元'))
    # test_json = '[{"altDate": 1474128000000,"altItem_CN": "注册资本变更"},null,{"altItem_CN": "注册资本变更", "altBe": "10.000000", "altAf": "100.000000", "altDate": 1474128000000}]'
    # test_json ='[null]'
    # print(get_alter_item(test_json, '123445678787'))
    pass
