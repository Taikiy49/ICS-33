class Device:
    def __init__(self, data):
        """Initializes the Device instance with the provided data."""
        self.data = data  # input data that contains the list of devices, propagates, alerts, cancels, and end time.
        self.propagation_to = []  # a list that keeps track of the current propagation in the loop.
        self.cancel_dict = {}  # a dictionary that stores the cancellation information for each device.

    def prepare_outcome(self) -> tuple:
        """Returns the all the cancellations, alerts, devices, and the program's end time before being sorted."""
        data = self.data
        list_devices, list_propagates, list_alerts, list_cancels, end = data[0], data[1], data[2], data[3], data[4]

        all_alerts = []
        all_cancels = []

        for device in list_devices:
            self.cancel_dict[device] = []

        for cancel in list_cancels:
            self.propagation_to = []
            self.propagation_to.append([cancel[1], cancel[3]])
            while int(self.propagation_to[0][1]) < int(end):
                for prop in list_propagates:
                    if self.propagation_to[0][0] == prop[1]:
                        if str(cancel[2]) not in str(self.cancel_dict[prop[1]]):
                            self.cancel_dict[prop[1]].append(f'{self.propagation_to[0][1]} {cancel[2]}')
                        send_text = f'@{self.propagation_to[0][1]}: #{self.propagation_to[0][0]} SENT CANCELLATION TO #{prop[2]}: {cancel[2]}'
                        self.propagation_to.append([prop[2], self.propagation_to[0][1]])
                        self.propagation_to[-1][1] = int(self.propagation_to[0][1]) + int(prop[3])
                        receive_text = f'@{int(self.propagation_to[-1][1])}: #{prop[2]} RECEIVED CANCELLATION FROM #{self.propagation_to[0][0]}: {cancel[2]}'
                        all_cancels.append(send_text)
                        all_cancels.append(receive_text)
                self.propagation_to = sorted(self.propagation_to, key=lambda x: int(x[1]))
                self.propagation_to.pop(0)
                if self.propagation_to:
                    continue
                else:
                    break

        run = True
        for alert in list_alerts:
            self.propagation_to = []
            self.propagation_to.append([alert[1], alert[3]])
            message = alert[2]
            while run and int(self.propagation_to[0][1]) < int(end):
                for prop in list_propagates:
                    if self.propagation_to[0][0] == prop[1]:
                        if str(message) in str(self.cancel_dict[self.propagation_to[0][0]]):
                            x = self.cancel_dict[self.propagation_to[0][0]][0].split()
                            if message in x:
                                if int(self.propagation_to[0][1]) <= int(x[0]):
                                    all_alerts.append(f'@{self.propagation_to[0][1]}: #{self.propagation_to[0][0]} SENT ALERT TO #{prop[2]}: {alert[2]}')
                                    self.propagation_to.append([prop[2], self.propagation_to[0][1]])
                                    self.propagation_to[-1][1] = int(self.propagation_to[0][1]) + int(prop[3])
                                    all_alerts.append(f'@{int(self.propagation_to[-1][1])}: #{prop[2]} RECEIVED ALERT FROM #{self.propagation_to[0][0]}: {alert[2]}')
                        else:
                            all_alerts.append(
                                f'@{self.propagation_to[0][1]}: #{self.propagation_to[0][0]} SENT ALERT TO #{prop[2]}: {alert[2]}')
                            self.propagation_to.append([prop[2], self.propagation_to[0][1]])
                            self.propagation_to[-1][1] = int(self.propagation_to[0][1]) + int(prop[3])
                            all_alerts.append(
                                f'@{int(self.propagation_to[-1][1])}: #{prop[2]} RECEIVED ALERT FROM #{self.propagation_to[0][0]}: {alert[2]}')

                self.propagation_to = sorted(self.propagation_to, key=lambda r: int(r[1]))
                self.propagation_to.pop(0)
                if self.propagation_to:
                    continue
                else:
                    break

        return all_cancels, all_alerts, list_devices, end


