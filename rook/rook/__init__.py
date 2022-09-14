import logging
from pathlib import Path
from typing import NoReturn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every

import rook.api

logging.config.fileConfig(Path(__file__).parent / 'logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

Server = FastAPI()
Server.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

Server.include_router(rook.api.router)

@Server.on_event('startup')
@repeat_every(seconds=60 * 60)
def fetch_plugins() -> NoReturn:
    logger.debug('Fetching plugins')
    ...
