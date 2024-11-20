import requests
import json


# 爬取的为塞力斯股票
def get_climb():
    url="https://stock.xueqiu.com/v5/stock/chart/kline.json"#抓包工具抓到的url

    # 由于爬取的网站原因，需要时常更新请求头和url的参数
    headers={
    'accept':'application/json, text/plain, */*',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cooki':'cookiesu=271728460102456; device_id=b1fb2e9385fecf2fcce67e9e25557341; s=al137hnugz; xq_a_token=691d6f0a678b98a172affb89759b9c46fd23b4e2; xqat=691d6f0a678b98a172affb89759b9c46fd23b4e2; xq_r_token=de180625dcdde2e538953eb202d55300cae40fe1; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTczNDM5Njg3MiwiY3RtIjoxNzMxOTAzNzk0OTAzLCJjaWQiOiJkOWQwbjRBWnVwIn0.nW2HfVt06_JFxAy-ZtNjTJsrW0XZF901UiYdk1f4w8RESO4cksHAbMSur4MMKlg_Xq_xFDHJN9zDk_ASVGp70tw8H1zD57rkT82Skk0nsaDFNJE2PIruefyHc_Qs0FJLFUM0WY3EtrE9CFHO5FAWewjGB_Yh9yd7NEpLq4Yx2ZRA_Orgv-tzSbsEoFSu7pcknn9Nj_LISyutToUE5KArpIsBUCBdtnddII7EX85V8dOM1wY3cPLcJgkPUhurwfBV_MuaAFJvggrKb_RDfFR_kAgt1nuqWmNRUThE6QtKBv2jyCKt2qMM-iFNTKkKj9GplxQHqHyiP2sLp91bP_PmbQ; u=271728460102456; Hm_lvt_1db88642e346389874251b5a1eded6e3=1729751712,1730193218,1731481766,1731903846; HMACCOUNT=90E645C6C593862A; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1731903917; ssxmod_itna=eqGxuQqiqYutDX7DHYTKCDUxxRgn=D7wxDtKiAqDl=DWqeGzDAxn40iDtxaLWbYhDqHeCg8PrWU7Gm03r8SjSm+atx+40aDbqGkK0Q44GGRxBYDQxAYDGDDPDocPD1D3qDkD7h6CMy1qGWDm4sDYyFDQHGe4DFc2IOP4i7DDyQkx07Y/KxDG5xGb078QKxe4Drka717tvxvIDkD75+DlpdcbDkW8dUejyEXIGGL7KDXOQDv1ywRhgeXc5z43raQADeD2ioOkaK+B4oYA2DCHi58iG4Kiio8mr90TDD=E1K4D; ssxmod_itna2=eqGxuQqiqYutDX7DHYTKCDUxxRgn=D7wxDtKiKDnxnKxDsfDw6EAlbDj4qh7U2hCcU=7HXsxdEx08DewGD==',
    'origin':'https://xueqiu.com',
    'priority':'u=1, i',
    'referer':'https://xueqiu.com/',
    'sec-ch-ua':'"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile':'?1',
    'sec-ch-ua-platform':'"Android"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-site',
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0',
    }#请求头
    param_data={
        'symbol':'SH601127',
        'begin':'1731990318274',
        'period':'day',
        'type':'before',
        'count':'-142',
        'indicator':'kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance',
        'md5__1632':'n4%2BxuDyD0DgD9DfhDmx0vfbiK4TO7YD0ObmYTD'
    }
    #url中所带的参数

    resp=requests.get(url=url,headers=headers,params=param_data)
    print(resp.text)
    data_json=json.loads(resp.text)

    column=data_json['data']['column']
    items=data_json['data']['item']
    return items
    # print(column)
    #print(items)




