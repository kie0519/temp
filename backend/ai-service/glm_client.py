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
    
    def calculate(self, query: str) -> tuple[str, str, int]:
        """
        使用 AI 进行智能计算

        Args:
            query: 用户的计算请求（自然语言）

        Returns:
            tuple[str, str, int]: (理解的表达式, 计算结果, 使用的token数)
        """
        # 读取系统提示词
        prompt_file = os.path.join(
            os.path.dirname(__file__), "prompts", "calculator_system.txt"
        )

        try:
            with open(prompt_file, "r", encoding="utf-8") as f:
                system_prompt = f.read()
        except FileNotFoundError:
            system_prompt = """你是一个数学计算助手。用户会用自然语言描述数学问题，你需要:
1. 理解用户的意图
2. 提取出标准的数学表达式
3. 计算结果

请以JSON格式返回:
{
  "expression": "提取的数学表达式",
  "result": "计算结果(仅数字)"
}"""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ]

        response = self.chat_completion(messages, temperature=0.7)

        # 提取结果
        content = response["choices"][0]["message"]["content"]
        tokens_used = response.get("usage", {}).get("total_tokens", 0)

        # 尝试解析JSON响应
        import json
        try:
            result_data = json.loads(content)
            expression = result_data.get("expression", "")
            result = result_data.get("result", "")
        except (json.JSONDecodeError, AttributeError):
            # 如果不是JSON格式,尝试直接解析
            expression = query
            result = content.strip()

        return expression, result, tokens_used

# 使用示例
if __name__ == "__main__":
    # 需要先设置环境变量 GLM_API_KEY
    client = GLMClient()
    result = client.calculate("帮我算 123 乘以 456")
    print(f"结果: {result}")
