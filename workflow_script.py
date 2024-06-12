import yaml
import platform

file_workflow_name_valid = 0
workflow_data_list = []
file_workflow_data = ""

system_info = platform.uname()
system = system_info.system
computer_name = system_info.node
os_release = system_info.release
os_version = system_info.version
os_machine = system_info.machine

while file_workflow_name_valid == 0:
    # file_name = input("Insira o caminho para o arquivo .yml do workflow: ")
    # job_name = input("Insira o nome do job que você quer testar: ")
    # step_name = input("Insira o nome do step que você quer testar: ")
    file_name = r"C:\Users\viara\OneDrive\PESSOAL\Documentos\code\githublocal\workflow.yml"
    job_name = "form-to-json"
    step_name = "Issue Forms Body Parser"

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        file_workflow_name_valid += 1
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist or can't be found.")
    except yaml.YAMLError as e:
        print(f"Erro parsin YAML file: {e}")

    for job in data["jobs"]:
        if job == job_name:
            if "steps" in data["jobs"][job]:
                for step_type in data["jobs"][job]["steps"]:
                    if step_type["name"] == step_name:
                        if "uses" in step_type:
                            if step_type["uses"] == "peter-evans/create-or-ipdate-comment@v1":
                                if f"""echo {step_type['with']['body']}""" not in workflow_data_list:
                                    workflow_data_list.append(f"echo {step_type['with']['body']}")
                            elif step_type["uses"] == "zentered/issue-forms-body-parser@v2.0.0":
                                print("This is not necessary because the code use the inputs of the html converted form to run your workflow.")
                            elif step_type["uses"] == "actions/checkout@v2":
                                print("You were checked out to the root of your repo.")
                        elif "run" in step_type:
                            if "gh" in step_type["run"]:
                                raise BaseException("We still cannot test this because it's a github cli command, we still working on this feature.")
                            elif "set-output" in step_type["run"]:
                                raise BaseException("We still cannot set a environment var on run, we still working on this feature.")
                            else:
                                if system.lower() == "windows":
                                    file_workflow_data += """
                                    @echo off
                                    setlocal
                                    """