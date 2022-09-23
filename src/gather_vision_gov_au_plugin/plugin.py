from gather_vision import model
from gather_vision.plugin import Entry


class PluginEntry(Entry):
    """The entry class for the plugin."""

    def update(self, args: model.UpdateArgs) -> model.UpdateResult:
        pass

    def show(self, args: model.ShowArgs) -> model.ShowResult:
        pass

