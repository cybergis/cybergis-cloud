# Configuration file for ipcluster.

c = get_config()  #noqa

c.Cluster.engine_launcher_class = 'slurm'
c.SlurmEngineSetLauncher.batch_template = """#!/bin/sh
#SBATCH --ntasks={n}
#SBATCH --export=ALL
#SBATCH --job-name=ipengine-{cluster_id}
#SBATCH --cpus-per-task=1
env | sort

mpirun {program_and_args}
"""

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
# IPClusterEngines(BaseParallelApplication) configuration
#------------------------------------------------------------------------------
#  See also: BaseIPythonApplication.add_ipython_dir_to_sys_path
# c.IPClusterEngines.add_ipython_dir_to_sys_path = False

## Whether to create profile dir if it doesn't exist
#  See also: BaseIPythonApplication.auto_create
# c.IPClusterEngines.auto_create = False

## whether to cleanup old logfiles before starting
#  See also: BaseParallelApplication.clean_logs
# c.IPClusterEngines.clean_logs = False

## String id to add to runtime files, to prevent name collisions when
#  See also: BaseParallelApplication.cluster_id
# c.IPClusterEngines.cluster_id = ''

## Whether to install the default config files into the profile dir.
#  See also: BaseIPythonApplication.copy_config_files
# c.IPClusterEngines.copy_config_files = False

## Launch the cluster and immediately exit.
#  
#          .. versionchanged:: 7.0
#              No longer leaves the ipcluster process itself running.
#              Prior to 7.0, --daemonize did not work on Windows.
#  Default: False
# c.IPClusterEngines.daemonize = False

## If engines stop in this time frame, assume something is wrong and tear down
#  the cluster.
#  Default: 30
# c.IPClusterEngines.early_shutdown = 30

## Path to an extra config file to load.
#  See also: BaseIPythonApplication.extra_config_file
# c.IPClusterEngines.extra_config_file = ''

## 
#  See also: BaseIPythonApplication.ipython_dir
# c.IPClusterEngines.ipython_dir = ''

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.IPClusterEngines.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.IPClusterEngines.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.IPClusterEngines.log_level = 30

## whether to log to a file
#  See also: BaseParallelApplication.log_to_file
# c.IPClusterEngines.log_to_file = False

## The ZMQ URL of the iplogger to aggregate logging.
#  See also: BaseParallelApplication.log_url
# c.IPClusterEngines.log_url = ''

## 
#  See also: Application.logging_config
# c.IPClusterEngines.logging_config = {}

## Whether to overwrite existing config files when copying
#  See also: BaseIPythonApplication.overwrite
# c.IPClusterEngines.overwrite = False

## The IPython profile to use.
#  See also: BaseIPythonApplication.profile
# c.IPClusterEngines.profile = 'default'

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.IPClusterEngines.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.IPClusterEngines.show_config_json = False

## Create a massive crash report when IPython encounters what may be an
#  See also: BaseIPythonApplication.verbose_crash
# c.IPClusterEngines.verbose_crash = False

## Set the working dir for the process.
#  See also: BaseParallelApplication.work_dir
# c.IPClusterEngines.work_dir = '/home/ubuntu'

#------------------------------------------------------------------------------
# IPClusterStart(IPClusterEngines) configuration
#------------------------------------------------------------------------------
#  See also: BaseIPythonApplication.add_ipython_dir_to_sys_path
# c.IPClusterStart.add_ipython_dir_to_sys_path = False

## whether to create the profile_dir if it doesn't exist
#  Default: True
# c.IPClusterStart.auto_create = True

## whether to cleanup old logs before starting
#  Default: True
# c.IPClusterStart.clean_logs = True

## String id to add to runtime files, to prevent name collisions when
#  See also: BaseParallelApplication.cluster_id
# c.IPClusterStart.cluster_id = ''

## Whether to install the default config files into the profile dir.
#  See also: BaseIPythonApplication.copy_config_files
# c.IPClusterStart.copy_config_files = False

## Launch the cluster and immediately exit.
#  See also: IPClusterEngines.daemonize
# c.IPClusterStart.daemonize = False

## If engines stop in this time frame, assume something is wrong and tear down
#  the cluster.
#  See also: IPClusterEngines.early_shutdown
# c.IPClusterStart.early_shutdown = 30

## Path to an extra config file to load.
#  See also: BaseIPythonApplication.extra_config_file
# c.IPClusterStart.extra_config_file = ''

## 
#  See also: BaseIPythonApplication.ipython_dir
# c.IPClusterStart.ipython_dir = ''

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.IPClusterStart.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.IPClusterStart.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.IPClusterStart.log_level = 30

## whether to log to a file
#  See also: BaseParallelApplication.log_to_file
# c.IPClusterStart.log_to_file = False

## The ZMQ URL of the iplogger to aggregate logging.
#  See also: BaseParallelApplication.log_url
# c.IPClusterStart.log_url = ''

## 
#  See also: Application.logging_config
# c.IPClusterStart.logging_config = {}

## Whether to overwrite existing config files when copying
#  See also: BaseIPythonApplication.overwrite
# c.IPClusterStart.overwrite = False

## The IPython profile to use.
#  See also: BaseIPythonApplication.profile
# c.IPClusterStart.profile = 'default'

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.IPClusterStart.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.IPClusterStart.show_config_json = False

## Create a massive crash report when IPython encounters what may be an
#  See also: BaseIPythonApplication.verbose_crash
# c.IPClusterStart.verbose_crash = False

## Set the working dir for the process.
#  See also: BaseParallelApplication.work_dir
# c.IPClusterStart.work_dir = '/home/ubuntu'

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
# Cluster(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## Class representing an IPP cluster
#  
#      i.e. one controller and one or more groups of engines
#  
#      Can start/stop/monitor/poll cluster resources
#  
#      All async methods can be called synchronously with a `_sync` suffix,
#      e.g. `cluster.start_cluster_sync()`
#  
#      .. versionchanged:: 8.0
#          controller and engine launcher classes can be specified via
#          `Cluster(controller='ssh', engines='mpi')`
#          without the `_launcher_class` suffix.

## Additional CLI args to pass to the controller.
#  Default: []
# c.Cluster.controller_args = []

## Set the IP address of the controller.
#  Default: ''
# c.Cluster.controller_ip = ''

## The class for launching a Controller. Change this value if you want
#          your controller to also be launched by a batch system, such as PBS,SGE,MPI,etc.
#  
#          Each launcher class has its own set of configuration options, for making sure
#          it will work in your environment.
#  
#          Note that using a batch launcher for the controller *does not* put it
#          in the same batch job as the engines, so they will still start separately.
#  
#          Third-party engine launchers can be registered via
#  `ipyparallel.engine_launchers` entry point.
#  
#          They can be selected via case-insensitive abbreviation, e.g.
#  
#              c.Cluster.controller_launcher_class = 'SSH'
#  
#          or:
#  
#              ipcluster start --controller=MPI
#  
#  Currently installed: 
#    - batch: ipyparallel.cluster.launcher.BatchControllerLauncher
#    - htcondor: ipyparallel.cluster.launcher.HTCondorControllerLauncher
#    - local: ipyparallel.cluster.launcher.LocalControllerLauncher
#    - lsf: ipyparallel.cluster.launcher.LSFControllerLauncher
#    - mpi: ipyparallel.cluster.launcher.MPIControllerLauncher
#    - pbs: ipyparallel.cluster.launcher.PBSControllerLauncher
#    - sge: ipyparallel.cluster.launcher.SGEControllerLauncher
#    - slurm: ipyparallel.cluster.launcher.SlurmControllerLauncher
#    - ssh: ipyparallel.cluster.launcher.SSHControllerLauncher
#    - winhpc: ipyparallel.cluster.launcher.WindowsHPCControllerLauncher
#  Default: 'ipyparallel.cluster.launcher.LocalControllerLauncher'
# c.Cluster.controller_launcher_class = 'ipyparallel.cluster.launcher.LocalControllerLauncher'

## Set the location (hostname or ip) of the controller.
#  
#          This is used by engines and clients to locate the controller
#          when the controller listens on all interfaces
#  Default: ''
# c.Cluster.controller_location = ''

## delay (in s) between starting the controller and the engines
#  Default: 1.0
# c.Cluster.delay = 1.0

