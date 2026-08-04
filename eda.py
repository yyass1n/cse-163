import pandas as pd
import plotly.express as px


def data_filter(df):
    """
    Filters the given dataframe to include only
    the Premier League match data from every season
    """
    epl_df = df[df['League'] == 'Premier-league']
    filtered_epl = epl_df[(epl_df['season_year'] >= '2018/2019') &
                          (epl_df['season_year'] <= '2021/2022')].copy()
    return filtered_epl


def possession_numbers(column):
    """
    Converts string representations of the possession percentages
    to floats.
    """
    curr = column[:-1]
    return float(curr)


def transform_possession(df):
    """
    Transforms the possession percentages from string to float in the
    given dataframe for the football dataset.
    """
    df['Ball_Possession_Home'] = df['Ball_Possession_Home'].apply(
        possession_numbers
    )
    df['Ball_Possession_Host'] = df['Ball_Possession_Host'].apply(
        possession_numbers
    )
    return df


def text_to_float(df, column):
    """
    Converts the specified columns in the football dataset from
    string to float.
    """
    for col in column:
        df[col] = df[col].apply(float)
    return df


def missing_data(df, cols_of_interest):
    """
    Prints the missing data from the football dataset for the given columns.
    """
    print('\nMissing Data:')
    print(df[cols_of_interest].isnull().sum())


def variable_summary(df, cols_of_interest):
   """
   Prints the 7 number summary for the columns of interest
   in the football dataset.
   """
   print('\nVariable Summary:')
   print(df[cols_of_interest].describe().T)


def get_outcome(row):
    """
    Determines the outcome of a match based on the
    scores of the home and away teams. Win means the home team won
    loss mean the away team won, and draw means the match ended in a tie.
    """
    if row['home_score'] > row['away_score']:
        return 'Win'
    elif row['home_score'] < row['away_score']:
        return 'Loss'
    else:
        return 'Draw'


def add_outcome(df):
    """
    Adds a new column 'Outcome' to the dataframe based on the match scores.
    Win, loss, or draw will be the values for the new column.
    """
    df['Outcome'] = df.apply(get_outcome, axis=1)
    return df


def possession_vs_outcome(df):
    """"
    Creates a box plot visualization for the possession percentages
    against match outcomes in the football dataset.
    """
    fig = px.box(
        df, x='Outcome', y='Ball_Possession_Home',
        title='Home Team Possession Percentage vs Match Outcome',
        labels={'Outcome': 'Match Outcome',
                'Ball_Possession_Home': 'Ball Possession Percentage'}
    )
    fig.show()


def possession_vs_goals(df):
    """
    Creates a box plot visualization for the possession percentages
    against the number of goals scored in the football dataset. Also
    creates a heatmap visualization for the same data in order to show
    the data cluster.
    """
    fig = px.box(
        df, x='home_score', y='Ball_Possession_Home',
        title='Home Team Possession Percentage by Goals Scored',
        labels={'Ball_Possession_Home': 'Ball Possession Percentage',
                'home_score': 'Goals Scored'}
    )
    fig.show()


    fig2 = px.density_heatmap(
        df, x='Ball_Possession_Home', y='home_score',
        title='Home Team Possession Percentage vs Goals Scored',
        labels={'Ball_Possession_Home': 'Ball Possession Percentage',
                'home_score': 'Goals Scored'}
    )
    fig2.show()


def main():
    df = pd.read_csv("data/Football.csv")
    print('full data shape:', df.shape)

    epl_df = data_filter(df)
    print('Premier league data from 2018/2019 to 2021/2022 shape:',
          epl_df.shape)

    epl_df = transform_possession(epl_df)

    cols_of_interest = ['Ball_Possession_Home', 'Ball_Possession_Host',
                        'home_score', 'away_score',
                        'Shots_on_Goal_Home', 'Shots_on_Goal_Host',
                        'Dangerous_Attacks_Host','Blocked_Shots_Home',
                        'Goalkeeper_Saves_Home', 'Goal_Attempts_Home',
                        'Goal_Attempts_Host']

    epl_df = text_to_float(epl_df, cols_of_interest)
    epl_df = add_outcome(epl_df)

    missing_data(epl_df, cols_of_interest)
    variable_summary(epl_df, cols_of_interest)

    possession_vs_outcome(epl_df)
    possession_vs_goals(epl_df)


if __name__ == "__main__":
    main()
