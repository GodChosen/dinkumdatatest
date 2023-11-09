from typing import Optional
from flask import Flask

appl = Flask(__name__)

fla = """
      _____
     `.___,'
      (___)
      <   >
       ) (
      /`-.\\
     /     \\
    / _    _\\
   :,' `-.' `:
   |         |
   :         ;
    \       /
     `.___.'
"""


@appl.route('/')
def hello():
    return f'<html><h1>Welcome to Dinkum Data!</h1><pre>{fla}</pre><p>This is a flask for you.</html>', 200


def sumit(*args: Optional[int]):
    product = 0
    for item in args:
        if item:
            product += item
    return product


def noneize(in_par, *args) -> None:
    return None
