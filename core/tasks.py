from celery import shared_task
from celery.utils.log import get_task_logger
import requests

logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("The sample task just ran.")
    res = requests.post(
        url="https://automation.shopino.app/api/v1/extract-product-info/",)
    data = res.json()