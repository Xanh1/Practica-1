import enum

class ProductStatus(enum.Enum):
    FRESH = 'Fresh'
    NEAR_EXPIRY = 'Near_Expiry'
    EXPIRED = 'Expired'
