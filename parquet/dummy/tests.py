from django.test import TestCase

from dummy.models import Dummy
import random
import pandas as pd

dummy_list = []
for i in range(10000):
    random_bool = random.choice([True, False])
    dummy_list.append(Dummy(title=f'title{i}', content=f'content{i}', is_delete=random_bool))
    pass
Dummy.objects.bulk_create(dummy_list)

from django.db import connection

query = str(Dummy.objects.filter(is_delete=True).query)

cursor = connection.cursor()

cursor.execute(query)
records = cursor.fetchall()
df = pd.DataFrame(records, columns=["id", "title", "content", "is_delete"])
df.to_parquet("dummy.deleted.gzip", compression="gzip")


