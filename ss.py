import requests

url = "https://www.iq.zain.com/ar/signin"

payload = "_session_key=phj5Yzbp2n7evcaVMubo4vMYDIfr8YNyI4ahitsG&_token=pJCdfCaPkyUhqteoLZqhNftJdiYnGb2rWU2Kiudu&login={}&password={}&remember=on&__ncforminfo=eMku4F0YlWhP_8tBn0oRefKmyWDnG6i-59UvMX1iRlRfH9ECG5MCR1LcvJsIzmP45zAqm_FM1rYSgdR_0qro1y-0K3IbBByUtam1IiQ4YRBYEhL03YAmuNmJS_iIwzoaXZ1Q-albATw%3D"

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/x-www-form-urlencoded",
  'sec-ch-ua': "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
  'sec-ch-ua-mobile': "?1",
  'X-OCTOBER-REQUEST-HANDLER': "onSignin",
  'X-Requested-With': "XMLHttpRequest",
  'X-OCTOBER-REQUEST-FLASH': "1",
  'sec-ch-ua-platform': "\"Android\"",
  'Origin': "https://www.iq.zain.com",
  'Sec-Fetch-Site': "same-origin",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Dest': "empty",
  'Referer': "https://www.iq.zain.com/ar/signin",
  'Accept-Language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
  'Cookie': "BNIS_STCookie=JC5uK+UKNrJcN7UYnHzPBNQspsyGXC7AW9XLj6rUio1oeSYZHXTiCmWI2VHvfljDWqSDC+VZmE3/cBXxDflXugb3Mlxjr7av; BNI_persistence=3Q9D05C7ulJCLaVE2CQAG4ci9CaB6reSpWvHrJ263O_J4pVGithj5ImnFVWbINTo8pXFt6h94yTR8xKajQQFiQ==; _gid=GA1.2.544943710.1715864286; _gac_UA-58707291-1=1.1715864286.Cj0KCQjw3ZayBhDRARIsAPWzx8pOxSeOR5PDjB-yVfEMeov2UveLdYHAGbaRMMHtq729g022rpG0JKEaAnklEALw_wcB; _gac_UA-100328890-1=1.1715864289.Cj0KCQjw3ZayBhDRARIsAPWzx8pOxSeOR5PDjB-yVfEMeov2UveLdYHAGbaRMMHtq729g022rpG0JKEaAnklEALw_wcB; _fbp=fb.1.1715864289449.1624679613; _scid=e522c3f6-8fa6-408a-a60e-7bcac915dc6e; _tt_enable_cookie=1; _ttp=-TzZwrkejZx1vZ35_gElBHOPlyY; _sctr=1%7C1715806800000; _scid_r=e522c3f6-8fa6-408a-a60e-7bcac915dc6e; _ga=GA1.2.455551560.1715864286; _ga_36KSZ76QBD=GS1.2.1715864291.1.1.1715864358.56.0.0; _ga_1M619RY0CS=GS1.2.1715864288.1.1.1715864358.56.0.0; _ga_58WJX7YKV7=GS1.1.1715864290.1.1.1715864358.55.0.0; october_session=eyJpdiI6ImFUUzZQajFWM1NjV2V2RUtMajMxWUE9PSIsInZhbHVlIjoiSEswRDFWMnJlZjdxT1JnQi9Oa3h4NWYwTk1WTStXZm5raTNmQU1wR1NoYktsVEd4KzZSRXF3WFJBZDBWMG41T0NjczBPaVZJbUpETyt4OTdZeUl2M3JyM3Z4VlFKd3d3WlQ0c0RIa2lnd1BrNEZ6V2M0ZHM0UHpnL0R5SzhwcnQiLCJtYWMiOiIyNWMxYmJjYTQ3M2Q0ZDRlYmUzOGIxMGU2MmUzMTE1ODk4MTE3ODYxNGRmNDZiMGZjYTk3YjMxMTkxN2IxY2RkIiwidGFnIjoiIn0%3D; BNIS_vid=G56Xx8GR2rbmY1awTJMgMeOWvkkPJB8Skh9kWst0b+mp2JEYoHJ9mrQYll5bU3uNvbSBUNEmwdV5BsHPuvCzp6uUv8eJJ0qWhZfSj1Sb8McxK8jS+s1EIyhdtlb8YsHkrz9/DMsJOWt52a1zMcQ2RU6kyc1vQ0j0EyV1jjODa8gm1CkwNGgDbSNcit34MDJHuVPjpVWAgiX9Y0BLlM7XzRSLqpnlK7El; BNIS___utm_is1=v44wwRpj/mU6fr3k1M77Uscngqpp6yWnLqza1Bjeo1X8VK7IKoPuOuBAQCJTZR4koIfbP2ty7h/ElOo93XivTqIVQNgaI/1XUUaUAyXLNsEa4pTgCDbz9g==; BNIS___utm_is2=Rtq113MIg4Y9UsOGjqVFNbFZhXGglF/l5EeS+u8JFcuTcz6UzZi8iv4AwMlA34EyenDIzAq/wUY=; BNIS___utm_is3=kSBN25EaD63HOwFj4nDpgiwmMwPfj4g0yO0dy87YS00gMqUuVxpcqAJkHr/txWzamHeXWPICCPvVmwb5VV/8OcLPcVCW9mrExcUdTX9GoG4=; BNIS_x-bni-jas=ULDSAG75Szo/g3Cdg6s337sJx7h8255i1IAilrtAy4EhRn4zH5LlUeqK1QipnbMT3ip6FyPzI/AsW5Bvpb7Rkj+fV8umyJWAE/cqoel6/laROhCQgrk/HQ==; BNES_october_session=lEmZPjk1SIC81r9ZVuveLCsAKTgnXI7zm0pWT5CSQ1VxFIwqyIT3krY1+2mshmlOZvZ3qwXmgn4PYVkjuxNArlouef/PKGKXPngF1Z/Tfmgky0tEy6eTaECzJZlWDNEBOBkP8mVCKvavyiYVFEynaOwSh7zivJUoSgonkJKiqJM7JE7zAuUdtNFM9AeygwaEB0NM8Co3YtmpaqmVDnIdox5FGhClpoGIOjPFHZ/ZDhtJNockzrW/TkNlCCY2sx0/oa7JnzBcOCrgosVyxAdVfyv3EhvLJnPBD+4yaprdGV0FxUdDef+gFVeJM1xamOms3zJ8UhXQubUc54Byohv3Fp4Y3GVevPgstMb1ofonpZRtoBWJegTKeE/1duhpzejFDwENvnCuDZQyUTW7PgyiwryjH+xKeNPiNKNelRIcBUBxLRu/civ7dlMgscHJ60ck2iMlNsVJvD9xSTzpi3bS9H91ZCqFt5uTxr3zXmUgCj8j0xfRFhfc06xpegVOGYAua1MQx/i0O4S+BM2/Ywq9R4CayFIBY+MV"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)
