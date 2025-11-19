/**
 * 布局组件
 */
import { Layout as AntLayout, Menu, Button, Space } from 'antd';
import {
  CalculatorOutlined,
  HistoryOutlined,
  LogoutOutlined,
  UserOutlined,
} from '@ant-design/icons';
import { Outlet, useNavigate, useLocation } from 'react-router-dom';
import { useAuthStore } from '@/stores/useAuthStore';

const { Header, Content, Footer } = AntLayout;

export const Layout = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { user, logout } = useAuthStore();

  const menuItems = [
    {
      key: '/',
      icon: <CalculatorOutlined />,
      label: '计算器',
    },
    {
      key: '/history',
      icon: <HistoryOutlined />,
      label: '历史记录',
    },
  ];

  const handleMenuClick = ({ key }: { key: string }) => {
    navigate(key);
  };

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <AntLayout style={{ minHeight: '100vh' }}>
      <Header
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          background: '#001529',
          padding: '0 24px',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', flex: 1 }}>
          <div
            style={{
              color: 'white',
              fontSize: 20,
              fontWeight: 600,
              marginRight: 48,
            }}
          >
            智能计算器
          </div>
          <Menu
            theme="dark"
            mode="horizontal"
            selectedKeys={[location.pathname]}
            items={menuItems}
            onClick={handleMenuClick}
            style={{ flex: 1, minWidth: 0 }}
          />
        </div>

        <Space>
          <span style={{ color: 'rgba(255, 255, 255, 0.65)' }}>
            <UserOutlined /> {user?.username}
          </span>
          <Button
            type="text"
            icon={<LogoutOutlined />}
            onClick={handleLogout}
            style={{ color: 'rgba(255, 255, 255, 0.65)' }}
          >
            退出
          </Button>
        </Space>
      </Header>

      <Content style={{ padding: '24px 48px' }}>
        <div style={{ minHeight: 380 }}>
          <Outlet />
        </div>
      </Content>

      <Footer style={{ textAlign: 'center' }}>
        智能计算器 ©2025 Created by zuojunwei
      </Footer>
    </AntLayout>
  );
};
