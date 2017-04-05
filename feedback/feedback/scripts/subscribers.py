from pyramid.events import (
    subscriber,
    BeforeRender,
)

from ..helpers import frontend


@subscriber(BeforeRender)
def add_global(event):
    event['h'] = frontend
