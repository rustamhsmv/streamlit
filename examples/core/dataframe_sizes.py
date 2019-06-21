import streamlit as st
import numpy as np
import pandas as pd

# Explicitly seed the RNG for deterministic results
np.random.seed(0)

st.title('Tables with different sizes')

st.header('Long cells that overflow')

st.write('''
    Long text should show an ellipsis. All cells should have a tooltip
    with their entire un-ellipsized contents.
    ''')

st.dataframe({
    'foo': ['hello', 'world', 'foo '*30],
    'bar': ['hello', 'world', 'bar'*30],
    'baz': [1, 2, 3],
    'boz': [1, 2, 3],
    'buz': [1, 2, 3],
    'biz'*30: [1, 2, 3],
    'bim': [1, 2, 3],
})

st.dataframe({
    'foo': ['hello', 'world', 'foo '*30],
})

ROWS = 2

st.header('Using st.dataframe')

for cols in [4, 5, 6, 20]:
    df = pd.DataFrame(np.random.randn(ROWS, cols), index=range(ROWS),
                      columns=range(cols))
    st.dataframe(df)

st.header('Overriding st.dataframe')

for cols in [4, 5, 6, 20]:
    df = pd.DataFrame(np.random.randn(ROWS, cols), index=range(ROWS),
                      columns=range(cols))
    df_elt = st.dataframe(np.random.randn(200, 200))
    df_elt.dataframe(df)

st.header('Using st.table')

for cols in [4, 5, 6, 20]:
    df = pd.DataFrame(np.random.randn(ROWS, cols), index=range(ROWS),
                      columns=range(cols))
    st.table(df)

st.header('Overriding st.table')

for cols in [4, 5, 6, 20]:
    df = pd.DataFrame(np.random.randn(ROWS, cols), index=range(ROWS),
                      columns=range(cols))
    df_elt = st.table(np.random.randn(200, 200))
    df_elt.table(df)