class RemoteControl:
    def __init__(self):
        self._commands = {}
        self._last_command = None

    def set_command(self, button_name, command):
        self._commands[button_name] = command

    def press(self, button_name):
        command = self._commands.get(button_name)
        if command:
            command.execute()
            self._last_command = command
        else:
            print(f"No command assigned to {button_name}")

    def display_last_command(self):
        print(f"Last Command {self._last_command}")
