# Nutrition_Analysis_Data-Analytics 📊
A data analysis project using **Python, Pandas, Matplotlib, and Seaborn** to explore and visualize nutrition-related data and primary benefits.
Dashboard is created using Power BI.

## 📝 Project Overview
This project focuses on analyzing nutrition datasets to extract meaningful insights such as:
1. Which supplement
 is best.
2. Which gender have more benefits of nutrition in weight gain and strength gain.
3. Which age group people have more benefit of Nutrition.

## 🗃️ Power BI Dashboard

<img width="4150" height="2400" alt="dashboard_page-01" src="https://github.com/user-attachments/assets/f81ed21b-6879-4dec-b020-167cc2bf8872" />


## 🛠️ Requirements
- Python
- Pandas
- Matplotlib
- Seaborn
- Numpy

## 🚀 How to Run the Project
1. Clone the repository:
   
 ``` bash
 git clone https://github.com/samyaktiwari16/Nutrition_Analysis_Data-Analytics.git
 ```
2. Navigate to project folder:
   
``` bash
cd Nutrition_analysis
```
3. Install dependencies:

``` bash
pip install pandas matplotlib seaborn
              or
pip install -r requirements.txt
```
4. Run the script:

``` bash
python Nutrition_analysis.py
```


## 📊 Key Analysis Performed

### Scatter Plot Analysis

<img width="1697" height="880" alt="Screenshot 2026-06-21 121819" src="https://github.com/user-attachments/assets/97d94708-efad-44f7-8242-66e6d619c6ae" />

The scatter plot illustrates the relationship between age and strength gain across different genders (Male, Female, and Non-binary).

- No strong correlation is observed between age and strength gain.
- Individuals from all genders exhibit similar distribution patterns.
- Most strength gain values fall between 5% and 30%.
- The data suggests that age and gender do not significantly influence strength improvement.

This indicates that other factors (such as diet, workout type, or consistency) may play a more important role.

###  Total Gain Analysis by Gender

<img width="1782" height="893" alt="Screenshot 2026-06-21 171025" src="https://github.com/user-attachments/assets/82089fd6-39f2-4bdd-bde3-1ba8de044332" />

The line graph represents the total initial weight, final weight, and strength gain across different genders.

- All groups show an increase in final weight compared to initial weight, indicating overall progress.
- Males have the highest total weight values, suggesting higher overall body mass.
- Non-binary individuals exhibit the highest total strength gain.

### Supplement Analysis

<img width="1682" height="822" alt="Screenshot 2026-07-06 143718" src="https://github.com/user-attachments/assets/44e4f4d4-60fe-411c-b4d5-6b61530ce32d" />

#### Weight change graph for each gender 

<img width="1658" height="876" alt="Screenshot 2026-06-21 122256" src="https://github.com/user-attachments/assets/c2bd8aa0-c13f-40c1-a370-17d5d2fed84d" />

The bar chart compares the number of people using different supplements based on their primary fitness goals.

- Creatine Monohydrate is primarily used for strength gain.
- Mass Gainer is most popular for weight gain.
- Users consuming both supplements show a more balanced distribution across benefits.
- Muscle recovery has relatively lower preference across all supplement types.

## 🧠 Future Improvements
- Add machine learning models for prediction
- Improve dataset quality
- Build interactive dashboard (Streamlit/Power BI)

##  🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.
