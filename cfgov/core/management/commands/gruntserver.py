import os
import subprocess
import atexit
import signal

from django.conf import settings
from django.contrib.staticfiles.management.commands.runserver import Command\
    as StaticfilesRunserverCommand


class Command(StaticfilesRunserverCommand):

    def inner_run(self, *args, **options):
        self.start_grunt()
        return super(Command, self).inner_run(*args, **options)

    def start_grunt(self):
        self.grunt_processes = []
        for dir in settings.GRUNT_WATCH:
            self.stdout.write('>>> Starting grunt in %s' % dir)
            sub = subprocess.Popen(
                'grunt watch',
                shell=True,
                stdin=subprocess.PIPE,
                stdout=self.stdout,
                stderr=self.stderr,
                cwd = settings.CFGOV_REFRESH,
            )

            self.grunt_processes.append(sub)

            self.stdout.write('>>> Grunt process on pid {0}'.format(sub.pid))

        def kill_grunt_processes(pids):
            for pid in pids: 
                self.stdout.write('>>> Closing grunt process %s' % pid)
                os.kill(pid, signal.SIGTERM)

        atexit.register(kill_grunt_processes, self.grunt_processes)
