from urllib.request import urlopen
import json
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
    else:
        return output.stdout.decode()
    
def Load_JSON_From_URL(url: str) -> dict:
    response = urlopen(url)
    data = json.loads(response.read())
    if not data:
        print("Response from URL was empty! {}".format(url))
        return {}
    else:
        return data

def Get_Valid_Info(prompt: str, valid_responses: list):
    
    if not isinstance(valid_responses[0], str):
        tmp = []
        for x in valid_responses:
            tmp.append(str(x))
        valid_responses = tmp
    while True:
        response = input(prompt)
        if response in valid_responses:
            break
        else:
            print("{} is not a valid repsonse.".format(response))
    return response