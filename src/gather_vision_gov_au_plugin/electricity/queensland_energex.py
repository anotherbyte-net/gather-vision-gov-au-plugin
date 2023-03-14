import dataclasses
import typing

from gather_vision.plugin import data


@dataclasses.dataclass
class QueenslandEnergexElectricityItem:
    pass


class QueenslandEnergexElectricity(data.WebData):
    demand_min = 0
    demand_max = 5500

    base_url = "https://www.energex.com.au"
    demand_url = f"{base_url}/static/Energex/Network%20Demand/networkdemand.txt"

    def initial_urls(self) -> typing.Iterable[str]:
        return [self.list_url]

    def parse_response(
        self, data: data.WebDataAvailable
    ) -> typing.Generator[typing.Union[str, data.IsDataclass], typing.Any, typing.Any]:
        pass
