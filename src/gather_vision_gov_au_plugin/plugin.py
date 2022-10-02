import logging

from gather_vision import model
from gather_vision.plugin import Entry

from .air import QueenslandAir
from .election import AustraliaElection
from .electricity import QueenslandEnergexElectricity
from .electricity import QueenslandErgonEnergyElectricity
from .petition import AustralianGovernmentPetitions
from .petition import BrisbaneCityCouncilPetitions
from .petition import QueenslandGovernmentPetitions
from .transport import QueenslandFuel

logger = logging.getLogger(__name__)


class PluginEntry(Entry):
    """The entry class for the plugin."""

    name = "gov_au"

    _data_sources = [
        # air
        QueenslandAir,
        # election
        AustraliaElection,
        # electricity
        QueenslandEnergexElectricity,
        QueenslandErgonEnergyElectricity,
        # government
        # petition
        AustralianGovernmentPetitions,
        QueenslandGovernmentPetitions,
        BrisbaneCityCouncilPetitions,
        # transport
        QueenslandFuel,
        # water
    ]

    def update(self, args: model.UpdateArgs) -> model.UpdateResult:
        logger.info(f"Update {self.name}")
        return model.UpdateResult()

    def list(self, args: model.ListArgs) -> model.ListResult:
        logger.info(f"List {self.name}")
        data_source_names = sorted(
            [
                f"{'.'.join(i.__module__.split('.')[1:])}.{i.__name__}"
                for i in self._data_sources
            ]
        )
        return model.ListResult({self.name: data_source_names})
