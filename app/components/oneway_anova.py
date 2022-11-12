import streamlit as st
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from components.alert import select_csv_alert

def oneway_anova_component():
    
    if not st.session_state.uploaded_file:
        select_csv_alert()

    else:
        df:pd.DataFrame =st.session_state.df
        
        ex=st.selectbox("独立変数",df.columns,key="independent_anova")
        ob=st.selectbox("従属変数",df.columns,key="dependent_anova")
        
        levels=list(set(df[ex]))
        levels_list=[df[df[ex]==level][ob] for level in levels]

        
        f,p=stats.f_oneway(*levels_list)

        '''
        結果の表示
        '''
        col1,col2=st.columns(2)
        col1.metric("f-value",f'{f:.2f}')
        col2.metric("p-value",f'{p:.3f}')

        '''
        棒グラフの描画
        '''
        fig=plt.figure(figsize=(20,10))
        ax=fig.add_subplot(111)
        p=sns.barplot(x=ex,y=ob,data=df,ax=ax)
        st.pyplot(fig)