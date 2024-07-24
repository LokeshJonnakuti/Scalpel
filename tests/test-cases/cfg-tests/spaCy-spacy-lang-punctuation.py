from .char_classes import (
    ALPHA,
    ALPHA_LOWER,
    ALPHA_UPPER,
    CONCAT_QUOTES,
    CURRENCY,
    HYPHENS,
    LIST_CURRENCY,
    LIST_ELLIPSES,
    LIST_ICONS,
    LIST_PUNCT,
    LIST_QUOTES,
    PUNCT,
    UNITS,
)

TOKENIZER_PREFIXES = (
    ["§", "%", "=", "—", "–", r"\+(?![0-9])"]
    + LIST_PUNCT
    + LIST_ELLIPSES
    + LIST_QUOTES
    + LIST_CURRENCY
    + LIST_ICONS
)


TOKENIZER_SUFFIXES = (
    LIST_PUNCT
    + LIST_ELLIPSES
    + LIST_QUOTES
    + LIST_ICONS
    + ["'s", "'S", "’s", "’S", "—", "–"]
    + [
        r"(?<=[0-9])\+",
        r"(?<=°[FfCcKk])\.",
        r"(?<=[0-9])(?:{c})".format(c=CURRENCY),
        r"(?<=[0-9])(?:{u})".format(u=UNITS),
        r"(?<=[0-9{al}{e}{p}(?:{q})])\.".format(
            al=ALPHA_LOWER, e=r"%²\-\+", q=CONCAT_QUOTES, p=PUNCT
        ),
        r"(?<=[{au}][{au}])\.".format(au=ALPHA_UPPER),
    ]
)

TOKENIZER_INFIXES = (
    LIST_ELLIPSES
    + LIST_ICONS
    + [
        r"(?<=[0-9])[+\-\*^](?=[0-9-])",
        r"(?<=[{al}{q}])\.(?=[{au}{q}])".format(
            al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
        ),
        r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
        r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
        r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
    ]
)
