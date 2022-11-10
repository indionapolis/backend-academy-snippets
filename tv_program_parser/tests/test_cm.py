from tvprogramlib import ContentManager, TvMazeClient

expected = """Name: Family Guy
Network Name: FOX
Network Country Name: United States
Summary: <p><b>Family Guy</b> follows Peter Griffin the endearingly ignorant dad, and his hilariously offbeat family of middle-class New Englanders in Quahog, RI. Lois is Peter's wife, a stay-at-home mom with no patience for her family's antics. Then there are their kids: 18-year-old Meg is an outcast at school and the Griffin family punching bag; 13-year-old Chris is a socially awkward teen who doesn't have a clue about the opposite sex; and one-year-old Stewie is a diabolically clever baby whose burgeoning sexuality is very much a work in progress. Rounding out the Griffin household is Brian the family dog and a ladies' man who is one step away from AA.</p>"""


def test_output(capfd):
    manager = ContentManager(
        search_query="Family Guy", client=TvMazeClient()
    )
    manager.get_content()
    result = manager.format_content()

    assert expected == result
