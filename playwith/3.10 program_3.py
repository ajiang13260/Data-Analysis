import requests,re

r = requests.get('https://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1')
r.encoding = r.apparent_encoding  # 这步什么用？解码编码？
pattern = re.compile('teams/.*?">(.*?)<.*?>\s+</figure>\s+</td>\s+<td></td>\s+.*?>(.*?)</td>\s+<.*?>(.*?)</td>\s+.*?>(.*?)</td>')
p = re.findall(pattern,r.text)
print(p)