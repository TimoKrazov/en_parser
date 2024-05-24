import streamlit as st
import pandas as pd


#Получение указанного диапазона
def get_selected_ranges(df, ranges) -> list:
    selected_ranges = []
    for start_row, end_row, start_col, end_col in ranges:
        selected_data = df.iloc[start_row - 1:end_row, start_col - 1:end_col]
        selected_ranges.append(selected_data)
    return selected_ranges

#Получение границ диапазона
def add_selected_range(df, ranges) -> list:
    #Cоздание полей для ввода диапазона
    col1, col2 = st.columns(2)

    #Получение значений, которые ввёл пользователь
    with col1:
        max_row_value = len(df) - 1
        start_row = st.number_input("Начальная строка", min_value=1, max_value=max_row_value + 1, key="start_row")
        end_row = st.number_input("Конечная строка", min_value=start_row, max_value=max_row_value + 1,
                                  value=max_row_value + 1, key="end_row")

    with col2:
        max_col_value = len(df.columns) - 1
        start_col = st.number_input("Начальный столбец", min_value=1, max_value=max_col_value + 1, key="start_col")
        end_col = st.number_input("Конечный столбец", min_value=start_col, max_value=max_col_value + 1,
                                  value=max_col_value + 1, key="end_col")
        if st.button("Добавить выбранный диапазон"):
            ranges.append((start_row, end_row, start_col, end_col))
    return ranges


#Очистка диапазона
def clear_ranges(ranges) -> list:
    ranges = []
    return ranges


#Возвращает выбранный диапазон с удалением пустых строк
def chooses_ranges(df):
    selected_data = df.iloc[0:len(df), 0:len(df.columns)]
    selected_data = selected_data.dropna(how='all')
    selected_data = selected_data.dropna(axis = 1, how='all')
    selected_data.columns = range(1, len(selected_data.columns) + 1)
    selected_data.index = range(1, len(selected_data) + 1)
    return selected_data


#Преобразование в csv-формат
def convert_to_csv(ranges) -> bytes:
    sd = pd.concat([*ranges], axis=1, join='inner')
    return sd.to_csv(index=False).encode('utf-16')
