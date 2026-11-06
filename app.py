from flask import Flask, redirect, request

app = Flask(__name__)

from urllib.parse import urlparse, urlunparse

FROM_DOMAIN = 'motips.pythonanywhere.com'
TO_DOMAIN = 'mweinb.github.io/after-tax-tips'

@app.before_request
def redirect_to_new_domain():
    # Get the full URL of the incoming request
    full_url = request.url

    # Parse the URL into components
    parsed_url = urlparse(full_url)

    # Check if the request is coming from the old domain
    if parsed_url.netloc == FROM_DOMAIN:
        # Replace the old domain with the new domain
        new_netloc = TO_DOMAIN
        new_url = urlunparse(parsed_url._replace(netloc=new_netloc))

        # Redirect to the new URL
        return redirect(new_url, code=301)  # 301 Moved Permanently
