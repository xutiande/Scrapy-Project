# import json
#
# with open('data.json', 'r', encoding='utf-8') as f:
#     text = json.load(f)
#     big_category_len = len(text['data'][-5]['s'][0]['s'])
#     for lens in range(big_category_len):
#         big_category_link = {}
#         big_category_link__list = text['data'][-5]['s'][0]['s'][lens]['s']  # 获取到链接处
#         big_category_name_list = text['data'][-5]['s'][0]['s'][lens]['n']  # 获取类名
#         big_category_name = big_category_name_list.split('|')[1]  # 提取
#         link_list = []
#         for i in big_category_link__list:  # 对链接进行清洗
#             link = i['n'].split('|')[0]
#             if '-' in link:
#                 split_link = 'https://list.jd.com/list.html?cat=' + ','.join(link.split("-"))
#                 link_list.append(split_link)
#             else:
#                 link_list.append('https://' + link)
#             big_category_link['big_category'] = big_category_name
#             big_category_link['big_category_link'] = link_list
#     print(big_category_link['big_category_link'][0])
