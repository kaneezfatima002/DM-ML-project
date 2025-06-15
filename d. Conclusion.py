import streamlit as st

st.title("Conclusion")
st.write("""The analysis of the World Happiness Report provided a comprehensive understanding of the factors driving happiness at a global scale.
The dataset included key features such as GDP per Capita, Social Support, Healthy Life Expectancy, Freedom to Make Life Choices, Generosity, and Perceptions of Corruption, with the Happiness Score serving as the target variable.
Data preparation involved dropping non-numeric columns to ensure compatibility with machine learning models.
Exploratory Data Analysis revealed that GDP per Capita, Social Support, and Healthy Life Expectancy were strongly positively correlated with the Happiness Score, while Perceptions of Corruption exhibited a negative correlation.
Visualizations such as scatter plot and histogram helped illustrate these relationships clearly.

We implemented two machine learning models: Linear Regression and K-Means Clustering. Linear Regression was used to predict the Happiness 
Score based on independent variables, with metrics such as Mean Squared Error (MSE) and R-squared used for evaluation. The model performed well, with
features like GDP per Capita, Social Support, and Healthy Life Expectancy having the most significant contributions to happiness. K-Means Clustering grouped
countries into clusters based on their happiness indicators, providing insights into global patterns. For example, countries within
the same cluster often shared similar levels of economic prosperity, social cohesion, and health.""")
st.header("Strong predictors:")
st.subheader("*GDP per capita, Social Support*, and *Healthy Life Expectancy* often have the strongest influence on happiness scores.")
st.header("Weak predictors:")
st.subheader("*Generosity* and *Freedom to Make Life Choices* are important but usually less impactful.")
st.header("Negative predictors:")
st.subheader("*Perception of Corruption* reduces happiness.")
st.header("Policy insights:")
st.write("""
1. **Economic Development:** Policies aimed at sustainable economic growth and reducing inequality can significantly boost happiness.
2. **Health and Well-being:** Investment in healthcare, mental health programs, and public health campaigns is essential.
3. **Social Policies:** Strengthening social safety nets and community programs can enhance social support.
4. **Transparency and Justice:** Reducing corruption and ensuring fairness in governance can lead to a happier society.

This project has practical applications for policymakers, who can use these insights to prioritize areas like economic growth, healthcare,
and anti-corruption measures to improve societal well-being. Clustering results can help countries benchmark themselves against peers and 
adopt best practices. Despite its success, the analysis is limited by the static nature of the dataset and the assumption of linear relationships. 
Future work could involve analyzing temporal trends, incorporating additional factors such as education and environment, and applying more
advanced machine learning models for deeper insights. Overall, this analysis demonstrates the power of data-driven approaches to 
understanding and improving global happiness.""")



