/*
 * RTEMS SHEL Example
 */
#include <rtems.h>
#include <stdlib.h>
#include <stdio.h>
#include <rtems/bdbuf.h>

rtems_task Init(rtems_task_argument ignored)
{
  start_shell();
  exit(0);
}
