"""
智谱 AI GLM-4.6 客户端
"""
import os
import httpx
from typing import Optional, Dict, List

class GLMClient:
    """智谱 AI 客户端封装"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GLM_API_KEY")
        self.base_url = "https://open.bigmodel.cn/api/paas/v4"
        
        if not self.api_key:
            raise ValueError("GLM_API_KEY 未设置")
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "glm-4.6",
        temperature: float = 1.0,
        max_tokens: int = 65536,
        stream: bool = False
    ) -> Dict:
        """
        调用 GLM 聊天完成 API
        
        Args:
            messages: 对话消息列表
            model: 模型名称
            temperature: 温度参数
            max_tokens: 最大 token 数
            stream: 是否流式响应
        
        Returns:
            API 响应结果
        """
        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": stream
        }
        
        with httpx.Client() as client:
            response = client.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
    
    def calculate(self, query: str) -> str:
        """
        使用 AI 进行智能计算
        
        Args:
            query: 用户的计算请求（自然语言）
        
        Returns:
            计算结果
        """
        messages = [
            {
                "role": "system",
                "content": "你是一个数学计算助手。用户会用自然语言描述数学问题，你需要理解问题并给出准确的计算结果。只返回计算结果，不要有多余的解释。"
            },
            {
                "role": "user",
                "content": query
            }
        ]
        
        result = self.chat_completion(messages)
        return result["choices"][0]["message"]["content"]

# 使用示例
if __name__ == "__main__":
    # 需要先设置环境变量 GLM_API_KEY
    client = GLMClient()
    result = client.calculate("帮我算 123 乘以 456")
    print(f"结果: {result}")
