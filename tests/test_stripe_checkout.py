import pytest
from stripe_checkout import StripeCheckout

@pytest.fixture
def stripe_checkout():
    stripe_public_key = "YOUR_STRIPE_PUBLIC_KEY"
    stripe_secret_key = "YOUR_STRIPE_SECRET_KEY"
    return StripeCheckout(stripe_public_key, stripe_secret_key)

def test_create_checkout_session(stripe_checkout):
    price_id = "YOUR_PRICE_ID"
    session_id = stripe_checkout.create_checkout_session(price_id)
    assert session_id is not None
    assert session_id.startswith("cs_test_")

def test_get_session(stripe_checkout):
    session_id = "YOUR_SESSION_ID"
    session = stripe_checkout.get_session(session_id)
    assert session is not None
    assert session["id"] == session_id
