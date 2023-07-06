from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
import pandas as pd

grades = pd.read_csv("grades.csv", dtype="string")

template_1 = "Schein_template.docx"

print('Erstelle Scheine:')

for data in grades.to_dict("index").values():

    document_1 = MailMerge(template_1)
    assert document_1.get_merge_fields() == data.keys()

    print(f"- {data['Name']}".ljust(20) + f": {data['Name']}.docx")
    document_1.merge(**data)
    document_1.write(f'{data["Name"]}.docx')

