# 测试

## 测试类型
- **unit/**: 单元测试
- **integration/**: 集成测试
- **e2e/**: 端到端测试
- **performance/**: 性能测试

## 测试框架
- Backend: pytest
- Frontend: Jest + React Testing Library
- E2E: Playwright / Cypress

## 运行测试
```bash
# 后端测试
pytest backend/tests/

# 前端测试
npm test

# E2E 测试
npx playwright test
```
