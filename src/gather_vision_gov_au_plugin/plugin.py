import logging

from gather_vision.plugin import entry, data

from gather_vision_gov_au_plugin.air import queensland as air_qld
from gather_vision_gov_au_plugin.election import australia as aust_election
from gather_vision_gov_au_plugin.electricity import queensland_energex as qld_energex
from gather_vision_gov_au_plugin.electricity import (
    queensland_ergon_energy as qld_ergon_energy,
)
from gather_vision_gov_au_plugin.petition import australia as aust_petition
from gather_vision_gov_au_plugin.petition import queensland as qld_petition
from gather_vision_gov_au_plugin.petition import queensland_brisbane as qld_bne_petition
from gather_vision_gov_au_plugin.transport import queensland_fuel as qld_fuel

logger = logging.getLogger(__name__)


class PluginEntry(entry.Entry):
    """The entry class for the plugin."""

    name = "gov_au"

    _data_sources = [
        # air
        air_qld.QueenslandAir,
        # election
        aust_election.AustraliaElection,
        # electricity
        qld_energex.QueenslandEnergexElectricity,
        qld_ergon_energy.QueenslandErgonEnergyElectricity,
        # government
        # petition
        aust_petition.AustralianGovernmentPetitions,
        qld_petition.QueenslandGovernmentPetitions,
        qld_bne_petition.BrisbaneCityCouncilPetitions,
        # transport
        qld_fuel.QueenslandFuel,
        # water
    ]

    def update(self, args: entry.UpdateArgs) -> entry.UpdateResult:
        logger.info(f"Update {self.name}")
        web_data = [
            i(plugin_name=args.name, plugin_data_source=args.data_source)
            for i in self._data_sources
            if issubclass(i, data.WebData)
        ]
        return entry.UpdateResult(web_data=web_data, local_data=list())

    def list(self, args: entry.ListArgs) -> entry.ListResult:
        logger.info(f"List {self.name}")
        data_source_names = sorted(
            [
                f"{'.'.join(i.__module__.split('.')[1:])}.{i.__name__}"
                for i in self._data_sources
            ]
        )
        return entry.ListResult({self.name: data_source_names})
