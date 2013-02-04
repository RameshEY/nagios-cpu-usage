nagios-cpu-usage
================
Nagios plugin to collect CPU metrics per core.

Usage: check_cpu_percentage.py [options]

Options:
  --version         Show version number and exit
  -h, --help        Show this help message and exit
  -C, --CPU         Specify which CPU to check (cpu, cpu0, cpu1, ...)
  -w, --warning     Exit with WARNING status if CPU usage exceeds this percentage
  -c, --critical    Exit with CRITICAL status if CPU usage exceeds this percentage
