# web2.py
#웹서버에 페이지 실행 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup
#블럭 주석 : ctrl + /
# <td class="title">
# 				<a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" onclick="nclk_v2(event,'lst.title','20853','50')">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# 						</td>