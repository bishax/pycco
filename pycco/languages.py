"""
A list of the languages that Pycco supports, mapping the file extension to
the name of the Pygments lexer and the symbol that indicates a comment. To
add another language to Pycco's repertoire, add it here.
"""

__all__ = ("supported_languages",)

DOUBLE_HASH = "##"
TRIPLE_QUOTE = '"""#'

def lang(name, comment_symbol, multistart=None, multiend=None):
    """
    Generate a language entry dictionary, given a name and comment symbol and
    optional start/end strings for multiline comments.
    """
    result = {
        "name": name,
        "comment_symbol": comment_symbol
    }
    if multistart is not None and multiend is not None:
        result.update(multistart=multistart, multiend=multiend)
    return result


supported_languages = {
    ".py": lang("python", DOUBLE_HASH, TRIPLE_QUOTE, TRIPLE_QUOTE),
    ".pyx": lang("cython", DOUBLE_HASH, TRIPLE_QUOTE, TRIPLE_QUOTE),
}
