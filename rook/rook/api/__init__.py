import logging

from fastapi import APIRouter


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix='/api',
)

##
# /api/presets
##

@router.get('/presets/popular')
async def presets_popular():
    # TODO: db, pagination
    # Below is a basic response from the go backend
    return {"page":1,"perPage":30,"totalItems":0,"totalPages":0,"items":[]}


@router.get('/presets/trending')
async def presets_trending():
    # TODO: db, pagination
    # Below is a basic response from the go backend
    return {"page":1,"perPage":30,"totalItems":0,"totalPages":0,"items":[]}


@router.get('/presets/search')
async def presets_search(q: str = ''):
    # TODO: db, pagination
    # Below is a basic response from the go backend
    logger.debug(f'Preset search with query string "{q}"')
    return {"page":1,"perPage":30,"totalItems":0,"totalPages":0,"items":[]}


##
# /api/collections/
##

# presets
@router.get('/collections/presets/records')
async def collection_preset_records(page: int = 1, perPage: int = 30, sort: str = '-created'):
    logger.debug(f'/collections/presets/records search with params {page=}, {perPage=}, {sort=}')
    return {"page":page,"perPage":perPage,"totalPages":0,"items":[]}

# plugins
@router.get('/collections/plugins/records')
async def collection_plugins_records(page: int = 1, perPage: int = 100):
    return {"page":page,"perPage":perPage,"items":[]}


# users
@router.get('/collections/user_settings/records')
async def collection_user_settings_records(page: int = 1, perPage: int = 30):
    return {"page":page,"perPage":perPage,"items":[]}


##
# /api/users/auth-methods
##

@router.get('/users/auth-methods')
async def auth_methods():
    return {"emailPassword":True,"authProviders":[]}
