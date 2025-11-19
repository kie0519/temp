/**
 * API 客户端
 * 封装所有后端 API 调用
 */
import axios, { AxiosInstance, AxiosError } from 'axios';
import type {
  LoginRequest,
  RegisterRequest,
  AuthResponse,
  User,
  CalculateRequest,
  CalculateResponse,
  AICalculateRequest,
  AICalculateResponse,
  HistoryResponse,
  AIUsageStats,
  APIError,
} from '@/types';

class APIClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: '/api/v1',
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // 请求拦截器 - 添加 token
    this.client.interceptors.request.use(
      (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
      },
      (error) => Promise.reject(error)
    );

    // 响应拦截器 - 处理错误
    this.client.interceptors.response.use(
      (response) => response,
      (error: AxiosError<APIError>) => {
        if (error.response?.status === 401) {
          // Token 过期,清除并跳转登录
          localStorage.removeItem('access_token');
          localStorage.removeItem('user');
          window.location.href = '/login';
        }
        return Promise.reject(error);
      }
    );
  }

  // ==================== 认证 API ====================

  /**
   * 用户注册
   */
  async register(data: RegisterRequest): Promise<User> {
    const response = await this.client.post<User>('/auth/register', data);
    return response.data;
  }

  /**
   * 用户登录
   */
  async login(data: LoginRequest): Promise<AuthResponse> {
    const response = await this.client.post<AuthResponse>('/auth/login', data);

    // 保存 token 和用户信息
    localStorage.setItem('access_token', response.data.access_token);
    localStorage.setItem('user', JSON.stringify(response.data.user));

    return response.data;
  }

  /**
   * 获取当前用户信息
   */
  async getCurrentUser(): Promise<User> {
    const response = await this.client.get<User>('/auth/me');
    return response.data;
  }

  /**
   * 登出
   */
  logout(): void {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
  }

  // ==================== 计算 API ====================

  /**
   * 基础计算
   */
  async calculate(data: CalculateRequest): Promise<CalculateResponse> {
    const response = await this.client.post<CalculateResponse>('/calculate', data);
    return response.data;
  }

  /**
   * 验证表达式
   */
  async validateExpression(expression: string): Promise<{ valid: boolean; message: string }> {
    const response = await this.client.post<{ valid: boolean; message: string }>(
      '/calculate/validate',
      { expression }
    );
    return response.data;
  }

  /**
   * AI 智能计算
   */
  async aiCalculate(data: AICalculateRequest): Promise<AICalculateResponse> {
    const response = await this.client.post<AICalculateResponse>('/calculate/ai', data);
    return response.data;
  }

  // ==================== 历史记录 API ====================

  /**
   * 获取历史记录
   */
  async getHistory(page = 1, pageSize = 20): Promise<HistoryResponse> {
    const response = await this.client.get<HistoryResponse>('/history', {
      params: { page, page_size: pageSize },
    });
    return response.data;
  }

  /**
   * 删除单条历史记录
   */
  async deleteHistory(id: string): Promise<void> {
    await this.client.delete(`/history/${id}`);
  }

  /**
   * 清空所有历史记录
   */
  async clearHistory(): Promise<{ message: string; deleted_count: number }> {
    const response = await this.client.delete<{ message: string; deleted_count: number }>('/history');
    return response.data;
  }

  /**
   * 获取 AI 使用统计
   */
  async getAIUsageStats(): Promise<AIUsageStats> {
    const response = await this.client.get<AIUsageStats>('/history/stats/ai-usage');
    return response.data;
  }
}

// 导出单例
export const apiClient = new APIClient();
