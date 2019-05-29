import requests
import json

# Get (내놔) => Get a HTML
# Post (받아라) => Post a Data


url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=859'
data = requests.get(url).text
lotto_data = json.loads(data)

print(lotto_data['firstWinamnt'])

'bit.do/4th4deep'