## The class for launching a set of Engines. Change this value
#          to use various batch systems to launch your engines, such as PBS,SGE,MPI,etc.
#          Each launcher class has its own set of configuration options, for making sure
#          it will work in your environment.
#  
#          Third-party engine launchers can be registered via
#  `ipyparallel.engine_launchers` entry point.
#  
#          They can be selected via case-insensitive abbreviation, e.g.
#  
#              c.Cluster.engine_launcher_class = 'ssh'
#  
#          or:
#  
#              ipcluster start --engines=mpi
#  
#  Currently installed: 
#    - batch: ipyparallel.cluster.launcher.BatchEngineSetLauncher
#    - htcondor: ipyparallel.cluster.launcher.HTCondorEngineSetLauncher
#    - local: ipyparallel.cluster.launcher.LocalEngineSetLauncher
#    - lsf: ipyparallel.cluster.launcher.LSFEngineSetLauncher
#    - mpi: ipyparallel.cluster.launcher.MPIEngineSetLauncher
#    - pbs: ipyparallel.cluster.launcher.PBSEngineSetLauncher
#    - sge: ipyparallel.cluster.launcher.SGEEngineSetLauncher
#    - slurm: ipyparallel.cluster.launcher.SlurmEngineSetLauncher
#    - ssh: ipyparallel.cluster.launcher.SSHEngineSetLauncher
#    - sshproxy: ipyparallel.cluster.launcher.SSHProxyEngineSetLauncher
#    - winhpc: ipyparallel.cluster.launcher.WindowsHPCEngineSetLauncher
#  Default: 'ipyparallel.cluster.launcher.LocalEngineSetLauncher'
# c.Cluster.engine_launcher_class = 'ipyparallel.cluster.launcher.LocalEngineSetLauncher'

## Timeout to use when waiting for engines to register
#  
#          before giving up.
#  Default: 60
# c.Cluster.engine_timeout = 60

## If True (default) load ipcluster config from profile directory, if present.
#  Default: True
# c.Cluster.load_profile = True

## The number of engines to start
#  Default: None
# c.Cluster.n = None

## Wait for controller's connection info before passing to engines via
#  $IPP_CONNECTION_INFO environment variable.
#  
#  Set to False to start engines immediately without waiting for the controller's
#  connection info to be available.
#  
#  When True, no connection file movement is required. False is mainly useful
#  when submitting the controller may take a long time in a job queue, and the
#  engines should enter the queue before the controller is running.
#  
#  .. versionadded:: 8.0
#  Default: True
# c.Cluster.send_engines_connection_env = True

#------------------------------------------------------------------------------
# BaseLauncher(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## An abstraction for starting, stopping and signaling a process.

## Set environment variables for the launched process
#  
#          .. versionadded:: 8.0
#  Default: {}
# c.BaseLauncher.environment = {}

## When a process exits, display up to this many lines of output
#  Default: 100
# c.BaseLauncher.output_limit = 100

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  Default: 60
# c.BaseLauncher.stop_timeout = 60

#------------------------------------------------------------------------------
# ControllerLauncher(BaseLauncher) configuration
#------------------------------------------------------------------------------
## Base class for launching ipcontroller

## command-line args to pass to ipcontroller
#  Default: []
# c.ControllerLauncher.controller_args = []

## Popen command to launch ipcontroller.
#  Default: ['/usr/bin/python3', '-m', 'ipyparallel.controller']
# c.ControllerLauncher.controller_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.controller']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.ControllerLauncher.environment = {}

## 
#  See also: BaseLauncher.output_limit
# c.ControllerLauncher.output_limit = 100

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.ControllerLauncher.stop_timeout = 60

#------------------------------------------------------------------------------
# BatchSystemLauncher(BaseLauncher) configuration
#------------------------------------------------------------------------------
## Launch an external process using a batch system.
#  
#      This class is designed to work with UNIX batch systems like PBS, LSF,
#      GridEngine, etc.  The overall model is that there are different commands
#      like qsub, qdel, etc. that handle the starting and stopping of the process.
#  
#      This class also has the notion of a batch script. The ``batch_template``
#      attribute can be set to a string that is a template for the batch script.
#      This template is instantiated using string formatting. Thus the template can
#      use {n} for the number of instances. Subclasses can add additional variables
#      to the template dict.

## The filename of the instantiated batch script.
#  Default: 'batch_script'
# c.BatchSystemLauncher.batch_file_name = 'batch_script'

## The string that is the batch script template itself.
#  Default: ''
# c.BatchSystemLauncher.batch_template = ''

## The file that contains the batch template.
#  Default: ''
# c.BatchSystemLauncher.batch_template_file = ''

## The name of the command line program used to delete jobs.
#  Default: ['']
# c.BatchSystemLauncher.delete_command = ['']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.BatchSystemLauncher.environment = {}

## A regular expression used to get the job id from the output of the
#          submit_command.
#  Default: ''
# c.BatchSystemLauncher.job_id_regexp = ''

## The group we wish to match in job_id_regexp (0 to match all)
#  Default: 0
# c.BatchSystemLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  
#          This lets you parameterize additional options,
#          such as wall_time with a custom template.
#  Default: {}
# c.BatchSystemLauncher.namespace = {}

## File in which to store stdout/err of processes
#  Default: ''
# c.BatchSystemLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.BatchSystemLauncher.output_limit = 100

## The batch queue.
#  Default: ''
# c.BatchSystemLauncher.queue = ''

## The name of the command line program used to send signals to jobs.
#  Default: ['']
# c.BatchSystemLauncher.signal_command = ['']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.BatchSystemLauncher.stop_timeout = 60

## The name of the command line program used to submit jobs.
#  Default: ['']
# c.BatchSystemLauncher.submit_command = ['']

#------------------------------------------------------------------------------
# BatchControllerLauncher(BatchSystemLauncher, ControllerLauncher) configuration
#------------------------------------------------------------------------------
## The filename of the instantiated batch script.
#  See also: BatchSystemLauncher.batch_file_name
# c.BatchControllerLauncher.batch_file_name = 'batch_script'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.BatchControllerLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.BatchControllerLauncher.batch_template_file = ''

## command-line args to pass to ipcontroller
#  See also: ControllerLauncher.controller_args
# c.BatchControllerLauncher.controller_args = []

## Popen command to launch ipcontroller.
#  See also: ControllerLauncher.controller_cmd
# c.BatchControllerLauncher.controller_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.controller']

## The name of the command line program used to delete jobs.
#  See also: BatchSystemLauncher.delete_command
# c.BatchControllerLauncher.delete_command = ['']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.BatchControllerLauncher.environment = {}

## A regular expression used to get the job id from the output of the
#  See also: BatchSystemLauncher.job_id_regexp
# c.BatchControllerLauncher.job_id_regexp = ''

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.BatchControllerLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.BatchControllerLauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.BatchControllerLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.BatchControllerLauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.BatchControllerLauncher.queue = ''

## The name of the command line program used to send signals to jobs.
#  See also: BatchSystemLauncher.signal_command
# c.BatchControllerLauncher.signal_command = ['']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.BatchControllerLauncher.stop_timeout = 60

## The name of the command line program used to submit jobs.
#  See also: BatchSystemLauncher.submit_command
# c.BatchControllerLauncher.submit_command = ['']

#------------------------------------------------------------------------------
# HTCondorLauncher(BatchSystemLauncher) configuration
#------------------------------------------------------------------------------
## A BatchSystemLauncher subclass for HTCondor.
#  
#      HTCondor requires that we launch the ipengine/ipcontroller scripts rather
#      that the python instance but otherwise is very similar to PBS.  This is because
#      HTCondor destroys sys.executable when launching remote processes - a launched
#      python process depends on sys.executable to effectively evaluate its
#      module search paths. Without it, regardless of which python interpreter you launch
#      you will get the to built in module search paths.
#  
#      We use the ip{cluster, engine, controller} scripts as our executable to circumvent
#      this - the mechanism of shebanged scripts means that the python binary will be
#      launched with argv[0] set to the *location of the ip{cluster, engine, controller}
#      scripts on the remote node*. This means you need to take care that:
#  
#      a. Your remote nodes have their paths configured correctly, with the ipengine and ipcontroller
#         of the python environment you wish to execute code in having top precedence.
#      b. This functionality is untested on Windows.
#  
#      If you need different behavior, consider making you own template.

