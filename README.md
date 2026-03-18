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

