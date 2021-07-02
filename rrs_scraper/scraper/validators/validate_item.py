import logging

logger = logging.getLogger(__name__)


def validate_item(item: dict):
    """Validate Item data and return dict of data.

    Args:
        item (dict): Feed Item dict

    Returns:
        dict: masked item dict
    """
    try:
        required_item_keys = ['title', 'author',
                              'summary', 'link', 'published']
        if not item.keys() in required_item_keys:
            logger.warning('Invalid item keys')
            return False, 'Invalid item keys'

        cleaned_data = {
            'title': item['title'],
            'author': item['author'],
            'summary': item['summary'],
            'link': item['link'],
            'rights': item['rights'],
            'publication_date': item['published']
        }
        return True, cleaned_data
    except Exception:
        logger.exception('Invalid item data')
        return False, 'Invalid item data'
