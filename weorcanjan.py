"""
A Python script that saves and restores sessions of applications.

This script can be used to save the current running applications that are currently
running and then restore them at a later time.
This can be useful for quickly
returning to a specific work environment, or for troubleshooting problems
with applications.

The script supports the following commands:

* `save`: Saves the state of all the currently running applications.

* `restore`: Restores the state of the applications from the saved session.

* `create-test-session`: Creates a test session file with a list of applications.

* `restore-test-session`: Restores the state of the applications from the
test session file.
"""

# core
import argparse
from itertools import chain
import os
import pathlib
# from pprint import pprint
import pprint
import platform
import psutil
import subprocess
import typing
# user land
import questionary
# local-res
from res.ignored_process_list import IGNORE_LIST

"""
too complicated:-
python -m pip install --upgrade pywin32
python -m pip install -U pywin32 pypiwi
"""


class Weorcanjan:
    """
    Main class to handle operation
    """

    # static class attributes
    DEFAULT_DATA_DIR_SEGMENT = "weorcanjan"
    DEFAULT_SESSION_SEGMENT = "saved-sessions"
    DEFAULT_EXTENSION = ".txt"
    # DEFAULT_SESSION_FILENAME = f"saved_session{DEFAULT_EXTENSION}"
    DEFAULT_TEST_SESSION_FILENAME = f"test_session{DEFAULT_EXTENSION}"
    DEFAULT_MYIGNORE_FILENAME = f"my_ignore{DEFAULT_EXTENSION}"
    DEFAULT_MANY_PROCESS = 190

    IGNORE_SET = set(IGNORE_LIST)

    SESSION_FILENAMES = {}

    @classmethod
    def new_session_factory(cls):
        pass

    @staticmethod
    def open_explorer(
        path: str
    ) -> None:
        subprocess.Popen(
            ["explorer.exe", path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    # todo(matt): optimise by storing as classy class class
    @staticmethod
    def get_data_path(
        *paths: typing.Optional[str]
    ) -> str:
        return os.path.join(
            os.getenv("APPDATA"),
            Weorcanjan.DEFAULT_DATA_DIR_SEGMENT,
            *paths
        )

    # use the questionary to put to ignore
    @staticmethod
    def merge_user_ignore(
        myignore_filename: str = DEFAULT_MYIGNORE_FILENAME
    ) -> None:

        # get expected my ignore file name
        my_ignore_path = Weorcanjan.get_data_path(myignore_filename)

        # merge in the users choices that are not part of the repository
        if os.path.exists(my_ignore_path):
            print("Found user my ignore list")

            with open(my_ignore_path) as f:
                for process in f.read().splitlines():
                    if tuple(process) not in Weorcanjan.IGNORE_SET:
                        Weorcanjan.IGNORE_SET.add(process)

            print("Completed merge of user ignore script")
            print("--> merged list:")
            pprint.pprint(Weorcanjan.IGNORE_SET)
            print("")
        else:
            print("")
            print("Could not find user ignore list..")
            print("")

    @staticmethod
    def get_number_of_processes() -> int:
        """
        Gets the number of processes that are running on Windows.

        This function uses the `psutil` library to get a list of all the processes that
        are currently running on Windows. It then iterates over the list of processes
        and counts the number of processes that have a name. The number of processes
        with a name is returned as the result of the function.

        Returns:
            int: The number of processes that are running on Windows.
        """
        processes = psutil.process_iter(["name"])
        number_of_processes = 0
        for process in processes:
            try:
                name = process.info["name"]  # noqa
                if name:
                    number_of_processes += 1
            except psutil.Error:
                pass
        return number_of_processes

    @staticmethod
    def ensure_data_dir() -> None:
        # Get the path to the saved session's directory.
        saved_sessions_dir = Weorcanjan.get_data_path(
            Weorcanjan.DEFAULT_SESSION_SEGMENT
        )

        if False is os.path.isdir(saved_sessions_dir):
            (pathlib.Path(saved_sessions_dir)
             .mkdir(parents=True, exist_ok=True))

    @staticmethod
    def create_test_session() -> None:
        """
        Creates a test session file with a list of applications.

        This function creates a test session file in the user's `APPDATA` directory. The
        file contains a list of the applications that are currently running. The
        function checks if Chrome and Firefox are running, and if so, it adds them
        to the list. If no applications are running, the function prints an error
        message and exits.

        Returns:
            None: None.
        """

        # Get the path to the saved session's directory.
        saved_sessions_dir = Weorcanjan.get_data_path(
            Weorcanjan.DEFAULT_SESSION_SEGMENT
        )

        Weorcanjan.ensure_data_dir()

        chrome_path = None
        firefox_path = None

        for process in psutil.process_iter([
            "name",
            "cmdline"
        ]):
            try:
                name = process.info["name"]  # noqa
                cmdline = process.info["cmdline"]  # noqa
                print(f"name: {name}")
                print(f"cmdline: {cmdline}")
                print("")
                if name == "chrome.exe":
                    print("Found Chrome running")
                    chrome_path = cmdline[0]
                if name == "firefox.exe":
                    print("Found Firefox running")
                    firefox_path = cmdline[0]
            except psutil.Error as psutil_err:
                print(psutil_err)

        if None is chrome_path and None is firefox_path:
            print("You must run either chrome and/or firefox for this to work")
            exit(1)

        # Create the test session file.
        with open(Weorcanjan.get_data_path(
            Weorcanjan.DEFAULT_TEST_SESSION_FILENAME
        ), "w") as f:
            if chrome_path:
                f.write(chrome_path + "\n")
            if firefox_path:
                f.write(firefox_path + "\n")

    @staticmethod
    def save_session(
        session_filename: str = typing.Union[str, None]
    ) -> None:
        """
        Saves the state of all the open applications.

        This function gets a list of all the processes for the current user, and then
        creates a set of open applications. The function then asks the user which
        applications they want to save, and saves the list of applications to a file.

        Args:
            session_filename: The name of the session to save. Defaults
            to `TEST_SESSION_FILENAME`.

        Returns:
            None: None.
        """

        assert None is not session_filename

        # Get a list of all the processes for the current user.
        processes = psutil.process_iter([
            "username",
            "name",
            "cmdline"
        ])

        # Create a set of open applications.
        open_applications = set()

        print("type")
        print(Weorcanjan.IGNORE_SET)

        for process in processes:
            try:
                name = process.info["name"]  # noqa
                cmdline = process.info["cmdline"]  # noqa
                if cmdline and tuple(cmdline) not in Weorcanjan.IGNORE_SET:
                    open_applications.add(cmdline[0])
            except psutil.Error as psutil_err:
                print(psutil_err)

        saved_sessions_dir = Weorcanjan.get_data_path()
        saved_sessions_filename = Weorcanjan.get_data_path(session_filename)

        Weorcanjan.ensure_data_dir()

        # questionary.select(
        #     "What do you want to do?",
        #     choices=[
        #         'Order a pizza',
        #         'Make a reservation',
        #         'Ask for opening hours'
        #     ]).ask()  # returns value of selection

        # Get the list of applications that the user wants to save.
        applications = []
        for app in open_applications:
            print(app)
            response = input("Do you want to save " + app + "? (y/n): ")
            if response == "y":
                applications.append(app)
            else:
                print(f"Omitted {app}")

        if len(applications) == 0:
            print("Nothing to do... exiting")
            exit(0)

        # Save the list of open applications to a file.
        with open(saved_sessions_filename, "w") as f:
            for app in applications:
                f.write(app + "\n")

    @staticmethod
    def restore_session(
        session_filename: str = typing.Union[str, None]
    ) -> None:
        """
        Restores the state of all the applications from the saved session.

        This function gets the list of saved applications from a file, and
        then restores the state of each application.

        Args:
            session_filename: The name of the session to restore. Defaults
            to `SESSION_DEFAULT_FILENAME`.

        Returns:
            None: None.
        """
        assert None is not session_filename

        session_filename = Weorcanjan.get_data_path(session_filename)

        # Get the list of saved applications from the file.
        with open(session_filename, "r") as f:
            apps = f.read().splitlines()

        # Restore the state of each application.
        for cmdline in apps:
            # Try to restore the application.
            try:
                subprocess.Popen(cmdline)
            except Exception as popen_err:
                print("Failed to restore application: " + cmdline)
                print(popen_err)

    @staticmethod
    def guard_invocation() -> None:
        # Check if the script is running in cmd.exe.
        # current_process = psutil.Process()
        # if current_process.name() != "cmd.exe":
        #     print("This script must be run in cmd.exe.")
        #     exit()

        # print("**WARNING** PLEASE DO NOT USE THIS UNLESS YOU UNDERSTAND WHAT EACH "
        #      "PROCESS IS ON YOUR MACHINE")

        # response = input("Continue? (y/n): ")
        # if "y" != response:
        #     print("Exiting...")
        #     exit(1)

        print("")
        num_of_process = Weorcanjan.get_number_of_processes()
        print(f"You have: {num_of_process} process running...")
        if num_of_process > Weorcanjan.DEFAULT_MANY_PROCESS:
            print(
                f"Over {Weorcanjan.DEFAULT_MANY_PROCESS} processes, try to exempt "
                "with your own list to reduce questions")
            print("")

    @staticmethod
    def guard_win_ver(
        windows_versions: typing.Union[int, typing.Tuple[int]] = 10
    ) -> None:
        if platform.system() != "Windows":
            print("This script is only intended for Windows.")
            print("")
            exit()
        release_version = platform.release()
        print(f"Platform release version: {release_version}.")
        max_version_check = None
        if isinstance(windows_versions, int):
            max_version_check = windows_versions
        elif isinstance(windows_versions, tuple):
            max_version_check = windows_versions[-1]
        assert max_version_check
        print("check max version:")
        print(max_version_check)
        if release_version != max_version_check:
            print("")
            print("Tested only on Windows 10, should work on 11")
            print("")

    ARGDEF_METHOD_DICT = {
        "save_session": {
            "long": "save", "short": "s", "t": "cmd"
        },
        "restore_session": {
            "long": "restore", "short": "r", "t": "cmd"
        },
        "open_data_dir": {
            "long": "open-data-dir", "short": "odd", "t": "cmd"
        },
        "create_test_session": {
            "long": "create-test-session", "short": "cts", "t": "debug"
        },
        "restore_test_session": {
            "long": "restore-test-session", "short": "rts", "t": "debug"
        },
        "test_merge_user_ignore": {
            "long": "test-merge-user-ignore", "short": "tmui", "t": "debug"
        },
        "guard_win_ver": {
            "long": "guard-win-ver", "short": "gwv", "t": "debug"
        }
    }
    ARGDEF_METHOD_DICT.__doc__ = """
    Defines all valid commands actions to map to methods.
    """
    ARGDEF_ACTIONS = list(chain(*(map(list, ARGDEF_METHOD_DICT.keys()))))
    ARGDEF_ACTIONS.__doc__ = """
    Convenience list of all commands
    """
    ARGDEF_CMDS = [
        key
        for key, value in ARGDEF_METHOD_DICT.items()
        if value["t"] == "cmd"
    ]
    ARGDEF_DEBUGS = [
        key
        for key, value in ARGDEF_METHOD_DICT.items()
        if value["t"] == "debug"
    ]

    @staticmethod
    def main() -> None:
        # Set up the arguments for the script as command only style
        parser = argparse.ArgumentParser(
            description="""
            Saves and restores sessions of applications.
            Please note:-
            You need to understand if saving the arguments for a program is a good idea
            or not.
            For example... chrome its a bad idea, as the main Chrome process will spawn the others..
            Whereas for a application like a paint app you might have some args you want to start it with.
            """
        )

        parser.add_argument(
            "action",
            choices=Weorcanjan.ARGDEF_ACTIONS,
            help="""
                The action to perform. Currently save or restore.
                Must be combined with `--name`.
            """
        )

        # add not action arguments
        parser.add_argument(
            "--debug",
            action="store_true",
            help="""
                Enable DEBUG mode; this will print a lot more information.
            """
        )

        parser.add_argument(
            "--allow-win11", "-aw11",
            action="store_true",
            dest="enable_win11",
            help="""
                Enable unsupported Windows 11
            """
        )

        parser.add_argument(
            "--name", "-n",
            dest="session_name",
            help="""
            The filename for the session saved in appData/Roaming/weorcanjan.
            """
        )

        parser.add_argument(
            "--myignore", "-mi",
            dest="myignore",
            help=f"""
            Set your ignore name file in data directory.
            Defaults too: {Weorcanjan.DEFAULT_MYIGNORE_FILENAME}.
            If you don't supply extension I will.
            """
        )

        args = parser.parse_args()

        Weorcanjan.guard_win_ver(11 if args.enable_win11 else 10)

        if args.debug:
            print("all commands:")
            print(Weorcanjan.ARGDEF_ACTIONS)
            print("")

        print(f"Action: {args.action}")

        # I suppose it should be def for typing
        check_match = lambda argdef, arg: (  # noqa
            argdef["long"] == arg or
            argdef["short"] == arg
        )

        if args.action not in Weorcanjan.ARGDEF_ACTIONS:
            parser.print_help()

        # action is not debugging...
        # todo(matt): too many lists, we just need one hmmm
        elif args.action in Weorcanjan.ARGDEF_CMDS:

            Weorcanjan.guard_invocation()

            # match commands that don't require any args
            if check_match(Weorcanjan.ARGDEF_METHOD_DICT.get("open_data_dir"),
                           args.action):
                Weorcanjan.open_explorer(Weorcanjan.get_data_path())

            # functional commands

            # functional block means we can merge user ignore if its exists
            if None is args.myignore:
                print("Hint: you can supply your own filename for user ignore list "
                      "using --myignore")
            Weorcanjan.merge_user_ignore(args.myignore)

            if args.session_name:
                print(f"You are using session_name: {args.session_name}.txt")
            else:
                print(f"--name is required to use {args.action}")
                exit(1)

            if check_match(Weorcanjan.ARGDEF_METHOD_DICT.get("save_session"),
                           args.action):
                Weorcanjan.save_session(args.name)
            if check_match(Weorcanjan.ARGDEF_METHOD_DICT.get("restore_session"),
                           args.action):
                Weorcanjan.restore_session(args.session_name)

        # lazy debugging and testing
        elif args.action in Weorcanjan.ARGDEF_DEBUGS:
            if check_match(Weorcanjan.ARGDEF_METHOD_DICT.get("create_test_session"),
                           args.action):
                Weorcanjan.create_test_session()
            elif check_match(Weorcanjan.ARGDEF_METHOD_DICT.get("merge_user_ignore"),
                             args.action):
                Weorcanjan.merge_user_ignore()
            elif check_match(Weorcanjan.ARGDEF_METHOD_DICT.get("guard_win_ver"),
                             args.action):
                Weorcanjan.guard_win_ver()


if __name__ == "__main__":
    Weorcanjan().main()
