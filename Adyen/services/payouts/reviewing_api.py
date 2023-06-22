from ..base import AdyenServiceBase


class ReviewingApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(ReviewingApi, self).__init__(client=client)
        self.service = "payouts"

    def confirm_third_party(self, request, idempotency_key=None, **kwargs):
        """
        Confirm a payout
        """
        endpoint = f"/confirmThirdParty"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def decline_third_party(self, request, idempotency_key=None, **kwargs):
        """
        Cancel a payout
        """
        endpoint = f"/declineThirdParty"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

