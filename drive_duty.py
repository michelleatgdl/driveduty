import os
import psutil
import platform
from datetime import datetime

class DriveDuty:
    def __init__(self):
        self.system = platform.system()

    def get_disk_partitions(self):
        partitions = psutil.disk_partitions(all=False)
        return partitions

    def get_disk_usage(self, partition):
        usage = psutil.disk_usage(partition.mountpoint)
        return usage

    def get_disk_io_counters(self):
        io_counters = psutil.disk_io_counters(perdisk=False)
        return io_counters

    def check_smart_status(self, device):
        if self.system == "Linux":
            try:
                result = os.popen(f"smartctl -H {device}").read()
                return "PASSED" in result
            except Exception as e:
                print(f"Error checking SMART status: {e}")
                return False
        else:
            print("SMART status check is only implemented for Linux.")
            return None

    def display_health_and_performance(self):
        print(f"System: {self.system}")
        for partition in self.get_disk_partitions():
            print(f"\nPartition: {partition.device}")
            usage = self.get_disk_usage(partition)
            print(f"  Total Size: {self._get_size(usage.total)}")
            print(f"  Used: {self._get_size(usage.used)} ({usage.percent}%)")
            print(f"  Free: {self._get_size(usage.free)}")

            if self.system == "Linux":
                smart_status = self.check_smart_status(partition.device)
                print(f"  SMART Status: {'PASSED' if smart_status else 'FAILED'}")

        io_counters = self.get_disk_io_counters()
        print("\nDisk IO Counters:")
        print(f"  Read Count: {io_counters.read_count}")
        print(f"  Write Count: {io_counters.write_count}")
        print(f"  Read Bytes: {self._get_size(io_counters.read_bytes)}")
        print(f"  Write Bytes: {self._get_size(io_counters.write_bytes)}")

    @staticmethod
    def _get_size(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

if __name__ == '__main__':
    drive_duty = DriveDuty()
    drive_duty.display_health_and_performance()