Possession by the Home Team in soccer: Overhyped or misunderstood?

Author: Yassin Yassin

This project will look at the possession percentages of the home team in football matches in the Premier League (English League). It looks at seasons 2018/19 up until 2021/22. The project statistically analyzed relationships that are connected with the possession of the home team.

Installations:
Install plotly, pandas, and scipy. Do this by typing pip install (insert) in your terminal, with the libraries going in the insert section. Exclude the paranthesis when installing.

Files:
data_processing.py is the file that has the untouched dataset. It filters the data to Premier league matches only from seasons 2018/19-2021/22. Transforms the columns required from strings to floats as well as adding a match outcome column that says whether each match was a win, loss, or draw.
analysis.py is the file that uses the filtered dataset to run an analysis. It creates different visualizations and performs 3 statistical tests. One ANOVA test and 2 pearson correlations, and this is the file that we use to gather our results for our research questions.
test.py is the file we use to test our implementation. We mainly focus on testing methods in the processing.py file since that file sets up our whole experiment. We use small pieces of data to test this.

Dataset:
https://www.kaggle.com/datasets/gokhanergul/football-match-statistics
Our dataset is from kaggle, and all you need to do to use it is download it and put it in a folder that you name "data" and name the dataset Football.csv. Make sure the data folder is inside the project directory. You should have data/Football.csv. As an example, say your project folder is called cse 163. Inside cse 163. you want to  have the analysis, processing, and test files. You also want to have the data folder, and inside the data folder you want the Football.csv file.

Running the project:
Install all libraries listed, set up the dataset given above, and type in python analysis.py into the terminal. This will open tabs with all the visualizations and give you the results of the statistical tests in the terminal. If you want to run the tests, type in python test.py into the terminal. To see the variable summary, type in python processing.py into the terminal and there will be a 7 number summary for the variables used in the experiment.

