def lst(file: str) -> tuple:
    """Reads an input file and extracts data to return lists of devices, propagates, alerts, cancels, and the
       program's end time."""
    list_devices = []
    list_propagates = []
    list_alerts = []
    list_cancels = []

    with open(file, 'r') as file:
        for line in file:
            if line:
                if line.startswith('LENGTH'):
                    end = line.split()[1]
                elif line.startswith('DEVICE'):
                    list_devices.append(line.split()[1])
                elif line.startswith('PROPAGATE'):
                    list_propagates.append(line.split())
                elif line.startswith('ALERT'):
                    list_alerts.append(line.split())
                elif line.startswith('CANCEL'):
                    list_cancels.append(line.split())

    return list_devices, list_propagates, list_alerts, list_cancels, end
