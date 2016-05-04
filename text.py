
import urllib
import bs4

url = "https://www.google.co.kr/?gws_rd=ssl"

#website에서 정보를 가져 옴
website = urllib.urlopen(url)
text = website.read()
website.close()


#가져온 정보를 해석
soup = bs4.BeautifulSoup(text, 'txml')
#해석한 정보에서 img포함된 파일을 추출함
imgs = soup. fint_all('img')


#추출한 내용을 하나씩 살펴본다.
print(imgs)

urllib.urletrleve("https://www.google.co.kr/search?hl=ko&site=imghp&tbm=isch&source=hp&biw=984&bih=532&q=%EC%BB%B4%ED%93%A8%ED%84%B0&oq=%EC%BB%B4%ED%93%A8%ED%84%B0&gs_l=img.3..0l10.2386.6335.0.6512.16.8.2.6.1.0.200.1093.0j7j1.8.0....0...1ac.1j4.64.img..2.7.664.7FQDRKvRwtk")

for image_info in imgs:
    print(image_info.get('src'))