## The filename of the instantiated batch script.
#  See also: BatchSystemLauncher.batch_file_name
# c.HTCondorLauncher.batch_file_name = 'batch_script'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.HTCondorLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.HTCondorLauncher.batch_template_file = ''

## The HTCondor delete command ['condor_rm']
#  Default: ['condor_rm']
# c.HTCondorLauncher.delete_command = ['condor_rm']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.HTCondorLauncher.environment = {}

## Regular expression for identifying the job ID [r'(\d+)\.$']
#  Default: '(\\d+)\\.$'
# c.HTCondorLauncher.job_id_regexp = '(\\d+)\\.$'

## The group we wish to match in job_id_regexp [1]
#  Default: 1
# c.HTCondorLauncher.job_id_regexp_group = 1

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.HTCondorLauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.HTCondorLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.HTCondorLauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.HTCondorLauncher.queue = ''

## The name of the command line program used to send signals to jobs.
#  See also: BatchSystemLauncher.signal_command
# c.HTCondorLauncher.signal_command = ['']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.HTCondorLauncher.stop_timeout = 60

## The HTCondor submit command ['condor_submit']
#  Default: ['condor_submit']
# c.HTCondorLauncher.submit_command = ['condor_submit']

#------------------------------------------------------------------------------
# HTCondorControllerLauncher(HTCondorLauncher, BatchControllerLauncher) configuration
#------------------------------------------------------------------------------
## Launch a controller using HTCondor.

## batch file name for the controller job.
#  Default: 'htcondor_controller'
# c.HTCondorControllerLauncher.batch_file_name = 'htcondor_controller'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.HTCondorControllerLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.HTCondorControllerLauncher.batch_template_file = ''

## command-line args to pass to ipcontroller
#  See also: ControllerLauncher.controller_args
# c.HTCondorControllerLauncher.controller_args = []

## Popen command to launch ipcontroller.
#  See also: ControllerLauncher.controller_cmd
# c.HTCondorControllerLauncher.controller_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.controller']

## The HTCondor delete command ['condor_rm']
#  See also: HTCondorLauncher.delete_command
# c.HTCondorControllerLauncher.delete_command = ['condor_rm']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.HTCondorControllerLauncher.environment = {}

## Regular expression for identifying the job ID [r'(\d+)\.$']
#  See also: HTCondorLauncher.job_id_regexp
# c.HTCondorControllerLauncher.job_id_regexp = '(\\d+)\\.$'

## The group we wish to match in job_id_regexp [1]
#  See also: HTCondorLauncher.job_id_regexp_group
# c.HTCondorControllerLauncher.job_id_regexp_group = 1

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.HTCondorControllerLauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.HTCondorControllerLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.HTCondorControllerLauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.HTCondorControllerLauncher.queue = ''

## The name of the command line program used to send signals to jobs.
#  See also: BatchSystemLauncher.signal_command
# c.HTCondorControllerLauncher.signal_command = ['']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.HTCondorControllerLauncher.stop_timeout = 60

## The HTCondor submit command ['condor_submit']
#  See also: HTCondorLauncher.submit_command
# c.HTCondorControllerLauncher.submit_command = ['condor_submit']

#------------------------------------------------------------------------------
# LocalProcessLauncher(BaseLauncher) configuration
#------------------------------------------------------------------------------
## Start and stop an external process in an asynchronous manner.
#  
#      This will launch the external process with a working directory of
#      ``self.work_dir``.

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.LocalProcessLauncher.environment = {}

## 
#  See also: BaseLauncher.output_limit
# c.LocalProcessLauncher.output_limit = 100

## Interval on which to poll processes (.
#  
#          Note: process exit should be noticed immediately,
#          due to use of Process.wait(),
#          but this interval should ensure we aren't leaving threads running forever,
#          as other signals/events are checked on this interval
#  Default: 30
# c.LocalProcessLauncher.poll_seconds = 30

## The number of seconds to wait for a process to exit after sending SIGTERM
#  before sending SIGKILL
#  Default: 5
# c.LocalProcessLauncher.stop_seconds_until_kill = 5

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.LocalProcessLauncher.stop_timeout = 60

#------------------------------------------------------------------------------
# LocalControllerLauncher(LocalProcessLauncher, ControllerLauncher) configuration
#------------------------------------------------------------------------------
## Launch a controller as a regular external process.

## command-line args to pass to ipcontroller
#  See also: ControllerLauncher.controller_args
# c.LocalControllerLauncher.controller_args = []

## Popen command to launch ipcontroller.
#  See also: ControllerLauncher.controller_cmd
# c.LocalControllerLauncher.controller_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.controller']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.LocalControllerLauncher.environment = {}

## 
#  See also: BaseLauncher.output_limit
# c.LocalControllerLauncher.output_limit = 100

## Interval on which to poll processes (.
#  See also: LocalProcessLauncher.poll_seconds
# c.LocalControllerLauncher.poll_seconds = 30

## The number of seconds to wait for a process to exit after sending SIGTERM
#  before sending SIGKILL
#  See also: LocalProcessLauncher.stop_seconds_until_kill
# c.LocalControllerLauncher.stop_seconds_until_kill = 5

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.LocalControllerLauncher.stop_timeout = 60

#------------------------------------------------------------------------------
# LSFLauncher(BatchSystemLauncher) configuration
#------------------------------------------------------------------------------
## A BatchSystemLauncher subclass for LSF.

## The filename of the instantiated batch script.
#  See also: BatchSystemLauncher.batch_file_name
# c.LSFLauncher.batch_file_name = 'batch_script'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.LSFLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.LSFLauncher.batch_template_file = ''

## The LSF delete command ['bkill']
#  Default: ['bkill']
# c.LSFLauncher.delete_command = ['bkill']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.LSFLauncher.environment = {}

## Regular expresion for identifying the job ID [r'\d+']
#  Default: '\\d+'
# c.LSFLauncher.job_id_regexp = '\\d+'

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.LSFLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.LSFLauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.LSFLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.LSFLauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.LSFLauncher.queue = ''

## The LSF signal command ['bkill', '-s']
#  Default: ['bkill', '-s']
# c.LSFLauncher.signal_command = ['bkill', '-s']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.LSFLauncher.stop_timeout = 60

## The LSF submit command ['bsub']
#  Default: ['bsub']
# c.LSFLauncher.submit_command = ['bsub']

#------------------------------------------------------------------------------
# LSFControllerLauncher(LSFLauncher, BatchControllerLauncher) configuration
#------------------------------------------------------------------------------
## Launch a controller using LSF.

## batch file name for the controller job.
#  Default: 'lsf_controller'
# c.LSFControllerLauncher.batch_file_name = 'lsf_controller'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.LSFControllerLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.LSFControllerLauncher.batch_template_file = ''

## command-line args to pass to ipcontroller
#  See also: ControllerLauncher.controller_args
# c.LSFControllerLauncher.controller_args = []

## Popen command to launch ipcontroller.
#  See also: ControllerLauncher.controller_cmd
# c.LSFControllerLauncher.controller_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.controller']

## The LSF delete command ['bkill']
#  See also: LSFLauncher.delete_command
# c.LSFControllerLauncher.delete_command = ['bkill']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.LSFControllerLauncher.environment = {}

## Regular expresion for identifying the job ID [r'\d+']
#  See also: LSFLauncher.job_id_regexp
# c.LSFControllerLauncher.job_id_regexp = '\\d+'

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.LSFControllerLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.LSFControllerLauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.LSFControllerLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.LSFControllerLauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.LSFControllerLauncher.queue = ''

## The LSF signal command ['bkill', '-s']
#  See also: LSFLauncher.signal_command
# c.LSFControllerLauncher.signal_command = ['bkill', '-s']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.LSFControllerLauncher.stop_timeout = 60

## The LSF submit command ['bsub']
#  See also: LSFLauncher.submit_command
# c.LSFControllerLauncher.submit_command = ['bsub']

#------------------------------------------------------------------------------
# MPILauncher(LocalProcessLauncher) configuration
#------------------------------------------------------------------------------
## Launch an external process using mpiexec.

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.MPILauncher.environment = {}

## The command line arguments to pass to mpiexec.
#  Default: []
# c.MPILauncher.mpi_args = []

