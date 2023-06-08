import streamlit as st
from PIL import Image

st.title('自己紹介')
st.caption('page1：　簡単にプロフィールを紹介します')

st.write('- 名前：横井陸哉\n\n- 生年月：2002年11月\n\n- 性別：男\n\n- 卒業年数：2025年3月卒業予定\n\n- 大学：工学院大学　情報学部　コンピュータ科学科\n\n- GPA：3.4\n\n- 研究室：セキュリティ科学研究室(予定)\n\n　現在はまだ正式には配属されておらず，仮配属という扱いです．')
st.write('- 趣味：テニス，料理')
st.write('- 特技：誰とでも打ち解けられる．タイピングが早い．')

my_image=Image.open('./gazou/my_gazou.png')
st.image(my_image,width=200)

st.write("以下に弊学のカリキュラムや特徴が記載された公式サイトへのURLを記載します．")
st.write("よろしければご覧ください．")

link='[工学院大学コンピュータ科学科公式URL](https://www.kogakuin.ac.jp/faculty/informatics/1j2.html)'

st.markdown(link,unsafe_allow_html=True)