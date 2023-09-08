#! /usr/bin/env python
import pandas as pd
from mailmerge import MailMerge
import frontmatter
from datetime import date

data = frontmatter.load('review.md')

data["review"] = data.content
data["Date"] = today = str(date.today())

template_1 = "review_template.docx"

document_1 = MailMerge(template_1)
# assert document_1.get_merge_fields() == data.keys()

for key in data.keys():
    data[key] = str(data[key])

document_1.merge(**data)
document_1.write(f'{str(date.today())}-{data["thesis_id"]}-{data["candidate"].replace(" ", "_")}_Gutachten.docx')
