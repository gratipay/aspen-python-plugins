"""Implement a Jinja2 renderer.

Jinja2 insists on unicode, and explicit loader objects. We assume with Jinja2
that your templates on the filesystem be encoded in UTF-8 (the result of the
template will be encoded to bytes for the wire per response.charset). We shim a
loader that returns the decoded content page and instructs Jinja2 not to
perform auto-reloading.

"""
from __future__ import absolute_import
from aspen import renderers

from jinja2 import BaseLoader, Environment, FileSystemLoader

class SimplateLoader(BaseLoader):
    """Jinja2 really wants to get templates via a Loader object.

    See: http://jinja.pocoo.org/docs/api/#loaders

    """

    def __init__(self, filepath, raw):
        self.filepath = filepath
        self.decoded = raw.decode('UTF-8')

    def get_source(self, environment, template):
        return self.decoded, self.filepath, True


class Renderer(renderers.Renderer):
    """Render the Jinja2 simplate

    You can use "context" to inject global variables/functions
    
    """

    ctx = {}

    def compile(self, filepath, raw):
        environment = self.meta
        return SimplateLoader(filepath, raw).load(environment, filepath)

    def render_content(self, context):
        charset = context['response'].charset

        # Pull in our requested context values
        for key in self.ctx:
            context[key] = self.ctx[key]

        # We inject the locals into the context as globals right
        # before we render the simplate.
        context['globals'] = locals

        return self.compiled.render(context).encode(charset)


class Factory(renderers.Factory):

    Renderer = Renderer

    def compile_meta(self, configuration):
        loader = None
        if configuration.project_root is not None:
            # Instantiate a loader that will be used to resolve template bases.
            loader = FileSystemLoader(configuration.project_root)
        return Environment(loader=loader)
