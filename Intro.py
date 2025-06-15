import streamlit as st

# Page Title
st.title("World Happiness Report")

st.image("G:\Downloads\Project_IDS\img.jpg")

st.header("Introduction")
st.write("""The analysis utilizes the 2019 World Happiness Report dataset, which 
assesses happiness levels across 156 countries, considering various socio-economic
and cultural influences. Each nation receives a rank and score for overall happiness,
as well as supplementary metrics like GDP per capita, social support, life expectancy,
freedom in making personal choices, generosity, and views on corruption. These elements
are employed to evaluate the well-being and quality of life for individuals in different areas.""")

# Objectives Section
st.header("Project Objectives")
st.write("""
The primary objectives of this project are to:

1. **Analyze Happiness Rankings**: Explore the rankings and scores of countries to identify the happiest and least happy nations globally.
2. **Examine Contributing Factors**: Investigate the relationship between happiness and key indicators such as GDP per capita, social support, and perceptions of corruption.
3. **Understand Regional Trends**: Compare happiness levels across regions to identify global patterns and disparities.
4. **Determine Key Drivers of Happiness**: Identify the factors that contribute most significantly to happiness and well-being.
5. **Provide Policy Insights**: Offer recommendations for governments and organizations to improve happiness and quality of life.
""")

