import streamlit as st
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns

from components.t_test import t_test_component
from components.oneway_anova import oneway_anova_component
from components.twoway_anova import twoway_anova_component
from components.sidebar import side_bar_component

'''
フォントサイズ・日本語フォントの設定
'''
sns.set(font_scale=3,font="IPAexGothic")


st.title("FastAnalysis📊")

with st.sidebar:
    side_bar_component()

with st.container():
    if "df" in st.session_state:
        with st.expander("データのプレビュー"):
            st.dataframe(st.session_state.df.head())


t_test_tab,oneway_anova_tab,twoway_anova_tab=st.tabs(["t検定","1元配置分散分析","2元配置分散分析"])

with t_test_tab:
    t_test_component()

with oneway_anova_tab:
    oneway_anova_component()

with twoway_anova_tab:
    twoway_anova_component()