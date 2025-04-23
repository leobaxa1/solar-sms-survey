import pandas as pd
from storage import get_all_responses

def export_to_excel():
    data = get_all_responses()
    rows = []
    for phone, answers in data.items():
        row = {'Phone': phone}
        row.update(answers)
        rows.append(row)

    df = pd.DataFrame(rows)
    filepath = "survey_results.xlsx"
    df.to_excel(filepath, index=False)
    return filepath