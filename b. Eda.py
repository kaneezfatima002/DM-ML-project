import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.title("EDA Operations")
st.header("Dataset")

dataset = pd.read_csv('2019.csv')
st.write(dataset)

st.subheader("Dataset Summary")
st.write(dataset.describe())

st.header("Summary statistics")
column = st.selectbox("Select a column to analyze:", dataset.columns)

if column:
    mean = round(dataset[column].mean(),4)
    median = round(dataset[column].median(),4)
    mode = dataset[column].mode()[0] if not dataset[column].mode().empty else "No mode"
    
    
    st.subheader(f"Statistics for column: *{column}*")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"**Mean:**\n\n ***{mean}***")
    c2.markdown(f"**Median:**\n\n ***{median}***")
    c3.markdown(f"**Mode:**\n\n ***{mode}***")
    
st.header("Visualizations")
st.subheader("Histogram:")
num_cols = dataset.select_dtypes(include=['float64', 'int64']).columns.tolist()
column_h = st.selectbox("Select a column:", num_cols)
if column_h:
    plt.figure(figsize=(4, 2))
    plt.hist(dataset[column_h], bins=20, color='green', edgecolor='black')
    plt.title(f'Distribution of {column_h}')
    plt.xlabel(column_h)
    plt.ylabel('Frequency')
    st.pyplot(plt)
    
st.subheader("Scatter Plot:")

col1 = st.selectbox("Select X-axis column", num_cols, key="scatter_x")
col2 = st.selectbox("Select Y-axis column", num_cols, key="scatter_y")

    
if col1 and col2 and col1 != col2:
    plt.figure(figsize=(4, 2))
    sns.scatterplot(data=dataset, x=col1, y=col2, color='green')
    plt.title(f'{col1} vs {col2}')
    plt.xlabel(col1)
    plt.ylabel(col2)
    st.pyplot(plt)
elif col1 == col2:
    st.warning("Select two different columns for X and Y axes.")
    
st.header("Correlation Analysis")
num_data = dataset.select_dtypes(include=['float64', 'int64'])
corr_matrix = num_data.corr()

st.subheader("Correlation Matrix:")
st.dataframe(corr_matrix)

st.header("Missing Value Analysis")
missing_val = dataset.isnull().sum()
t_missing = missing_val.sum()

if t_missing > 0:
    st.subheader(f"There are *{t_missing}* values in dataset. ")
else:
    st.subheader("There is *no missing value* in the dataset.")
    
st.header("Outlier Detection")

outlier_cols = ["GDP per capita","Social support","Healthy life expectancy","Freedom to make life choices","Generosity","Perceptions of corruption"]
sel_out_col = st.selectbox("Select a column for outlier detection:", outlier_cols) 
if sel_out_col:
    Q1 = dataset[sel_out_col].quantile(0.25)  # First quartile
    Q3 = dataset[sel_out_col].quantile(0.75)  # Third quartile
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = dataset.loc[(dataset[sel_out_col] < lower_bound) | (dataset[sel_out_col] > upper_bound)]
    st.write(f"Outlier Summary for {sel_out_col}")
    st.write(f"Number of outliers: {len(outliers)}")

    if len(outliers) > 0:
        st.dataframe(outliers[[sel_out_col]])
        
    fig, ax = plt.subplots(figsize=(4, 2))
    sns.boxplot(x=dataset[sel_out_col], color="green", ax=ax)
    ax.set_title(f"Boxplot for {sel_out_col}")
    st.pyplot(fig)
    
st.header("Data Types and Unique Values")
st.subheader("Datatypes:")
st.write(dataset.dtypes)
st.subheader("Unique Values Count:")
st.write(dataset.nunique())

st.header("Feature Distribution")
dist_col = st.selectbox("Select a column for distribution analysis:", num_cols)
if dist_col:
    fig, ax = plt.subplots()
    sns.histplot(dataset[dist_col], kde=True, ax=ax, color="green")
    ax.set_title(f"Distribution of {dist_col}")
    st.pyplot(fig)

st.header("Trend Analysis")
x_axis = st.selectbox("Select a column for x-axis:", num_cols)
y_axis = st.selectbox("Select a column for y-axis:", num_cols)
fig, ax = plt.subplots()
sns.lineplot(data=dataset, x=x_axis, y=y_axis, ax=ax, color="green")
ax.set_title(f"{x_axis} vs. {y_axis}")
st.pyplot(fig)


st.header("Pairwise Relationships")
x_column = st.selectbox("Select X-axis column for pairwise analysis:", num_cols)
y_column = st.selectbox("Select Y-axis column for pairwise analysis:", num_cols)
if x_column and y_column:
    fig, ax = plt.subplots()
    sns.scatterplot(data=dataset, x=x_column, y=y_column, ax=ax, color="green")
    ax.set_title(f"Pairwise Relationship between {x_column} and {y_column}")
    st.pyplot(fig)
    


st.header("Cluster Analysis")
selected_features = st.multiselect("Select features for clustering:", num_cols)
if len(selected_features) > 1:
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(dataset[selected_features])

    num_clusters = st.slider("Select the number of clusters:", min_value=2, max_value=10, value=3)
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)

    # Add cluster labels to the dataset
    dataset['Cluster'] = clusters
    st.write(dataset[['Cluster'] + selected_features].head())

    # Visualize clusters (if 2 features selected)
    if len(selected_features) == 2:
        fig, ax = plt.subplots()
        sns.scatterplot(x=selected_features[0], y=selected_features[1], hue=dataset['Cluster'], palette="viridis", data=dataset, ax=ax)
        ax.set_title("K-Means Clustering")
        st.pyplot(fig)


