/**
 * 首页 - 计算器页面
 */
import { Calculator } from '@/components/Calculator/Calculator';

export const HomePage = () => {
  return (
    <div style={{ maxWidth: 1200, margin: '0 auto', padding: '24px 0' }}>
      <Calculator />
    </div>
  );
};
