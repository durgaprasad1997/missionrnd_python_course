import os
import summer_pre_assign_package1
import summer_pre_assign_package1.summer_pre_assign_package3
import summer_pre_assign_package1.summer_pre_assign_package2

from summer_pre_assign_package1 import module1
from summer_pre_assign_package1 import module3

import logging
import logging.config

config = {

    'version': 1,

    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s : [%(levelname)s] -> %(name)s: %(message)s'
        },

    },

    'handlers': {

        'main':
            {
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.FileHandler',
                'filename': 'summer_pre_assign4_main_log.log',
                'mode': 'w'

            },
        'summer_pre_assign_package1':
            {
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.FileHandler',
                'filename': 'p1.log',
                'mode': 'w'
            },
        'summer_pre_assign_package1.summer_pre_assign_package2': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'p2.log',
            'mode': 'w'

        },
        'console':
            {
                'level': 'WARNING',
                'formatter': 'standard',
                'class': 'logging.StreamHandler'
            },

    },
    "loggers": {
        "summer_pre_assign4.summer_pre_assign_package1": {
            "level": "DEBUG",
            "handlers": ["console", "summer_pre_assign_package1"],
            "propagate": False
        },

        "summer_pre_assign4.summer_pre_assign_package1.summer_pre_assign_package2": {
            "level": "DEBUG",
            "handlers": ["console", "summer_pre_assign_package1.summer_pre_assign_package2"],
            "propagate": False
        }
    },

    "root": {
        "level": "DEBUG",
        "handlers": ["console", "main"],
        'propagate': False
    }
}
if __name__ == '__main__':
    logger = logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)
    logger.error("This is a log from main at ERROR level")
    logger.warning("This is a log from main at ERROR level")
    logger.info("Entering Main")

    module1.f1()
    module1.f2()
    summer_pre_assign_package1.summer_pre_assign_package2.module2.f3()
    summer_pre_assign_package1.summer_pre_assign_package2.module2.f4()
    module3.f5()
    summer_pre_assign_package1.summer_pre_assign_package3.module4.f6()

    logger.error("Exiting Main")

