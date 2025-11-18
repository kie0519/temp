# AI 服务

## 概述
基于智谱 GLM-4.6 的 AI 增强服务，提供自然语言计算、解题助手等功能。

## 功能特性
- ✅ 自然语言理解（"帮我算 123 乘以 456"）
- ✅ 解题步骤拆解
- ✅ 智能推荐
- ✅ 公式识别

## 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 配置 API Key
创建 `.env` 文件：
```bash
GLM_API_KEY=your_api_key_here
GLM_API_BASE=https://open.bigmodel.cn/api/paas/v4
```

### 使用示例
```python
from glm_client import GLMClient

client = GLMClient()
result = client.calculate("帮我算 123 加 456")
print(result)  # 输出: 579
```

## API 使用

### 基础调用
```python
import httpx

response = httpx.post(
    "https://open.bigmodel.cn/api/paas/v4/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "glm-4.6",
        "messages": [
            {"role": "system", "content": "你是一个数学计算助手"},
            {"role": "user", "content": "123 + 456 等于多少？"}
        ]
    }
)
```

## 提示词工程

### 计算器 Agent 提示词
参见 `prompts/calculator_system.txt`

### 解题助手提示词
参见 `prompts/tutor_system.txt`

## 开发计划
- [ ] 实现 GLM Client 封装
- [ ] 设计计算器 Agent 提示词
- [ ] 添加对话上下文管理
- [ ] 实现流式响应
- [ ] 添加错误重试机制

---
**维护者**: zuojunwei  
**最后更新**: 2025-11-17
