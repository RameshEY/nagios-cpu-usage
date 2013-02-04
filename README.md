nagios-cpu-usage
================
Nagios plugin to collect CPU metrics per core.

Installation
------------
1. Copy the script to the Nagios plugin directory:
```
    mv linux-cpu-usage.py /usr/lib/nagios/plugins/check_linux_cpu
```
2. Add execute permissions to the script:
```
    chmod +x /usr/lib/nagios/plugins/check_linux_cpu
````
3. Edit /etc/nagios3/conf.d/commands.cfg:
```
    define command {
        command_name check_linux_cpu
        command_line /usr/lib/nagios/plugins/check_linux_cpu -C $ARG1$ -w $ARG2$ -c $ARG3$
    }
```

4. Edit /etc/nagios3/conf.d/services.cfg:
```
    define service {
        hostgroup_name desired_hostgroup
        service_description linux_cpu_usage
        check_command check_linux_cpu!cpu!25!75
        use generic-service
        notification_options w,u,c,r
        notifications_enabled 1
        contact_groups emailonly
    }
```

5. Reload Nagios configuration:
```
    /etc/init.d/nagios3 reload
```

This will set up an alert for all hosts in desired_hostgroup which warns at 25% overall CPU usage, and triggers a critical alert at 75% overall CPU usage.

Usage
-----
```
check_cpu_percentage.py [options]

Options:
  --version         Show version number and exit
  -h, --help        Show this help message and exit
  -C, --CPU         Specify which CPU to check (cpu, cpu0, cpu1, ...)
  -w, --warning     Exit with WARNING status if CPU usage exceeds this percentage
  -c, --critical    Exit with CRITICAL status if CPU usage exceeds this percentage
```
