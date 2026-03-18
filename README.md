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
│   │   ├── settings.py               # Django 全局配置文件
│   │   ├── urls.py                   # 项目主路由配置
│   │   └── wsgi.py                   # WSGI 服务入口
│   ├── web/                          # 核心业务应用
│   │   ├── models/                   # 数据模型层
│   │   │   ├── character.py          # 角色数据模型
│   │   │   ├── friend.py             # 好友&消息数据模型
│   │   │   └── user.py               # 用户数据模型
│   │   ├── views/                    # 视图层（按业务模块拆分）
│   │   │   ├── create/character/     # 角色创建管理模块
│   │   │   │   ├── create.py         # 创建角色接口
│   │   │   │   ├── get_list.py       # 获取角色列表
│   │   │   │   ├── get_single.py     # 获取单个角色详情
│   │   │   │   ├── remove.py         # 删除角色
│   │   │   │   └── update.py         # 更新角色信息
│   │   │   ├── friend/               # 好友管理模块
│   │   │   │   ├── message/          # 消息处理模块
│   │   │   │   │   ├── asr/          # 语音识别能力
│   │   │   │   │   ├── chat/         # 聊天核心功能
│   │   │   │   │   │   ├── chat.py   # 流式聊天API
│   │   │   │   │   │   └── graph.py  # 聊天逻辑图编排
│   │   │   │   │   ├── memory/       # 记忆管理模块
│   │   │   │   │   │   ├── graph.py  # 记忆逻辑图
│   │   │   │   │   │   └── update.py # 记忆更新接口
│   │   │   │   │   └── get_history.py # 获取聊天历史记录
│   │   │   │   ├── get_list.py       # 获取好友列表
│   │   │   │   ├── get_or_create.py  # 获取/创建好友关系
│   │   │   │   └── remove.py         # 删除好友关系
│   │   │   ├── homepage/             # 首页模块
│   │   │   │   └── index.py          # 首页视图接口
│   │   │   ├── profile/              # 个人资料模块
│   │   │   │   └── update.py         # 更新个人资料
│   │   │   ├── user/account/         # 用户账户模块
│   │   │   │   ├── get_user_info.py  # 获取用户信息
│   │   │   │   ├── login.py          # 用户登录接口
│   │   │   │   ├── logout.py         # 用户登出接口
│   │   │   │   ├── refresh_token.py  # 刷新用户Token
│   │   │   │   └── register.py       # 用户注册接口
│   │   │   ├── user/utils/           # 用户相关工具类
│   │   │   │   └── photo.py          # 头像处理工具
│   │   │   └── index.py              # 视图统一入口
│   │   ├── documents/utils/          # 文档处理工具集
│   │   │   ├── custom_embeddings.py  # 自定义向量嵌入
│   │   │   └── insert_documents.py   # 文档入库工具
│   │   ├── migrations/               # 数据库迁移文件
│   │   ├── templates/                # Django模板目录
│   │   │   └── index.html            # 主页模板
│   │   ├── admin.py                  # Django Admin后台配置
│   │   ├── apps.py                   # 应用注册配置
│   │   ├── tests.py                  # 单元测试文件
│   │   ├── urls.py                   # Web应用路由配置
│   │   └── views.py                  # 视图入口文件
│   └── manage.py                     # Django管理脚本
│
├── frontend/                         # 前端项目根目录（Vue3 + Vite）
│   ├── src/                          # 前端源代码目录
│   │   ├── assets/                   # 全局静态资源
│   │   │   └── main.css              # 全局样式文件
│   │   ├── components/               # 公共可复用组件
│   │   │   ├── character/            # 角色相关组件
│   │   │   │   ├── chat_field/       # 聊天输入区域组件
│   │   │   │   │   ├── character_photo_field/
│   │   │   │   │   │   └── CharacterPhotoField.vue  # 角色照片上传组件
│   │   │   │   │   ├── chat_history/ # 聊天记录展示组件
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
│   │   │       └── UserMenu.vue      # 用户菜单组件
│   │   ├── js/                       # 前端工具脚本
│   │   │   ├── http/                 # HTTP请求封装
│   │   │   │   ├── api.js            # 通用API接口封装
│   │   │   │   └── streamApi.js      # 流式请求API封装
│   │   │   └── utils/                # 通用工具函数
│   │   │       └── base_64-file.js   # Base64与文件互转工具
│   │   ├── router/                   # Vue Router路由配置
│   │   │   └── index.js              # 路由定义文件
│   │   ├── stores/                   # Pinia状态管理
│   │   │   ├── counter.js            # 计数器示例状态
│   │   │   └── user.js               # 用户全局状态
│   │   ├── views/                    # 页面视图
│   │   │   ├── create/               # 创建相关页面
│   │   │   │   ├── character/        # 角色创建页面
│   │   │   │   │   ├── components/   # 页面子组件
│   │   │   │   │   ├── CreateCharacter.vue # 创建角色页面
│   │   │   │   │   └── UpdateCharacter.vue # 更新角色页面
│   │   │   │   └── CreateIndex.vue   # 创建页入口
│   │   │   ├── error/                # 异常页面
│   │   │   │   └── NotFoundIndex.vue # 404页面
│   │   │   ├── friend/               # 好友页面
│   │   │   │   └── FriendIndex.vue   # 好友列表页
│   │   │   ├── homepage/             # 首页
│   │   │   │   └── HomepageIndex.vue # 首页视图
│   │   │   └── user/                 # 用户相关页面
│   │   │       ├── account/          # 账户管理页面
│   │   │       │   ├── LoginIndex.vue    # 登录页
│   │   │       │   └── RegisterIndex.vue # 注册页
│   │   │       ├── profile/          # 个人资料页
│   │   │       │   ├── components/   # 页面子组件
│   │   │       │   └── ProfileIndex.vue  # 资料页主文件
│   │   │       └── space/            # 用户空间页
│   │   │           ├── components/   # 页面子组件
│   │   │           └── SpaceIndex.vue    # 空间页主文件
│   │   ├── App.vue                   # Vue根组件
│   │   └── main.js                   # Vue项目入口文件
│   ├── .gitignore                    # 前端Git忽略配置
│   ├── README.md                     # 前端项目说明
│   ├── index.html                    # HTML入口模板
│   ├── jsconfig.json                 # JS配置文件
│   ├── package-lock.json             # 依赖锁定文件
│   ├── package.json                  # 项目依赖配置
│   └── vite.config.js                # Vite构建配置
│
├── .gitignore                        # 项目全局Git忽略配置
└── README.md                         # 项目总说明文档

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

