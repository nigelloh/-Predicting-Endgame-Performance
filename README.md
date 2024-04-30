Aim
This project aims to explore the relationship between endgame outcomes in the popular game "League of Legends" and early to mid-game decisions. By analyzing various factors such as champion selection and minions killed, the goal is to provide insights beneficial to players, especially newcomers, in enhancing their game sense and performance.

Datasets
The investigation utilizes three datasets ('EUmatch.csv', 'KRmatch.csv', and 'NAmatch.csv'), comprising data from "challenger" rank matches in January 2022 across different regions. Each dataset contains details of randomly selected players to ensure independence and diversity. The features include various gameplay statistics like assists, kills, gold earned, and minions killed.

Preprocessing and Wrangling
The datasets were merged to increase sample size and combined insight into high-level gameplay. Empty rows and irrelevant columns were removed to clean the data. Feature selection techniques such as mutual information and chi-square tests were employed to filter noise and select attributes relevant to the research question.

Analysis Methods
Linear regression and decision trees were chosen as supervised learning models to predict end-of-game statistics and classify minions killed based on early-game decisions. Feature filtering and model fitting techniques were utilized to enhance model performance and interpretability.

Preliminary Analysis
The preliminary analysis focused on identifying trends in champion popularity and gold earned among top-ranked players. Visualizations such as histograms and bar charts were used to illustrate these trends and provide insights into player behavior and strategies.

Modelling
Linear regression models were fitted to predict gold earned, while decision trees were employed to classify minions killed. Evaluation metrics such as R-squared, Root Mean Squared Error (RMSE), and Mean Absolute Percent Error (MAPE) were utilized to assess model performance.

Discussion
The discussion section analyzed the results of the linear regression and decision tree models, highlighting the significance of features in predicting endgame outcomes. The impact of variables like damage dealt on gold earned was examined, and the suitability of the models for the dataset was discussed.

Evaluation
Limitations of the research, including data biases, outdated information, and potential model inaccuracies, were addressed. Suggestions for future improvements, such as dealing with outliers and refining role definitions, were provided to enhance the robustness of the analyses.






