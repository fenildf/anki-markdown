#!/usr/bin/python3
# Anki-Markdown

__author__ = "Vivek Rai"
__date__ = "28th November, 2014"
__license__ = "AGPL3"

import markdown
from anki.hooks import addHook
from anki.utils import stripHTML
from aqt.utils import showInfo


def strip_html(html):
    return str(stripHTML(html))

# See how latex.py uses similar function for converting latex html
# tags to appropriate images.
# [1]: https://github.com/dae/anki/blob/master/anki/latex.py#L38
def render_markdown(html, type, fields, model, data, col):
    """ Hook main mungeQA event and render edit area HTML content.

    @args
    html: HTML data
    type: question(q) or answer(a)
    fields: contains Tags, Type, Deck, Subdeck etc., information
    model: Model name
    data: [cid, nid, mid, did, ord, tags, flds]
    col: collection

    Returns the modified/rendered HTML.
    """
    before = "Before md: " + html
    after = "After md: " + markdown.markdown(strip_html(html))
    showInfo(before)
    showInfo(after)
    return html
    # should grab source text

# Hook our function to mungeQA filter which contains the generated HTML for
# the front and back of cards. We can use this to convert text in html tags
# to approprite markdown.
# See http://ankisrs.net/docs/addons.html#hooks,
#     https://github.com/dae/anki/blob/master/anki/collection.py#L525
addHook('mungeQA', render_markdown)
