/**
 * 计算器状态管理
 */
import { create } from 'zustand';
import type { CalculateResponse, AICalculateResponse } from '@/types';
import { apiClient } from '@/services/api';

interface CalculatorState {
  expression: string;
  result: number | null;
  isLoading: boolean;
  error: string | null;
  useAI: boolean;

  // Actions
  setExpression: (expr: string) => void;
  calculate: () => Promise<void>;
  aiCalculate: (query: string) => Promise<void>;
  clear: () => void;
  toggleAI: () => void;
  clearError: () => void;
}

export const useCalculatorStore = create<CalculatorState>((set, get) => ({
  expression: '',
  result: null,
  isLoading: false,
  error: null,
  useAI: false,

  setExpression: (expr: string) => {
    set({ expression: expr, error: null });
  },

  calculate: async () => {
    const { expression } = get();
    if (!expression.trim()) {
      set({ error: '请输入表达式' });
      return;
    }

    set({ isLoading: true, error: null });
    try {
      const response: CalculateResponse = await apiClient.calculate({ expression });
      set({
        result: response.result,
        isLoading: false,
      });
    } catch (error: any) {
      set({
        error: error.response?.data?.detail || '计算失败',
        result: null,
        isLoading: false,
      });
    }
  },

  aiCalculate: async (query: string) => {
    if (!query.trim()) {
      set({ error: '请输入查询' });
      return;
    }

    set({ isLoading: true, error: null });
    try {
      const response: AICalculateResponse = await apiClient.aiCalculate({ query });
      set({
        expression: response.understood,
        result: response.result,
        isLoading: false,
      });
    } catch (error: any) {
      set({
        error: error.response?.data?.detail || 'AI计算失败',
        result: null,
        isLoading: false,
      });
    }
  },

  clear: () => {
    set({
      expression: '',
      result: null,
      error: null,
    });
  },

  toggleAI: () => {
    set((state) => ({ useAI: !state.useAI }));
  },

  clearError: () => set({ error: null }),
}));
