import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
    #0.1秒ずつ遅れてバーが埋まっていく。
    # 以下コードは、これが終わるまで実行されない。

'Done!'

st.write('DataFrame')


left_colmun, right_column = st.columns(2)
#2つカラムが作成され、left_columnとright_columnにはいる
button = left_colmun.button('右列に文字を表示')
if button:
    right_column.write("表示したよん")

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
#羅列すれば、よくあるFAQのサイトみたいに使える。

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.write(df)

st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
#dataframeだと引数をつけられる。axis=1で列がハイライトされる

st.table(df)
#スタティック＝静的なテーブルが作れる。つまりソート不可。
#表については、StleamlitサイトのAPIreferencesのDisplayData参照

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

#ダブルクォーテーション3つで囲まれた部分はMarkdown
#逆向きのダッシュ？で囲まれた部分はコードの形式で表示される

"""### 色々グラフを書いてみる"""
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
#20行3列の乱数を、正規分布をもとに作成される

st.line_chart(df)
#折れ線グラフ。拡大縮小移動や、CSVやPNGでの保存もできる

st.area_chart(df)
#塗りつぶされた折れ線グラフ

st.bar_chart(df)
#棒グラフ。他にもヒストグラムなどいろいろなチャートが用意されている。


"""### 緯度と経度でランダムにピックアップ"""
df = pd.DataFrame(
    np.random.rand(100,2)/[50, 50]+[35.69, 139.70],
    columns=['lat','lon']
)
#lat,lonは緯度と経度。
#それぞれ50で割って乱数を小さくし、新宿付近の緯度経度を足して近づける

st.map(df)

#mapについてもAPIのページに使い方がいろいろ書いてある



"""### チェックボックス"""
st.write('Dysplay Image')

if st.checkbox('Show Image'):
#checkboxはtrueORfalseで帰ってくる。

    img = Image.open('s512_f_traffic_6_0.png')
    st.image(img, caption='Cloud', use_column_width=True)

    #use_column_width=Trueで実際に表示されたサイトの幅に合わせて表示。
    # 2カラムにできたりもするらしい。

    #写真のほかにもビデオや音楽を表示することができる。


"""### セレクトボックス"""
option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))
)

'あなたの好きな数字は', option, 'です。'

"""### テキストボックス"""
st.write('Interactive Widgets')
text = st.sidebar.text_input('あなたの趣味を教えてください。')
'あなたの趣味は', text,'です。'
#sidebarとつけることで、ページの左のサイドバーが作成されてそこに出る


"""### スライダー"""
condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
'コンディション',condition
#0,100,50は、最小値、最大値、デフォルト表示

#余談。一部選択してCtrl＋D押すと同じ文字列が選択される。
#一気に同じ文字を削除したいときに便利。



