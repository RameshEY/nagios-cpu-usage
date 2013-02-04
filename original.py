#!/usr/bin/env python

from time import sleep

def get_cpu_stats():

    cpu_stats = open('/proc/stat', 'r').read().strip()

    lines = cpu_stats.split('\n')

    stats = {}
    cpulist = []

    for full_line in lines:
        line = full_line.split()
        id = line[0]
        if 'cpu' in id:
            cpulist.append(id)
            user = float(line[1])
            nice = float(line[2])
            system = float(line[3])
            idle = float(line[4])
            iowait = float(line[5])
            irq = float(line[6])
            softirq = float(line[7])
            steal = float(line[8])
            guest = float(line[9])

            active = user + nice + system + guest
            total = user + nice + system + idle + iowait + irq + softirq + steal + guest

            stats[id] = {'active': active, 'st': steal, 'total': total}

    return stats, cpulist

def main():

    reading1, cpulist = get_cpu_stats()
    sleep(10)
    reading2, cpulist = get_cpu_stats()

    print 'Core ID\tActive CPU\tCPU Steal\tCombined\tAlert Level'
    print '-------\t----------\t---------\t--------\t-----------'

    for cpu in cpulist:

        active = reading2[cpu]['active'] - reading1[cpu]['active']
        steal = reading2[cpu]['st'] - reading1[cpu]['st']
        total = reading2[cpu]['total'] - reading1[cpu]['total']

        active_p = active / total * 100
        steal_p = steal / total * 100
        combined_p = active_p + steal_p

        if active_p > 75.0:
            alert_level = 'CRITICAL'
        elif active_p > 25.0:
            alert_level = 'WARNING'
        else:
            alert_level = 'OK'

        print '%s\t%.1f%%\t\t%.1f%%\t\t%.1f%%\t\t%s' % (cpu, active_p, steal_p, combined_p, alert_level)

if __name__ == '__main__':
    main()
