from .base import BaseProvider

class AffiliateFeedProvider(BaseProvider):
    source_name='affiliate_feed'
    def fetch_products(self): return []
    def normalize(self, raw_product): return raw_product
