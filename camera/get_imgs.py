import requests
from ted.models import Face, Picture


def thing():
    face = Face.objects.get(id=1)
    print(face)

# url = 'https://news.artnet.com/app/news-upload/2015/11/1133593_942736-256x256.jpg'
# r = requests.get(url, allow_redirects=True)
# open('imagename.png', 'wb').write(r.content)