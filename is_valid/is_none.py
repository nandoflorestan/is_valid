from .base import Predicate, instantiate
from .explanation import Explanation


@instantiate
class is_none(Predicate):
    """
    A predicate that checks if the data is None.
    """

    def __init__(self):
        self._valid_exp = Explanation(True, 'none', 'Data is None.')
        self._not_valid_exp = Explanation(
            False, 'not_none', 'Data is not None.'
        )

    def _evaluate(self, data, explain):
        return (
            (self._valid_exp if explain else True)
            if data is None else
            (self._not_valid_exp if explain else False)
        )
