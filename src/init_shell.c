#include <rtems/shell.h>
#include <rtems/bdbuf.h>

void start_shell(void)
{
	printf(" =========================\n");
	printf(" starting shell\n");
	printf(" =========================\n");

	rtems_shell_init(
		"SHLL",
		RTEMS_MINIMUM_STACK_SIZE * 4,
		100,
		"/dev/console",
		false,
		true,
		NULL
	);
}
