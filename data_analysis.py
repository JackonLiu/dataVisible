#coding=utf-8
import pandas as pd
import json

import codecs
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

from props import history_score

font_set = FontProperties(fname=r"/home/lxp/文档/others/simsun.ttc", size=15)
csv_data = pd.read_csv('5_chengji.csv')
student = pd.read_csv('2_student_info.csv')
'汇总各个科目班级历史最高分趋势和历史最低分趋势'
"分析各个班级平均分、原始分、绝对分排名，支持总分和单科目；"
"对班级学生排名分布情况进行统计，包括总分和单科目；"
"对每个班级每个分数段学生排名人数进行统计;"
"比对不同班级学生考试总分，在不同分数段的分布情况，比对指标包括：原始分、标准分、离均值；"
"比对不同班级学生考试每个科目，在不同分数段的分布情况，比对指标包括：原始分、标准分、离均值。"


fig, ax = plt.subplots()
# 筛选政治科目的数据
mes_sub_name=csv_data['mes_sub_name']
exam_term_all=csv_data['exam_term']
sub_name=list(set(mes_sub_name))
#把float数据转化为str
class_name = [str(x) for x in sub_name]
class_name.remove('1B模块总分')
class_name.remove('nan')
exam_term=list(set(exam_term_all))
exam_term.sort()
for name in class_name:
    select_class = csv_data[csv_data['mes_sub_name'] == name]
    for term in exam_term:
        class_term = select_class[select_class['exam_term'] == term]
        class_term_Score = class_term['mes_Score']
        maxScore = class_term_Score.max()
        minScore = class_term_Score.min()
        # 对多级嵌套数据进行赋值
        history_score[name][term][0] = maxScore
        history_score[name][term][1] = minScore
        # mes_T_Score为y, 同时设置s=10为气泡大小，并设置颜色透明度等
        ax.scatter(history_score[name][term][0], term,
                   s=20, alpha=0.6)
        ax.scatter(history_score[name][term][1], term,
                   s=20, alpha=0.6)


    ax.set_xlabel(u'该科目最高、最低成绩趋势', fontproperties=font_set)
    ax.set_ylabel(u'学期', fontproperties=font_set)
    ax.set_title(u'学生成绩气泡图', fontproperties=font_set)

    # 显示网格
    ax.grid(True)
    fig.tight_layout()
    plt.show()



json_data = json.dumps(history_score, ensure_ascii=False,indent = 4)

with codecs.open('maxScore.json', 'a',encoding='utf-8') as f_six:
    f_six.write(json_data)

    #折线图
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # ax.plot(history_score[name][term][0], term)
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.legend(['该科目最高、最低成绩趋势', '学期'], fontproperties=font_set)
    # plt.show()

    # 条形图
    # means_men = (20, 35, 30, 35, 27)
    # std_men = np.arange(73)
    #
    # opacity = 0.4
    # error_config = {'ecolor': '0.3'}
    # n_groups = 5 ##组数
    # ##生成0, 1, 2, 3, ...
    # index = np.arange(n_groups)
    # bar_width = 0.05  ## 条的宽度
    # className = history_score[name]['mes_sub_name']
    # mes_StudentID = history_score[name]['mes_StudentID']
    # mes_T_Score = history_score[name]['mes_T_Score']
    #
    # ## 条形图的第一类条
    # rects1 = plt.bar(mes_T_Score, bar_width,
    #                  alpha=opacity,
    #                  color='b',
    #                  error_kw=error_config,
    #                  label='score')
    # plt.xlabel(u'学生ID', fontproperties=font_set)
    # plt.ylabel(u'学生成绩', fontproperties=font_set)
    # plt.title(u'学生成绩条形图', fontproperties=font_set)
    # plt.xticks(index + bar_width, mes_T_Score)
    #
    # plt.legend()  # 显示标注
    # ## 自动调整subplot的参数给指定的填充区
    # plt.tight_layout()
    # plt.show()



# 最基本的循环
# for i in history_score:
#     print(i, history_score[i])
#
# # 这种循环花的时间比第一种长，建议使用第一种循环
# for k, v in history_score.items():
#     print(k, v)



