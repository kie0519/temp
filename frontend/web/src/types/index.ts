/**
 * 类型定义文件
 */

// 用户相关类型
export interface User {
  id: string;
  username: string;
  email: string;
  is_active: boolean;
  is_premium: boolean;
  created_at: string;
  updated_at: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  username: string;
  email: string;
  password: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  expires_in: number;
  user: User;
}

// 计算相关类型
export interface CalculateRequest {
  expression: string;
}

export interface CalculateResponse {
  expression: string;
  result: number;
  calculation_id: string;
}

export interface AICalculateRequest {
  query: string;
}

export interface AICalculateResponse {
  query: string;
  understood: string;
  result: number;
  calculation_id: string;
  tokens_used?: number;
}

// 历史记录类型
export interface HistoryItem {
  id: string;
  expression: string;
  result: string | null;
  calculation_type: 'basic' | 'scientific' | 'ai';
  created_at: string;
}

export interface HistoryResponse {
  items: HistoryItem[];
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
}

// AI 使用统计
export interface AIUsageStats {
  total_queries: number;
  total_tokens: number;
}

// API 错误响应
export interface APIError {
  detail: string;
}
