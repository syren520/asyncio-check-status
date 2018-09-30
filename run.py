import requests

cookies = {
    'JSESSIONID': 'B6A51910C87E68C5EDDB996030A88E85',
    '_ga': 'GA1.3.1020197703.1535345432',
    '_gid': 'GA1.3.404415782.1538255720',
    '_gat_GSA_ENOR0': '1',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://egov.uscis.gov',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://egov.uscis.gov/casestatus/mycasestatus.do',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,nl;q=0.8,zh-CN;q=0.7,zh;q=0.6,zh-TW;q=0.5,es;q=0.4',
}

data = {
  'changeLocale': '',
  'completedActionsCurrentPage': '',
  'upcomingActionsCurrentPage': '',
  'appReceiptNum': 'WAC1815151099',
  'caseStatusSearchBtn': 'CHECK STATUS'
}

response = requests.post('https://egov.uscis.gov/casestatus/mycasestatus.do', headers=headers, cookies=cookies, data=data)

print(response.text)

