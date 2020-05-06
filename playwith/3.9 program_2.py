import requests,re
# from bs4 import BeautifulSoup


# r = requests.get('https://money.cnn.com/data/dow30/')
  
# pattern = re.compile('''class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span><\/td>\s+.*?class="wsod_stream">(.*?)<\/span>''')
# p = re.findall(pattern,r.text)
# print(p)

def retrieve_dji_list():
    r = requests.get('https://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span><\/td>\s+.*?class="wsod_stream">(.*?)<\/span>')
    
    dji_list_in_text = re.findall(search_pattern,r.text)
    return dji_list_in_text

dji_list = retrieve_dji_list()
print(dji_list)