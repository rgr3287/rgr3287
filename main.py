import feedparser, time

URL = "http://rgr3287.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300%&section=header&text=hyeonGeun%20Gwak&fontSize=80&animation=twinkling)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Frgr3287%2Fhit-counter&count_bg=%233D71C8&title_bg=%23555555&icon=sourcegraph.svg&icon_color=%23E7E7E7&title=count&edge_flat=false)](https://hits.seeyoufarm.com)

<h2>💪My Tech Stack</h2>

<img src="https://img.shields.io/badge/html5-F05138?style=flat-square&logo=HTML5&logoColor=white"/> <img src="https://img.shields.io/badge/git-151515?style=flat-square&logo=git&logoColor=white"/> <img src="https://img.shields.io/badge/Golang-0040FF?style=flat-square&logo=go&logoColor=white"/> <img src="https://img.shields.io/badge/TypeScript-5882FA?style=flat-square&logo=TypeScript&logoColor=white"/> <img src="https://img.shields.io/badge/AngularJS-FF0000?style=flat-square&logo=AngularJS&logoColor=white"/> <img src="https://img.shields.io/badge/Npm-F78181?style=flat-square&logo=npm&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2E64FE?style=flat-square&logo=docker&logoColor=white"/> <img src="https://img.shields.io/badge/CSS3-FE2EF7?style=flat-square&logo=css3&logoColor=white"/> <img src="https://img.shields.io/badge/Postman-FF8000?style=flat-square&logo=Postman&logoColor=white"/> <img src="https://img.shields.io/badge/MariaDB-04B4AE?style=flat-square&logo=MariaDB&logoColor=white"/> <img src="https://img.shields.io/badge/JavaScript-FFFF00?style=flat-square&logo=JavaScript&logoColor=white"/>  
<img src="https://img.shields.io/badge/Github-585858?style=flat-square&logo=Github&logoColor=white"/> <img src="https://img.shields.io/badge/Oracle-FF0040?style=flat-square&logo=Sass&logoColor=white"/> <img src="https://img.shields.io/badge/Sass-FF00FF?style=flat-square&logo=Oracle&logoColor=white"/> <img src="https://img.shields.io/badge/Rxjs-F781F3?style=flat-square&logo=Rxjs&logoColor=white"/> <img src="https://img.shields.io/badge/Node.js-01DF3A?style=flat-square&logo=Node.js&logoColor=white"/> <img src="https://img.shields.io/badge/NGINX-0B614B?style=flat-square&logo=NGINX&logoColor=white"/> <img src="https://img.shields.io/badge/Intellij-1C1C1C?style=flat-square&logo=intellijidea&logoColor=white"/> <img src="https://img.shields.io/badge/Slack-6A0888?style=flat-square&logo=slack&logoColor=white"/> <img src="https://img.shields.io/badge/VScode-0040FF?style=flat-square&logo=visualstudiocode&logoColor=white"/> <img src="https://img.shields.io/badge/MacOS-000000?style=flat-square&logo=macos&logoColor=white"/>

<h2>😀Most Used languages</h2>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=rgr3287&layout=compact"><br><br>

<h2>🌵Git And BaekJoon Stats</h2>

![HyeonGeun's GitHub stats](https://github-readme-stats.vercel.app/api?username=rgr3287&show_icons=true&theme=radical)
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=rgr3287)](https://solved.ac/rgr3287/)

## 👓Latest Blog Post

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
