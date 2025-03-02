# 带缓冲池的贝叶斯优化器
# 原先的贝叶斯优化器算法流程:
#    创建贝叶斯优化器,指定函数(可以不指定)、参数范围等
#    指定采样函数,使用UCB方法
#    for i in range(0,n):
#      通过采样函数suggest获取下一个采样点
#      将采样点输入到黑盒函数中获取目标值
#      将采样点和目标值register,也就是记录到GP中去。

# 现在的贝叶斯优化器算法流程：
#    创建带缓冲池的贝叶斯优化器
#    指定采样函数,使用UCB方法
#    (运行在一个async def函数中)
#    when get posted target and config:
#      当缓冲区较小,
#      全部用于训练
#
#      当缓冲区较大,
#      优化器记录posted次数,
#      每接收到max_size * 0.05次posted后,
#          删除之前的GP
#          获取新的采样点集合
#          生成新的GP
#      使用新的GP获取下一个采样点
#      将采样点输入到黑盒函数中等待回复
#
#    需要修改的主要是register函数






