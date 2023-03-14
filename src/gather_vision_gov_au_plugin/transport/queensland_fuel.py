import dataclasses
import typing

from gather_vision.plugin import data

# https://www.data.qld.gov.au/dataset/find-a-charging-station-electric-vehicle/resource/a34d4b5f-8e3c-4995-8950-2e84fd7bb4d5
# https://www.data.qld.gov.au/dataset/fuel-price-reporting


@dataclasses.dataclass
class QueenslandFuelItem:
    pass


class QueenslandFuel(data.WebData):
    def initial_urls(self) -> typing.Iterable[str]:
        return [self.list_url]

    def parse_response(
        self, data: data.WebDataAvailable
    ) -> typing.Generator[typing.Union[str, data.IsDataclass], typing.Any, typing.Any]:
        pass
