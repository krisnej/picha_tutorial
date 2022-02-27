# import sys
# # append the path of the parent directory
# sys.path.append("..")
# import celery
# from celery.decorators import periodic_task
from picha.celery import task

from celery.utils.log import get_task_logger

from photos.utils import save_latest_flickr_image

logger = get_task_logger(__name__)


@task
def task_save_latest_flickr_image():
    """
    Saves latest image from Flickr
    """
    save_latest_flickr_image()
    logger.info("Saved image from Flickr")
