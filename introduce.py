import  streamlit  as  st
# 网页基本信息配置
st.set_page_config(
    page_title="个人信息卡片"
)
st.title("自我介绍卡片生成器")
with  st.sidebar:
    name = st.text_input("你的姓名")
    age = st.number_input("你的年龄")
    hobby = st.text_input("你的爱好")
    subject = st.text_input("你最喜欢的学科")

if  st.button("生成我的个人信息卡片"):
    st.write(f"你的名字：{name}<br>你的年龄：{age}<br>你的爱好：{hobby}<br>你最喜欢的学科：{subject}<br>",unsafe_allow_html=True)