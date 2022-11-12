import streamlit as st
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def side_bar_component():
    st.file_uploader("CSVファイルを選択", accept_multiple_files=False,key="uploaded_file")
    if st.session_state.uploaded_file:
        st.session_state.df=pd.read_csv(st.session_state.uploaded_file)
        