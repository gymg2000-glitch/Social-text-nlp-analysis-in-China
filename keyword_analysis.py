import pandas as pd
import jieba as jb
'''
import wordcloud as wcc
import pyecharts.options as opts
from pyecharts.charts import WordCloud
'''
data =pd.read_excel("悼念.xlsx",engine="openpyxl")
data=data.fillna("")
wc=""
for i in range(10814):
    wc += data["文本"][i]
words=jb.lcut(wc)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)

re=pd.DataFrame(items)
re.to_excel("词云.xlsx")
'''
txt=" ".join(words)
c=wcc.WordCloud(width=1000,background_color="white",height=700,font_path = "msyh.ttc")
c.generate(txt)
c.to_file("baodao.png")

(
    WordCloud()
    .add(series_name="热点分析", data_pair=items, word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="热点分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("词云.html")
)
'''