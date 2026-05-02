from fastapi import APIRouter
from ..config import settings
router=APIRouter(prefix='/payments',tags=['payments'])

@router.post('/create-checkout-session')
def checkout(): return {'status':'placeholder','message':'Configure Stripe keys','price_id':settings.stripe_premium_price_id}
@router.post('/create-premium-session')
def premium(): return {'status':'placeholder','product':'premium_subscription'}
@router.post('/create-sponsored-placement-session')
def sponsored(): return {'status':'placeholder','product':'sponsored_part'}
@router.post('/webhook')
def webhook(): return {'received':True,'note':'Verify signature with STRIPE_WEBHOOK_SECRET in production'}
