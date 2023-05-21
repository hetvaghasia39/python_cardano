from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class StatusChoices(models.TextChoices):
    pending = "P", _("Pending")
    in_ledger = "L", _("In Ledger")


class Wallet(models.Model):
    """
    User's wallet details
    """

    user_fk = models.ForeignKey("User", on_delete=models.CASCADE)
    wallet_name = models.CharField(
        max_length=200, verbose_name=_("Wallet name"), blank=True, null=True
    )
    wallet_id = models.CharField(max_length=200, blank=True, null=True)
    mnemonic = models.TextField(blank=True, verbose_name=_("Mnemonic code"), null=True)
    balance = models.FloatField(default=0, verbose_name=_("Wallet balance"))
    asset_no = models.IntegerField(default=0, verbose_name=_("Number of assets"))


class Address(models.Model):
    """
    Payment addressess of wallet
    """

    wallet_fk = models.ForeignKey("Wallet", on_delete=models.CASCADE)
    address = models.CharField(max_length=200)


class AssetKeys(models.Model):
    """
    all common keys
    """

    vkey = models.CharField(max_length=200, verbose_name=_("Verification key"))
    skey = models.CharField(max_length=200, verbose_name=_("Signing key"))
    payment_addr = models.CharField(max_length=200, verbose_name=_("Payment address"))
    policy_vkey = models.CharField(
        max_length=200, verbose_name=_("Policy verification key")
    )
    policy_skey = models.CharField(max_length=200, verbose_name=_("Policy signing key"))
    policy_id = models.CharField(max_length=200, verbose_name=_("PolicyId"))


class Asset(models.Model):
    """
    asset details for wallet
    """

    address_fk = models.ForeignKey(
        "Address", verbose_name=_("Owner address"), on_delete=models.CASCADE
    )
    asset_owner = models.ForeignKey(
        "User", verbose_name=_("Owner user"), on_delete=models.CASCADE
    )
    asset_name = models.CharField(max_length=200, verbose_name=_("Asset name"))
    hex_name = models.CharField(max_length=200, verbose_name=_("Hexadecimal name"))
    asset_desc = models.CharField(max_length=200, verbose_name=_("Asset description"))
    media_type = models.CharField(max_length=200, verbose_name=_("Asset media type"))
    ipfs_link = models.CharField(max_length=200, verbose_name=_("Asset link"))


class Transaction(models.Model):
    """
    all transactions of wallet
    """

    wallet_fk = models.ForeignKey("Wallet", on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=200, verbose_name=_("TansactionId"))
    payment_addr = models.CharField(max_length=200, verbose_name=_("Payment address"))
    amount = models.FloatField(verbose_name=_("Amount"))
    asset_fk = models.ForeignKey(
        "Asset", on_delete=models.CASCADE, blank=True, null=True
    )
    withdrawal = models.TextField()
    status = models.CharField(max_length=1, choices=StatusChoices())
