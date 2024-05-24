# Configuration file for ipengine.

c = get_config()  #noqa

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
## This is an application.

## The date format used by logging formatters for %(asctime)s
#  Default: '%Y-%m-%d %H:%M:%S'
# c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  Default: '[%(name)s]%(highlevel)s %(message)s'
# c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  Choices: any of [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
#  Default: 30
# c.Application.log_level = 30

## Configure additional log handlers.
#  
#  The default stderr logs handler is configured by the log_level, log_datefmt
#  and log_format settings.
#  
#  This configuration can be used to configure additional handlers (e.g. to
#  output the log to a file) or for finer control over the default handlers.
#  
#  If provided this should be a logging configuration dictionary, for more
#  information see:
#  https://docs.python.org/3/library/logging.config.html#logging-config-
#  dictschema
#  
#  This dictionary is merged with the base logging configuration which defines
#  the following:
#  
#  * A logging formatter intended for interactive use called
#    ``console``.
#  * A logging handler that writes to stderr called
#    ``console`` which uses the formatter ``console``.
#  * A logger with the name of this application set to ``DEBUG``
#    level.
#  
#  This example adds a new handler that writes to a file:
#  
#  .. code-block:: python
#  
#     c.Application.logging_config = {
#         'handlers': {
#             'file': {
#                 'class': 'logging.FileHandler',
#                 'level': 'DEBUG',
#                 'filename': '<path/to/file>',
#             }
#         },
#         'loggers': {
#             '<application-name>': {
#                 'level': 'DEBUG',
#                 # NOTE: if you don't list the default "console"
#                 # handler here then it will be disabled
#                 'handlers': ['console', 'file'],
#             },
#         }
#     }
#  Default: {}
# c.Application.logging_config = {}

## Instead of starting the Application, dump configuration to stdout
#  Default: False
# c.Application.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  Default: False
# c.Application.show_config_json = False

#------------------------------------------------------------------------------
# BaseIPythonApplication(Application) configuration
#------------------------------------------------------------------------------
#  Default: False
# c.BaseIPythonApplication.add_ipython_dir_to_sys_path = False

## Whether to create profile dir if it doesn't exist
#  Default: False
# c.BaseIPythonApplication.auto_create = False

## Whether to install the default config files into the profile dir.
#          If a new profile is being created, and IPython contains config files for that
#          profile, then they will be staged into the new directory.  Otherwise,
#          default config files will be automatically generated.
#  Default: False
# c.BaseIPythonApplication.copy_config_files = False

## Path to an extra config file to load.
#  
#      If specified, load this config file in addition to any other IPython
#  config.
#  Default: ''
# c.BaseIPythonApplication.extra_config_file = ''

## The name of the IPython directory. This directory is used for logging
#  configuration (through profiles), history storage, etc. The default is usually
#  $HOME/.ipython. This option can also be specified through the environment
#  variable IPYTHONDIR.
#  Default: ''
# c.BaseIPythonApplication.ipython_dir = ''

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.BaseIPythonApplication.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.BaseIPythonApplication.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.BaseIPythonApplication.log_level = 30

## 
#  See also: Application.logging_config
# c.BaseIPythonApplication.logging_config = {}

## Whether to overwrite existing config files when copying
#  Default: False
# c.BaseIPythonApplication.overwrite = False

## The IPython profile to use.
#  Default: 'default'
# c.BaseIPythonApplication.profile = 'default'

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.BaseIPythonApplication.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.BaseIPythonApplication.show_config_json = False

## Create a massive crash report when IPython encounters what may be an
#          internal error.  The default is to append a short message to the
#          usual traceback
#  Default: False
# c.BaseIPythonApplication.verbose_crash = False

#------------------------------------------------------------------------------
# BaseParallelApplication(BaseIPythonApplication) configuration
#------------------------------------------------------------------------------
## The base Application for ipyparallel apps
#  
#      Primary extensions to BaseIPythonApplication:
#  
#      * work_dir
#      * remote logging via pyzmq
#      * IOLoop instance

