from __future__ import print_function

rtems_version = "6"

try:
    import rtems_waf.rtems as rtems
except:
    print('error: no rtems_waf git submodule')
    import sys
    sys.exit(1)

def init(ctx):
    # Initialize RTEMS v6
    rtems.init(ctx, version="6", long_commands=True)


def options(opt):
    # Inherit RTEMS CLI flags
    rtems.options(opt)


def configure(conf):
    rtems.configure(conf)


def build(bld):
    rtems.build(bld)

    bld(
        features='c cprogram',
        target='shell_example_rtems',
        cflags='-g -O2',
        source=['src/init.c', 'src/init_shell.c', 'src/main.c'],
    )

