# 项目代码结构说明

## 项目概述
- 1.支持用户创建并分享任意多个虚拟女友/男友/朋友，可以自定义角色音色、性格、简介；
- 2.支持语音识别、语音合成、语音复刻，实现跟虚拟人物语音通话交流；
- 3.支持function call、知识库；
- 4.后端采用Django，前端采用Vue，大模型框架采用LangChain(LangGraph)；

---

## 技术栈

### 后端 (Backend)
- **框架**: Django 6.0
- **认证**: JWT (SimpleJWT)
- **API**: Django REST Framework
- **数据库**: SQLite3
- **AI 集成**: LangChain
- **实时通信**: WebSocket (TTS 语音合成)

### 前端 (Frontend)
- **框架**: Vue 3.5.28
- **状态管理**: Pinia 3.0.4
- **路由**: Vue Router 5.0.2
- **HTTP 客户端**: Axios
- **构建工具**: Vite 7.3.1
- **UI 框架**: TailwindCSS 4.x + DaisyUI
- **语音处理**: @ricky0123/vad-web
- **SSE 流式接收**: @microsoft/fetch-event-source

---

## 完整目录结构

PythonProject1/
├── backend/                          # 后端项目根目录（Django）
│   ├── backend/                      # Django 核心配置目录
│   │   ├── asgi.py                   # ASGI 异步服务入口
│   │   ├── settings.py               # Django 全局配置
│   │   ├── urls.py                   # 项目主路由
│   │   └── wsgi.py                   # WSGI 服务入口
│   ├── web/                          # 核心业务应用
│   │   ├── models/                   # 数据模型层
│   │   │   ├── character.py          # 角色模型
│   │   │   ├── friend.py             # 好友 & 消息模型
│   │   │   └── user.py               # 用户模型
│   │   ├── views/                    # 视图层（按业务拆分）
│   │   │   ├── create/character/     # 角色创建模块
│   │   │   │   ├── create.py         # 创建角色
│   │   │   │   ├── get_list.py       # 获取角色列表
│   │   │   │   ├── get_single.py     # 获取单个角色
│   │   │   │   ├── remove.py         # 删除角色
│   │   │   │   └── update.py         # 更新角色
│   │   │   ├── friend/               # 好友模块
│   │   │   │   ├── message/          # 消息处理
│   │   │   │   │   ├── asr/          # 语音识别
│   │   │   │   │   ├── chat/         # 聊天功能
│   │   │   │   │   │   ├── chat.py   # 流式聊天 API
│   │   │   │   │   │   └── graph.py  # 聊天图编排
│   │   │   │   │   ├── memory/       # 记忆管理
│   │   │   │   │   │   ├── graph.py  # 记忆图
│   │   │   │   │   │   └── update.py # 更新记忆
│   │   │   │   │   └── get_history.py # 获取聊天记录
│   │   │   │   ├── get_list.py       # 获取好友列表
│   │   │   │   ├── get_or_create.py  # 获取/创建好友关系
│   │   │   │   └── remove.py         # 删除好友
│   │   │   ├── homepage/             # 首页模块
│   │   │   │   └── index.py          # 首页视图
│   │   │   ├── profile/              # 个人资料模块
│   │   │   │   └── update.py         # 更新资料
│   │   │   ├── user/account/         # 用户账户模块
│   │   │   │   ├── get_user_info.py  # 获取用户信息
│   │   │   │   ├── login.py          # 登录
│   │   │   │   ├── logout.py         # 登出
│   │   │   │   ├── refresh_token.py  # 刷新 Token
│   │   │   │   └── register.py       # 注册
│   │   │   ├── user/utils/           # 用户工具类
│   │   │   │   └── photo.py          # 头像处理
│   │   │   └── index.py              # 视图入口
│   │   ├── documents/utils/          # 文档处理工具
│   │   │   ├── custom_embeddings.py  # 自定义向量嵌入
│   │   │   └── insert_documents.py   # 文档入库
│   │   ├── migrations/               # 数据库迁移文件
│   │   ├── templates/                # Django 模板
│   │   │   └── index.html            # 主页模板
│   │   ├── admin.py                  # Django Admin 配置
│   │   ├── apps.py                   # 应用注册配置
│   │   ├── tests.py                  # 单元测试
│   │   ├── urls.py                   # Web 应用路由
│   │   └── views.py                  # 视图统一入口
│   └── manage.py                     # Django 管理脚本