#  See also: BaseIPythonApplication.add_ipython_dir_to_sys_path
# c.BaseParallelApplication.add_ipython_dir_to_sys_path = False

## Whether to create profile dir if it doesn't exist
#  See also: BaseIPythonApplication.auto_create
# c.BaseParallelApplication.auto_create = False

## whether to cleanup old logfiles before starting
#  Default: False
# c.BaseParallelApplication.clean_logs = False

## String id to add to runtime files, to prevent name collisions when
#          using multiple clusters with a single profile simultaneously.
#  
#          When set, files will be named like:
#  'ipcontroller-<cluster_id>-engine.json'
#  
#          Since this is text inserted into filenames, typical recommendations apply:
#          Simple character strings are ideal, and spaces are not recommended (but should
#          generally work).
#  Default: ''
# c.BaseParallelApplication.cluster_id = ''

## Whether to install the default config files into the profile dir.
#  See also: BaseIPythonApplication.copy_config_files
# c.BaseParallelApplication.copy_config_files = False

## Path to an extra config file to load.
#  See also: BaseIPythonApplication.extra_config_file
# c.BaseParallelApplication.extra_config_file = ''

## 
#  See also: BaseIPythonApplication.ipython_dir
# c.BaseParallelApplication.ipython_dir = ''

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.BaseParallelApplication.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.BaseParallelApplication.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.BaseParallelApplication.log_level = 30

## whether to log to a file
#  Default: False
# c.BaseParallelApplication.log_to_file = False

## The ZMQ URL of the iplogger to aggregate logging.
#  Default: ''
# c.BaseParallelApplication.log_url = ''

## 
#  See also: Application.logging_config
# c.BaseParallelApplication.logging_config = {}

## Whether to overwrite existing config files when copying
#  See also: BaseIPythonApplication.overwrite
# c.BaseParallelApplication.overwrite = False

## The IPython profile to use.
#  See also: BaseIPythonApplication.profile
# c.BaseParallelApplication.profile = 'default'

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.BaseParallelApplication.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.BaseParallelApplication.show_config_json = False

## Create a massive crash report when IPython encounters what may be an
#  See also: BaseIPythonApplication.verbose_crash
# c.BaseParallelApplication.verbose_crash = False

## Set the working dir for the process.
#  Default: '/home/ubuntu'
# c.BaseParallelApplication.work_dir = '/home/ubuntu'

#------------------------------------------------------------------------------
# IPEngine(BaseParallelApplication) configuration
#------------------------------------------------------------------------------
#  See also: BaseIPythonApplication.add_ipython_dir_to_sys_path
# c.IPEngine.add_ipython_dir_to_sys_path = False

## Whether to create profile dir if it doesn't exist
#  See also: BaseIPythonApplication.auto_create
# c.IPEngine.auto_create = False

## whether to cleanup old logfiles before starting
#  See also: BaseParallelApplication.clean_logs
# c.IPEngine.clean_logs = False

## String id to add to runtime files, to prevent name collisions when
#  See also: BaseParallelApplication.cluster_id
# c.IPEngine.cluster_id = ''

## Whether to install the default config files into the profile dir.
#  See also: BaseIPythonApplication.copy_config_files
# c.IPEngine.copy_config_files = False

## The engine's public key for CURVE security.
#          Usually autogenerated on launch.
#  Default: b''
# c.IPEngine.curve_publickey = b''

## The engine's secret key for CURVE security.
#          Usually autogenerated on launch.
#  Default: b''
# c.IPEngine.curve_secretkey = b''

## The controller's public key for CURVE security
#  Default: b''
# c.IPEngine.curve_serverkey = b''

## The class for handling displayhook.
#          Typically 'ipykernel.displayhook.ZMQDisplayHook'
#  Default: 'ipykernel.displayhook.ZMQDisplayHook'
# c.IPEngine.display_hook_factory = 'ipykernel.displayhook.ZMQDisplayHook'

## Enable the nanny process.
#  
#      The nanny process enables remote signaling of single engines
#      and more responsive notification of engine shutdown.
#  
#      .. versionadded:: 7.0
#  Default: True
# c.IPEngine.enable_nanny = True

