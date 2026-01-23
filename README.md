## 项目简介:
- 1.支持用户创建并分享任意多个虚拟女友/男友/朋友，可以自定义角色音色、性格、简介；
- 2.支持语音识别、语音合成、语音复刻，实现跟虚拟人物语音通话交流；
- 3.支持function call、知识库；
- 4.后端采用Django，前端采用Vue，大模型框架采用LangChain(LangGraph)；

## 开发环境搭建

### 后端环境

```bash
# 进入后端目录
cd backend

# 安装依赖
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers

# 数据库迁移
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser

# 启动开发服务器
python manage.py runserver
```

### 前端环境

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```
