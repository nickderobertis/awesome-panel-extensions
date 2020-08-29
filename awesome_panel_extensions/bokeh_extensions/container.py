from bokeh.models import Box
from bokeh.core.properties import (
    List,
    String,
    Seq,
)


class Container(Box):
    child_css_classes = List(
        String,
        help="""
    A list of CSS class names to add to the immediate children of the DOM element. 
    
    Note: the class names are
    simply added as-is, no other guarantees are provided.

    It is also permissible to assign from tuples, however these are adapted -- the
    property will always contain a list.
    """,
    ).accepts(Seq(String), lambda x: list(x))