## Path to an extra config file to load.
#  See also: BaseIPythonApplication.extra_config_file
# c.IPEngine.extra_config_file = ''

## Request this engine ID.
#  
#          If run in MPI, will use the MPI rank.
#          Otherwise, let the Hub decide what our rank should be.
#  Default: None
# c.IPEngine.id = None

## Code to execute in the user namespace when initializing MPI
#  Default: '\nfrom mpi4py import MPI\nmpi_rank = MPI.COMM_WORLD.Get_rank()\nmpi_size = MPI.COMM_WORLD.Get_size()\n'
# c.IPEngine.init_mpi = '\nfrom mpi4py import MPI\nmpi_rank = MPI.COMM_WORLD.Get_rank()\nmpi_size = MPI.COMM_WORLD.Get_size()\n'

## 
#  See also: BaseIPythonApplication.ipython_dir
# c.IPEngine.ipython_dir = ''

## The location (an IP address) of the controller.  This is
#          used for disambiguating URLs, to determine whether
#          loopback should be used to connect or the public address.
#  Default: ''
# c.IPEngine.location = ''

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.IPEngine.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.IPEngine.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.IPEngine.log_level = 30

## whether to log to a file
#  See also: BaseParallelApplication.log_to_file
# c.IPEngine.log_to_file = False

## The URL for the iploggerapp instance, for forwarding
#          logging to a central location.
#  Default: ''
# c.IPEngine.log_url = ''

## 
#  See also: Application.logging_config
# c.IPEngine.logging_config = {}

## The maximum number of times a check for the heartbeat ping of a
#          controller can be missed before shutting down the engine.
#  
#          If set to 0, the check is disabled.
#  Default: 50
# c.IPEngine.max_heartbeat_misses = 50

## Per-engine delay for mpiexec-launched engines
#  
#          avoids flooding the controller with registrations,
#          which can stall under heavy load.
#  
#          Default: .02 (50 engines/sec, or 3000 engines/minute)
#  Default: 0.02
# c.IPEngine.mpi_registration_delay = 0.02

## The OutStream for handling stdout/err.
#          Typically 'ipykernel.iostream.OutStream'
#  Default: 'ipykernel.iostream.OutStream'
# c.IPEngine.out_stream_factory = 'ipykernel.iostream.OutStream'

## Whether to overwrite existing config files when copying
#  See also: BaseIPythonApplication.overwrite
# c.IPEngine.overwrite = False

## Whether to use paramiko instead of openssh for tunnels.
#  Default: False
# c.IPEngine.paramiko = False

## The IPython profile to use.
#  See also: BaseIPythonApplication.profile
# c.IPEngine.profile = 'default'

## Override the registration URL
#  Default: ''
# c.IPEngine.registration_url = ''

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.IPEngine.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.IPEngine.show_config_json = False

## The SSH private key file to use when tunneling connections to the Controller.
#  Default: ''
# c.IPEngine.sshkey = ''

## The SSH server to use for tunneling connections to the Controller.
#  Default: ''
# c.IPEngine.sshserver = ''

## specify a command to be run at startup
#  Default: ''
# c.IPEngine.startup_command = ''

## specify a script to be run at startup
#  Default: ''
# c.IPEngine.startup_script = ''

## The time (in seconds) to wait for the Controller to respond
#          to registration requests before giving up.
#  Default: 5.0
# c.IPEngine.timeout = 5.0

## The full location of the file containing the connection information for
#          the controller. If this is not given, the file must be in the
#          security directory of the cluster directory.  This location is
#          resolved using the `profile` or `profile_dir` options.
#  Default: ''
# c.IPEngine.url_file = ''

#  Default: 'ipcontroller-engine.json'
# c.IPEngine.url_file_name = 'ipcontroller-engine.json'

## Enable MPI integration.
#  
#          If set, MPI rank will be requested for my rank,
#          and additionally `mpi_init` will be executed in the interactive shell.
#  Default: False
# c.IPEngine.use_mpi = False

