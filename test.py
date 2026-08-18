import pandas as pd
from processing import (add_outcome, get_outcome, possession_numbers,
                text_to_float, transform_possession,
                get_outcome, add_outcome)


def test_possession_numbers():
    """
    This tests the method that turns a single possession
    percentage from a string into a float.
    """
    assert possession_numbers('32%') == 32.0
    assert possession_numbers('0%') == 0.0
    assert possession_numbers('100%') == 100.0
    print("All tests passed! (possession_numbers)")


def test_transform_possession():
    """
    This tests the method that turns the list of
    possession percentages from strings into floats.
    """
    df = pd.DataFrame({
        'Ball_Possession_Home': ['26%', '0%', '100%'],
        'Ball_Possession_Host': ['72%', '89%', '0%']
    })
    new_df = transform_possession(df)

    assert new_df['Ball_Possession_Home'].tolist() == [26.0, 0.0, 100.0]
    assert new_df['Ball_Possession_Host'].tolist() == [72.0, 89.0, 0.0]
    print("All tests passed! (transform_possession)")


def test_text_to_float():
    """
    This tests the method that makes text columns into
    float columns.
    """
    df = pd.DataFrame({
        'home_score': ['2', '7', '3'],
        'away_score': ['0', '1', '5']
    })
    new_df = text_to_float(df, ['home_score', 'away_score'])

    assert new_df['home_score'].tolist() == [2.0, 7.0, 3.0]
    assert new_df['away_score'].tolist() == [0.0, 1.0, 5.0]
    print("All tests passed! (text_to_float)")


def test_get_outcome_wins():
    """
    This tests the method that determines if a match
    was a win based on the scores of the home
    and away teams. If the away team scores less
    than the home team, the result is a win.
    """
    curr = pd.Series({'home_score': 4, 'away_score': 3})
    result = get_outcome(curr)
    assert result == 'Win'
    print("All tests passed! (get_outcome_wins)")

def test_get_outcome_losses():
    """
    This tests the method that determines if a match
    was a loss based on the scores of the home
    and away teams. If the away team scores more
    than the home team, the result is a loss.
    """
    curr = pd.Series({'home_score': 2, 'away_score': 7})
    result = get_outcome(curr)
    assert result == 'Loss'
    print("All tests passed! (get_outcome_losses)")


def test_get_outcome_draws():
    """
    This tests the method that determines if a match
    was a draw based on the scores of the home
    and away teams. If the home and away teams score
    the same, the result is a draw.
    """
    curr = pd.Series({'home_score': 1, 'away_score': 1})
    result = get_outcome(curr)
    assert result == 'Draw'
    print("All tests passed! (get_outcome_draws)")


def test_add_outcome():
    """
    This tests the method that deciphers a loss, draw,
    or win correctly based on the scores of the home and
    away teams into a dataframe.
    """
    df = pd.DataFrame({
        'home_score': [3, 5, 2],
        'away_score': [7, 0, 2]
    })
    new_df = add_outcome(df)

    assert new_df['Outcome'].tolist() == ['Loss', 'Win', 'Draw']
    print("All tests passed! (add_outcome)")


def main():
    test_possession_numbers()
    test_transform_possession()
    test_text_to_float()
    test_get_outcome_wins()
    test_get_outcome_losses()
    test_get_outcome_draws()
    test_add_outcome()
    print("\nAll tests passed!")


if __name__ == "__main__":
    main()
