/**
 * 计算器主组件
 */
import { useState } from 'react';
import { Card, Input, Button, Space, Switch, message, Spin } from 'antd';
import {
  CalculatorOutlined,
  RobotOutlined,
  ClearOutlined,
} from '@ant-design/icons';
import { useCalculatorStore } from '@/stores/useCalculatorStore';

const { TextArea } = Input;

export const Calculator = () => {
  const {
    expression,
    result,
    isLoading,
    error,
    useAI,
    setExpression,
    calculate,
    aiCalculate,
    clear,
    toggleAI,
    clearError,
  } = useCalculatorStore();

  const [aiQuery, setAiQuery] = useState('');

  const handleCalculate = async () => {
    clearError();
    if (useAI) {
      // AI 计算
      if (!aiQuery.trim()) {
        message.warning('请输入自然语言查询');
        return;
      }
      await aiCalculate(aiQuery);
      if (!error) {
        message.success('AI 计算完成');
      }
    } else {
      // 基础计算
      if (!expression.trim()) {
        message.warning('请输入数学表达式');
        return;
      }
      await calculate();
      if (!error) {
        message.success('计算完成');
      }
    }
  };

  const handleClear = () => {
    clear();
    setAiQuery('');
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleCalculate();
    }
  };

  return (
    <Card
      title="智能计算器"
      extra={
        <Space>
          <span>AI 模式</span>
          <Switch
            checked={useAI}
            onChange={toggleAI}
            checkedChildren={<RobotOutlined />}
            unCheckedChildren={<CalculatorOutlined />}
          />
        </Space>
      }
      style={{ maxWidth: 600, margin: '0 auto' }}
    >
      <Spin spinning={isLoading}>
        <Space direction="vertical" style={{ width: '100%' }} size="large">
          {/* 输入区域 */}
          {useAI ? (
            <div>
              <div style={{ marginBottom: 8, fontWeight: 500 }}>
                自然语言查询
              </div>
              <TextArea
                value={aiQuery}
                onChange={(e) => setAiQuery(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="例如: 帮我算123加456"
                rows={3}
                disabled={isLoading}
              />
            </div>
          ) : (
            <div>
              <div style={{ marginBottom: 8, fontWeight: 500 }}>
                数学表达式
              </div>
              <TextArea
                value={expression}
                onChange={(e) => setExpression(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="例如: 2 + 3 * 4 或 sqrt(16)"
                rows={3}
                disabled={isLoading}
              />
            </div>
          )}

          {/* AI 理解的表达式 */}
          {useAI && expression && (
            <div>
              <div style={{ marginBottom: 8, fontWeight: 500, color: '#1890ff' }}>
                AI 理解为
              </div>
              <Input value={expression} readOnly />
            </div>
          )}

          {/* 结果显示 */}
          {result !== null && (
            <div>
              <div style={{ marginBottom: 8, fontWeight: 500 }}>计算结果</div>
              <div
                style={{
                  fontSize: 32,
                  fontWeight: 600,
                  color: '#52c41a',
                  textAlign: 'center',
                  padding: '16px 0',
                  background: '#f0f2f5',
                  borderRadius: 4,
                }}
              >
                {result}
              </div>
            </div>
          )}

          {/* 错误提示 */}
          {error && (
            <div
              style={{
                color: '#ff4d4f',
                background: '#fff1f0',
                border: '1px solid #ffccc7',
                borderRadius: 4,
                padding: 12,
              }}
            >
              {error}
            </div>
          )}

          {/* 操作按钮 */}
          <Space style={{ width: '100%' }}>
            <Button
              type="primary"
              icon={useAI ? <RobotOutlined /> : <CalculatorOutlined />}
              onClick={handleCalculate}
              loading={isLoading}
              block
              size="large"
            >
              {useAI ? 'AI 计算' : '计算'}
            </Button>
            <Button
              icon={<ClearOutlined />}
              onClick={handleClear}
              disabled={isLoading}
              size="large"
            >
              清空
            </Button>
          </Space>

          {/* 快捷按钮 (仅基础模式) */}
          {!useAI && (
            <div>
              <div style={{ marginBottom: 8, fontWeight: 500 }}>常用函数</div>
              <Space wrap>
                {[
                  'sqrt(',
                  'sin(',
                  'cos(',
                  'tan(',
                  'log(',
                  'exp(',
                  'abs(',
                  'pow(',
                  'pi',
                  'e',
                ].map((func) => (
                  <Button
                    key={func}
                    size="small"
                    onClick={() => setExpression(expression + func)}
                  >
                    {func}
                  </Button>
                ))}
              </Space>
            </div>
          )}

          {/* 使用提示 */}
          <div style={{ fontSize: 12, color: '#8c8c8c' }}>
            {useAI ? (
              <>
                💡 提示: 使用自然语言描述您的计算需求,AI 会理解并执行
                <br />
                例如: "帮我算100的平方根" 或 "2的10次方是多少"
              </>
            ) : (
              <>
                💡 提示: 支持 +, -, *, /, **, % 等运算符
                <br />
                支持函数: sqrt, sin, cos, tan, log, exp, abs, pow
                <br />
                支持常量: pi, e, tau | 按 Enter 键快速计算
              </>
            )}
          </div>
        </Space>
      </Spin>
    </Card>
  );
};
