import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    data = pd.read_csv('C:/Users/user/Documents/Sir Neil/PYTHON/premid/ObesityDataSet_raw_and_data_sinthetic.csv')
    return data


def categorize_columns(data):
    bins_age = [10, 20, 30, 40, 50, 60, 70]
    labels_age = ['10-19', '20-29', '30-39', '40-49', '50-59', '60-69']
    data['Age'] = pd.cut(data['Age'], bins=bins_age, labels=labels_age, right=False)

    bins_fcvc = [1, 2, 3, float('inf')]
    labels_fcvc = ['1', '2', '3']
    data['FCVC'] = pd.cut(data['FCVC'], bins=bins_fcvc, labels=labels_fcvc, right=False)

    bins_ncp = [1, 2, 3, 4, float('inf')]
    labels_ncp = ['1', '2', '3', '4']
    data['NCP'] = pd.cut(data['NCP'], bins=bins_ncp, labels=labels_ncp, right=False)

    bins_ch2o = [1, 2, 3, float('inf')]
    labels_ch2o = ['1', '2', '3']
    data['CH2O'] = pd.cut(data['CH2O'], bins=bins_ch2o, labels=labels_ch2o, right=False)

    bins_faf = [0, 1, 2, 3, float('inf')]
    labels_faf = ['0', '1', '2', '3']
    data['FAF'] = pd.cut(data['FAF'], bins=bins_faf, labels=labels_faf, right=False)

    bins_tue = [0, 1, 2, float('inf')]
    labels_tue = ['0', '1', '2']
    data['TUE'] = pd.cut(data['TUE'], bins=bins_tue, labels=labels_tue, right=False)

    bins_height = [1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    labels_height = ['1.4-1.49', '1.5-1.59', '1.6-1.69', '1.7-1.79', '1.8-1.89', '1.9-1.99']
    data['Height'] = pd.cut(data['Height'], bins=bins_height, labels=labels_height, right=False)

    bins_weight = [38.0, 61.33, 83.67, 106.0, 128.33, 150.67, 173.1]
    labels_weight = ['38-61', '62-83', '84-106', '107-128', '129-150', '151-173']
    data['Weight'] = pd.cut(data['Weight'], bins=bins_weight, labels=labels_weight, right=False)

    return data


def plot_distribution(data, column):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data[column], kde=True, ax=ax)
    ax.set_title(f'Distribution of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Count')
    st.pyplot(fig)


def plot_pie_chart(data, column):
    fig, ax = plt.subplots(figsize=(8, 6))
    data[column].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_title(f'Pie Chart of {column}')
    st.pyplot(fig)


def plot_box_plot(data, column):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x=data[column], ax=ax)
    ax.set_title(f'Box Plot of {column}')
    ax.set_xlabel(column)
    st.pyplot(fig)

def load_data2():
    data2 = pd.read_csv('C:/Users/user/Documents/Sir Neil/PYTHON/premid/ObesityDataSet_raw_and_data_sinthetic.csv')
    return data2

# Function to plot a correlation heatmap
def plot_correlation_heatmap(data2):
    fig, ax = plt.subplots(figsize=(12, 8))
    numeric_data = data2.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_data.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

def main():
    st.title('Insights from Obesity Dataset')
    st.write('This app showcases insights from the obesity dataset.')

    data = load_data()
    data = categorize_columns(data)
    data2 = load_data2()

    st.sidebar.header('Options')

    if st.sidebar.checkbox('Show Dataset'):
        st.write(data)

    if st.sidebar.checkbox('Show Data Summary'):
        st.write(data.describe(include='all'))

    st.sidebar.write("""
    ## About the Dataset
    The dataset contains information about individuals including attributes such as age, gender, height, weight, physical activity level, eating habits, transportation mode, and family history of obesity.
    The target variable, 'NObeyesdad', represents the level of obesity classified into several categories.
    We'll explore various insights from this dataset using different visualization charts.
    """)

    visualization_type = st.sidebar.selectbox('Select Visualization Type', [
        'Distribution Plot', 'Pie Chart', 'Box Plot', 'Correlation Heatmap'
    ])

    if visualization_type == 'Distribution Plot':
        selected_column = st.sidebar.selectbox('Select Column for Distribution Plot', data.columns)
        plot_distribution(data, selected_column)
    elif visualization_type == 'Pie Chart':
        categorical_columns = ['Age', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE', 'Height', 'Weight']
        selected_column = st.sidebar.selectbox('Select Column for Pie Chart', categorical_columns)
        plot_pie_chart(data, selected_column)
    elif visualization_type == 'Box Plot':
        selected_column = st.sidebar.selectbox('Select Column for Box Plot', data.columns)
        plot_box_plot(data, selected_column)
    elif visualization_type == 'Correlation Heatmap':
        plot_correlation_heatmap(data2)

if __name__ == '__main__':
    main()
