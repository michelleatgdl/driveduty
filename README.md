# DriveDuty

DriveDuty is a Python-based tool designed to monitor hard drive health and performance. It provides useful insights into the storage status, including disk usage and IO operations, and checks the SMART status on Linux systems.

## Features

- Lists all disk partitions with their usage statistics.
- Reports total, used, and free space on each partition.
- Displays disk IO operation counts and bytes read/written.
- Checks the SMART status of hard drives on Linux systems.

## Requirements

- Python 3.6+
- `psutil` library
- `smartmontools` for Linux (if checking SMART status)

## Installation

1. Ensure you have Python 3.6 or higher installed.
2. Install the `psutil` library via pip:
   ```bash
   pip install psutil
   ```
3. For Linux systems, ensure `smartmontools` is installed to check SMART status:
   ```bash
   sudo apt-get install smartmontools
   ```

## Usage

Run the program using Python:
```bash
python drive_duty.py
```

## Notes

- SMART status checking is only available on Linux systems.
- Adjust permissions accordingly if you encounter issues with SMART status checks.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bugs.

## Contact

For any questions or support, please contact the project maintainer.