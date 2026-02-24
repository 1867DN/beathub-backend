"""
Centralized Enums Module

Contains all shared enumeration types used across models and schemas.
"""
from enum import Enum


class DeliveryMethod(Enum):
    """Order delivery method options"""
    DRIVE_THRU = 1
    ON_HAND = 2
    HOME_DELIVERY = 3


class Status(Enum):
    """Order status options"""
    PENDING = 1
    IN_PROGRESS = 2
    DELIVERED = 3
    CANCELED = 4
    APPROVED = 5
    RETURN_REQUESTED = 6


class PaymentType(Enum):
    """Bill payment type options"""
    CASH = 1
    CARD = 2
    DEBIT = 3
    CREDIT = 4
    BANK_TRANSFER = 5
    MERCADOPAGO = 6
    PAYPAL = 7


class Role(str, Enum):
    """User role options"""
    USER = "user"
    ADMIN = "admin"
