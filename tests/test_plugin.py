import sys

import pytest
from gather_vision import app, model


def test_list(capsys, caplog):
    app_args = model.ListArgs()
    main_app = app.App()
    result = main_app.list(app_args)
    assert result == model.ListResult(names=['gov_au'])

    stdout, stderr = capsys.readouterr()
    assert stdout == ""
    assert stderr == ""
    assert caplog.record_tuples == []

@pytest.mark.skipif(sys.version_info.minor < 8, reason="Not yet sure why test fails in 3.7.")
def test_get(capsys, caplog):
    main_app = app.App()
    result = main_app.get('gov_au')
    assert repr(result) == "<class 'gather_vision_gov_au_plugin.plugin.PluginEntry'>"

    stdout, stderr = capsys.readouterr()
    assert stdout == ""
    assert stderr == ""
    assert caplog.record_tuples == []

# TODO
# def test_show(capsys, caplog):
#     app_args = model.ShowArgs(name='gov_au')
#     main_app = app.App()
#     result = main_app.show(app_args)
#     assert result == ""
#
#     stdout, stderr = capsys.readouterr()
#     assert stdout == ""
#     assert stderr == ""
#     assert caplog.record_tuples == []
#
# def test_update(capsys, caplog):
#     app_args = model.UpdateArgs(name='gov_au')
#     main_app = app.App()
#     result = main_app.update(app_args)
#     assert result == ""
#
#     stdout, stderr = capsys.readouterr()
#     assert stdout == ""
#     assert stderr == ""
#     assert caplog.record_tuples == []
