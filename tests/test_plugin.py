from gather_vision import app, model

from gather_vision_gov_au_plugin.plugin import PluginEntry


def test_list(capsys, caplog):
    app_args = model.ListArgs()
    main_app = app.App()
    result = main_app.list(app_args)
    assert result == model.ListResult(
        items={
            PluginEntry.name: [
                "air.qld.QueenslandAir",
                "election.national.AustraliaElection",
                "electricity.qld_energex.QueenslandEnergexElectricity",
                "electricity.qld_ergon_energy.QueenslandErgonEnergyElectricity",
                "petition.national.AustralianGovernmentPetitions",
                "petition.qld.QueenslandGovernmentPetitions",
                "petition.qld_bne.BrisbaneCityCouncilPetitions",
                "transport.qld_fuel.QueenslandFuel",
            ]
        }
    )

    stdout, stderr = capsys.readouterr()
    assert stdout == ""
    assert stderr == ""
    assert caplog.record_tuples == [
        ("gather_vision_gov_au_plugin.plugin", 20, "List gov_au"),
    ]


# @pytest.mark.skipif(
#     sys.version_info.minor < 8, reason="Not yet sure why test fails in 3.7."
# )
def test_update(capsys, caplog):
    app_args = model.UpdateArgs(name=PluginEntry.name)
    main_app = app.App()
    result = main_app.update(app_args)
    assert result == model.UpdateResult()

    stdout, stderr = capsys.readouterr()
    assert stdout == ""
    assert stderr == ""
    assert caplog.record_tuples == [
        ("gather_vision_gov_au_plugin.plugin", 20, "Update gov_au"),
    ]
