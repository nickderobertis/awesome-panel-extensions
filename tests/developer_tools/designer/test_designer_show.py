"""In this module we use the Awesome Panel Designer as a show case for developing the ...
Awesome Panel Designer :-)"""
# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring

import pathlib

from awesome_panel_extensions.developer_tools.designer import (Designer,
                                                               ReloadService,
                                                               components)
from awesome_panel_extensions.developer_tools.designer.components.component_with_error import \
    ComponentWithError
from awesome_panel_extensions.developer_tools.designer.views import ErrorView

FIXTURES = pathlib.Path(__file__).parent / "fixtures"
COMPONENT_CSS = FIXTURES / "component.css"
COMPONENT_JS = FIXTURES / "component.js"
COMPONENT2_JS = FIXTURES / "component2.js"

TITLE_COMPONENT = ReloadService(
    component=components.TitleComponent, css_path=COMPONENT_CSS, js_path=COMPONENT_JS,
)
EMPTY_COMPONENT = ReloadService(
    component=components.EmptyComponent, css_path=COMPONENT_CSS, js_path=COMPONENT2_JS,
)
CENTERED_COMPONENT = ReloadService(
    component=components.CenteredComponent,
    css_path=COMPONENT_CSS,
    js_path=COMPONENT_JS,
    component_parameters={"component": components.TitleComponent()},
)
STOPPED_COMPONENT = ReloadService(
    component=components.StoppedComponent, css_path=COMPONENT_CSS, js_path=COMPONENT_JS,
)
COMPONENT_WITH_ERROR = ReloadService(component=ComponentWithError)
# pylint: disable=line-too-long
ERROR_MESSAGE = 'Traceback (most recent call last):\n  File "c:\\repos\\private\\awesome-panel\\package\\awesome_panel\\designer\\services\\reload_service.py", line 100, in _reload_component\n    self.component_instance = self.component()\n  File "c:\\repos\\private\\awesome-panel\\package\\awesome_panel\\designer\\components\\component_with_error.py", line 3, in __init__\n    raise NotImplementedError()\nNotImplementedError\n'
# pylint: enable=line-too-long
ERROR_VIEW = ReloadService(
    component=ErrorView,
    css_path=COMPONENT_CSS,
    js_path=COMPONENT_JS,
    component_parameters={"error_message": ERROR_MESSAGE},
)


RELOAD_SERVICES = [
    TITLE_COMPONENT,
    EMPTY_COMPONENT,
    CENTERED_COMPONENT,
    STOPPED_COMPONENT,
    COMPONENT_WITH_ERROR,
    ERROR_VIEW,
]


def test_designer(port=5007, show=False):
    """Run this with `python`, `panel serve --dev` or the integrated python runner or debugger in
    your editor or IDE.

    Args:
        show (bool, optional): [description]. Defaults to False. Change to True if you want to
        use with Pytest.
    """
    designer = Designer(reload_services=RELOAD_SERVICES)
    if show:
        designer._show(port=port)


if __name__.startswith("__main__") or __name__.startswith("bokeh"):
    test_designer(show=True)