## The mpiexec command to use in starting the process.
#  Default: ['mpiexec']
# c.MPILauncher.mpi_cmd = ['mpiexec']

## 
#  See also: BaseLauncher.output_limit
# c.MPILauncher.output_limit = 100

## Interval on which to poll processes (.
#  See also: LocalProcessLauncher.poll_seconds
# c.MPILauncher.poll_seconds = 30

## The number of seconds to wait for a process to exit after sending SIGTERM
#  before sending SIGKILL
#  See also: LocalProcessLauncher.stop_seconds_until_kill
# c.MPILauncher.stop_seconds_until_kill = 5

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.MPILauncher.stop_timeout = 60

#------------------------------------------------------------------------------
# MPIControllerLauncher(MPILauncher, ControllerLauncher) configuration
#------------------------------------------------------------------------------
## Launch a controller using mpiexec.

## command-line args to pass to ipcontroller
#  See also: ControllerLauncher.controller_args
# c.MPIControllerLauncher.controller_args = []

## Popen command to launch ipcontroller.
#  See also: ControllerLauncher.controller_cmd
# c.MPIControllerLauncher.controller_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.controller']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.MPIControllerLauncher.environment = {}

## The command line arguments to pass to mpiexec.
#  See also: MPILauncher.mpi_args
# c.MPIControllerLauncher.mpi_args = []

## The mpiexec command to use in starting the process.
#  See also: MPILauncher.mpi_cmd
# c.MPIControllerLauncher.mpi_cmd = ['mpiexec']

## 
#  See also: BaseLauncher.output_limit
# c.MPIControllerLauncher.output_limit = 100

## Interval on which to poll processes (.
#  See also: LocalProcessLauncher.poll_seconds
# c.MPIControllerLauncher.poll_seconds = 30

## The number of seconds to wait for a process to exit after sending SIGTERM
#  before sending SIGKILL
#  See also: LocalProcessLauncher.stop_seconds_until_kill
# c.MPIControllerLauncher.stop_seconds_until_kill = 5

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.MPIControllerLauncher.stop_timeout = 60

#------------------------------------------------------------------------------
# PBSLauncher(BatchSystemLauncher) configuration
#------------------------------------------------------------------------------
## A BatchSystemLauncher subclass for PBS.

## The filename of the instantiated batch script.
#  See also: BatchSystemLauncher.batch_file_name
# c.PBSLauncher.batch_file_name = 'batch_script'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.PBSLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.PBSLauncher.batch_template_file = ''

## The PBS delete command ['qdel']
#  Default: ['qdel']
# c.PBSLauncher.delete_command = ['qdel']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.PBSLauncher.environment = {}

## Regular expresion for identifying the job ID [r'\d+']
#  Default: '\\d+'
# c.PBSLauncher.job_id_regexp = '\\d+'

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.PBSLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.PBSLauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.PBSLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.PBSLauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.PBSLauncher.queue = ''

## The PBS signal command ['qsig']
#  Default: ['qsig', '-s']
# c.PBSLauncher.signal_command = ['qsig', '-s']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.PBSLauncher.stop_timeout = 60

## The PBS submit command ['qsub']
#  Default: ['qsub']
# c.PBSLauncher.submit_command = ['qsub']

#------------------------------------------------------------------------------
# PBSControllerLauncher(PBSLauncher, BatchControllerLauncher) configuration
#------------------------------------------------------------------------------
## Launch a controller using PBS.

## batch file name for the controller job.
#  Default: 'pbs_controller'
# c.PBSControllerLauncher.batch_file_name = 'pbs_controller'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.PBSControllerLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.PBSControllerLauncher.batch_template_file = ''

## command-line args to pass to ipcontroller
#  See also: ControllerLauncher.controller_args
# c.PBSControllerLauncher.controller_args = []

## Popen command to launch ipcontroller.
#  See also: ControllerLauncher.controller_cmd
# c.PBSControllerLauncher.controller_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.controller']

## The PBS delete command ['qdel']
#  See also: PBSLauncher.delete_command
# c.PBSControllerLauncher.delete_command = ['qdel']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.PBSControllerLauncher.environment = {}

## Regular expresion for identifying the job ID [r'\d+']
#  See also: PBSLauncher.job_id_regexp
# c.PBSControllerLauncher.job_id_regexp = '\\d+'

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.PBSControllerLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.PBSControllerLauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.PBSControllerLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.PBSControllerLauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.PBSControllerLauncher.queue = ''

## The PBS signal command ['qsig']
#  See also: PBSLauncher.signal_command
# c.PBSControllerLauncher.signal_command = ['qsig', '-s']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.PBSControllerLauncher.stop_timeout = 60

## The PBS submit command ['qsub']
#  See also: PBSLauncher.submit_command
# c.PBSControllerLauncher.submit_command = ['qsub']

#------------------------------------------------------------------------------
# SGELauncher(PBSLauncher) configuration
#------------------------------------------------------------------------------
## Sun GridEngine is a PBS clone with slightly different syntax

## The filename of the instantiated batch script.
#  See also: BatchSystemLauncher.batch_file_name
# c.SGELauncher.batch_file_name = 'batch_script'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.SGELauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.SGELauncher.batch_template_file = ''

## The PBS delete command ['qdel']
#  See also: PBSLauncher.delete_command
# c.SGELauncher.delete_command = ['qdel']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.SGELauncher.environment = {}

## Regular expresion for identifying the job ID [r'\d+']
#  See also: PBSLauncher.job_id_regexp
# c.SGELauncher.job_id_regexp = '\\d+'

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.SGELauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.SGELauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.SGELauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.SGELauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.SGELauncher.queue = ''

## The PBS signal command ['qsig']
#  See also: PBSLauncher.signal_command
# c.SGELauncher.signal_command = ['qsig', '-s']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.SGELauncher.stop_timeout = 60

## The PBS submit command ['qsub']
#  See also: PBSLauncher.submit_command
# c.SGELauncher.submit_command = ['qsub']

#------------------------------------------------------------------------------
# SGEControllerLauncher(SGELauncher, BatchControllerLauncher) configuration
#------------------------------------------------------------------------------
## Launch a controller using SGE.

## batch file name for the ipontroller job.
#  Default: 'sge_controller'
# c.SGEControllerLauncher.batch_file_name = 'sge_controller'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.SGEControllerLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.SGEControllerLauncher.batch_template_file = ''

## command-line args to pass to ipcontroller
#  See also: ControllerLauncher.controller_args
# c.SGEControllerLauncher.controller_args = []

## Popen command to launch ipcontroller.
#  See also: ControllerLauncher.controller_cmd
# c.SGEControllerLauncher.controller_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.controller']

## The PBS delete command ['qdel']
#  See also: PBSLauncher.delete_command
# c.SGEControllerLauncher.delete_command = ['qdel']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.SGEControllerLauncher.environment = {}

## Regular expresion for identifying the job ID [r'\d+']
#  See also: PBSLauncher.job_id_regexp
# c.SGEControllerLauncher.job_id_regexp = '\\d+'

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.SGEControllerLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.SGEControllerLauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.SGEControllerLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.SGEControllerLauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.SGEControllerLauncher.queue = ''

## The PBS signal command ['qsig']
#  See also: PBSLauncher.signal_command
# c.SGEControllerLauncher.signal_command = ['qsig', '-s']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.SGEControllerLauncher.stop_timeout = 60

## The PBS submit command ['qsub']
#  See also: PBSLauncher.submit_command
# c.SGEControllerLauncher.submit_command = ['qsub']

#------------------------------------------------------------------------------
# SlurmLauncher(BatchSystemLauncher) configuration
#------------------------------------------------------------------------------
## A BatchSystemLauncher subclass for slurm.

## Slurm account to be used
#  Default: ''
# c.SlurmLauncher.account = ''

## The filename of the instantiated batch script.
#  See also: BatchSystemLauncher.batch_file_name
# c.SlurmLauncher.batch_file_name = 'batch_script'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.SlurmLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.SlurmLauncher.batch_template_file = ''

## The slurm delete command ['scancel']
#  Default: ['scancel']
# c.SlurmLauncher.delete_command = ['scancel']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.SlurmLauncher.environment = {}

