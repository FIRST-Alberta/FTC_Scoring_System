from subprocess import CompletedProcess, run, CalledProcessError, TimeoutExpired
from tempfile import NamedTemporaryFile
from time import sleep


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
    
def Move_File_Contents_to_Remote_Host(file_contents: str, destination: str, host: str):
    """This function will:
        1. Write file contents to a temporary file on this machine.
        2. Copy that file to the home directory of the remote host.
        3. Move that file to the destination on the host.
    """
    with NamedTemporaryFile(mode="w+", delete=False) as tmp:
        file_name = tmp.name
        tmp.write(file_contents)
    print(file_name)
    print(file_contents)
    Run_Cmd("scp {} {}:~/{}".format(file_name, host, file_name.split("/")[1]))
    sleep(5)
    Run_Cmd("ssh {} 'sudo mv ~/{} {}'".format(host, file_name.split("/")[1], destination))
    sleep(5)
    Run_Cmd("ssh {} 'sudo chmod 644 {}'".format(host, destination))
    sleep(5)
    
