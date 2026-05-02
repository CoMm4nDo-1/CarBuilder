from .base import BaseProvider

class ManualSeedProvider(BaseProvider):
    source_name='manual_seed'
    def fetch_products(self): return []
    def normalize(self, raw_product): return raw_product
