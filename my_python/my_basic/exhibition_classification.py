# -*- coding:utf-8 -*-
# Author: Lane
# Date: 2023/3/4 14:39
import asyncio
from pathlib import Path
import numpy as np
import pandas as pd
from collections import defaultdict
import re

# from similarity.pipline import sentence2tensor

# config_pd = pd.read_excel('./exhibition_classification_word_config v2.xlsx')
# print(config_pd.to_dict())
nan = None
_config = {'食品饮品': {0: '饼干', 1: '糕点', 2: '零食', 3: '麻花', 4: '巧克力制品', 5: '肉', 6: '食品', 7: '薯片', 8: '糖果', 9: '饮品', 10: '餐饮', 11: '茶餐', 12: '外卖', 13: '酒', 14: '乳制品', 15: '乳业', 16: '饮食', 17: nan, 18: nan, 19: nan, 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan, 37: nan, 38: nan, 39: nan, 40: nan, 41: nan, 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '五金建材': {0: '板材', 1: '防水工程', 2: nan, 3: '建材', 4: '建筑', 5: '建筑加固', 6: '室内装饰', 7: '土木', 8: '土石方', 9: '装修', 10: '装潢', 11: '五金', 12: '陶瓷', 13: '钩锁', 14: '铰链', 15: '弹簧', 16: '合页', 17: '泵阀', 18: '泵', 19: '阀', 20: '阀门', 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan, 37: nan, 38: nan, 39: nan, 40: nan, 41: nan, 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '商贸综合': {0: '财务顾问', 1: '传媒', 2: '财务咨询', 3: '储蓄业务', 4: '存款', 5: '代理兑付', 6: '代理发行', 7: '代理记账', 8: '贷款', 9: '担保', 10: '公关处理', 11: '电子商务', 12: '商业综合', 13: '会务', 14: '会议及展览服务', 15: '活动策划', 16: '加盟', 17: '进出口', 18: '连锁', 19: '履约', 20: '贸易', 21: '票据', 22: '票据承兑', 23: '品牌管理', 24: '品牌塑造', 25: '企业管理', 26: '企业形象策划', 27: '融资', 28: '商贸', 29: '商业贸易', 30: '税务服务', 31: '诉讼保全', 32: '贴现', 33: '投资', 34: '网络推广', 35: '写大字', 36: '信用社', 37: '宣传片', 38: '银行', 39: '营销', 40: '债券', 41: '债券发行', 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '工业制造': {0: nan, 1: '设备', 2: '配件', 3: '零件', 4: '阀门', 5: '机械', 6: '金属', 7: '仪器仪表', 8: '零部件', 9: nan, 10: '农机', 11: '工业', 12: '机械', 13: nan, 14: '仪器', 15: '暖通', 16: '制冷', 17: '仪表', 18: nan, 19: nan, 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan, 37: nan, 38: nan, 39: nan, 40: nan, 41: nan, 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '药品保健': {0: '(?<!不含)(?<!非)药', 1: '(?<!不含)(?<!非)医', 2: '核酸', 3: '健康咨询', 4: '口服', 5: '临床', 6: '轮椅', 7: '生物', 8: '卫生', 9: '细胞', 10: '血糖', 11: '血脂', 12: '胰岛素', 13: '诊疗', 14: '健康管理', 15: '养生保健', 16: '口腔', 17: '生命科技', 18: nan, 19: nan, 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan, 37: nan, 38: nan, 39: nan, 40: nan, 41: nan, 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '宠物农林': {0: '宠物', 1: '动物', 2: '鹅(?!肉)', 3: '狗(?!肉)', 4: '水果', 5: '花卉', 6: '鸡(?!肉)', 7: '家禽', 8: '林木', 9: '驴(?!肉)', 10: '猫(?!肉)', 11: '苗', 12: '牛(?!肉)', 13: '农业', 14: '蔬', 15: '树(?!立)', 16: '饲料', 17: '兔(?!肉)', 18: '鸭(?!肉)', 19: '羊(?!肉)', 20: '养殖', 21: '鱼(?!肉)', 22: '园艺', 23: '种植', 24: '种子', 25: '猪(?!肉)', 26: '园林', 27: '水产品', 28: '粮油', 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan, 37: nan, 38: nan, 39: nan, 40: nan, 41: nan, 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '化工环保': {0: '环保', 1: '噪声', 2: '排污', 3: '除尘', 4: '酸雾', 5: '净化', 6: '除臭', 7: '尾气', 8: '污水', 9: '废', 10: '污染', 11: '环境', 12: '节能', 13: '净水', 14: '清淤', 15: '清洁', 16: '橡胶', 17: '塑料', 18: '橡胶制品', 19: 'EDTA', 20: '氨', 21: '醇', 22: '肥料', 23: '复合肥', 24: '隔膜', 25: '化肥', 26: '化学', 27: '碱', 28: '胶骨', 29: '胶管', 30: '硫酸', 31: '钠', 32: '尿素', 33: '硼', 34: '醛', 35: '软管', 36: '塑料制品', 37: '酸钠', 38: '烯', 39: '纤维', 40: '酰卤', 41: '橡塑', 42: '盐酸', 43: '有机', 44: '元素肥', 45: '酯', 46: '再生资源', 47: '化工', 48: '资源回收', 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '电子软件': {0: '变电', 1: 'IT设备', 2: 'SMT', 3: '电力', 4: '电子(?!商)', 5: '软件', 6: '数码', 7: '通信', 8: '通讯', 9: '信息技术', 10: '智能设备', 11: '科技', 12: '数字技术', 13: '技术开发(?!区)', 14: '计算机软.?件', 15: '互联网安全', 16: '人工智能', 17: '数据服务', 18: '物联网技术', 19: '技术服务', 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan, 37: nan, 38: nan, 39: nan, 40: nan, 41: nan, 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '能源电力': {0: '氢能', 1: '能源', 2: '煤', 3: '燃煤', 4: '风能', 5: '燃料', 6: '电池', 7: '风电', 8: '节能', 9: '焦炭', 10: '热力', 11: '水力', 12: '太阳能', 13: '矿', 14: nan, 15: '暖通', 16: '制冷', 17: '合金', 18: '钢铁', 19: '冶金', 20: '光伏', 21: '机电', 22: '矿产', 23: '电力', 24: '新能源', 25: '光电', 26: '加油站', 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan, 37: nan, 38: nan, 39: nan, 40: nan, 41: nan, 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '美容珠宝': {0: '美容', 1: '医美', 2: '美发', 3: '美肤', 4: '整形', 5: '医学美容', 6: '理发', 7: '整容', 8: '化妆', 9: nan, 10: '美甲', 11: '洗头', 12: '护理', 13: '皮肤', 14: '口红', 15: '首饰', 16: '珠宝', 17: '个人护理', 18: '钟表眼镜', 19: '奢侈品', 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan, 37: nan, 38: nan, 39: nan, 40: nan, 41: nan, 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '房产家居': {0: '房.?产', 1: '厨具', 2: '橱柜', 3: '储物箱', 4: '灯具', 5: '吊顶', 6: '儿童房', 7: '置业', 8: '房屋', 9: '家居', 10: '家具', 11: '建材装饰', 12: nan, 13: '居间', 14: '门窗', 15: '全屋', 16: '沙发', 17: '商品房', 18: '家用电器', 19: '梳妆台', 20: '衣柜', 21: '椅', 22: '桌', 23: '租房', 24: '卫浴', 25: '家电', 26: '照明', 27: '浴室', 28: '电视', 29: '住房', 30: '房地产咨询', 31: '餐具', 32: '地毯', 33: '挂毯', 34: '地产', 35: nan, 36: nan, 37: nan, 38: nan, 39: nan, 40: nan, 41: nan, 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '安防防护': {0: '安防', 1: '报警', 2: '监控', 3: '安全防范', 4: '对讲', 5: '门禁', 6: '防盗(?!门)', 7: '安全技术', 8: '信息安全', 9: '保安', 10: '防范工程', 11: '消防', 12: '入侵', 13: '防盗', 14: '灾', 15: '定位', 16: '安全器材', 17: '防火', 18: '防水', 19: '保险柜', 20: '抗爆', 21: '保密', 22: '泄爆', 23: '防弹', 24: '防护', 25: '警示', 26: '护罩', 27: '屏蔽', 28: '防雷', 29: '避雷', 30: '劳防', 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan, 37: nan, 38: nan, 39: nan, 40: nan, 41: nan, 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '文教娱乐': {0: '代言', 1: '电视剧', 2: '电影', 3: '吊床', 4: '动画', 5: '动漫', 6: '歌曲', 7: '共享服务', 8: '观光', 9: '广播电视', 10: '户外', 11: '活动组织', 12: '健身', 13: '降落伞', 14: '节目', 15: '剧情', 16: '刻字', 17: '乐器', 18: '礼仪', 19: '美术', 20: '明星', 21: '模特', 22: '品牌包装', 23: '棋', 24: '庆典', 25: '沙滩', 26: '商演', 27: '摄影', 28: '收藏', 29: nan, 30: '体育', 31: '铁石装饰品', 32: '网红', 33: '文化', 34: '文艺', 35: '文娱', 36: '舞台', 37: '形象设计', 38: '休闲', 39: '衍生', 40: '演出', 41: '艺人', 42: '艺术', 43: '音乐', 44: '音响', 45: '音像', 46: '影视', 47: '游戏', 48: '娱乐', 49: '瑜伽', 50: '桌游', 51: '自行车', 52: '办公用品', 53: '媒体', 54: '文教', 55: '出版', 56: '教育', 57: '婚庆', 58: '麻将', 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '礼品玩具': {0: '礼品', 1: '芭比', 2: '抱枕', 3: '布偶', 4: '创意', 5: '公仔', 6: '挂件', 7: '积木', 8: '吉祥物', 9: '纪念品', 10: '拼图', 11: '棋', 12: '人偶', 13: '台.?历', 14: '娃娃', 15: '玩具', 16: '益智', 17: '节日用品', 18: nan, 19: nan, 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan, 37: nan, 38: nan, 39: nan, 40: nan, 41: nan, 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '旅游运输': {0: '旅游', 1: '班车', 2: '搬运', 3: '水路', 4: '仓储', 5: '车辆租赁', 6: '出国', 7: '出入境', 8: '航线', 9: '回程', 10: '货运', 11: '机票', 12: '接机', 13: '景区', 14: '酒店', 15: '客车租赁', 16: '空运', 17: '陆运', 18: '旅行', 19: '旅行社', 20: '票务', 21: '签证', 22: '水运', 23: '物流', 24: '一日游', 25: '运输', 26: '文旅', 27: '装卸', 28: '海运', 29: '承运', 30: '客运', 31: '多式联运', 32: '门票', 33: '车辆', 34: '摩托车', 35: '汽摩配件', 36: '汽车', 37: '船舶', 38: '船', 39: '住宿', 40: '宾馆', 41: '酒店', 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '服装纺织': {0: '服装', 1: '运动套装', 2: '床上用品', 3: '针织', 4: '休闲装', 5: '童装', 6: '工装', 7: '睡衣', 8: '连衣裙', 9: '羽绒服', 10: '西裤', 11: '袜', 12: '鞋', 13: '校服', 14: '制服', 15: '衬衫', 16: '西服', 17: '西装', 18: '皮革制品', 19: '箱包', 20: '纺织品', 21: '运动服', 22: '家纺', 23: '配饰', 24: '珠宝', 25: '金银', 26: '首饰', 27: '钟表', 28: '眼镜', 29: '工艺品', 30: '钻石', 31: '戒指', 32: '吊坠', 33: '手链', 34: '手镯', 35: '翡翠', 36: '银饰', 37: '玉器', 38: '耳钉', 39: '耳环', 40: '玉石', 41: '内衣', 42: '服饰', 43: '皮革', 44: '纺织', 45: '纺机', 46: '服装', 47: '婴童展', 48: '男装', 49: '女装', 50: '男女装', 51: '竹席', 52: '裘革', 53: '羽绒', 54: '棉服', 55: '袜子', 56: '鞋袜', 57: '裙子', 58: nan, 59: '涤纶', 60: '化纤', 61: nan, 62: nan, 63: '面料', 64: '绒', 65: nan, 66: nan, 67: '丝绸', 68: nan, 69: '亚麻', 70: '酒店用品', 71: '毯'}, '包装印刷': {0: '报纸', 1: '彩印', 2: '出版', 3: '打印', 4: '复印', 5: '海报', 6: '画册', 7: '课本', 8: '期刊', 9: '书籍', 10: '书刊', 11: '台历', 12: '网印', 13: '宣传册', 14: '宣传单', 15: '印染', 16: '印刷', 17: '印务', 18: '杂志', 19: '纸张', 20: '装订', 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan, 37: nan, 38: nan, 39: nan, 40: nan, 41: nan, 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}, '其他展会': {0: '家政', 1: '保洁', 2: '综合展会', 3: '物业', 4: '养老', 5: '宗教', 6: '广告', 7: '广告行业', 8: '委员会', 9: '保险', 10: '协会', 11: '网吧', 12: nan, 13: nan, 14: nan, 15: nan, 16: nan, 17: nan, 18: nan, 19: nan, 20: nan, 21: nan, 22: nan, 23: nan, 24: nan, 25: nan, 26: nan, 27: nan, 28: nan, 29: nan, 30: nan, 31: nan, 32: nan, 33: nan, 34: nan, 35: nan, 36: nan, 37: nan, 38: nan, 39: nan, 40: nan, 41: nan, 42: nan, 43: nan, 44: nan, 45: nan, 46: nan, 47: nan, 48: nan, 49: nan, 50: nan, 51: nan, 52: nan, 53: nan, 54: nan, 55: nan, 56: nan, 57: nan, 58: nan, 59: nan, 60: nan, 61: nan, 62: nan, 63: nan, 64: nan, 65: nan, 66: nan, 67: nan, 68: nan, 69: nan, 70: nan, 71: nan}}
exhibition_type_df_and_tensor: tuple = None


####################################################################


async def get_exhibition_type_df_and_tensor():
    """读取展会分类目录, 以及对应的向量"""

    file_dir = Path(__file__).parent
    df_path = file_dir.joinpath("会刊分类.xlsx")
    exhibition_type_df = pd.read_excel(df_path, sheet_name='优化')

    # 过滤掉'exh_name'列中非str类型的数据
    filter_index = exhibition_type_df['exh_name'].apply(lambda x: isinstance(x, str))
    exhibition_type_df = exhibition_type_df.loc[filter_index]

    target = exhibition_type_df['exh_name'].tolist()
    tensor_path = file_dir.joinpath("会刊分类_exh_name_tensor.npy")
    if tensor_path.exists():
        vecs = np.load(tensor_path)
    else:
        target_tensor = [sentence2tensor(i) for i in target]
        target_tensor = await asyncio.gather(*target_tensor)

        # 尽量减小消耗的内存
        vecs = np.concatenate(target_tensor, axis=0)
        vecs = np.dot(vecs, 100)
        vecs = vecs.astype(np.half)
        np.save(tensor_path, vecs)
    return exhibition_type_df, vecs


async def get_exhibition_type_from_sim_tensor(exhibition_name: str):
    global exhibition_type_df_and_tensor
    if exhibition_type_df_and_tensor is None:
        # 内部标签
        exhibition_type_df_and_tensor = await get_exhibition_type_df_and_tensor()
    # 外部标签
    exhibition_type_tensor = await sentence2tensor([exhibition_name])
    exhibition_type_tensor = (exhibition_type_tensor * 100).astype(np.half)

    similarity = (exhibition_type_df_and_tensor[1] * exhibition_type_tensor).sum(axis=1)
    similarity_index = np.argmax(similarity)
    inner_exhibition_type = exhibition_type_df_and_tensor[0].iloc[similarity_index]

    # 因为乘了两次，所以需要除掉
    return inner_exhibition_type["会刊分类"], np.max(similarity) / 10000

class ClassificationOfExhibitors:
    """参展企业分类"""
    def __init__(self):
        # self.config_pd = config_pd
        self.config_pd = pd.DataFrame.from_dict(_config)
        self.init_keys_dict()
        # self.check_repeat_keys()

    def init_keys_dict(self):
        self.gt_one_name_keys = {}
        self.name_keys = {}
        for name in self.config_pd.columns:
            keys = self.config_pd[name].tolist()
            keys = [*filter(lambda x: isinstance(x, str), keys)]
            self.name_keys[name] = '|'.join(keys)

            gt_one_keys = filter(lambda x: len(x) > 1, keys)
            self.gt_one_name_keys[name] = '|'.join(gt_one_keys)

    def check_repeat_keys(self):
        """显示出同一关键词在不同目录下存在"""
        keys_dict = {}
        for name in self.config_pd.columns:
            keys = self.config_pd[name].tolist()
            keys = [*filter(lambda x: isinstance(x, str), keys)]
            keys_dict[name] = set(keys)

        names = list(keys_dict.keys())
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                common_elements = keys_dict[names[i]] & keys_dict[names[j]]
                if len(common_elements) > 0:
                    print(f"{names[i]}, {names[j]} repeat elements: {common_elements}")

    def exhibition_classification(self, name: str, op_scope: str, content: str, threshold=0.1, diff=None):
        score_dict = defaultdict(float)

        # 名称中存在，超过两个字的单词，得分乘8
        if name and isinstance(name, str):
            for k, v in self.gt_one_name_keys.items():
                re_find = re.findall(v, name)
                count = len(re_find)
                if count > 0:
                    score_dict[k] = count * 8.5
                    # if k in diff:
                    # print(f"name: {name}")
                    # print(f"{k} find in name: {re_find}")

        # 经营范围中出现 乘0.618
        if op_scope and isinstance(op_scope, str):
            for k, v in self.name_keys.items():
                re_find = re.findall(v, op_scope)
                count = len(re_find)
                if count > 0:
                    score_dict[k] += count * 0.618
                    # if k in diff:
#                     print(f"op_scope: {op_scope}")
#                     print(f"{k} find in op_scope: {re_find}")

            # 商贸综合：销售、批发
            sell_regx = "销售|零售|批发|零售"
            re_find = len(re.findall(sell_regx, op_scope))
            if re_find:
                score_dict['商贸综合'] += re_find * 0.618 * 0.28

        # 其他中出现 乘1.618
        if content and isinstance(content, str):
            for k, v in self.name_keys.items():
                re_find = re.findall(v, content)
                count = len(re_find)
                if count > 0:
                    score_dict[k] += count * 0.618 * 2
                    # if k in diff:
#                     print(f"content: {content}")
#                     print(f"{k} find in content: {re_find}")

        # 特殊行业特殊处理
        for k, v in score_dict.items():
            if k == "工业制造":
                score_dict[k] *= 0.85

        # 计算平均得分
        if score_dict:
            total_score = sum(score_dict.values())
            score_dict = {
                k: round(v / total_score, 4)
                for k, v in score_dict.items()
            }
        else:
            score_dict["其他展会"] = 1

        return {
            k: v
            for k, v in score_dict.items() if v > threshold
        }

class TheClassificationOfTheExhibitionItself(ClassificationOfExhibitors):
    """展会本身的分类"""
    def __init__(self):
        super().__init__()
        xlsx_path = Path(__file__).parent.joinpath("exhibition_classification_word_config v2.xlsx")
        self.config_pd = pd.read_excel(xlsx_path)
        self.init_keys_dict()
        # self.check_repeat_keys()

    def classification(self, exhibit_name, exhibit_desc, exhibit_scope):
        score_dict = defaultdict(float)

        # 名称中存在，超过两个字的单词，得分乘10
        if exhibit_name and isinstance(exhibit_name, str):
            for k, v in self.gt_one_name_keys.items():
                re_find = re.findall(v, exhibit_name)
                count = len(re_find)
                if count > 0:
                    score_dict[k] = count * 10
                    # print(f"{k} find in exhibit_name: {re_find}")

        # 展会范围中出现 乘0.618
        if exhibit_scope and isinstance(exhibit_scope, str):
            for k, v in self.name_keys.items():
                re_find = re.findall(v, exhibit_scope)
                count = len(re_find)
                if count > 0:
                    score_dict[k] += count * 0.618
#                     print(f"{k} find in op_scope: {re_find}")

        # 其展会描述出现 乘0.618
        if exhibit_desc and isinstance(exhibit_desc, str):
            for k, v in self.name_keys.items():
                re_find = re.findall(v, exhibit_desc)
                count = len(re_find)
                if count > 0:
                    score_dict[k] += count * 0.618
#                     print(f"{k} find in content: {re_find}")

        # 计算平均得分
        total_score = 0
        if score_dict:
            total_score = sum(score_dict.values())
            score_dict = {
                k: round(v / total_score, 4)
                for k, v in score_dict.items()
            }
        else:
            score_dict["其他展会"] = 1

        # score_dict["total_score"] = total_score
        return {
            k: v
            for k, v in score_dict.items()
        }



def main1():
    er = ClassificationOfExhibitors()
    name = "宁波市江北红苹果床上用品有限公司"
    op = """
    家纺制品、草席、竹席的制造、加工、批发、零售、代购代销；纺织原料、服饰、日用百货、化妆品、箱包、皮革制品、工艺品、玩具、家具的批发、零售。
    """
    co = """
    宁波市江北红苹果床上用品有限公司位于浙江省宁波市江北甬江街道梅堰路503弄8号，主营幼儿园，宾馆，酒店床上用品，订做各种规格花色的被子，床垫枕芯枕套三件套，四件套多件套等床上用品。        宁波江北红苹果床上用品有限公司是一家专业设计幼儿园宾馆酒店床上用品的民营企业，公司自创立以来秉承顾客至上，锐意进取的经营理念，坚持质量第一信誉至上的原则为广大经营者提供优质的产品和服务，多年来一直为多家知名的品牌公司贴牌生产，同多家正规超市商场酒店宾馆幼儿园医院有着良好的合作关系。        公司生产的产品采用优质的原材料手感柔软贴身舒适花色齐全，款式多样，做工精细，风格独特具有国际时尚最新潮流。        公司将本着“互利共赢诚信务实”的原则欢迎新老客户来我公司参观考察，我公司将为您提供诚信周到的服务。官网：、宁波市江北红苹果床上用品有限公司是一家经工商注册、依法经营的企业，位于浙江-，详细地址（浙江省宁波市江北区梅堰路503弄8号），这里人文、创业环境好，各类交通发达。电话（87638072）。 宁波市江北红苹果床上用品有限公司是（家具批发）等产品与及服务的专业提供商，拥有完整、科学的管理与服务体系及先进的生产设备，服务及产品质量有保障。 我们一贯坚持“质量第一，用户至上，优质服务，信守合同”的宗旨，凭借着高质量的产品，良好的信誉，优质的服务，用户遍布各地。 您如果对我们的产品感兴趣的话，可以直接在线提交采购信息我们会及时跟您联系。、宁波市江北红苹果床上用品有限公司位于浙江省宁波市江北甬江街道梅堰路503弄8号，主营幼儿园，宾馆，酒店床上用品，订做各种规格花色的被子，床垫枕芯枕套三件套，四件套多件套等床上用品。 宁波江北红苹果床上用品有限公司是一家专业设计幼儿园宾馆酒店床上用品的民营企业，公司自创立以来秉承顾客至上，锐意进取的经营理念，坚持质量第一信誉至上的原则为广大经营者提供优质的产品和服务，多年来一直为多家的品牌公司贴牌生产，同多家正规超市商场酒店宾馆幼儿园医院有着良好的合作关系。 公司生产的产品采用优质的原材料手感柔软贴身舒适花色齐全，款式多样，做工精细，风格独特具有国际时尚潮流。 公司将本着“互利共赢诚信务实”的原则欢迎新老客户来我公司参观考察，我公司将为您提供诚信周到的服务。、宁波市江北红苹果床上用品有限公司成立于2001年,注册资金50万元人民币。是一家有限责任公司（自然人投资或控股），宁波市江北红苹果床上用品有限公司法人是张川，主要面象—市场，客户群为—。****50人，公司经营模式为生产型，不断提升企业的核心竞争力，使企业在发展中树立起良好的社会形象。主营范围：，凭借专业的水平和成熟的技术。公司将始终坚持“质量*，信誉*”的宗旨，以科学的管理手段，雄厚的技术力量，将不断深化改革，创新机制，适应市场，全面发展，欢迎各界朋友莅临参观、指导和业务洽谈。、本公司成立于2011年8月我们有好的产品和专业的团队，公司发展迅速，我们为客户提供的产品、良好的技术支持、健全的售后服务，宁波市江北红苹果床上用品有限公司是生产加工各种布袋知名企业，如果您对我公司的产品服务有兴趣，请在线留言或者来电咨询。、宁波市江北红苹果床上用品有限公司位于浙江江南水乡兼海港城市宁波，具体地址是浙江省宁波市江北区梅堰路503弄8号，在宁波工商注册成立，注册资本，主要经营项目为： 家具批发。本单位为客户提供服务的同时，也使企业得到发展。 本单位是生活服务 批发零售行业内企业，如果您对我们的产品或服务有兴趣，期待您在线留言或者来电咨询，我们将在收到您的信息后，回复您！、主营床上用品，汽车配件包装布袋等等，目前需要扩大规模，需吃苦耐劳的熟练缝纫工、本公司成立于2011年8月   我们有好的产品和专业的团队，公司发展迅速，我们为客户提供最好的产品、良好的技术支持、健全的售后服务，宁波市江北红苹果床上用品有限公司是生产加工各种布袋知名企业，如果您对我公司的产品服务有兴趣，请在线留言或者来电咨询。联系方式是13867861395，欢迎您的来电。、宁波市江北红苹果床上用品有限公司 位于浙江省宁波市江北甬江街道梅堰路503弄8号，主营幼儿园，宾馆，酒店床上用品，订做各种规格花色的被子，床垫枕芯枕套三件套，四件套多件套等床上用品。 宁波江北红苹果床上用品有限公司是一家*设计幼儿园宾馆酒店床上用品的民营企业，公司自创立以来秉承顾客至上，锐意进取的经营理念，坚持质量**信誉至上的原则为广大经营者提供**的产品和服务，多年来一直为多家的**公司贴牌生产，同多家正规*市商场酒店宾馆幼儿园医院有着良好的合作关系。 公司生产的产品采用**的原材料手感柔软贴身舒适花色齐全，款式多样，做工精细，风格*特具有**时尚较新潮流。 公司将本着“互利共赢诚信务实”的原则欢迎新老客户来我公司参观考察，我公司将为您提供诚信周到的服务。、简要介绍： 宁波市江北红苹果床上用品有限公司成立于(2014-07-20)，位于:浙江省宁波市江北区梅堰路503弄8号，企业注册资金 1031（万元），职员团队不断壮大，现有人数（500-1000人），企业实力强，经营状况良好，是你可以放心的合作伙伴。 我们主要提供:家具批发等产品与服务，对于产品与服务，我们严格进行质量管理，以满足用户需求为已任，力争为用户提供优质完善的解决方案。对我们的产品与服务有兴趣你可以电话咨询(87638072)。 宁波市江北红苹果床上用品有限公司一直以“品质保证、服务专业、顾客满意”为经营宗旨，以“求仁为大、求利为小、真正服务为人民”为经营理念，开拓进取，务实创新。 目前宁波市江北红苹果床上用品有限公司在业界已有一定的知名度。 陈荣光欢迎各界朋友来人、来函、来电、来邮与我们联系洽谈合作！、宁波市江北红苹果床上用品有限公司 位于浙江省宁波市江北甬江街道梅堰路503弄8号，主营幼儿园，宾馆，酒店床上用品，订做各种规格花色的被子，床垫枕芯枕套三件套，四件套多件套等床上用品。 宁波江北红苹果床上用品有限公司是一家专业设计幼儿园宾馆酒店床上用品的民营企业，公司自创立以来秉承顾客至上，锐意进取的经营理念，坚持质量第一信誉至上的原则为广大经营者提供优质的产品和服务，多年来一直为多家知名的品牌公司贴牌生产，同多家正规超市商场酒店宾馆幼儿园医院有着良好的合作关系。 公司生产的产品采用优质的原材料手感柔软贴身舒适花色齐全，款式多样，做工精细，风格独特具有国际时尚最新潮流。 公司将本着“互利共赢诚信务实”的原则欢迎新老客户来我公司参观考察，我公司将为您提供诚信周到的服务。、宁波市江北红苹果床上用品有限公司位于浙江省宁波市江北甬江街道梅堰路503弄8号，主营幼儿园，宾馆，酒店床上用品，订做各种规格花色的被子，床垫枕芯枕套三件套，四件套多件套等床上用品。 宁波江北红苹果床上用品有限公司是一家专业设计幼儿园宾馆酒店床上用品的民营企业，公司自创立以来秉承顾客上，锐意进取的经营理念，坚持信誉上的原则为广大经营者提供优质的产品和服务，多年来一直为多家知名的品牌公司贴牌生产，同多家正规超市商场酒店宾馆幼儿园医院有着良好的合作关系。 公司生产的产品采用优质的原材料手感柔软贴身舒适花色齐全，款式多样，做工精细，风格独特具有国际时尚潮流。 公司将本着“互利共赢诚信务实”的原则欢迎新老客户来我公司参观考察，我公司将为您提供诚信周到的服务。、宁波市江北红苹果床上用品有限公司位于浙江省宁波市江北甬江街道梅堰路503弄8号，主营幼儿园，宾馆，酒店床上用品，订做各种规格花色的被子，床垫枕芯枕套三件套，四件套多件套等床上用品。 宁波江北红苹果床上用品有限公司是一家专业设计幼儿园宾馆酒店床上用品的民营企业，公司自创立以来秉承顾客至上，锐意进取的经营理念，坚持质量第一信誉至上的原则为广大经营者提供优质的产品和服务，多年来一直为多家知名的品牌公司贴牌生产，同多家正规超市商场酒店宾馆幼儿园医院有着良好的合作关系。 公司生产的产品采用优质的原材料手感柔软贴身舒适花色齐全，款式多样，做工精细，风格独特具有国际时尚新潮流。 公司将本着“互利共赢诚信务实”的原则欢迎新老客户来我公司参观考察，我公司将为您提供诚信周到的服务。&各种帆布绒布，宁波被子厂家，各类床上用品，宁波家纺床品 ，宁波酒店床上用品，宁波床上用品批发，生产加工各种布袋，宁波宾馆穿上用品，宁波床上用品批发 ，宁波宾馆床上用品，宁波被子批发，幼儿园床上用品，宁波家纺床品，宁波被子批发 ，家具批发，宁波被子厂家 &家纺制品、草席、竹席的制造、加工、批发、零售、代购代销；纺织原料、服饰、日用百货、化妆品、箱包、皮革；家纺制品、草席、竹席的制造、加工、批发、零售、代购代销；纺织原料、服饰、日用百货、化妆品、箱包、皮革制品、工艺品、玩具、家具的批发、零售。；宁波家纺床品，宁波被子厂家，宁波宾馆穿上用品；床品套装；家具批发&宁波市江北红苹果床上用品有限公司，2001年08月13日成立，经营范围包括一般经营项目：家纺制品、草席、竹席的制造、加工、批发、零售、代购代销等。
    """
    sco = er.exhibition_classification(name, op, co)
    import pprint
    pprint.pprint(sco)
    check_dff = lambda x: er.exhibition_classification(
        x['ent_name'],
        x['op_scope'],
        x['res'],
    )
    df = pd.read_excel('reg_date.xlsx')
    df['cls_score'] = df.apply(check_dff, axis=1)
    df["all_cls"] = df["cls_score"].map(
        lambda x: ",".join(x.keys() if x else '')
    )

    import operator
    def get_best_role(score_dict: dict):
        max_score = max(score_dict.items(), key=operator.itemgetter(1))
        best_role = [max_score[0]]
        for k, v in score_dict.items():
            if max_score[0] != k and max_score[1] == v:
                best_role.append(k)
        return ','.join(best_role)
    df["best_cls"] = df["cls_score"].map(get_best_role)
    df['cls_score'] = df['cls_score'].map(lambda x: ','.join([f"{k}:{v}" for k,v in x.items()]))
    df.to_excel(f"v3_classification.xlsx", index=False, engine='xlsxwriter')


def main2():
    name = "越南国际家具及木工机械展览会"
    scope = """
    展品范围：1.干燥设备、锯木机械、锯木厂设备，木材车削机、木材弯曲机、黏合机、钻孔及填装圆木榫机、人造板生产设备，粉尘收集设备；2.木材前处理机械及设备，木材加工机械及设备气动工具、电动工具等；木材加工机械及设备；3.木材及木器传送技术；4.油漆，喷涂及抛光技术、涂料及粘合剂等；油漆，喷涂、胶合；原木及木匠工具。5.家具装饰材料、家具配件与家具五金、家具生产材料、家具半成品与部件等；6.家具构配件家具装饰五金；喷漆及干燥设备、刀具及配件等各式家具的生产设备和工具，贴面、装饰纸及表面处理材料、封边条、织物与皮革、原辅材料与配件，家居配套用品等。7.原木、木材、人造板及板材、木皮、贴面、装饰纸及表面处理材料、木材及木器传送技术；林业成套设备，营林采伐设备。
    """
    desc = """
    2013年越南国际家具及木工机械展举办时间：2013年10月12日-15日举办地点：越南胡志明市SECC国际展览中心展会回顾：2009年的第八届越南国际木工机械展出面程达23,500平米，占地800个摊位，345家来自全球21个国地/地区参与展会，其中包括澳洲、中国、丹麦、法国、德国、香港、印度、意大利、日本、马来西亚、菲律宾、新加坡、台湾、泰国、瑞士、西班牙、美国及越南。展出的主题为各式木工机械、刀具、配件及木工家具半成品等。展品范围：1.干燥设备、锯木机械、锯木厂设备,木材车削机、木材弯曲机、黏合机、钻孔及填装圆木榫机、人造板生产设备,粉尘收集设备；2.木材前处理机械及设备,木材加工机械及设备气动工具、电动工具等；木材加工机械及设备；3.木材及木器传送技术；4.油漆，喷涂及抛光技术、涂料及粘合剂等；油漆，喷涂、胶合；原木及木匠工具。5.家具装饰材料、家具配件与家具五金、家具生产材料、家具半成品与部件等；6.家具构配件家具装饰五金；喷漆及干燥设备、刀具及配件等各式家具的生产设备和工具,贴面、装饰纸及表面处理材料、封边条、织物与皮革、原辅材料与配件，家居配套用品等。7.原木、木材、人造板及板材、木皮、贴面、装饰纸及表面处理材料、木材及木器传送技术；林业成套设备,营林采伐设备。市场介绍：1.越南是继中国之外的最大的欧美家具产业转移的地区。2.随着越南对欧盟、美、日家具出口的扩大，越南家具市场已成为全球增长速度最快，最受瞩目的家具出口市场。该国家具业者如雨后春笋般迅速发展。据不完整统计，2006年1月-10月，越木制家具出口金额达8.35亿USD，全年可望达到10亿美金，该行业中共有2000家生产、加工企业和300多家具出口企业。3.越南已与台湾签订国家层次的投资保障协定、避免双重课税协定、农渔业合作协定及台越劳工协定。我经济部亦正推动签署贸易协定及暂准通关协定。4.越南政府鼓励木制品出口，放宽相关木制品出口规定，及成立富财、同奈、平阳等专业性的大型木制品生产地，在显示越南政府重视越南木业的发展。加上越南木制品甚受欧盟、美国及日本青睐，以及越南木制品企业引进先进之木制品加工技术设备，提升产品在国际市场竞争力。5.目前越南木制品出口潜力超过马来西亚、泰国及印尼等，由于越南木制品品质较佳及价钱比泰国和印尼低于3％至5％。目前约80％至85％之木材供加工木制品均从国外输入越南市场。CNENA
    """
    er = TheClassificationOfTheExhibitionItself()
    sco = er.classification(name, desc, scope)
    import pprint
    pprint.pprint(sco)


def main3():
    tsv_from_data_lake_path = "part-00000-0bd554fc-2e0d-4f04-a7ff-0aa70ccf7ef6-c000.csv"
    df = pd.read_csv(tsv_from_data_lake_path, sep="\t")
    df = df.dropna(subset=['identity'])
    def get_best_role(score_dict: dict):
        max_score = max(score_dict.items(), key=operator.itemgetter(1))
        best_role = [max_score[0]]
        for k, v in score_dict.items():
            if max_score[0] != k and max_score[1] == v:
                best_role.append(k)
        return ','.join(best_role)

    import json
    df["identity"] = df["identity"].str.replace(r'\\"', '"')
    df["identity"] = df["identity"].str.replace(r'\\', '"')
    df["identity"] = df["identity"].str.replace(r'}"', '}')
    # df["identity"] = df["identity"].str.replace(r'}"', '"}')
    df["identity"] = df["identity"].map(eval)
    df["best_cls"] = df["identity"].map(get_best_role)
    df['identity'] = df['identity'].map(lambda x: ','.join([f"{k}:{v}" for k, v in x.items()]))
    save_path = tsv_from_data_lake_path.split('.')
    df.to_excel(f"{save_path[0]}_classification.xlsx", index=False, engine='xlsxwriter')

if __name__ == '__main__':
    import operator

    main1()
    # main2()
    # main3()