## Create a massive crash report when IPython encounters what may be an
#  See also: BaseIPythonApplication.verbose_crash
# c.IPEngine.verbose_crash = False

## The maximum number of seconds to wait for url_file to exist.
#          This is useful for batch-systems and shared-filesystems where the
#          controller and engine are started at the same time and it
#          may take a moment for the controller to write the connector files.
#  Default: 10
# c.IPEngine.wait_for_url_file = 10

## Set the working dir for the process.
#  See also: BaseParallelApplication.work_dir
# c.IPEngine.work_dir = '/home/ubuntu'

#------------------------------------------------------------------------------
# InteractiveShell(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
## An enhanced, interactive shell for Python.

## 'all', 'last', 'last_expr' or 'none', 'last_expr_or_assign' specifying which
#  nodes should be run interactively (displaying output from expressions).
#  Choices: any of ['all', 'last', 'last_expr', 'none', 'last_expr_or_assign']
#  Default: 'last_expr'
# c.InteractiveShell.ast_node_interactivity = 'last_expr'

## A list of ast.NodeTransformer subclass instances, which will be applied to
#  user input before code is run.
#  Default: []
# c.InteractiveShell.ast_transformers = []

## Automatically run await statement in the top level repl.
#  Default: True
# c.InteractiveShell.autoawait = True

## Make IPython automatically call any callable object even if you didn't type
#  explicit parentheses. For example, 'str 43' becomes 'str(43)' automatically.
#  The value can be '0' to disable the feature, '1' for 'smart' autocall, where
#  it is not applied if there are no more arguments on the line, and '2' for
#  'full' autocall, where all callable objects are automatically called (even if
#  no arguments are present).
#  Choices: any of [0, 1, 2]
#  Default: 0
# c.InteractiveShell.autocall = 0

## Autoindent IPython code entered interactively.
#  Default: True
# c.InteractiveShell.autoindent = True

## Enable magic commands to be called without the leading %.
#  Default: True
# c.InteractiveShell.automagic = True

## The part of the banner to be printed before the profile
#  Default: "Python 3.8.10 (default, Mar 13 2023, 10:26:41) \nType 'copyright', 'credits' or 'license' for more information\nIPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.\n"
# c.InteractiveShell.banner1 = "Python 3.8.10 (default, Mar 13 2023, 10:26:41) \nType 'copyright', 'credits' or 'license' for more information\nIPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.\n"

## The part of the banner to be printed after the profile
#  Default: ''
# c.InteractiveShell.banner2 = ''

## Set the size of the output cache.  The default is 1000, you can change it
#  permanently in your config file.  Setting it to 0 completely disables the
#  caching system, and the minimum value accepted is 3 (if you provide a value
#  less than 3, it is reset to 0 and a warning is issued).  This limit is defined
#  because otherwise you'll spend more time re-flushing a too small cache than
#  working
#  Default: 1000
# c.InteractiveShell.cache_size = 1000

## Use colors for displaying information about objects. Because this information
#  is passed through a pager (like 'less'), and some pagers get confused with
#  color codes, this capability can be turned off.
#  Default: True
# c.InteractiveShell.color_info = True

## Set the color scheme (NoColor, Neutral, Linux, or LightBG).
#  Choices: any of ['Neutral', 'NoColor', 'LightBG', 'Linux'] (case-insensitive)
#  Default: 'Neutral'
# c.InteractiveShell.colors = 'Neutral'

#  Default: False
# c.InteractiveShell.debug = False

## Don't call post-execute functions that have failed in the past.
#  Default: False
# c.InteractiveShell.disable_failing_post_execute = False

## If True, anything that would be passed to the pager
#          will be displayed as regular output instead.
#  Default: False
# c.InteractiveShell.display_page = False

## (Provisional API) enables html representation in mime bundles sent to pagers.
#  Default: False
# c.InteractiveShell.enable_html_pager = False

## Total length of command history
#  Default: 10000
# c.InteractiveShell.history_length = 10000

