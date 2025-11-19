/**
 * 历史记录列表组件
 */
import { useEffect, useState } from 'react';
import { Card, Table, Button, Space, message, Tag, Popconfirm } from 'antd';
import { DeleteOutlined, ClearOutlined, ReloadOutlined } from '@ant-design/icons';
import { apiClient } from '@/services/api';
import type { HistoryItem, HistoryResponse } from '@/types';

export const HistoryList = () => {
  const [data, setData] = useState<HistoryResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState(1);
  const [pageSize, setPageSize] = useState(10);

  const fetchHistory = async () => {
    setLoading(true);
    try {
      const response = await apiClient.getHistory(page, pageSize);
      setData(response);
    } catch (error: any) {
      message.error('获取历史记录失败');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchHistory();
  }, [page, pageSize]);

  const handleDelete = async (id: string) => {
    try {
      await apiClient.deleteHistory(id);
      message.success('删除成功');
      fetchHistory();
    } catch (error) {
      message.error('删除失败');
    }
  };

  const handleClearAll = async () => {
    try {
      const result = await apiClient.clearHistory();
      message.success(`已清空 ${result.deleted_count} 条记录`);
      fetchHistory();
    } catch (error) {
      message.error('清空失败');
    }
  };

  const columns = [
    {
      title: '表达式',
      dataIndex: 'expression',
      key: 'expression',
      ellipsis: true,
    },
    {
      title: '结果',
      dataIndex: 'result',
      key: 'result',
      width: 150,
      render: (text: string) => (
        <span style={{ fontWeight: 600, color: '#52c41a' }}>{text}</span>
      ),
    },
    {
      title: '类型',
      dataIndex: 'calculation_type',
      key: 'calculation_type',
      width: 100,
      render: (type: string) => {
        const colorMap: Record<string, string> = {
          basic: 'blue',
          scientific: 'cyan',
          ai: 'purple',
        };
        return <Tag color={colorMap[type]}>{type}</Tag>;
      },
    },
    {
      title: '时间',
      dataIndex: 'created_at',
      key: 'created_at',
      width: 180,
      render: (text: string) => new Date(text).toLocaleString('zh-CN'),
    },
    {
      title: '操作',
      key: 'action',
      width: 100,
      render: (_: any, record: HistoryItem) => (
        <Popconfirm
          title="确定删除这条记录?"
          onConfirm={() => handleDelete(record.id)}
          okText="确定"
          cancelText="取消"
        >
          <Button
            type="link"
            danger
            size="small"
            icon={<DeleteOutlined />}
          >
            删除
          </Button>
        </Popconfirm>
      ),
    },
  ];

  return (
    <Card
      title="计算历史"
      extra={
        <Space>
          <Button
            icon={<ReloadOutlined />}
            onClick={fetchHistory}
            loading={loading}
          >
            刷新
          </Button>
          <Popconfirm
            title="确定清空所有历史记录?"
            onConfirm={handleClearAll}
            okText="确定"
            cancelText="取消"
          >
            <Button icon={<ClearOutlined />} danger>
              清空
            </Button>
          </Popconfirm>
        </Space>
      }
      style={{ maxWidth: 1200, margin: '24px auto' }}
    >
      <Table
        dataSource={data?.items || []}
        columns={columns}
        rowKey="id"
        loading={loading}
        pagination={{
          current: page,
          pageSize: pageSize,
          total: data?.total || 0,
          showSizeChanger: true,
          showTotal: (total) => `共 ${total} 条`,
          onChange: (newPage, newPageSize) => {
            setPage(newPage);
            setPageSize(newPageSize);
          },
        }}
      />
    </Card>
  );
};
