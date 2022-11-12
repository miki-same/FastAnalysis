import streamlit as st
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from components.alert import select_csv_alert

def twoway_anova_component():
    if not st.session_state.uploaded_file:
        select_csv_alert()
    else:
        st.write("データ")
        df:pd.DataFrame =st.session_state.df
        ex = st.multiselect("説明変数を選択してください（複数選択可）", df.columns)
        ob = st.selectbox("目的変数を選択してください", df.columns)
        if len(ex)!=2:
            st.warning('独立変数を2つ選んでください。')
        else:
            formula= f'{ob} ~ ({ex[0]})  + ({ex[1]}) + ({ex[0]}):({ex[1]})'
            model=ols(formula,df).fit()
            aov_table=anova_lm(model,typ=2)

            #aov_tableから統計量を選択
            f_ex_1=aov_table["F"][f"{ex[0]}"]
            f_ex_2=aov_table["F"][f"{ex[1]}"]
            f_interaction=aov_table["F"][f"{ex[0]}:{ex[1]}"]
            p_ex_1=aov_table["PR(>F)"][f"{ex[0]}"]
            p_ex_2=aov_table["PR(>F)"][f"{ex[1]}"]
            p_interaction=aov_table["PR(>F)"][f"{ex[0]}:{ex[1]}"]
            
            
            '''
            結果の表示
            '''
            st.markdown(f"#### {ex[0]}")
            ex1_f,ex1_p=st.columns(2)
            ex1_p.metric("F-value",f'{f_ex_1:.2f}')
            ex1_f.metric("p-value",f'{p_ex_1:.3f}')

            st.markdown(f"#### {ex[1]}")
            ex2_f,ex2_p=st.columns(2)
            ex2_p.metric("F-value",f'{f_ex_2:.2f}')
            ex2_f.metric("p-value",f'{p_ex_2:.3f}')

            st.markdown(f"#### {ex[0]} x {ex[1]}")
            itr_f,itr_p=st.columns(2)
            itr_p.metric("F-value",f'{f_interaction:.2f}')
            itr_f.metric("p-value",f'{p_interaction:.3f}')

            '''
            棒グラフの描画
            '''
            fig=plt.figure(figsize=(20,10))
            ax=fig.add_subplot(111)
            p=sns.barplot(x=ex[0],y=ob,hue=ex[1],data=df,ax=ax)
            st.pyplot(fig)