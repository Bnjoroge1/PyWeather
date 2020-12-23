from argparse import Action
from ..core import Unit


class CustomUnitAction(Action):
     def __call__(self, parser, namespace, values,
     option_string=None):
          unit = Unit[values.upper()]
          setattr(namespace, self.dest, unit)
          