## The number of saved history entries to be loaded into the history buffer at
#  startup.
#  Default: 1000
# c.InteractiveShell.history_load_length = 1000

## Class to use to instantiate the shell inspector
#  Default: 'IPython.core.oinspect.Inspector'
# c.InteractiveShell.inspector_class = 'IPython.core.oinspect.Inspector'

#  Default: ''
# c.InteractiveShell.ipython_dir = ''

## Start logging to the given file in append mode. Use `logfile` to specify a log
#  file to **overwrite** logs to.
#  Default: ''
# c.InteractiveShell.logappend = ''

## The name of the logfile to use.
#  Default: ''
# c.InteractiveShell.logfile = ''

## Start logging to the default log file in overwrite mode. Use `logappend` to
#  specify a log file to **append** logs to.
#  Default: False
# c.InteractiveShell.logstart = False

## Select the loop runner that will be used to execute top-level asynchronous
#  code
#  Default: 'IPython.core.interactiveshell._asyncio_runner'
# c.InteractiveShell.loop_runner = 'IPython.core.interactiveshell._asyncio_runner'

#  Choices: any of [0, 1, 2]
#  Default: 0
# c.InteractiveShell.object_info_string_level = 0

## Automatically call the pdb debugger after every exception.
#  Default: False
# c.InteractiveShell.pdb = False

#  Default: False
# c.InteractiveShell.quiet = False

#  Default: '\n'
# c.InteractiveShell.separate_in = '\n'

#  Default: ''
# c.InteractiveShell.separate_out = ''

#  Default: ''
# c.InteractiveShell.separate_out2 = ''

## Show rewritten input, e.g. for autocall.
#  Default: True
# c.InteractiveShell.show_rewritten_input = True

## Enables rich html representation of docstrings. (This requires the docrepr
#  module).
#  Default: False
# c.InteractiveShell.sphinxify_docstring = False

## Warn if running in a virtual environment with no IPython installed (so IPython
#  from the global environment is used).
#  Default: True
# c.InteractiveShell.warn_venv = True

#  Default: True
# c.InteractiveShell.wildcards_case_sensitive = True

## Switch modes for the IPython exception handlers.
#  Choices: any of ['Context', 'Plain', 'Verbose', 'Minimal'] (case-insensitive)
#  Default: 'Context'
# c.InteractiveShell.xmode = 'Context'

#------------------------------------------------------------------------------
# ZMQInteractiveShell(InteractiveShell) configuration
#------------------------------------------------------------------------------
## A subclass of InteractiveShell for ZMQ.

## 
#  See also: InteractiveShell.ast_node_interactivity
# c.ZMQInteractiveShell.ast_node_interactivity = 'last_expr'

## 
#  See also: InteractiveShell.ast_transformers
# c.ZMQInteractiveShell.ast_transformers = []

## 
#  See also: InteractiveShell.autoawait
# c.ZMQInteractiveShell.autoawait = True

## 
#  See also: InteractiveShell.autocall
# c.ZMQInteractiveShell.autocall = 0

## 
#  See also: InteractiveShell.automagic
# c.ZMQInteractiveShell.automagic = True

## The part of the banner to be printed before the profile
#  See also: InteractiveShell.banner1
# c.ZMQInteractiveShell.banner1 = "Python 3.8.10 (default, Mar 13 2023, 10:26:41) \nType 'copyright', 'credits' or 'license' for more information\nIPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.\n"

## The part of the banner to be printed after the profile
#  See also: InteractiveShell.banner2
# c.ZMQInteractiveShell.banner2 = ''

## 
#  See also: InteractiveShell.cache_size
# c.ZMQInteractiveShell.cache_size = 1000

## 
#  See also: InteractiveShell.color_info
# c.ZMQInteractiveShell.color_info = True

## Set the color scheme (NoColor, Neutral, Linux, or LightBG).
#  See also: InteractiveShell.colors
# c.ZMQInteractiveShell.colors = 'Neutral'

#  See also: InteractiveShell.debug
# c.ZMQInteractiveShell.debug = False