├── frontend/                         # 前端项目根目录（Vue3 + Vite）
│   ├── src/                          # 源代码目录
│   │   ├── assets/                   # 全局静态资源
│   │   │   └── main.css              # 全局样式
│   │   ├── components/               # 公共可复用组件
│   │   │   ├── character/            # 角色相关组件
│   │   │   │   ├── chat_field/       # 聊天输入区域
│   │   │   │   │   ├── character_photo_field/
│   │   │   │   │   │   └── CharacterPhotoField.vue  # 角色照片上传
│   │   │   │   │   ├── chat_history/ # 聊天记录展示
│   │   │   │   │   │   ├── message/  # 单条消息组件
│   │   │   │   │   │   └── ChatHistory.vue
│   │   │   │   │   ├── input_field/  # 输入框组件
│   │   │   │   │   └── ChatField.vue # 聊天模块主组件
│   │   │   │   └── Character.vue     # 角色主组件
│   │   │   └── navbar/               # 导航栏组件
│   │   │       ├── icon/             # 图标组件集
│   │   │       │   ├── CameraIcon.vue
│   │   │       │   ├── CreateIcon.vue
│   │   │       │   ├── FriendIcon.vue
│   │   │       │   ├── HomePageIcon.vue
│   │   │       │   ├── KeyboardIcon.vue
│   │   │       │   ├── LoginIcon.vue
│   │   │       │   ├── MenuIcon.vue
│   │   │       │   ├── MicIcon.vue
│   │   │       │   ├── RemoveIcon.vue
│   │   │       │   ├── SearchIcon.vue
│   │   │       │   ├── SendIcon.vue
│   │   │       │   ├── UpdateIcon.vue
│   │   │       │   ├── UserLogoutIcon.vue
│   │   │       │   ├── UserProfileIcon.vue
│   │   │       │   └── UserSpaceIcon.vue
│   │   │       ├── NavBar.vue        # 导航栏主组件
│   │   │       └── UserMenu.vue      # 用户菜单
│   │   ├── js/                       # 工具脚本
│   │   │   ├── http/                 # HTTP 请求封装
│   │   │   │   ├── api.js            # 通用 API 封装
│   │   │   │   └── streamApi.js      # 流式请求封装
│   │   │   └── utils/                # 通用工具函数
│   │   │       └── base_64-file.js   # Base64 <-> 文件转换
│   │   ├── router/                   # Vue Router 路由
│   │   │   └── index.js
│   │   ├── stores/                   # Pinia 状态管理
│   │   │   ├── counter.js            # 示例模块
│   │   │   └── user.js               # 用户全局状态
│   │   ├── views/                    # 页面视图
│   │   │   ├── create/               # 创建相关页面
│   │   │   │   ├── character/
│   │   │   │   │   ├── components/   # 页面子组件
│   │   │   │   │   ├── CreateCharacter.vue
│   │   │   │   │   └── UpdateCharacter.vue
│   │   │   │   └── CreateIndex.vue
│   │   │   ├── error/                # 异常页面
│   │   │   │   └── NotFoundIndex.vue # 404
│   │   │   ├── friend/               # 好友页面
│   │   │   │   └── FriendIndex.vue
│   │   │   ├── homepage/             # 首页
│   │   │   │   └── HomepageIndex.vue
│   │   │   └── user/                 # 用户相关页面
│   │   │       ├── account/          # 账户
│   │   │       │   ├── LoginIndex.vue
│   │   │       │   └── RegisterIndex.vue
│   │   │       ├── profile/          # 个人资料
│   │   │       │   ├── components/
│   │   │       │   └── ProfileIndex.vue
│   │   │       └── space/            # 用户空间
│   │   │           ├── components/
│   │   │           └── SpaceIndex.vue
│   │   ├── App.vue                   # 根组件
│   │   └── main.js                   # 入口文件
│   ├── .gitignore
│   ├── README.md
│   ├── index.html
│   ├── jsconfig.json
│   ├── package-lock.json
│   ├── package.json
│   └── vite.config.js

├── .gitignore                        # 项目全局忽略配置
└── README.md                         # 项目总说明

---

## 核心功能模块(对话Agent和记忆Agent协作)

### 1. 用户认证系统 (`/backend/web/views/user/`)
- **注册**: `register.py` - 用户注册功能
- **登录**: `login.py` - JWT 登录认证
- **登出**: `logout.py` - 用户登出
- **Token 刷新**: `refresh_token.py` - 刷新访问令牌
- **用户信息**: `get_user_info.py` - 获取当前用户信息

### 2. 角色管理系统 (`/backend/web/views/create/character/`)
- **创建角色**: `create.py` - 创建新的虚拟角色
- **角色列表**: `get_list.py` - 获取角色列表
- **单个角色**: `get_single.py` - 获取角色详情
- **更新角色**: `update.py` - 修改角色信息
- **删除角色**: `remove.py` - 删除角色

### 3. 好友聊天系统 (`/backend/web/views/friend/`)
- **好友管理**:
  - `get_list.py` - 好友列表
  - `get_or_create.py` - 获取或创建好友
  - `remove.py` - 删除好友
  
- **消息处理**:
  - **聊天** (`/message/chat/`):
    - `chat.py` - 流式聊天 API，支持 SSE 实时推送
    - `graph.py` - LangChain 聊天图编排
  
  - **记忆管理** (`/message/memory/`):
    - `update.py` - 更新长期记忆
    - `graph.py` - 记忆处理流程
  
  - **语音功能** (`/message/asr/`):
    - `asr.py` - 自动语音识别
  
  - **历史记录** (`/message/get_history.py`):
    - 获取聊天历史记录

### 4. 数据模型 (`/backend/web/models/`)
- **character.py**: 角色模型定义（性格、外观等）
- **friend.py**: 好友关系、消息记录、系统提示词
- **user.py**: 用户资料模型

### 5. 前端核心组件
- **导航系统**: `NavBar.vue` + 图标组件集
- **聊天界面**: `ChatField.vue` + `ChatHistory.vue`
- **角色管理**: `Character.vue` + 创建/更新表单
- **用户菜单**: `UserMenu.vue`

---

## API 路由架构

### 后端路由 (`/backend/web/urls.py`)
### 前端路由 (`/frontend/src/router/index.js`)

## 运行方式
### 后端启动
cd backend
python manage.py runserver
### 前端启动
cd frontend
npm run dev

## 语音识别、翻译服务
<img width="1188" height="1236" alt="image" src="https://github.com/user-attachments/assets/5a726b9b-9471-4bf1-b1cd-314ed68bc087" />

## 语音合成服务
<img width="904" height="1232" alt="image" src="https://github.com/user-attachments/assets/02fbfd15-dba0-4467-ad65-5eb666b2b2cc" />

