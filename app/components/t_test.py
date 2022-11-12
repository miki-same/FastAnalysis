import streamlit as st
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from components.alert import select_csv_alert
def t_test_component():
    if not st.session_state.uploaded_file:
        select_csv_alert()
    else:
        df:pd.DataFrame =st.session_state.df
        ex=st.selectbox("独立変数",df.columns,key="independent_t")
        ob=st.selectbox("従属変数",df.columns,key="dependent_t")
        
        
        if len(set(df[ex]))!=2:
            st.warning('独立変数の水準数が不正です。')
        
        else:
            level1=list(set(df[ex]))[0]
            level2=list(set(df[ex]))[1]

            level1_list=df[df[ex]==level1][ob]
            level2_list=df[df[ex]==level2][ob]

            t,p=stats.ttest_ind(level1_list,level2_list,equal_var=True)

            #統計量を表示
            col1,col2=st.columns(2)
            col1.metric("t-value",f'{t:.2f}')
            col2.metric("p-value",f'{p:.3f}')

            '''
            棒グラフの描画
            '''
            fig=plt.figure(figsize=(20,10))
            ax=fig.add_subplot(111)
            p=sns.barplot(x=ex,y=ob,data=df,ax=ax)
            st.pyplot(fig)