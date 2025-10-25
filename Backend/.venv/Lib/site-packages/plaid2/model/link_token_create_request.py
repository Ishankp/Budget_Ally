from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .link_token_account_filters import LinkTokenAccountFilters
from .link_token_create_request_auth import LinkTokenCreateRequestAuth
from .link_token_create_request_identity_verification import LinkTokenCreateRequestIdentityVerification
from .link_token_create_request_income_verification import LinkTokenCreateRequestIncomeVerification
from .link_token_create_request_payment_initiation import LinkTokenCreateRequestPaymentInitiation
from .link_token_create_request_transfer import LinkTokenCreateRequestTransfer
from .link_token_create_request_user import LinkTokenCreateRequestUser


class LinkTokenCreateRequest(BaseModel):
    income_verification: Optional[LinkTokenCreateRequestIncomeVerification] = None
    """Specifies options for initializing Link for use with the Income (beta) product. This field is required if `income_verification` is included in the `products` array."""

    client_name: str
    """The name of your application, as it should be displayed in Link. Maximum length of 30 characters. If a value longer than 30 characters is provided, Link will display "This Application" instead."""

    institution_data: Optional[str] = None
    """A map containing data used to highlight institutions in Link."""

    auth: Optional[LinkTokenCreateRequestAuth] = None
    """Specifies options for initializing Link for use with the Auth product. This field can be used to enable or disable extended Auth flows for the resulting Link session. Omitting any field will result in a default that can be configured by your account manager."""

    transfer: Optional[LinkTokenCreateRequestTransfer] = None
    """Specifies options for initializing Link for use with the Transfer product."""

    additional_consented_products: Optional[List[str]] = None
    """(Beta) This field has no effect unless you are participating in the Product Scope Transparency beta program.
    List of additional Plaid product(s) you wish to collect consent for. These products will not be billed until you start using them by calling the relevant endpoints.
    
    `balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically have consent collected.
    
    Institutions that do not support these products will still be shown in Link"""

    products: Optional[List[str]] = None
    """List of Plaid product(s) you wish to use. If launching Link in update mode, should be omitted; required otherwise.
    
    `balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically be initialized when any other product is initialized.
    
    The products specified here will determine which institutions will be available to your users in Link. Only institutions that support *all* requested products can be selected; a if a user attempts to select an institution that does not support a listed product, a "Connectivity not supported" error message will appear in Link. To maximize the number of institutions available, initialize Link with the minimal product set required for your use case. Additional products can be added after Link initialization by calling the relevant endpoints. For details and exceptions, see [Choosing when to initialize products](https://plaid.com/docs/link/best-practices/#choosing-when-to-initialize-products).
    
    Note that, unless you have opted to disable Instant Match support, institutions that support Instant Match will also be shown in Link if `auth` is specified as a product, even though these institutions do not contain `auth` in their product array.
    
    In Production, you will be billed for each product that you specify when initializing Link. Note that a product cannot be removed from an Item once the Item has been initialized with that product. To stop billing on an Item for subscription-based products, such as Liabilities, Investments, and Transactions, remove the Item via `/item/remove`."""

    identity_verification: Optional[LinkTokenCreateRequestIdentityVerification] = None
    """Specifies option for initializing Link for use with the Identity Verification product."""

    account_filters: Optional[LinkTokenAccountFilters] = None
    """By default, Link will provide limited account filtering: it will only display Institutions that are compatible with all products supplied in the `products` parameter of `/link/token/create`, and, if `auth` is specified in the `products` array, will also filter out accounts other than `checking` and `savings` accounts on the Account Select pane. You can further limit the accounts shown in Link by using `account_filters` to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering applies to both the Account Select view (if enabled) and the Institution Select view. Institutions that do not support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the value `"all"`. If the `account_filters` filter is used, any account type for which a filter is not specified will be entirely omitted from Link. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema).
    
    For institutions using OAuth, the filter will not affect the list of accounts shown by the bank in the OAuth window.
    """

    webhook: Optional[str] = None
    """The destination URL to which any webhooks should be sent."""

    eu_config: Optional[bool] = None
    """Configuration parameters for EU flows"""

    update: Optional[bool] = None
    """Specifies options for initializing Link for [update mode](https://plaid.com/docs/link/update-mode)."""

    country_codes: List[str]
    """Specify an array of Plaid-supported country codes using the ISO-3166-1 alpha-2 country code standard. Institutions from all listed countries will be shown.  Supported country codes are: `US`, `CA`, `DE`, `ES`, `FR`, `GB`, `IE`, `IT`, `NL`. For a complete mapping of supported products by country, see https://plaid.com/global/.
    
    If Link is launched with multiple country codes, only products that you are enabled for in all countries will be used by Link. Note that while all countries are enabled by default in Sandbox and Development, in Production only US and Canada are enabled by default. To gain access to European institutions in the Production environment, [file a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access) via the Plaid dashboard. If you initialize with a European country code, your users will see the European consent panel during the Link flow.
    
    If using a Link customization, make sure the country codes in the customization match those specified in `country_codes`. If both `country_codes` and a Link customization are used, the value in `country_codes` may override the value in the customization.
    
    If using the Auth features Instant Match, Same-day Micro-deposits, or Automated Micro-deposits, `country_codes` must be set to `['US']`."""

    android_package_name: Optional[str] = None
    """The name of your app's Android package. Required if using the `link_token` to initialize Link on Android. When creating a `link_token` for initializing Link on other platforms, this field must be left blank. Any package name specified here must also be added to the Allowed Android package names setting on the [developer dashboard](https://dashboard.plaid.com/team/api). """

    language: str
    """The language that Link should be displayed in.
    
    Supported languages are:
    - English (`'en'`)
    - French (`'fr'`)
    - Spanish (`'es'`)
    - Dutch (`'nl'`)
    - German(`'de'`)
    
    When using a Link customization, the language configured here must match the setting in the customization, or the customization will not be applied."""

    user_token: Optional[str] = None
    """A user token generated using `/user/create`. Any item created during the link session will be associated with the user."""

    link_customization_name: Optional[str] = None
    """The name of the Link customization from the Plaid Dashboard to be applied to Link. If not specified, the `default` customization will be used. When using a Link customization, the language in the customization must match the language selected via the `language` parameter, and the countries in the customization should match the country codes selected via `country_codes`."""

    institution_id: Optional[str] = None
    """Used for certain Europe-only configurations, as well as certain legacy use cases in other regions."""

    user: LinkTokenCreateRequestUser
    """An object specifying information about the end user who will be linking their account."""

    redirect_uri: Optional[str] = None
    """A URI indicating the destination where a user should be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. The `redirect_uri` should not contain any query parameters. When used in Production or Development, must be an https URI. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. If `android_package_name` is specified, this field should be left blank.  Note that any redirect URI must also be added to the Allowed redirect URIs list in the [developer dashboard](https://dashboard.plaid.com/team/api)."""

    access_token: Optional[str] = None
    """The `access_token` associated with the Item to update, used when updating or modifying an existing `access_token`. Used when launching Link in update mode, when completing the Same-day (manual) Micro-deposit flow, or (optionally) when initializing Link as part of the Payment Initiation (UK and Europe) flow."""

    payment_initiation: Optional[LinkTokenCreateRequestPaymentInitiation] = None
    """Specifies options for initializing Link for use with the Payment Initiation (Europe) product. This field is required if `payment_initiation` is included in the `products` array."""

    deposit_switch: Optional[str] = None
    """Specifies options for initializing Link for use with the Deposit Switch (beta) product. This field is required if `deposit_switch` is included in the `products` array."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LinkTokenCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "LinkTokenCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
