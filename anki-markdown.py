#!/usr/bin/python3
# Anki-Markdown

__author__ = "Vivek Rai"
__date__ = "28th November, 2014"
__license__ = "AGPL3"

import anki
from aqt import mw


def render_markdown(flag, note, fidx):
    """ Hooks to main editFocusLost event and renders edit area Markdown
    content (if present) to proper HTML.

     Accepts three arguments: a modified flag, the note, and the current field.
     If a filter makes no changes it returns the modified flag the same as it
     received it; if it makes a change it returns True.
    """
    # should grab source text
    srcTxt = mw.col.media.strip(n[src])
    if not srcTxt:
        return flag
    # should update field
    try:
        pass
    except Exception:
        raise
    return True

addHook('editFocusLost', render_markdown)