## Don't call post-execute functions that have failed in the past.
#  See also: InteractiveShell.disable_failing_post_execute
# c.ZMQInteractiveShell.disable_failing_post_execute = False

## If True, anything that would be passed to the pager
#  See also: InteractiveShell.display_page
# c.ZMQInteractiveShell.display_page = False

## 
#  See also: InteractiveShell.enable_html_pager
# c.ZMQInteractiveShell.enable_html_pager = False

## Total length of command history
#  See also: InteractiveShell.history_length
# c.ZMQInteractiveShell.history_length = 10000

## 
#  See also: InteractiveShell.history_load_length
# c.ZMQInteractiveShell.history_load_length = 1000

## Class to use to instantiate the shell inspector
#  See also: InteractiveShell.inspector_class
# c.ZMQInteractiveShell.inspector_class = 'IPython.core.oinspect.Inspector'

#  See also: InteractiveShell.ipython_dir
# c.ZMQInteractiveShell.ipython_dir = ''

## 
#  See also: InteractiveShell.logappend
# c.ZMQInteractiveShell.logappend = ''

## 
#  See also: InteractiveShell.logfile
# c.ZMQInteractiveShell.logfile = ''

## 
#  See also: InteractiveShell.logstart
# c.ZMQInteractiveShell.logstart = False

## Select the loop runner that will be used to execute top-level asynchronous
#  code
#  See also: InteractiveShell.loop_runner
# c.ZMQInteractiveShell.loop_runner = 'IPython.core.interactiveshell._asyncio_runner'

#  See also: InteractiveShell.object_info_string_level
# c.ZMQInteractiveShell.object_info_string_level = 0

## 
#  See also: InteractiveShell.pdb
# c.ZMQInteractiveShell.pdb = False

#  See also: InteractiveShell.quiet
# c.ZMQInteractiveShell.quiet = False

#  See also: InteractiveShell.separate_in
# c.ZMQInteractiveShell.separate_in = '\n'

#  See also: InteractiveShell.separate_out
# c.ZMQInteractiveShell.separate_out = ''

#  See also: InteractiveShell.separate_out2
# c.ZMQInteractiveShell.separate_out2 = ''

## Show rewritten input, e.g. for autocall.
#  See also: InteractiveShell.show_rewritten_input
# c.ZMQInteractiveShell.show_rewritten_input = True

## 
#  See also: InteractiveShell.sphinxify_docstring
# c.ZMQInteractiveShell.sphinxify_docstring = False

## Warn if running in a virtual environment with no IPython installed (so IPython
#  from the global environment is used).
#  See also: InteractiveShell.warn_venv
# c.ZMQInteractiveShell.warn_venv = True

#  See also: InteractiveShell.wildcards_case_sensitive
# c.ZMQInteractiveShell.wildcards_case_sensitive = True

## Switch modes for the IPython exception handlers.
#  See also: InteractiveShell.xmode
# c.ZMQInteractiveShell.xmode = 'Context'

#------------------------------------------------------------------------------
# ProfileDir(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## An object to manage the profile directory and its resources.
#  
#      The profile directory is used by all IPython applications, to manage
#      configuration, logging and security.
#  
#      This object knows how to find, create and manage these directories. This
#      should be used by any code that wants to handle profiles.

## Set the profile location directly. This overrides the logic used by the
#          `profile` option.
#  Default: ''
# c.ProfileDir.location = ''

