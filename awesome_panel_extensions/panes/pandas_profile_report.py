"""# PandasProfileReport

The PandasProfileReport pane enables a user to show a ProfileReport generated by the
[Pandas profile_report](https://github.com/pandas-profiling/pandas-profiling) package.
"""
import html

import panel as pn
import param
from pandas_profiling import ProfileReport

# pylint: disable=line-too-long
EMPTY_HTML_REPORT = "<p>No report specified</p>"
HTML_LOADING_REPORT = "<p>Loading Report ...</p>"
GREEN = "#174c4f"
ORANGE = "#cc5c29"
LOGO_URL = "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/application/pages/pandas_profiling_app/pandas_profiler_logo.png"
# pylint: enable=line-too-long

STYLE = """
<style>
iframe {
    width:100%;
    height:800px;
}
</style>
"""


class PandasProfileReport(pn.pane.HTML):
    """The PandasProfilingApp showcases how to integrate the Pandas Profiling Report with Panel"""

    profile_report = param.ClassSelector(class_=ProfileReport)

    def __init__(self, **params):
        self._rename["profile_report"]=None
        super().__init__(**params)

        self._update_object()

    @param.depends("profile_report", watch=True)
    def _update_object(self):
        if not self.profile_report:
            self.object = EMPTY_HTML_REPORT
            return

        self.object = HTML_LOADING_REPORT
        self.object = self._to_html(self.profile_report)

    def _to_html(self, profile_report: ProfileReport) -> str:
        html_report = profile_report.to_html()
        html_report = html.escape(html_report)
        return (
            f"""<iframe srcdoc="{html_report}" frameborder="0" allowfullscreen></iframe>"""
        )

    def __str__(self):
        return "Pandas Profile Report"

    def __repr__(self):
        return self.__str__()


def test_app():
    pn.config.sizing_mode = "stretch_width"
    pandas_profile_report = PandasProfileReport()
    return pandas_profile_report


if __name__.startswith("bokeh"):
    test_app().servable()
if __name__ == "__main__":
    test_app().show(port=5007)