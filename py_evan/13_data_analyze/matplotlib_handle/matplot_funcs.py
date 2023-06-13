# coding:utf-8
# time: 2023/6/12
# author: evan
# matplotlib基本函数
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def gen_graph():
    fig, axs = plt.subplots(2, 1)

    # 生成数据
    data = np.random.randn(100)

    # 填充数据、绘制图表
    axs[0].hist(data, bins=50, color='red')
    axs[1].plot(data, color='green')

    # 参数设置
    axs[0].set_title('normalized distribution')
    axs[1].set_title('random sample')
    axs[0].set_xlabel('value')
    axs[0].set_ylabel('freq')
    axs[1].set_xlabel('index')
    axs[1].set_ylabel('value')
    # 调整巨鹿
    fig.tight_layout()

    # 显示
    plt.show()


def draw_scatter():
    """
    散点图
    :return:
    """
    # 探索：商品均价 vs 销售数量的相关性
    data = pd.read_excel("../order2019.xlsx")
    types = data['goodsID'].unique().tolist()
    len(types)

    prices = []
    amounts = []

    for t in types:
        price = data[data['goodsID'] == t]['orderAmount'].mean()
        amount = len(data[data['goodsID'] == t])

        prices.append(price)
        amounts.append(amount)

    # 绘制散点图

    plt.scatter(x=prices, y=amounts, color='green', marker='*')

    plt.title('goods prices vs amounts')
    plt.xlabel('price')
    plt.ylabel('amount')

    plt.xlim(600, 1500)
    plt.ylim(40, 160)
    plt.grid()

    # 随机比较和可视化3个商品的订单和销售情况
    prices = []
    amounts = []

    for t in ['PR000064', 'PR000582', 'PR000302']:
        price = data[data['goodsID'] == t]['orderAmount'].mean()
        amount = len(data[data['goodsID'] == t])

        prices.append(price)
        amounts.append(amount)

    plt.scatter(x=prices[0], y=amounts[0], color='green', marker='*')
    plt.scatter(x=prices[1], y=amounts[1], color='red')
    plt.scatter(x=prices[2], y=amounts[2], color='blue', marker='+')

    plt.title('goods prices vs amounts')
    plt.xlabel('price')
    plt.ylabel('amount')

    plt.xlim(600, 1500)
    plt.ylim(40, 160)
    plt.grid()
    plt.show()


def heat_map():
    """
    热力图：散点图坐标轴为数值型数据，热力图类别型数据，体现的是两组变量的相关性
    :return:
    """
    # 案例背景：工厂出货品质的好坏
    factories = ['fac1', 'fac2', 'fac3', 'fac4', 'fac5']
    quanlity = ['bad', 'poor', 'general', 'good', 'great']
    result = np.round(np.random.random(25).reshape(5, 5), 1)
    fig, ax = plt.subplots(1, 1)

    ax.imshow(result)

    # 轮流锁定单元格
    for i in np.arange(len(factories)):
        for j in np.arange(len(quanlity)):
            plt.text(j, i, result[i][j], color='w', ha='center', va='center')

    # 设置坐标轴的类别数据标签
    ax.set_xticks(np.arange(len(quanlity)))
    ax.set_yticks(np.arange(len(factories)))
    ax.set_xticklabels(quanlity)
    ax.set_yticklabels(factories)

    # 修饰工作
    ax.set_title('goods quality of factories')
    fig.tight_layout()
    plt.show()


def distribution_graph():
    data = pd.read_excel("../order2019.xlsx")
    # 直方图：类别（数值）、频数（频率）
    plt.hist(data['orderAmount'], bins=1000)
    plt.xlim(data['orderAmount'].min(), 5000)
    plt.ylim(0, 2000)
    plt.show()


if __name__ == '__main__':
    # gen_graph()
    # draw_scatter()
    distribution_graph()