#------------------------------------------------------------------------------
# Session(Configurable) configuration
#------------------------------------------------------------------------------
## Object for handling serialization and sending of messages.
#  
#      The Session object handles building messages and sending them
#      with ZMQ sockets or ZMQStream objects.  Objects can communicate with each
#      other over the network via Session objects, and only need to work with the
#      dict-based IPython message spec. The Session will handle
#      serialization/deserialization, security, and metadata.
#  
#      Sessions support configurable serialization via packer/unpacker traits,
#      and signing with HMAC digests via the key/keyfile traits.
#  
#      Parameters
#      ----------
#  
#      debug : bool
#          whether to trigger extra debugging statements
#      packer/unpacker : str : 'json', 'pickle' or import_string
#          importstrings for methods to serialize message parts.  If just
#          'json' or 'pickle', predefined JSON and pickle packers will be used.
#          Otherwise, the entire importstring must be used.
#  
#          The functions must accept at least valid JSON input, and output
#  *bytes*.
#  
#          For example, to use msgpack:
#          packer = 'msgpack.packb', unpacker='msgpack.unpackb'
#      pack/unpack : callables
#          You can also set the pack/unpack callables for serialization directly.
#      session : bytes
#          the ID of this Session object.  The default is to generate a new UUID.
#      username : unicode
#          username added to message headers.  The default is to ask the OS.
#      key : bytes
#          The key used to initialize an HMAC signature.  If unset, messages
#          will not be signed or checked.
#      keyfile : filepath
#          The file containing a key.  If this is set, `key` will be initialized
#          to the contents of the file.

## Threshold (in bytes) beyond which an object's buffer should be extracted to
#  avoid pickling.
#  Default: 1024
# c.Session.buffer_threshold = 1024

## Whether to check PID to protect against calls after fork.
#  
#          This check can be disabled if fork-safety is handled elsewhere.
#  Default: True
# c.Session.check_pid = True

## Threshold (in bytes) beyond which a buffer should be sent without copying.
#  Default: 65536
# c.Session.copy_threshold = 65536

## Debug output in the Session
#  Default: False
# c.Session.debug = False

## The maximum number of digests to remember.
#  
#          The digest history will be culled when it exceeds this value.
#  Default: 65536
# c.Session.digest_history_size = 65536

## The maximum number of items for a container to be introspected for custom serialization.
#          Containers larger than this are pickled outright.
#  Default: 64
# c.Session.item_threshold = 64

## execution key, for signing messages.
#  Default: b''
# c.Session.key = b''

## path to file containing execution key.
#  Default: ''
# c.Session.keyfile = ''

## Metadata dictionary, which serves as the default top-level metadata dict for
#  each message.
#  Default: {}
# c.Session.metadata = {}

## The name of the packer for serializing messages.
#              Should be one of 'json', 'pickle', or an import name
#              for a custom callable serializer.
#  Default: 'json'
# c.Session.packer = 'json'

## The UUID identifying this session.
#  Default: ''
# c.Session.session = ''

## The digest scheme used to construct the message signatures.
#          Must have the form 'hmac-HASH'.
#  Default: 'hmac-sha256'
# c.Session.signature_scheme = 'hmac-sha256'

## The name of the unpacker for unserializing messages.
#          Only used with custom functions for `packer`.
#  Default: 'json'
# c.Session.unpacker = 'json'

## Username for the Session. Default is your system username.
#  Default: 'ubuntu'
# c.Session.username = 'ubuntu'

#------------------------------------------------------------------------------
# Kernel(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
## The base kernel class.

## Whether to use appnope for compatibility with OS X App Nap.
#  
#          Only affects OS X >= 10.9.
#  Default: True
# c.Kernel._darwin_app_nap = True

#  Default: 0.0005
# c.Kernel._execute_sleep = 0.0005

#  Default: 0.01
# c.Kernel._poll_interval = 0.01

## Set to False if you want to debug python standard and dependent libraries.
#  Default: True
# c.Kernel.debug_just_my_code = True

## time (in seconds) to wait for messages to arrive
#          when aborting queued requests after an error.
#  
#          Requests that arrive within this window after an error
#          will be cancelled.
#  
#          Increase in the event of unusually slow network
#          causing significant delays,
#          which can manifest as e.g. "Run all" in a notebook
#          aborting some, but not all, messages after an error.
#  Default: 0.0
# c.Kernel.stop_on_error_timeout = 0.0

#------------------------------------------------------------------------------
# IPythonKernel(Kernel) configuration
#------------------------------------------------------------------------------
## The IPython Kernel class.

