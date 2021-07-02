import logging

logger = logging.getLogger(__name__)


def validate_feed(feed: dict):
    """Validate feed data and return dict of data.

    Args:
        feed (dict): Feed feed dict

    Returns:
        dict: masked feed dict
    """
    try:
        required_feed_keys = ['title', 'author',
                              'subtitle', 'link', 'rights', 'updated']
        if not feed.keys() in required_feed_keys:
            logger.warning('Invalid feed keys')
            return False, 'Invalid feed keys'

        cleaned_data = {
            'title': feed['title'],
            'author': feed['author'],
            'subtitle': feed['subtitle'],
            'link': feed['link'],
            'rights': feed['rights'],
            'last_update': feed['updated']
        }
        return True, cleaned_data
    except Exception:
        logger.exception('Invalid item data')
        return False, 'Invalid item data'
