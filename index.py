#coding=utf-8

import util
import news
import risk
import tips
import covid

if __name__ == '__main__':
    all_data = covid.get_all_data()
    risk_area = risk.get_risk_area()
    risk_area_merge = risk.get_risk_area_merge()
    news_list = news.get_news_list()
    tips_list = tips.get_tips_list()

    util.write_json('all_data', all_data)
    util.write_json('risk_area', risk_area)
    util.write_json('risk_area_merge', risk_area_merge)
    util.write_json('news_list', news_list)
    util.write_json('tips_list', tips_list)
