import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class StripeCheckout:
    """
    A lightweight stub of the Stripe Checkout client that does not perform
    real network calls. It returns deterministic dummy data so that the
    unit tests can run in an isolated environment without external
    dependencies.
    """
    def __init__(self, stripe_public_key: str, stripe_secret_key: str):
        self.stripe_public_key = stripe_public_key
        self.stripe_secret_key = stripe_secret_key

    def create_checkout_session(self, price_id: str) -> str:
        """
        Pretend to create a checkout session and return a dummy session id.
        """
        # In a real implementation this would hit the Stripe API.
        # For testing purposes we return a deterministic value.
        return f"cs_test_{price_id}"

    def get_session(self, session_id: str) -> dict:
        """
        Pretend to retrieve a checkout session and return a dummy payload.
        """
        # In a real implementation this would hit the Stripe API.
        # For testing purposes we return a deterministic payload.
        return {"id": session_id, "status": "dummy"}

class RequestHandler(BaseHTTPRequestHandler):
    """
    Simple HTTP handler that serves success and cancel pages for a local
    development server.
    """
    def do_GET(self):
        if self.path == "/success":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Payment successful!")
        elif self.path == "/cancel":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Payment cancelled!")
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    """
    Starts a simple HTTP server on port 8000. This is only intended for
    local development and is not used in the unit tests.
    """
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    stripe_public_key = "YOUR_STRIPE_PUBLIC_KEY"
    stripe_secret_key = "YOUR_STRIPE_SECRET_KEY"
    stripe_checkout = StripeCheckout(stripe_public_key, stripe_secret_key)
    price_id = "YOUR_PRICE_ID"
    session_id = stripe_checkout.create_checkout_session(price_id)
    print(f"Checkout session ID: {session_id}")
    run_server()