## Whether to use appnope for compatibility with OS X App Nap.
#  See also: Kernel._darwin_app_nap
# c.IPythonKernel._darwin_app_nap = True

#  See also: Kernel._execute_sleep
# c.IPythonKernel._execute_sleep = 0.0005

#  See also: Kernel._poll_interval
# c.IPythonKernel._poll_interval = 0.01

## Set to False if you want to debug python standard and dependent libraries.
#  See also: Kernel.debug_just_my_code
# c.IPythonKernel.debug_just_my_code = True

#  Default: [{'text': 'Python Reference', 'url': 'https://docs.python.org/3.8'}, {'text': 'IPython Reference', 'url': 'https://ipython.org/documentation.html'}, {'text': 'NumPy Reference', 'url': 'https://docs.scipy.org/doc/numpy/reference/'}, {'text': 'SciPy Reference', 'url': 'https://docs.scipy.org/doc/scipy/reference/'}, {'text': 'Matplotlib Reference', 'url': 'https://matplotlib.org/contents.html'}, {'text': 'SymPy Reference', 'url': 'http://docs.sympy.org/latest/index.html'}, {'text': 'pandas Reference', 'url': 'https://pandas.pydata.org/pandas-docs/stable/'}]
# c.IPythonKernel.help_links = [{'text': 'Python Reference', 'url': 'https://docs.python.org/3.8'}, {'text': 'IPython Reference', 'url': 'https://ipython.org/documentation.html'}, {'text': 'NumPy Reference', 'url': 'https://docs.scipy.org/doc/numpy/reference/'}, {'text': 'SciPy Reference', 'url': 'https://docs.scipy.org/doc/scipy/reference/'}, {'text': 'Matplotlib Reference', 'url': 'https://matplotlib.org/contents.html'}, {'text': 'SymPy Reference', 'url': 'http://docs.sympy.org/latest/index.html'}, {'text': 'pandas Reference', 'url': 'https://pandas.pydata.org/pandas-docs/stable/'}]

## time (in seconds) to wait for messages to arrive
#  See also: Kernel.stop_on_error_timeout
# c.IPythonKernel.stop_on_error_timeout = 0.0

## Set this flag to False to deactivate the use of experimental IPython
#  completion APIs.
#  Default: True
# c.IPythonKernel.use_experimental_completions = True

#------------------------------------------------------------------------------
# IPythonParallelKernel(IPythonKernel) configuration
#------------------------------------------------------------------------------
## Extend IPython kernel for parallel computing

## Whether to use appnope for compatibility with OS X App Nap.
#  See also: Kernel._darwin_app_nap
# c.IPythonParallelKernel._darwin_app_nap = True

#  See also: Kernel._poll_interval
# c.IPythonParallelKernel._poll_interval = 0.01

## Set to False if you want to debug python standard and dependent libraries.
#  See also: Kernel.debug_just_my_code
# c.IPythonParallelKernel.debug_just_my_code = True

#  See also: IPythonKernel.help_links
# c.IPythonParallelKernel.help_links = [{'text': 'Python Reference', 'url': 'https://docs.python.org/3.8'}, {'text': 'IPython Reference', 'url': 'https://ipython.org/documentation.html'}, {'text': 'NumPy Reference', 'url': 'https://docs.scipy.org/doc/numpy/reference/'}, {'text': 'SciPy Reference', 'url': 'https://docs.scipy.org/doc/scipy/reference/'}, {'text': 'Matplotlib Reference', 'url': 'https://matplotlib.org/contents.html'}, {'text': 'SymPy Reference', 'url': 'http://docs.sympy.org/latest/index.html'}, {'text': 'pandas Reference', 'url': 'https://pandas.pydata.org/pandas-docs/stable/'}]

## time (in seconds) to wait for messages to arrive
#  See also: Kernel.stop_on_error_timeout
# c.IPythonParallelKernel.stop_on_error_timeout = 0.0

## Set this flag to False to deactivate the use of experimental IPython
#  completion APIs.
#  See also: IPythonKernel.use_experimental_completions
# c.IPythonParallelKernel.use_experimental_completions = True
