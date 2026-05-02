from fastapi import APIRouter
router=APIRouter(prefix='/users',tags=['users'])
@router.get('')
def users_placeholder(): return {'message':'User account routes placeholder'}