## Regular expresion for identifying the job ID [r'\d+']
#  Default: '\\d+'
# c.SlurmLauncher.job_id_regexp = '\\d+'

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.SlurmLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.SlurmLauncher.namespace = {}

## Extra Slurm options
#  Default: ''
# c.SlurmLauncher.options = ''

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.SlurmLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.SlurmLauncher.output_limit = 100

## Slurm QoS to be used
#  Default: ''
# c.SlurmLauncher.qos = ''

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.SlurmLauncher.queue = ''

## The slurm signal command ['scancel', '-s']
#  Default: ['scancel', '-s']
# c.SlurmLauncher.signal_command = ['scancel', '-s']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.SlurmLauncher.stop_timeout = 60

## The slurm submit command ['sbatch']
#  Default: ['sbatch']
# c.SlurmLauncher.submit_command = ['sbatch']

## Slurm timelimit to be used
#  Default: ''
# c.SlurmLauncher.timelimit = ''

#------------------------------------------------------------------------------
# SlurmControllerLauncher(SlurmLauncher, BatchControllerLauncher) configuration
#------------------------------------------------------------------------------
## Launch a controller using Slurm.

## Slurm account to be used
#  See also: SlurmLauncher.account
# c.SlurmControllerLauncher.account = ''

## batch file name for the controller job.
#  Default: 'slurm_controller.sbatch'
# c.SlurmControllerLauncher.batch_file_name = 'slurm_controller.sbatch'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.SlurmControllerLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.SlurmControllerLauncher.batch_template_file = ''

## command-line args to pass to ipcontroller
#  See also: ControllerLauncher.controller_args
# c.SlurmControllerLauncher.controller_args = []

## Popen command to launch ipcontroller.
#  See also: ControllerLauncher.controller_cmd
# c.SlurmControllerLauncher.controller_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.controller']

## The slurm delete command ['scancel']
#  See also: SlurmLauncher.delete_command
# c.SlurmControllerLauncher.delete_command = ['scancel']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.SlurmControllerLauncher.environment = {}

## Regular expresion for identifying the job ID [r'\d+']
#  See also: SlurmLauncher.job_id_regexp
# c.SlurmControllerLauncher.job_id_regexp = '\\d+'

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.SlurmControllerLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.SlurmControllerLauncher.namespace = {}

## Extra Slurm options
#  See also: SlurmLauncher.options
# c.SlurmControllerLauncher.options = ''

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.SlurmControllerLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.SlurmControllerLauncher.output_limit = 100

## Slurm QoS to be used
#  See also: SlurmLauncher.qos
# c.SlurmControllerLauncher.qos = ''

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.SlurmControllerLauncher.queue = ''

## The slurm signal command ['scancel', '-s']
#  See also: SlurmLauncher.signal_command
# c.SlurmControllerLauncher.signal_command = ['scancel', '-s']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.SlurmControllerLauncher.stop_timeout = 60

## The slurm submit command ['sbatch']
#  See also: SlurmLauncher.submit_command
# c.SlurmControllerLauncher.submit_command = ['sbatch']

## Slurm timelimit to be used
#  See also: SlurmLauncher.timelimit
# c.SlurmControllerLauncher.timelimit = ''

#------------------------------------------------------------------------------
# SSHLauncher(LocalProcessLauncher) configuration
#------------------------------------------------------------------------------
## A minimal launcher for ssh.
#  
#      To be useful this will probably have to be extended to use the ``sshx``
#      idea for environment variables.  There could be other things this needs
#      as well.

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.SSHLauncher.environment = {}

## hostname on which to launch the program
#  Default: ''
# c.SSHLauncher.hostname = ''

## user@hostname location for ssh in one setting
#  Default: ''
# c.SSHLauncher.location = ''

## 
#  See also: BaseLauncher.output_limit
# c.SSHLauncher.output_limit = 100

## Interval on which to poll processes (.
#  See also: LocalProcessLauncher.poll_seconds
# c.SSHLauncher.poll_seconds = 30

## The remote profile_dir to use.
#  
#          If not specified, use calling profile, stripping out possible leading
#  homedir.
#  Default: ''
# c.SSHLauncher.remote_profile_dir = ''

## Remote path to Python interpreter, if needed
#  Default: 'python3'
# c.SSHLauncher.remote_python = 'python3'

## args to pass to scp
#  Default: []
# c.SSHLauncher.scp_args = []

## command for sending files
#  Default: ['scp']
# c.SSHLauncher.scp_cmd = ['scp']

## args to pass to ssh
#  Default: []
# c.SSHLauncher.ssh_args = []

## command for starting ssh
#  Default: ['ssh']
# c.SSHLauncher.ssh_cmd = ['ssh']

## The number of seconds to wait for a process to exit after sending SIGTERM
#  before sending SIGKILL
#  See also: LocalProcessLauncher.stop_seconds_until_kill
# c.SSHLauncher.stop_seconds_until_kill = 5

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.SSHLauncher.stop_timeout = 60

## List of (remote, local) files to fetch after starting
#  Default: []
# c.SSHLauncher.to_fetch = []

## List of (local, remote) files to send before starting
#  Default: []
# c.SSHLauncher.to_send = []

## username for ssh
#  Default: ''
# c.SSHLauncher.user = ''

#------------------------------------------------------------------------------
# SSHControllerLauncher(SSHLauncher, ControllerLauncher) configuration
#------------------------------------------------------------------------------
## command-line args to pass to ipcontroller
#  See also: ControllerLauncher.controller_args
# c.SSHControllerLauncher.controller_args = []

## Popen command to launch ipcontroller.
#  See also: ControllerLauncher.controller_cmd
# c.SSHControllerLauncher.controller_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.controller']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.SSHControllerLauncher.environment = {}

## hostname on which to launch the program
#  See also: SSHLauncher.hostname
# c.SSHControllerLauncher.hostname = ''

## user@hostname location for ssh in one setting
#  See also: SSHLauncher.location
# c.SSHControllerLauncher.location = ''

## 
#  See also: BaseLauncher.output_limit
# c.SSHControllerLauncher.output_limit = 100

## Interval on which to poll processes (.
#  See also: LocalProcessLauncher.poll_seconds
# c.SSHControllerLauncher.poll_seconds = 30

## The remote profile_dir to use.
#  See also: SSHLauncher.remote_profile_dir
# c.SSHControllerLauncher.remote_profile_dir = ''

## Remote path to Python interpreter, if needed
#  See also: SSHLauncher.remote_python
# c.SSHControllerLauncher.remote_python = 'python3'

## args to pass to scp
#  See also: SSHLauncher.scp_args
# c.SSHControllerLauncher.scp_args = []

## command for sending files
#  See also: SSHLauncher.scp_cmd
# c.SSHControllerLauncher.scp_cmd = ['scp']

## args to pass to ssh
#  See also: SSHLauncher.ssh_args
# c.SSHControllerLauncher.ssh_args = []

## command for starting ssh
#  See also: SSHLauncher.ssh_cmd
# c.SSHControllerLauncher.ssh_cmd = ['ssh']

## The number of seconds to wait for a process to exit after sending SIGTERM
#  before sending SIGKILL
#  See also: LocalProcessLauncher.stop_seconds_until_kill
# c.SSHControllerLauncher.stop_seconds_until_kill = 5

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.SSHControllerLauncher.stop_timeout = 60

## List of (remote, local) files to fetch after starting
#  See also: SSHLauncher.to_fetch
# c.SSHControllerLauncher.to_fetch = []

## List of (local, remote) files to send before starting
#  See also: SSHLauncher.to_send
# c.SSHControllerLauncher.to_send = []

## username for ssh
#  See also: SSHLauncher.user
# c.SSHControllerLauncher.user = ''

#------------------------------------------------------------------------------
# WindowsHPCLauncher(BaseLauncher) configuration
#------------------------------------------------------------------------------
## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.WindowsHPCLauncher.environment = {}

## The command for submitting jobs.
#  Default: ''
# c.WindowsHPCLauncher.job_cmd = ''

## The filename of the instantiated job script.
#  Default: 'ipython_job.xml'
# c.WindowsHPCLauncher.job_file_name = 'ipython_job.xml'

## A regular expression used to get the job id from the output of the
#          submit_command.
#  Default: '\\d+'
# c.WindowsHPCLauncher.job_id_regexp = '\\d+'

