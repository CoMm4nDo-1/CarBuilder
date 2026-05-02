from .base import BaseProvider

class EbayMotorsProvider(BaseProvider):
    source_name='ebay_motors'
    def fetch_products(self): return []
    def normalize(self, raw_product): return raw_product
