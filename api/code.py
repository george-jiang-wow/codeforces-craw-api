import io
import json
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
from PIL import Image, ImageDraw, ImageFont
class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path.startswith('/code'):
            params = parse.parse_qs(parse.urlparse(self.path).query)
            user_wants_data = params.get('data', [''])[0]
            self.send_response(200)
            self.send_header('Content-Type', 'image/jpeg')
            self.end_headers()
            cookies={"__client_id":token,"_uid":"395758"}
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47 BOTE"}
            re=r.get("https://www.luogu.com.cn/user/395758",headers=headers,cookies=cookies)
            headers["X-CSRF-TOKEN"]=re.text.split('<meta name="X-Csrf-Token" content="')[1].split('">')[0]
            usersetting=user_wants_data
            payload = {'submissionId': usersetting, 'csrf_token': re.text.split('<meta name="X-Csrf-Token" content="')[1].split('">')[0]}
            url = 'https://codeforc.es/data/submitSource'
            response = requests.post(url,headers=headers,cookies=cookies,data=payload)
            txt1 = response.text
            ans=txt1
            self.wfile.write(ans)
            return
