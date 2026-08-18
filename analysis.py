import pandas as pd
import plotly.express as px
from scipy import stats
from processing import preparing_data


def possession_vs_outcome(df):
    """"
    Creates a box plot and violin plot visualization for the possession percentages
    against match outcomes in the football dataset.
    """
    fig = px.box(
        df, x='Outcome', y='Ball_Possession_Home',
        title='Home Team Possession Percentage vs Match Outcome',
        labels={'Outcome': 'Match Outcome',
                'Ball_Possession_Home': 'Ball Possession Percentage'}
    )
    fig.show()

    fig2 = px.violin(
        df, x='Outcome', y='Ball_Possession_Home',
        title='Home Team Possession Percentage vs Match Outcome',
        labels={'Outcome': 'Match Outcome',
                'Ball_Possession_Home': 'Ball Possession Percentage'},
    )
    fig2.show()


def possession_vs_conceded_goals(df):
    '''
    Creates a scatter plot and heat mapvisualization for the possession percentages
    against the number of goals conceded in the football dataset. This
    shows us the relationship between goals conceded and
    possession percentage for the home team.
    '''
    fig = px.scatter(
        df, x='Ball_Possession_Home', y='away_score', trendline='ols',
        title='Home Team Possession Percentage vs Goals Conceded',
        labels={'Ball_Possession_Home': 'Home Team Possession Percentage',
                'away_score': 'Goals Conceded'}
    )
    fig.show()

    fig2 = px.density_heatmap(
        df, x='Ball_Possession_Home', y='away_score',
        title='Home Team Possession Percentage vs Goals Conceded',
        labels={'Ball_Possession_Home': 'Ball Possession Percentage',
                'away_score': 'Goals Conceded'}
    )
    fig2.show()


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


def anova_possession_outcome(df):
    """
    This method performs an ANOVA test to see if there are
    significant differences in possession percentages
    across different match outcomes.
    """
    win = df[df['Outcome'] == 'Win']['Ball_Possession_Home']
    loss = df[df['Outcome'] == 'Loss']['Ball_Possession_Home']
    draw = df[df['Outcome'] == 'Draw']['Ball_Possession_Home']

    result = stats.f_oneway(win, loss, draw)
    print('\nANOVA Test Results for possession by match outcome:')
    print('F-statistic:', result.statistic, 'p-value:', result.pvalue)


def correlation_possession_conceded_goals(df):
    """
    This function finds the correlation between possession
    and goals conceded in the given dataset.
    """
    r, p = stats.pearsonr(df['Ball_Possession_Home'], df['away_score'])
    print('\nCorrelation between possession and goals conceded:')
    print('r:', r, 'p-value:', p)


def correlation_possession_goals_scored(df):
    """
    This function finds the correlation between possession and
    goals scored in the dataset.
    """
    r, p = stats.pearsonr(df['Ball_Possession_Home'], df['home_score'])
    print('\nCorrelation between possession and goals scored:')
    print('r:', r, 'p-value:', p)

def main():
    epl_df = preparing_data("data/Football.csv")

    possession_vs_outcome(epl_df)
    anova_possession_outcome(epl_df)

    possession_vs_conceded_goals(epl_df)
    correlation_possession_conceded_goals(epl_df)

    possession_vs_goals(epl_df)
    correlation_possession_goals_scored(epl_df)


if __name__ == "__main__":
    main()