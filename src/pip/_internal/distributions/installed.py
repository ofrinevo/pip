from pip._internal.distributions.base import AbstractDistribution


class InstalledDistribution(AbstractDistribution):
    """Represents an installed package.

    This does not need any preparation as the required information has already
    been computed.
    """

    def dist(self):
        return self.req.satisfied_by

    def prep_for_dist(self, finder, build_isolation):
        pass