## 
#  See also: BaseLauncher.output_limit
# c.WindowsHPCLauncher.output_limit = 100

## The hostname of the scheduler to submit the job to.
#  Default: ''
# c.WindowsHPCLauncher.scheduler = ''

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.WindowsHPCLauncher.stop_timeout = 60

#------------------------------------------------------------------------------
# WindowsHPCControllerLauncher(WindowsHPCLauncher) configuration
#------------------------------------------------------------------------------
## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.WindowsHPCControllerLauncher.environment = {}

## The command for submitting jobs.
#  See also: WindowsHPCLauncher.job_cmd
# c.WindowsHPCControllerLauncher.job_cmd = ''

## WinHPC xml job file.
#  Default: 'ipcontroller_job.xml'
# c.WindowsHPCControllerLauncher.job_file_name = 'ipcontroller_job.xml'

## A regular expression used to get the job id from the output of the
#  See also: WindowsHPCLauncher.job_id_regexp
# c.WindowsHPCControllerLauncher.job_id_regexp = '\\d+'

## 
#  See also: BaseLauncher.output_limit
# c.WindowsHPCControllerLauncher.output_limit = 100

## The hostname of the scheduler to submit the job to.
#  See also: WindowsHPCLauncher.scheduler
# c.WindowsHPCControllerLauncher.scheduler = ''

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.WindowsHPCControllerLauncher.stop_timeout = 60

#------------------------------------------------------------------------------
# EngineLauncher(BaseLauncher) configuration
#------------------------------------------------------------------------------
## Base class for launching one engine

## command-line arguments to pass to ipengine
#  Default: []
# c.EngineLauncher.engine_args = []

## command to launch the Engine.
#  Default: ['/usr/bin/python3', '-m', 'ipyparallel.engine']
# c.EngineLauncher.engine_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.engine']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.EngineLauncher.environment = {}

## 
#  See also: BaseLauncher.output_limit
# c.EngineLauncher.output_limit = 100

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.EngineLauncher.stop_timeout = 60

#------------------------------------------------------------------------------
# BatchEngineSetLauncher(BatchSystemLauncher, EngineLauncher) configuration
#------------------------------------------------------------------------------
## The filename of the instantiated batch script.
#  See also: BatchSystemLauncher.batch_file_name
# c.BatchEngineSetLauncher.batch_file_name = 'batch_script'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.BatchEngineSetLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.BatchEngineSetLauncher.batch_template_file = ''

## The name of the command line program used to delete jobs.
#  See also: BatchSystemLauncher.delete_command
# c.BatchEngineSetLauncher.delete_command = ['']

## command-line arguments to pass to ipengine
#  See also: EngineLauncher.engine_args
# c.BatchEngineSetLauncher.engine_args = []

## command to launch the Engine.
#  See also: EngineLauncher.engine_cmd
# c.BatchEngineSetLauncher.engine_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.engine']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.BatchEngineSetLauncher.environment = {}

## A regular expression used to get the job id from the output of the
#  See also: BatchSystemLauncher.job_id_regexp
# c.BatchEngineSetLauncher.job_id_regexp = ''

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.BatchEngineSetLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.BatchEngineSetLauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.BatchEngineSetLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.BatchEngineSetLauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.BatchEngineSetLauncher.queue = ''

## The name of the command line program used to send signals to jobs.
#  See also: BatchSystemLauncher.signal_command
# c.BatchEngineSetLauncher.signal_command = ['']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.BatchEngineSetLauncher.stop_timeout = 60

## The name of the command line program used to submit jobs.
#  See also: BatchSystemLauncher.submit_command
# c.BatchEngineSetLauncher.submit_command = ['']

#------------------------------------------------------------------------------
# HTCondorEngineSetLauncher(HTCondorLauncher, BatchEngineSetLauncher) configuration
#------------------------------------------------------------------------------
## Launch Engines using HTCondor

## batch file name for the engine(s) job.
#  Default: 'htcondor_engines'
# c.HTCondorEngineSetLauncher.batch_file_name = 'htcondor_engines'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.HTCondorEngineSetLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.HTCondorEngineSetLauncher.batch_template_file = ''

## The HTCondor delete command ['condor_rm']
#  See also: HTCondorLauncher.delete_command
# c.HTCondorEngineSetLauncher.delete_command = ['condor_rm']

## command-line arguments to pass to ipengine
#  See also: EngineLauncher.engine_args
# c.HTCondorEngineSetLauncher.engine_args = []

## command to launch the Engine.
#  See also: EngineLauncher.engine_cmd
# c.HTCondorEngineSetLauncher.engine_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.engine']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.HTCondorEngineSetLauncher.environment = {}

## Regular expression for identifying the job ID [r'(\d+)\.$']
#  See also: HTCondorLauncher.job_id_regexp
# c.HTCondorEngineSetLauncher.job_id_regexp = '(\\d+)\\.$'

## The group we wish to match in job_id_regexp [1]
#  See also: HTCondorLauncher.job_id_regexp_group
# c.HTCondorEngineSetLauncher.job_id_regexp_group = 1

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.HTCondorEngineSetLauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.HTCondorEngineSetLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.HTCondorEngineSetLauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.HTCondorEngineSetLauncher.queue = ''

## The name of the command line program used to send signals to jobs.
#  See also: BatchSystemLauncher.signal_command
# c.HTCondorEngineSetLauncher.signal_command = ['']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.HTCondorEngineSetLauncher.stop_timeout = 60

## The HTCondor submit command ['condor_submit']
#  See also: HTCondorLauncher.submit_command
# c.HTCondorEngineSetLauncher.submit_command = ['condor_submit']

#------------------------------------------------------------------------------
# LocalEngineLauncher(LocalProcessLauncher, EngineLauncher) configuration
#------------------------------------------------------------------------------
## Launch a single engine as a regular external process.

## command-line arguments to pass to ipengine
#  See also: EngineLauncher.engine_args
# c.LocalEngineLauncher.engine_args = []

## command to launch the Engine.
#  See also: EngineLauncher.engine_cmd
# c.LocalEngineLauncher.engine_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.engine']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.LocalEngineLauncher.environment = {}

## 
#  See also: BaseLauncher.output_limit
# c.LocalEngineLauncher.output_limit = 100

## Interval on which to poll processes (.
#  See also: LocalProcessLauncher.poll_seconds
# c.LocalEngineLauncher.poll_seconds = 30

## The number of seconds to wait for a process to exit after sending SIGTERM
#  before sending SIGKILL
#  See also: LocalProcessLauncher.stop_seconds_until_kill
# c.LocalEngineLauncher.stop_seconds_until_kill = 5

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.LocalEngineLauncher.stop_timeout = 60

#------------------------------------------------------------------------------
# LocalEngineSetLauncher(LocalEngineLauncher) configuration
#------------------------------------------------------------------------------
## Launch a set of engines as regular external processes.

## delay (in seconds) between starting each engine after the first.
#          This can help force the engines to get their ids in order, or limit
#          process flood when starting many engines.
#  Default: 0.1
# c.LocalEngineSetLauncher.delay = 0.1

## command-line arguments to pass to ipengine
#  See also: EngineLauncher.engine_args
# c.LocalEngineSetLauncher.engine_args = []

## command to launch the Engine.
#  See also: EngineLauncher.engine_cmd
# c.LocalEngineSetLauncher.engine_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.engine']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.LocalEngineSetLauncher.environment = {}

## 
#  See also: BaseLauncher.output_limit
# c.LocalEngineSetLauncher.output_limit = 100

## Interval on which to poll processes (.
#  See also: LocalProcessLauncher.poll_seconds
# c.LocalEngineSetLauncher.poll_seconds = 30

## The number of seconds to wait for a process to exit after sending SIGTERM
#  before sending SIGKILL
#  See also: LocalProcessLauncher.stop_seconds_until_kill
# c.LocalEngineSetLauncher.stop_seconds_until_kill = 5

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.LocalEngineSetLauncher.stop_timeout = 60

#------------------------------------------------------------------------------
# LSFEngineSetLauncher(LSFLauncher, BatchEngineSetLauncher) configuration
#------------------------------------------------------------------------------
## Launch Engines using LSF

