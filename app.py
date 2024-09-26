import pandas as pd
import streamlit as st
from sql_queries import *

st.title('Test aggiornamento Database')

st.upload_file(label='carica')


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


db_path = 'sqlite:///test.db'
engine = create_database(db_path=db_path)


create_table(
    engine=engine,
    table_name='persone',
    column_types={
        'id':'INTEGER',
        'nome':'TEXT',
        'cognome':'TEXT'
    }, primary_keys=['id'])



if st.button('insert'):
    insert_table(engine=engine, table_name='persone', df=dataframe)

if st.button('Vedi dati'):
    df = select_from(engine=engine, from_table='persone')
    st.write(df)

