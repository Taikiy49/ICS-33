from pathlib import Path
import create_lists
import prepare


def _read_input_file_path() -> Path:
    """Reads the input file path from the standard input and returns a path object representing the input file path"""

    return Path(input())


def print_outcome(more_data: tuple[list, list, list, int]) -> None:
    """Prints the entire outcome with all the alerts and cancellations from the given data"""

    final_state_cancels, final_state_alerts, list_devices, end = more_data

    change_final = []
    stop_cancel = []
    for state in final_state_cancels:
        if state.split(':')[1:] not in stop_cancel:
            x = state.split(':')[1:]
            stop_cancel.append(x)
            change_final.append(state)

    final_state_cancels = change_final

    cancel_list = []
    for state in final_state_cancels:
        if 'SENT CANCELLATION' in state:
            x = state.split()
            cancel_list.append([int(x[0][1:-1]), x[1], x[5][:-1], x[6]])

    entire_final_state = final_state_alerts + final_state_cancels
    sorted_entire_final_state = sorted(entire_final_state, key=lambda r: int(r.split()[0][1:-1]))

    for state in sorted_entire_final_state:
        x = int(state.split()[0][1:-1])
        if x < int(end):
            print(state)
    print(f'@{end}: END')


def main() -> None:
    """Runs the simulation program in its entirety."""
    try:  # main is not tested but all sub-functions are not tested through coverage
        x = create_lists.lst(str(_read_input_file_path()))
        y = prepare.Device(x).prepare_outcome()
        print_outcome(y)

    except FileNotFoundError:
        print('FILE NOT FOUND')
    except IsADirectoryError:
        print('FILE NOT FOUND')


if __name__ == '__main__':
    main()
