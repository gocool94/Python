from urllib.request import urlopen

import re

url = "https://www.livechennai.com/Vegetable_price_chennai.asp"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]

pattern = re.compile(
    r'^<tr> <td align="center"> <img src="images/Avarai\.jpg" width="50" height="40" border="0"></td> <td>Avarai \(1 Kg\) : <img src="images/avari-tamil\.jpg" ></td> <td align="right">45\.00</td></tr> <tr>$',
    re.IGNORECASE)

print(pattern.match(html))
