from .base import BaseProvider

class VendorAPIProvider(BaseProvider):
    source_name='vendor_api'
    def fetch_products(self): return []
    def normalize(self, raw_product): return raw_product
