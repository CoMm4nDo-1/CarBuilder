def resolved_purchase_url(product_url: str, affiliate_url: str | None):
    return affiliate_url or product_url
