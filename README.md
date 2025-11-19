# 智能计算器 - 全平台产研标杆项目

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg)](https://reactjs.org/)

> 一个从产品设计到多端实现的完整标杆项目，展示现代软件开发的全流程

## 📖 项目简介

这是一个**智能计算器**项目，不仅仅是一个简单的计算工具，更是一个完整的产品研发案例，涵盖：

- 💼 **产品设计**: BRD/MRD/PRD/FRD 全套文档
- 🔧 **后端实现**: CLI/API/AI 服务
- 🎨 **前端实现**: Web/桌面/移动/小程序
- 🔌 **硬件实现**: Arduino/树莓派/ESP32
- 🤖 **AI 增强**: 智谱 GLM-4.6 集成
- 🚀 **DevOps**: Docker/CI/CD/K8s

## ✨ 核心特性

### 基础功能
- ✅ 四则运算（加减乘除）
- ✅ 科学计算（幂、模、平方根等）
- ✅ 历史记录管理
- ✅ 多主题支持

### AI 增强功能
- 🤖 自然语言计算（"帮我算123乘以456"）
- 📝 手写公式识别
- 🎯 智能推荐
- 📚 解题步骤详解

### 全平台支持
- 💻 CLI 命令行版本
- 🌐 Web 网页版
- 🖥️ 桌面应用（Windows/macOS/Linux）
- 📱 移动应用（iOS/Android）
- 🧩 小程序（微信/支付宝）
- 🔌 硬件版本（Arduino/树莓派）

## 🏗️ 项目结构

```
intelligent-calculator/
├── docs/                  # 文档中心
│   ├── product/          # 产品文档（BRD/MRD/PRD/FRD）
│   ├── design/           # 设计文档（架构/UI/UX）
│   ├── development/      # 开发文档（环境/规范）
│   └── ai/               # AI 文档（集成/提示词）
│
├── backend/              # 后端实现
│   ├── cli/             # CLI 版本
│   ├── api/             # FastAPI 服务
│   └── ai-service/      # AI 服务（GLM-4.6）
│
├── frontend/            # 前端实现
│   ├── web/            # Web 应用（React/Vue）
│   ├── desktop/        # 桌面应用（Electron/Tauri）
│   ├── mobile/         # 移动应用（RN/Flutter）
│   └── mini-program/   # 小程序（微信/支付宝）
│
├── hardware/           # 硬件实现
│   ├── arduino/       # Arduino 版本
│   ├── raspberry-pi/  # 树莓派版本
│   └── esp32/         # ESP32 物联网版本
│
├── tests/             # 测试
├── devops/            # DevOps 配置
└── scripts/           # 工具脚本
```

详细结构参见 [PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md)

## 🚀 快速开始

### 1. CLI 版本（最简单）

```bash
# 克隆项目
git clone https://github.com/kie0519/temp.git
cd temp

# 运行 CLI 计算器
python backend/cli/calculator_cli.py
```

### 2. API 服务

```bash
# 安装依赖
cd backend/api
pip install -r requirements.txt

# 启动服务
uvicorn app:app --reload

# 访问文档
open http://localhost:8000/docs
```

### 3. Web 应用

```bash
# 安装依赖
cd frontend/web
npm install

# 启动开发服务器
npm run dev

# 访问应用
open http://localhost:5173
```

详细部署指南参见 [DEPLOYMENT.md](docs/DEPLOYMENT.md)

## 📚 学习路径

### 阶段一：产品设计（1-2周）
1. 阅读 [BRD](docs/product/BRD.md) - 了解商业需求
2. 阅读 [MRD](docs/product/MRD.md) - 了解市场需求
3. 阅读 [PRD](docs/product/PRD.md) - 了解产品需求
4. 阅读 [FRD](docs/product/FRD.md) - 了解功能需求

### 阶段二：后端开发（2-3周）
1. CLI 版本：Python 基础计算
2. API 服务：FastAPI + RESTful
3. AI 服务：智谱 GLM-4.6 集成

### 阶段三：前端开发（3-4周）
1. Web 应用：React 实现
2. 桌面应用：Electron 打包
3. 移动应用：React Native 开发

### 阶段四：硬件实现（2-3周）
1. Arduino 原型制作
2. 树莓派完整系统
3. ESP32 物联网版本

### 阶段五：DevOps（1-2周）
1. Docker 容器化
2. CI/CD 流程
3. 云端部署

## 🤝 贡献指南

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)

### 开发规范
- 提交信息遵循 [Conventional Commits](https://www.conventionalcommits.org/)
- 代码风格遵循项目 [编码规范](docs/development/coding-standards.md)
- 使用 Git Flow 工作流

## 📄 文档

### 产品文档
- [BRD - 商业需求文档](docs/product/BRD.md)
- [MRD - 市场需求文档](docs/product/MRD.md)
- [PRD - 产品需求文档](docs/product/PRD.md)
- [FRD - 功能需求文档](docs/product/FRD.md)

### 技术文档
- [系统架构设计](docs/design/architecture.md)
- [API 使用指南](docs/api/API_USAGE.md)
- [部署指南](docs/DEPLOYMENT.md)
- [项目进度报告](docs/PROJECT_PROGRESS.md)
- [项目结构说明](docs/PROJECT_STRUCTURE.md)

### 开发文档
- [Git 学习指南](docs/development/GIT_PRACTICE_TODO.md)
- [API Swagger 文档](http://localhost:8000/docs) (需启动后端服务)

## 🛠️ 技术栈

### 后端
- Python 3.8+
- FastAPI
- SQLAlchemy
- PostgreSQL

### 前端
- React 18+
- TypeScript
- Vite
- Ant Design

### AI
- 智谱 GLM-4.6
- Prompt Engineering

### DevOps
- Docker
- GitHub Actions
- Kubernetes

## 📊 项目进度

**当前进度: 50%** (已完成文档、后端、前端 Web)

### 已完成 ✅
- [x] 项目规划与架构设计
- [x] 产品文档（BRD/MRD/PRD/FRD）
- [x] 系统架构设计
- [x] CLI 版本实现
- [x] 数据库模型和迁移
- [x] API 服务实现 (10个端点)
- [x] AI 功能集成 (智谱 GLM-4.6)
- [x] Web 前端实现 (React + TypeScript)

### 进行中 🚧
- [ ] 单元测试和集成测试
- [ ] Docker 容器化
- [ ] CI/CD 流程

### 待开发 📋
- [ ] 桌面应用 (Electron/Tauri)
- [ ] 移动端 (React Native/Flutter)
- [ ] 小程序 (微信/支付宝)
- [ ] 硬件版本 (Arduino/树莓派)
- [ ] 生产环境部署

## 📈 统计数据

- **代码行数**: ~3500+ 行
  - 产品文档: 2500+ 行
  - 后端代码: 1400+ 行
  - 前端代码: 1300+ 行
- **文档数量**: 20+ 篇
- **Git 提交**: 35+ 次
- **API 端点**: 10 个
- **支持平台**: 2 个 (CLI + Web, 计划 7+)

## 📝 变更日志

详见 [CHANGELOG.md](CHANGELOG.md)

## 📜 开源协议

本项目采用 MIT 协议 - 详见 [LICENSE](LICENSE)

## 👤 作者

**zuojunwei (kie)**
- GitHub: [@kie0519](https://github.com/kie0519)
- 项目仓库: [temp](https://github.com/kie0519/temp)

## 🙏 致谢

- 感谢智谱 AI 提供的 GLM-4.6 模型
- 感谢开源社区的贡献

---

⭐ 如果这个项目对你有帮助，欢迎 Star！
