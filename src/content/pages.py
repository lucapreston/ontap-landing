"""Every guide, tool and listicle, with the day it goes live.

A page is only built (and listed in the sitemap and hubs) once its publish
date has arrived, so the 14-day rollout happens on its own: the daily GitHub
Action (.github/workflows/publish.yml) rebuilds the site each morning.
"""
from dataclasses import dataclass, field


@dataclass
class Page:
    slug: str            # URL path, no slashes: getontap.net/<slug>/
    kind: str            # tool / best / alt / city / page
    title: str           # <title> and listings (keyword first)
    description: str     # meta description, ~150 chars
    lede: str            # first paragraph (HTML allowed)
    body: str            # HTML
    publish: str         # YYYY-MM-DD
    keyword: str         # the search it's written for
    h1: str = ""
    faq: list = field(default_factory=list)   # [(question, answer HTML)]
    related: list = field(default_factory=list)
    cta: str = ""
    updated: str = ""
    lang: str = "en"


def all_pages():
    from . import tools, cities, best, alternatives, marketing
    pages = tools.PAGES + cities.PAGES + best.PAGES + alternatives.PAGES + marketing.PAGES
    slugs = [p.slug for p in pages]
    assert len(slugs) == len(set(slugs)), "duplicate slug"
    return pages
