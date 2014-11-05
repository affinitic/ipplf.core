# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger('ipplf.core')


def installCore(context):
    if context.readDataFile('ipplf.core-default.txt') is None:
        return

    logger.info('Installing ipplf.core')
