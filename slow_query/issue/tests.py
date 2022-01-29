import random

from django.test import TestCase

# Create your tests here.

from django.db import connection
from django.test.utils import CaptureQueriesContext

from account.models import Account
from issue.models import Issue
from work.models import Work
accounts = []
for i in range(1,201):
    accounts.append(Account(name=f'유저{i}'))
Account.objects.bulk_create(accounts)
available_issue_type_list = [2, 3, 4]
ids = Issue.objects.filter(model_type__in=available_issue_type_list, is_complete=False).exclude(works__model_type=4).order_by('id').values_list('id', flat=True)[:200]
issues = Issue.objects.filter(id__in=ids)

for issue, account in zip(issues, accounts):
    issue.account = account
    issue.save()


model_types = list(range(100))
is_completes = [True, False]
issues = []
for _ in range(10000):
    issues.append(Issue(model_type=random.sample(model_types, 1)[0], is_complete=random.sample(is_completes, 1)[0]))
Issue.objects.bulk_create(issues)

for i in issues:
    works = []
    works_model_types = list(range(10))
    five_types = set()
    while len(five_types) <= 5:
        five_types.add(random.sample(works_model_types, 1)[0])
    for tp in five_types:
        works.append(Work(issue=i, is_complete=random.sample(is_completes, 1)[0], model_type=tp))
    Work.objects.bulk_create(works)

# slow query
with CaptureQueriesContext(connection) as cqc:
    available_issue_type_list = [2, 3, 4]
    Issue.objects.filter(model_type__in=available_issue_type_list, is_complete=False).exclude(works__model_type=4).order_by('id').first()
    print(cqc.captured_queries)

cursor = connection.cursor()

query = '''EXPLAIN (ANALYZE, COSTS, VERBOSE, BUFFERS, FORMAT JSON) 
SELECT "issue_issue"."id", "issue_issue"."model_type", "issue_issue"."is_complete" FROM "issue_issue" WHERE (NOT "issue_issue"."is_complete" AND "issue_issue"."model_type" IN (2, 3, 4) AND NOT (EXISTS(SELECT (1) AS "a" FROM "work_work" U1 WHERE (U1."model_type" = 4 AND U1."issue_id" = ("issue_issue"."id")) LIMIT 1))) ORDER BY "issue_issue"."id" ASC LIMIT 1'''

cursor.execute(query)
res = cursor.fetchone()
res[0]

from django.db import connection
from django.test.utils import CaptureQueriesContext
with CaptureQueriesContext(connection) as cqc:
    available_issue_type_list = [2, 3, 4]
    exclude_issue_ids = Work.objects.filter(model_type=4).values_list('issue', flat=True)
    Issue.objects.filter(model_type__in=available_issue_type_list, is_complete=False).exclude(id__in=exclude_issue_ids).order_by('id').first()
    result = cqc.captured_queries


query = '''EXPLAIN (ANALYZE, COSTS, VERBOSE, BUFFERS, FORMAT JSON) 
SELECT "issue_issue"."id", "issue_issue"."model_type", "issue_issue"."is_complete" FROM "issue_issue" WHERE (NOT "issue_issue"."is_complete" AND "issue_issue"."model_type" IN (2, 3, 4) AND NOT ("issue_issue"."id" IN (SELECT U0."issue_id" FROM "work_work" U0 WHERE U0."model_type" = 4))) ORDER BY "issue_issue"."id" ASC LIMIT 1'''

cursor.execute(query)
res = cursor.fetchone()
res[0]


with CaptureQueriesContext(connection) as cqc:
    available_issue_type_list = [2, 3, 4]
    Issue.objects.filter(
        model_type__in=available_issue_type_list,
        account=accounts[0],
        is_complete=False
    ).exclude(works__model_type=4).order_by('id').first()
    print(cqc.captured_queries)


query = '''EXPLAIN (ANALYZE, COSTS, VERBOSE, BUFFERS, FORMAT JSON) SELECT "issue_issue"."id", "issue_issue"."model_type", "issue_issue"."is_complete", "issue_issue"."account_id" FROM "issue_issue" WHERE ("issue_issue"."account_id" = 1 AND NOT "issue_issue"."is_complete" AND "issue_issue"."model_type" IN (2, 3, 4) AND NOT (EXISTS(SELECT (1) AS "a" FROM "work_work" U1 WHERE (U1."model_type" = 4 AND U1."issue_id" = ("issue_issue"."id")) LIMIT 1))) ORDER BY "issue_issue"."id" ASC LIMIT 1'''
account = Account.objects.get(id=72)

with CaptureQueriesContext(connection) as cqc:
    available_issue_type_list = [2, 3, 4]
    exclude_issue_ids = Work.objects.filter(
        model_type=4, account=account
    ).values_list('issue', flat=True)

    Issue.objects.filter(model_type__in=available_issue_type_list,
                         is_complete=False,
                         account=account
                         ).exclude(id__in=exclude_issue_ids).order_by('id').first()
    result = cqc.captured_queries


query = '''EXPLAIN (ANALYZE, COSTS, VERBOSE, BUFFERS, FORMAT JSON) SELECT "issue_issue"."id", "issue_issue"."model_type", "issue_issue"."is_complete", "issue_issue"."account_id" FROM "issue_issue" WHERE ("issue_issue"."account_id" = 1 AND NOT "issue_issue"."is_complete" AND "issue_issue"."model_type" IN (2, 3, 4) AND NOT ("issue_issue"."id" IN (SELECT U0."issue_id" FROM "work_work" U0 WHERE (U0."account_id" = 1 AND U0."model_type" = 4)))) ORDER BY "issue_issue"."id" ASC LIMIT 1'''


query  = '''EXPLAIN (ANALYZE, COSTS, VERBOSE, BUFFERS, FORMAT JSON) SELECT "issue_issue"."id", "issue_issue"."model_type", "issue_issue"."is_complete", "issue_issue"."account_id" FROM "issue_issue" WHERE ("issue_issue"."account_id" = 72 AND NOT "issue_issue"."is_complete" AND "issue_issue"."model_type" IN (2, 3, 4) AND NOT ("issue_issue"."id" IN (SELECT U0."issue_id" FROM "work_work" U0 WHERE (U0."account_id" = 72 AND U0."model_type" = 4)))) ORDER BY "issue_issue"."id" ASC LIMIT 1'''