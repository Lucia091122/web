'''我的主页'''
import streamlit as st
import PIL as Image
import time

page = st.sidebar.radio("路西弗的书房", ["留言板", "路西弗的日常", "路西弗的推荐", "路西弗的文章"])

def img_change(img):
    width , height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
    return img

def page1():
    '''路西弗的推荐'''
    color = st.radio(
        '选择：',
        ['路西弗的电影推荐', '路西弗的书籍推荐', '路西弗的音乐推荐'],
        captions=['路西弗的电影推荐', '路西弗的书籍推荐', '路西弗的音乐推荐']
    )
    if color == '路西弗的电影推荐':
        st.write(":brown路西弗的电影推荐")
        st.image("图片1.png")
        st.text("奥本海默  导演：克里斯托弗·诺兰 主演：基里安·墨菲")
        st.text("真的超级好看！叙事结构是诺兰常用的三段式手法，可能会看不懂，还有很多历史名人和物理学术语，但是真的超级好看！立意也很好，非常推荐大家静下心来去欣赏")
        st.write('提问：路西弗最喜欢的诺兰的电影是哪个？:sunglasses:')
        cb1 = st.checkbox('A. 奥本海默')
        cb2 = st.checkbox('B. 盗梦空间')
        cb3 = st.checkbox('C. 信条')
        cb4 = st.checkbox('D. 蝙蝠侠三部曲')
        l = ['A. 奥本海默', 'B. 盗梦空间', 'C. 信条', '4错误答案']
        if st.button('确认答案'):
            if 'A. 奥本海默' == True or 'B. 盗梦空间' == True and 'C. 信条' == False and 'D. 蝙蝠侠三部曲' == False:
                st.write(':sunglasses:回答正确:sunglasses:')
        st.write("(:clapper:来点Oppie~:clapper:)")
        st.image("图片3.png")
        st.write('----')
        go = st.selectbox('路西弗超级喜欢的小破站视频', ['奥本海默科普', '法国大革命史'])
        if go == '奥本海默科普':
            st.link_button('跳转到'+go, 'https://www.bilibili.com/video/BV1rb4y1L7sS/?spm_id_from=333.337.search-card.all.click')
        elif go == '法国大革命史':
            st.link_button('跳转到'+go, 'https://www.bilibili.com/video/BV12f4y1w7b5/?spm_id_from=333.337.search-card.all.click')
        st.write("-----------------------------------------")
    elif color == '路西弗的书籍推荐':
        st.write("路西弗的书籍推荐")
        st.write("-----------------------------------------")
    elif color == '路西弗的音乐推荐':
        st.write("路西弗的音乐推荐")
        st.write("-----------------------------------------")
    
def page2():
    '''路西弗的文章'''
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')
    my_open = st.toggle('是否开启智能词典')
    if my_open:
        st.write('开启')
        st.write(':blue智能词典')
        with open('words_space.txt', 'r', encoding='utf-8') as f:
            words_list = f.read().split('\n')
        for i in range(len(words_list)):
            words_list[i] = words_list[i].split('#')
        words_dict = {}
        for i in words_list:
            words_dict[i[1]] = [int(i[0]), i[2]]
        with open('check_out_times.txt', 'r', encoding = 'utf-8') as f:
            times_list = f.read().split('\n')
        for i in range(len(times_list)):
            times_list[i] = times_list[i].split('#')
        times_dict = {}
        for i in times_list:
            times_dict[int(i[0])] = int(i[1])
        for i in words_list:
            words_dict[i[1]] = [int(i[0]), i[2]]
        for i in range(len(times_list)):
            times_list[i] = times_list[i].split('#')
        times_dict = {}
        for i in times_list:
            times_dict[int(i[0])] = int(i[1])
        word = st.text_input("请输入要查询的单词")
        if word in words_dict:
            st.write(words_dict[word])
            n = words_dict[word][0]
            if n in times_dict:
                times_dict[n] += 1
            else:
                times_dict[n] = 1
            with open('check_out_times.txt', 'r', encoding = 'utf-8') as f:
                message = ''
                for k, v in times_dict.items():
                    message += str(k) + '#' + str(v) + '\n'
                message = message[:-1]
                f.write("查询次数：", times_dict[n])
            if word == 'python':
                st.code('''print('hello world')''')
            if word == 'snow':
                st.snow()
            if word == 'birthday':
                st.balloons()
    else:
        st.write('关闭')
    
def page3():
    '''路西弗的日常'''
    st.write(":crescent_moon:先来看点美图~~~:crescent_moon:")
    uploaded_file = st.file_uploader("上传图片", type = ['png', 'jpg', 'jpeg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = image_open(uploaded_file)
    tab1, tab2, tab3, tab4 = (["原图", "改图1", "改图2", "改图3"])
    with tab1:
        st.image(img)
    with tab2:
        st.image(img_change(img, 0, 2, 1))
    with tab3:
        st.image(img_change(img, 1, 2, 0))
    with tab4:
        st.image(img_change(img, 1, 0, 2))
    
def page4():
    '''留言板'''
    st.write('路西弗的留言板')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.text(i[1]+':'+i[2])#st.text(i[1]+':'+i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def img_change(img, rc, gc, bc):
    width , height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == "路西弗的推荐":
    page1()
elif page == "路西弗的文章":
    page2()
elif page == "路西弗的日常":
    page3()
elif page == "留言板":
    page4()