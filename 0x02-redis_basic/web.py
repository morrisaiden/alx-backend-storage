#!/usr/bin/env python3
"""Module for implementing an expiring web cache and tracker
"""
import requests
import redis
from functools import wraps

CACHE_EXPIRATION_TIME = 10  # seconds

# Initialize Redis connection
r = redis.Redis()


def cache(fn):
    """Decorator that caches the output of the function."""
    @wraps(fn)
    def wrapped(*args, **kwargs):
        url = args[0]
        cache_key = f"cache:{url}"
        count_key = f"count:{url}"
        cached_content = r.get(cache_key)
        if cached_content:
            # Increment the access count
            r.incr(count_key)
            return cached_content.decode('utf-8')


        content = fn(*args, **kwargs)
        r.setex(cache_key, CACHE_EXPIRATION_TIME, content)
        r.set(count_key, 1)
        return content
    return wrapped


@cache
def get_page(url: str) -> str:
    """Fetches the content of the given URL and caches it.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the page.
    """
    response = requests.get(url)
    return response.content.decode('utf-8')


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(r.get(f"count:{url}").decode('utf-8'))
    print(get_page(url))
    print(r.get(f"count:{url}").decode('utf-8'))
