"""
Use this plugin to activate coverage report.

To install this plugin, you need to activate ``coverage-plugin``
with extra requirements :

::

    $ pip install nose2[coverage-plugin]


Next, you can enable coverage reporting with :

::

    $ nose2 --with-coverage

Or with this lines in ``unittest.cfg`` :

::

    [coverage]
    always-on = True


"""

# pylint: disable= invalid-name
# Because these are the names you gave it
# pylint: disable= no-member
# Because this is how you set it up
# pylint: disable= bare-except
# Because these are set up in a way that works and i don't want to break it
# pylint: disable= attribute-defined-outside-init
# Because i don't want to break the code

from nose2.events import Plugin


class Coverage(Plugin):
    """This sets up the coverage method"""
    configSection = 'coverage'
    commandLineSwitch = ('C', 'with-coverage', 'Turn on coverage reporting')

    def __init__(self):
        """Get our config and add our command line arguments."""
        self.conSource = self.config.as_list('coverage', [])
        self.conReport = self.config.as_list('coverage-report', [])
        self.conConfig = self.config.as_str('coverage-config', '').strip()
        self.covSource = self.config.as_str('coverage-source', '').strip()

        group = self.session.pluginargs
        group.add_argument(
            '--coverage', action='append', default=[], metavar='PATH',
            dest='coverage_source',
            help='Measure coverage for filesystem path (multi-allowed)'
        )
        group.add_argument(
            '--coverage-report', action='append', default=[], metavar='TYPE',
            choices=['term', 'term-missing', 'annotate', 'html', 'xml'],
            dest='coverage_report',
            help='Generate selected reports, available types:'
                 ' term, term-missing, annotate, html, xml (multi-allowed)'
        )
        group.add_argument(
            '--coverage-config', action='store', default='', metavar='FILE',
            dest='coverage_config',
            help='Config file for coverage, default: .coveragerc'
        )

    def handleArgs(self, event):
        """Get our options in order command line, config file, hard coded."""

        self.covSource = (event.args.coverage_source or
                          self.conSource or ['.'])
        self.covReport = (event.args.coverage_report or
                          self.conReport or ['term'])
        self.covConfig = (event.args.coverage_config or
                          self.conConfig or '.coveragerc')

        self.covController = None
        try:
            import cov_core
        except:
            print('Warning: you need to install [coverage-plugin] '
                  'extra requirements to use this plugin')
            return

        self.covController = cov_core.Central(self.covSource,
                                              self.covReport,
                                              self.covConfig)
        self.covController.start()


    def afterSummaryReport(self, event):
        """Only called if active so stop coverage and produce reports."""

        if self.covController:
            self.covController.finish()
            self.covController.summary(event.stream)
