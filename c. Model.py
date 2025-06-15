import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error  
from sklearn.metrics import r2_score

dataset = pd.read_csv('2019.csv')

data_prepared = dataset.drop(['Country or region'], axis=1)        
data_prepared = (data_prepared - data_prepared.min()) / (data_prepared.max() - data_prepared.min())

st.header("Prepared Dataset for ML Model:")
st.write(data_prepared)
data_prepared.to_csv('prepared_data.csv', index=False)

data_prepared = pd.read_csv('prepared_data.csv') 
st.title("Linear Regression on World Happiness Dataset")

st.header("Feature and Target Selection")
features = data_prepared.columns.drop('Score')
feature = st.selectbox("Select a feature (predictor):", features)
target = 'Score'

if feature:
    X = data_prepared[[feature]].values
    Y = data_prepared[target].values

    model = LinearRegression()
    model.fit(X, Y)
    Y_pred = model.predict(X)

    mse = mean_squared_error(Y, Y_pred)
    r2 = r2_score(Y, Y_pred)
    slope = model.coef_[0]
    intercept = model.intercept_

    st.subheader("Model Results:")
    st.write(f"**Optimal Intercept (theta_0):** {intercept}")
    st.write(f"**Optimal Slope (theta_1):** {slope}")
    st.write(f"**Mean Squared Error (MSE):** {mse}")
    st.write(f"**R² Score (Accuracy):** {r2}")

    st.subheader("Regression Line Visualization")
    fig, ax = plt.subplots()
    ax.scatter(X, Y, color='green', label='Actual Data')
    ax.plot(X, Y_pred, color='red', label='Regression Line')
    ax.set_xlabel(feature)
    ax.set_ylabel(target)
    ax.set_title('Linear Regression')
    ax.legend()
    st.pyplot(fig)

st.subheader("Evaluations:")
st.write("**Slope** indicates the positive influence of the selected feature on *happiness score*, if it has a positive value, otherwise a negative influence.\n Low value of **MSE** indicates that the model is predicting well and selected feature strongly correlates with happiness.")
st.header("Predictions")
st.subheader("GPD per capita:")
st.write("A *higher GDP per capita* typically leads to *higher happiness scores*, as it reflects better economic conditions, access to resources, and improved living standards. Economic prosperity allows individuals to meet their basic needs and spend on education, and health, contributing to overall well-being.")
st.subheader("Social support:")
st.write("Social bonds provide emotional support and reduce loneliness. A *higher level of social support* is strongly correlated with *higher happiness scores*. People with strong social connections feel more secure and have less chances of stress and mental health issues.")
st.subheader("Healthy life expectancy:")
st.write("*Health is a base of happiness*. Good health enables individuals to work, socialize, and enjoy life without the burden of illness or disability.")
st.subheader("Freedom to make life choices:")
st.write("*Societies with fewer restrictions tend to have happier populations.* People with greater freedom to choose their paths often feel more satisfied and empowered.")
st.subheader("Generosity:")
st.write("Generosity reflects a sense of community and interconnectedness. *Act of giving is a source of happiness.*")
st.subheader("Perceptions of corruption:")
st.write("*Lower corruption perceptions are associated with higher happiness scores*, as corruption leads to trust issues in institutions and creates frustration. Societies perceived as fair and just promote higher levels of life satisfaction.")
st.subheader("Dystopia residual:")
st.write("This is a baseline measure included to account for other unmeasured factors affecting happiness, such as culture, environment, or governance. *Countries with higher residuals perform better on happiness* beyond the measurable factors.")    
