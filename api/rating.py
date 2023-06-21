import io
import json
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
from PIL import Image, ImageDraw, ImageFont
class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path.startswith('/rating'):
            params = parse.parse_qs(parse.urlparse(self.path).query)
            user_wants_data = params.get('data', [''])[0]
            self.send_response(200)
            self.send_header('Content-Type', 'image/jpeg')
            self.end_headers()
            usersetting=user_wants_data
            url = 'https://www.spoj.com/users/'+usersetting+'/'
            response = requests.get(url)
            txt1 = response.text
            problem_sloved=txt1.split("Problems solved</dt>\n\t\t\t\t\t\t\t\t<dd>")[1].split("</dd>")[0]
            solution_accepted=txt1.split("Solutions submitted</dt>\n\t\t\t\t\t\t\t\t<dd>")[1].split("</dd>")[0]
            font_path = './data/font.ttf'
            font = ImageFont.truetype(font_path, 20)
            img_size = (7*len(problem_sloved)+92, 28)
            img_color = (255, 255, 255)
            img_text = f"AC: {problem_sloved} ; Solution: {solution_accepted}" 
            img = Image.new('RGB', img_size, img_color)
            draw = ImageDraw.Draw(img)
            draw.text((5, 5), img_text, font=font, fill=(0, 0, 0))
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG")
            img_byte = buffered.getvalue()
            self.wfile.write(img_byte)
            return
