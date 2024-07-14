import logging

_log_level = logging.DEBUG 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d - %(name)s : %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger("EMA")
logger.setLevel(_log_level)

logging.getLogger('botocore.hooks').setLevel(logging.WARNING)
logging.getLogger('botocore.utils').setLevel(logging.WARNING)
logging.getLogger('botocore.credentials').setLevel(logging.WARNING)
logging.getLogger('botocore.loaders').setLevel(logging.WARNING)
logging.getLogger('botocore.endpoint').setLevel(logging.WARNING)
logging.getLogger('botocore.regions').setLevel(logging.WARNING)
logging.getLogger('botocore.retryhandler').setLevel(logging.WARNING)
logging.getLogger('botocore.parsers').setLevel(logging.WARNING)
logging.getLogger('botocore.httpsession').setLevel(logging.WARNING)
logging.getLogger('botocore.client').setLevel(logging.WARNING)
