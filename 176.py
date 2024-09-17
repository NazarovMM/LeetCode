import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.sort_values(
        by=['salary'], na_position='last', ascending=False)
    if len(employee['id']) > 1 and len(employee['salary'].unique()) > 1:
        return pd.DataFrame(data=[employee['salary'].unique()[1]], columns=['SecondHighestSalary'])
    else:
        return pd.DataFrame(data=[None], columns=['SecondHighestSalary'])