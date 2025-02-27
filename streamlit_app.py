import streamlit as st
import pandas as pd
import os

# 设置 CSV 文件路径
csv_path = r"C:\Users\a00219912\Downloads\SPPALL\Quickly_get_faccts_sale.csv"

# 读取 CSV 数据
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    
    # Streamlit 页面标题
    st.title("CSV 数据筛选器")

    # 选择筛选列（默认选第一列）
    filter_column = st.selectbox("选择要筛选的列", df.columns)

    # 获取唯一值
    unique_values = df[filter_column].dropna().unique()

    # 创建多选筛选器
    selected_values = st.multiselect("选择要筛选的值", unique_values)

    # 筛选数据
    if selected_values:
        filtered_df = df[df[filter_column].isin(selected_values)]
    else:
        filtered_df = df  # 若未选择筛选项，则显示全部数据

    # 显示数据
    st.write(filtered_df)
else:
    st.error(f"文件未找到: {csv_path}")
