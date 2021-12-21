from celery import shared_task


@shared_task
def serializer_test(base_date):
    print(type(base_date))
    return str(type(base_date))
