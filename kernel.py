class Process:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name

class Kernel:
    def __init__(self):
        self.processes = []
        self.next_pid = 1

    def create_process(self, name):
        process = Process(self.next_pid, name)
        self.processes.append(process)
        self.next_pid += 1
        return process

    def list_processes(self):
        return [(proc.pid, proc.name) for proc in self.processes]

    def kill_process(self, pid):
        self.processes = [proc for proc in self.processes if proc.pid != pid]

    def run_command(self, command):
        if command == "ls":
            return "\n".join([f"{proc.pid}: {proc.name}" for proc in self.processes])
        else:
            return "Unknown command."

# Example usage:
kernel = Kernel()
kernel.create_process("init")
kernel.create_process("shell")
print(kernel.run_command("ls"))
