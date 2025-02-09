import os
import subprocess

from PySide6.QtCore import QRunnable, Slot, QSettings


class SSHWorker(QRunnable):
    @Slot()
    def run(self):
        if os.environ.get("LIBRECHAT_CONNECTOR_HOST") is None:
            raise RuntimeError(
                "LIBRECHAT_CONNECTOR_HOST environment variable is not set"
            )
        computer_name = os.environ.get("LIBRECHAT_CONNECTOR_HOST")

        # p = subprocess.run(
        #     ["tailscale", "status"], capture_output=True, encoding="utf-8"
        # )
        # assert p.returncode == 0
        # ip_addr = None
        # for line in p.stdout.split("\n"):
        #     chunks = line.split()
        #     if chunks[1] == computer_name:
        #         ip_addr = chunks[0]
        #         break

        # if ip_addr is None:
        #     raise RuntimeError(
        #         f"Could not determine IP address for computer name '{computer_name}'"
        #     )

        # print("ip = ", ip_addr)

        self._ssh = subprocess.Popen(
            f"ssh {computer_name} -L 3080:localhost:3080", shell=True
        )

    def stop(self):
        self._ssh.terminate()
