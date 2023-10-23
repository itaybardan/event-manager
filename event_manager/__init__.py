import importlib.resources
import json
import logging
import os

from dotmap import DotMap

import event_manager.resources

CONFIG = DotMap(json.loads(importlib.resources.read_text(event_manager.resources.__name__, 'config.json')))
logging.basicConfig(level=CONFIG.log.level, format=CONFIG.log.format)


