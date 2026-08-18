import pandas as pd

def data_filter(df):
    """
    Filters the given dataframe to include only
    the Premier League match data from every season
    """
    epl_df = df[df['League'] == 'Premier-league']
    filtered_epl = epl_df[(epl_df['season_year'] >= '2018/2019') &
                          (epl_df['season_year'] <= '2021/2022')].copy()
    return filtered_epl


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


def preparing_data(filename):
    df = pd.read_csv(filename)
    cols_of_interest = ['Ball_Possession_Home', 'Ball_Possession_Host',
                        'home_score', 'away_score']

    epl_df = data_filter(df)
    epl_df = transform_possession(epl_df)
    epl_df = text_to_float(epl_df, cols_of_interest)
    epl_df = add_outcome(epl_df)

    return epl_df

def main():
    epl_df = preparing_data("data/Football.csv")
    print('Premier league data from 2018/2019 to 2021/2022 shape:',
          epl_df.shape)

    cols_of_interest = ['Ball_Possession_Home', 'Ball_Possession_Host',
                        'home_score', 'away_score']
    missing_data(epl_df, cols_of_interest)
    variable_summary(epl_df, cols_of_interest)

if __name__ == "__main__":
    main()