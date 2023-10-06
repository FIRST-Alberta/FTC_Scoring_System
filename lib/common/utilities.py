from subprocess import CompletedProcess, run, CalledProcessError, TimeoutExpired


def Run_Cmd(cmd: str, timeout:int=5) -> str:
    try:
        output = run(cmd,
                     capture_output=True,
                     check=True,
                     shell=True,
                     timeout=timeout)
    except CalledProcessError as e:
        print("An exception occurred while attempting to run: {}"
              "Return Code: {}"
              "STDOUT: {}"
              "STDERR: {}".format(e.cmd, e.returncode, e.stdout, e.stderr))
    except TimeoutExpired as e:
        print("A timeout occurred while attempting to run: {}"
              "STDOUT: {}"
              "STDERR: {}".format(e.cmd, e.stdout, e.stderr))
        return None
    else:
        return output.stdout.decode()

def Get_Server_Name(ip : bool=False):
    name = Run_Cmd("hostname")
    if name:
        return name.strip() + ".local"
