import pandas as pd

"""
    Write a solution to display the first 3 rows of this DataFrame.
"""


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    #Easy

    return employees.iloc[[0, 1, 2]]