## batch file name for the engine(s) job.
#  Default: 'lsf_engines'
# c.LSFEngineSetLauncher.batch_file_name = 'lsf_engines'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.LSFEngineSetLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.LSFEngineSetLauncher.batch_template_file = ''

## The LSF delete command ['bkill']
#  See also: LSFLauncher.delete_command
# c.LSFEngineSetLauncher.delete_command = ['bkill']

## command-line arguments to pass to ipengine
#  See also: EngineLauncher.engine_args
# c.LSFEngineSetLauncher.engine_args = []

## command to launch the Engine.
#  See also: EngineLauncher.engine_cmd
# c.LSFEngineSetLauncher.engine_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.engine']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.LSFEngineSetLauncher.environment = {}

## Regular expresion for identifying the job ID [r'\d+']
#  See also: LSFLauncher.job_id_regexp
# c.LSFEngineSetLauncher.job_id_regexp = '\\d+'

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.LSFEngineSetLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.LSFEngineSetLauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.LSFEngineSetLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.LSFEngineSetLauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.LSFEngineSetLauncher.queue = ''

## The LSF signal command ['bkill', '-s']
#  See also: LSFLauncher.signal_command
# c.LSFEngineSetLauncher.signal_command = ['bkill', '-s']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.LSFEngineSetLauncher.stop_timeout = 60

## The LSF submit command ['bsub']
#  See also: LSFLauncher.submit_command
# c.LSFEngineSetLauncher.submit_command = ['bsub']

#------------------------------------------------------------------------------
# MPIEngineSetLauncher(MPILauncher, EngineLauncher) configuration
#------------------------------------------------------------------------------
## Launch engines using mpiexec

## command-line arguments to pass to ipengine
#  See also: EngineLauncher.engine_args
# c.MPIEngineSetLauncher.engine_args = []

## command to launch the Engine.
#  See also: EngineLauncher.engine_cmd
# c.MPIEngineSetLauncher.engine_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.engine']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.MPIEngineSetLauncher.environment = {}

## The command line arguments to pass to mpiexec.
#  See also: MPILauncher.mpi_args
# c.MPIEngineSetLauncher.mpi_args = []

## The mpiexec command to use in starting the process.
#  See also: MPILauncher.mpi_cmd
# c.MPIEngineSetLauncher.mpi_cmd = ['mpiexec']

## 
#  See also: BaseLauncher.output_limit
# c.MPIEngineSetLauncher.output_limit = 100

## Interval on which to poll processes (.
#  See also: LocalProcessLauncher.poll_seconds
# c.MPIEngineSetLauncher.poll_seconds = 30

## The number of seconds to wait for a process to exit after sending SIGTERM
#  before sending SIGKILL
#  See also: LocalProcessLauncher.stop_seconds_until_kill
# c.MPIEngineSetLauncher.stop_seconds_until_kill = 5

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.MPIEngineSetLauncher.stop_timeout = 60

#------------------------------------------------------------------------------
# PBSEngineSetLauncher(PBSLauncher, BatchEngineSetLauncher) configuration
#------------------------------------------------------------------------------
## Launch Engines using PBS

## batch file name for the engine(s) job.
#  Default: 'pbs_engines'
# c.PBSEngineSetLauncher.batch_file_name = 'pbs_engines'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.PBSEngineSetLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.PBSEngineSetLauncher.batch_template_file = ''

## The PBS delete command ['qdel']
#  See also: PBSLauncher.delete_command
# c.PBSEngineSetLauncher.delete_command = ['qdel']

## command-line arguments to pass to ipengine
#  See also: EngineLauncher.engine_args
# c.PBSEngineSetLauncher.engine_args = []

## command to launch the Engine.
#  See also: EngineLauncher.engine_cmd
# c.PBSEngineSetLauncher.engine_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.engine']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.PBSEngineSetLauncher.environment = {}

## Regular expresion for identifying the job ID [r'\d+']
#  See also: PBSLauncher.job_id_regexp
# c.PBSEngineSetLauncher.job_id_regexp = '\\d+'

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.PBSEngineSetLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.PBSEngineSetLauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.PBSEngineSetLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.PBSEngineSetLauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.PBSEngineSetLauncher.queue = ''

## The PBS signal command ['qsig']
#  See also: PBSLauncher.signal_command
# c.PBSEngineSetLauncher.signal_command = ['qsig', '-s']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.PBSEngineSetLauncher.stop_timeout = 60

## The PBS submit command ['qsub']
#  See also: PBSLauncher.submit_command
# c.PBSEngineSetLauncher.submit_command = ['qsub']

#------------------------------------------------------------------------------
# SGEEngineSetLauncher(SGELauncher, BatchEngineSetLauncher) configuration
#------------------------------------------------------------------------------
## Launch Engines with SGE

## batch file name for the engine(s) job.
#  Default: 'sge_engines'
# c.SGEEngineSetLauncher.batch_file_name = 'sge_engines'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.SGEEngineSetLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.SGEEngineSetLauncher.batch_template_file = ''

## The PBS delete command ['qdel']
#  See also: PBSLauncher.delete_command
# c.SGEEngineSetLauncher.delete_command = ['qdel']

## command-line arguments to pass to ipengine
#  See also: EngineLauncher.engine_args
# c.SGEEngineSetLauncher.engine_args = []

## command to launch the Engine.
#  See also: EngineLauncher.engine_cmd
# c.SGEEngineSetLauncher.engine_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.engine']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.SGEEngineSetLauncher.environment = {}

## Regular expresion for identifying the job ID [r'\d+']
#  See also: PBSLauncher.job_id_regexp
# c.SGEEngineSetLauncher.job_id_regexp = '\\d+'

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.SGEEngineSetLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.SGEEngineSetLauncher.namespace = {}

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.SGEEngineSetLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.SGEEngineSetLauncher.output_limit = 100

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.SGEEngineSetLauncher.queue = ''

## The PBS signal command ['qsig']
#  See also: PBSLauncher.signal_command
# c.SGEEngineSetLauncher.signal_command = ['qsig', '-s']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.SGEEngineSetLauncher.stop_timeout = 60

## The PBS submit command ['qsub']
#  See also: PBSLauncher.submit_command
# c.SGEEngineSetLauncher.submit_command = ['qsub']

#------------------------------------------------------------------------------
# SlurmEngineSetLauncher(SlurmLauncher, BatchEngineSetLauncher) configuration
#------------------------------------------------------------------------------
## Launch Engines using Slurm

## Slurm account to be used
#  See also: SlurmLauncher.account
# c.SlurmEngineSetLauncher.account = ''

## batch file name for the engine(s) job.
#  Default: 'slurm_engine.sbatch'
# c.SlurmEngineSetLauncher.batch_file_name = 'slurm_engine.sbatch'

## The string that is the batch script template itself.
#  See also: BatchSystemLauncher.batch_template
# c.SlurmEngineSetLauncher.batch_template = ''

## The file that contains the batch template.
#  See also: BatchSystemLauncher.batch_template_file
# c.SlurmEngineSetLauncher.batch_template_file = ''

## The slurm delete command ['scancel']
#  See also: SlurmLauncher.delete_command
# c.SlurmEngineSetLauncher.delete_command = ['scancel']

## command-line arguments to pass to ipengine
#  See also: EngineLauncher.engine_args
# c.SlurmEngineSetLauncher.engine_args = []

## command to launch the Engine.
#  See also: EngineLauncher.engine_cmd
# c.SlurmEngineSetLauncher.engine_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.engine']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.SlurmEngineSetLauncher.environment = {}

## Regular expresion for identifying the job ID [r'\d+']
#  See also: SlurmLauncher.job_id_regexp
# c.SlurmEngineSetLauncher.job_id_regexp = '\\d+'

## The group we wish to match in job_id_regexp (0 to match all)
#  See also: BatchSystemLauncher.job_id_regexp_group
# c.SlurmEngineSetLauncher.job_id_regexp_group = 0

## Extra variables to pass to the template.
#  See also: BatchSystemLauncher.namespace
# c.SlurmEngineSetLauncher.namespace = {}

## Extra Slurm options
#  See also: SlurmLauncher.options
# c.SlurmEngineSetLauncher.options = ''

## File in which to store stdout/err of processes
#  See also: BatchSystemLauncher.output_file
# c.SlurmEngineSetLauncher.output_file = ''

