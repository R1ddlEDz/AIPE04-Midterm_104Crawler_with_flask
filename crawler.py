import requests
from bs4 import BeautifulSoup as bs
import re
from pprint import pprint
from time import sleep
import random


def find_jobs(keyword=None, area=None, ro=1, jobexp=1, page=1):
    custom_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
        "Referer": "https://www.104.com.tw/jobs/search"
    }
    url = "https://www.104.com.tw/jobs/search/api/jobs?"

    job_params = {
        "ro": 1,  # 0全部職缺 1正2兼
        "jobexp": 1,  # 工作經驗 1年以下
        "page": page,  # 網頁第幾頁
        # "keyword" : "", #關鍵字
        # "area" : "", #地區 6001001000(台北市) 6001002000 (新北市) 6001005000 (桃園市) 6001006000 (新竹縣市)
    }

    if keyword is not None:
        job_params['keyword'] = keyword

    if area is not None:
        job_params['area'] = area

    if jobexp != 1:
        job_params['jobexp'] = jobexp

    if ro != 1:
        job_params['ro'] = ro

    # url = f'https://www.104.com.tw/jobs/search/api/jobs?area={area}&jobsource=index_s&keyword={key_word}&mode=s&order=15&page=1&pagesize=20{job_exp}'

    all_jobs = []

    # total_page = int(data['metadata']['pagination']['count'])
    total_page = 99999999
    page = 1

    res = requests.get(url, headers=custom_headers, params=job_params)
    data = res.json()
    if total_page == 99999999:
        total_page = int(data['metadata']['pagination']['count'])

    jobs = data['data']
    all_jobs.extend(jobs)
    print(f"正在擷取第{job_params['page']}頁...")
    print(f"已擷取全部資料，總共獲得{len(all_jobs)}筆資料")

    filtered_list = []  # 整理過的資料 包含日期，應徵人數，公司名稱，工作名稱，以及網頁連結
    keep_keys = ['appearDate', 'applyCnt', 'custName', 'jobName', 'link']
    # target_list = data['data']
    for data_list in all_jobs:
        new_data = {
            key: data_list[key]
            for key in keep_keys
            if key in data_list
        }
        if 'link' in data_list and 'job' in data_list['link']:
            new_data['link'] = data_list['link']['job']
        filtered_list.append(new_data)

    job_id_list = []  # 每個104網站的id
    for item in filtered_list:
        job_id_list.append(item['link'][-5:])

    return filtered_list, job_id_list, total_page


def get_job_deails(job_id):
    url = f'https://www.104.com.tw/api/jobs/{job_id}'
    c_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
        "Referer": "https://www.104.com.tw/"
    }
    r = requests.get(url, headers=c_headers)
    datatest = r.json()

    if 'data' not in datatest:
        print("API 回傳資料沒有 data：")
        print(datatest)
        return {}

    job_details_keepkeys = [
        # jobDescription在jobDetail裡面 salary也在jobDetail裡面
        'jobDescription', 'salary', 'addressRegion', 'addressDetail',
    ]
    condition_list_keepkeys = [
        'workExp', 'edu', 'major', 'language', 'other'
    ]
    job_details_list = {
        key: (datatest['data']['jobDetail'][key]).replace(
            "\n", "").replace("\r", "").replace("\t", "")
        for key in job_details_keepkeys
    }
    condition_list = {
        key: (datatest['data']['condition'][key])
        for key in condition_list_keepkeys
    }

    if condition_list.get('language') and len(condition_list['language']) > 0:
        condition_list['language'] = condition_list['language'][0]['language']
    else:
        condition_list['language'] = ''

    if condition_list.get('other'):
        condition_list['other'] = condition_list['other'].replace(
            "\n", "").replace("\r", "").replace("\t", "")
    else:
        condition_list['other'] = ''
    job_details_list.update(condition_list)

    return (job_details_list)


def search_jobs(keyword=None, area=None, ro=0, page=1):
    filtered_list, job_id_list, total_page = find_jobs(
        keyword=keyword,
        area=area,
        ro=ro,
        page=page
    )
    count = len(job_id_list)
    for job, job_id in zip(filtered_list, job_id_list):
        count -= 1
        print(f"正在查詢工作內容: {job_id}，還有{count}個")
        details = get_job_deails(job_id)
        job.update(details)
        sleep(random.uniform(0.8, 1.1))
    return filtered_list, total_page