## 
#  See also: BaseLauncher.output_limit
# c.SlurmEngineSetLauncher.output_limit = 100

## Slurm QoS to be used
#  See also: SlurmLauncher.qos
# c.SlurmEngineSetLauncher.qos = ''

## The batch queue.
#  See also: BatchSystemLauncher.queue
# c.SlurmEngineSetLauncher.queue = ''

## The slurm signal command ['scancel', '-s']
#  See also: SlurmLauncher.signal_command
# c.SlurmEngineSetLauncher.signal_command = ['scancel', '-s']

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.SlurmEngineSetLauncher.stop_timeout = 60

## The slurm submit command ['sbatch']
#  See also: SlurmLauncher.submit_command
# c.SlurmEngineSetLauncher.submit_command = ['sbatch']

## Slurm timelimit to be used
#  See also: SlurmLauncher.timelimit
# c.SlurmEngineSetLauncher.timelimit = ''

#------------------------------------------------------------------------------
# SSHEngineSetLauncher(LocalEngineSetLauncher, SSHLauncher) configuration
#------------------------------------------------------------------------------
## delay (in seconds) between starting each engine after the first.
#  See also: LocalEngineSetLauncher.delay
# c.SSHEngineSetLauncher.delay = 0.1

## command-line arguments to pass to ipengine
#  See also: EngineLauncher.engine_args
# c.SSHEngineSetLauncher.engine_args = []

## command to launch the Engine.
#  See also: EngineLauncher.engine_cmd
# c.SSHEngineSetLauncher.engine_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.engine']

## dict of engines to launch.  This is a dict by hostname of ints,
#          corresponding to the number of engines to start on that host.
#  Default: {}
# c.SSHEngineSetLauncher.engines = {}

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.SSHEngineSetLauncher.environment = {}

## hostname on which to launch the program
#  See also: SSHLauncher.hostname
# c.SSHEngineSetLauncher.hostname = ''

## user@hostname location for ssh in one setting
#  See also: SSHLauncher.location
# c.SSHEngineSetLauncher.location = ''

## 
#  See also: BaseLauncher.output_limit
# c.SSHEngineSetLauncher.output_limit = 100

## Interval on which to poll processes (.
#  See also: LocalProcessLauncher.poll_seconds
# c.SSHEngineSetLauncher.poll_seconds = 30

## The remote profile_dir to use.
#  See also: SSHLauncher.remote_profile_dir
# c.SSHEngineSetLauncher.remote_profile_dir = ''

## Remote path to Python interpreter, if needed
#  See also: SSHLauncher.remote_python
# c.SSHEngineSetLauncher.remote_python = 'python3'

## args to pass to scp
#  See also: SSHLauncher.scp_args
# c.SSHEngineSetLauncher.scp_args = []

## command for sending files
#  See also: SSHLauncher.scp_cmd
# c.SSHEngineSetLauncher.scp_cmd = ['scp']

## args to pass to ssh
#  See also: SSHLauncher.ssh_args
# c.SSHEngineSetLauncher.ssh_args = []

## command for starting ssh
#  See also: SSHLauncher.ssh_cmd
# c.SSHEngineSetLauncher.ssh_cmd = ['ssh']

## The number of seconds to wait for a process to exit after sending SIGTERM
#  before sending SIGKILL
#  See also: LocalProcessLauncher.stop_seconds_until_kill
# c.SSHEngineSetLauncher.stop_seconds_until_kill = 5

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.SSHEngineSetLauncher.stop_timeout = 60

## List of (remote, local) files to fetch after starting
#  See also: SSHLauncher.to_fetch
# c.SSHEngineSetLauncher.to_fetch = []

## List of (local, remote) files to send before starting
#  See also: SSHLauncher.to_send
# c.SSHEngineSetLauncher.to_send = []

## username for ssh
#  See also: SSHLauncher.user
# c.SSHEngineSetLauncher.user = ''

#------------------------------------------------------------------------------
# SSHProxyEngineSetLauncher(SSHLauncher, EngineLauncher) configuration
#------------------------------------------------------------------------------
## Launcher for calling
#      `ipcluster engines` on a remote machine.
#  
#      Requires that remote profile is already configured.

## command-line arguments to pass to ipengine
#  See also: EngineLauncher.engine_args
# c.SSHProxyEngineSetLauncher.engine_args = []

## command to launch the Engine.
#  See also: EngineLauncher.engine_cmd
# c.SSHProxyEngineSetLauncher.engine_cmd = ['/usr/bin/python3', '-m', 'ipyparallel.engine']

## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.SSHProxyEngineSetLauncher.environment = {}

## hostname on which to launch the program
#  See also: SSHLauncher.hostname
# c.SSHProxyEngineSetLauncher.hostname = ''

## Extra CLI arguments to pass to ipcluster engines
#  Default: []
# c.SSHProxyEngineSetLauncher.ipcluster_args = []

#  Default: []
# c.SSHProxyEngineSetLauncher.ipcluster_cmd = []

## user@hostname location for ssh in one setting
#  See also: SSHLauncher.location
# c.SSHProxyEngineSetLauncher.location = ''

## 
#  See also: BaseLauncher.output_limit
# c.SSHProxyEngineSetLauncher.output_limit = 100

## Interval on which to poll processes (.
#  See also: LocalProcessLauncher.poll_seconds
# c.SSHProxyEngineSetLauncher.poll_seconds = 30

## The remote profile_dir to use.
#  See also: SSHLauncher.remote_profile_dir
# c.SSHProxyEngineSetLauncher.remote_profile_dir = ''

## Remote path to Python interpreter, if needed
#  See also: SSHLauncher.remote_python
# c.SSHProxyEngineSetLauncher.remote_python = 'python3'

## args to pass to scp
#  See also: SSHLauncher.scp_args
# c.SSHProxyEngineSetLauncher.scp_args = []

## command for sending files
#  See also: SSHLauncher.scp_cmd
# c.SSHProxyEngineSetLauncher.scp_cmd = ['scp']

## args to pass to ssh
#  See also: SSHLauncher.ssh_args
# c.SSHProxyEngineSetLauncher.ssh_args = []

## command for starting ssh
#  See also: SSHLauncher.ssh_cmd
# c.SSHProxyEngineSetLauncher.ssh_cmd = ['ssh']

## The number of seconds to wait for a process to exit after sending SIGTERM
#  before sending SIGKILL
#  See also: LocalProcessLauncher.stop_seconds_until_kill
# c.SSHProxyEngineSetLauncher.stop_seconds_until_kill = 5

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.SSHProxyEngineSetLauncher.stop_timeout = 60

## List of (remote, local) files to fetch after starting
#  See also: SSHLauncher.to_fetch
# c.SSHProxyEngineSetLauncher.to_fetch = []

## List of (local, remote) files to send before starting
#  See also: SSHLauncher.to_send
# c.SSHProxyEngineSetLauncher.to_send = []

## username for ssh
#  See also: SSHLauncher.user
# c.SSHProxyEngineSetLauncher.user = ''

#------------------------------------------------------------------------------
# WindowsHPCEngineSetLauncher(WindowsHPCLauncher) configuration
#------------------------------------------------------------------------------
## Set environment variables for the launched process
#  See also: BaseLauncher.environment
# c.WindowsHPCEngineSetLauncher.environment = {}

## The command for submitting jobs.
#  See also: WindowsHPCLauncher.job_cmd
# c.WindowsHPCEngineSetLauncher.job_cmd = ''

## jobfile for ipengines job
#  Default: 'ipengineset_job.xml'
# c.WindowsHPCEngineSetLauncher.job_file_name = 'ipengineset_job.xml'

## A regular expression used to get the job id from the output of the
#  See also: WindowsHPCLauncher.job_id_regexp
# c.WindowsHPCEngineSetLauncher.job_id_regexp = '\\d+'

## 
#  See also: BaseLauncher.output_limit
# c.WindowsHPCEngineSetLauncher.output_limit = 100

## The hostname of the scheduler to submit the job to.
#  See also: WindowsHPCLauncher.scheduler
# c.WindowsHPCEngineSetLauncher.scheduler = ''

## The number of seconds to wait for a process to exit before raising a
#  TimeoutError in stop
#  See also: BaseLauncher.stop_timeout
# c.WindowsHPCEngineSetLauncher.stop_timeout = 60
