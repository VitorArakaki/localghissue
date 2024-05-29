import yaml
import json

file_name_valid = 0
file_data = ""
# Prompt the user to enter the YAML file name
while file_name_valid == 0:
    file_name = input("Insira o caminho para o arquivo .yml do formulário: ")

    try:
        # Open the specified YAML file
        with open(file_name, 'r', encoding='utf-8') as file:
            # Load the contents of the file into a dictionary
            data = yaml.safe_load(file)
        file_name_valid += 1
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
style = """

    <style>
      body {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        font-family: Arial, sans-serif;
        overflow-y: scroll;
        overflow-x: hidden;
        height: 100%;
        background-color: rgb(36, 36, 36);
      }
      h1 {
        width: 100%;
        text-align: start;
        color: white;
      }
      .formTitle {
        width: 100%;
        text-align: start;
        color: white;
        font-weight: bold;
        margin-right: 20px;
        font-size: 120%;
      }
      .labelText {
        padding: 10px;
        background-color: rgba(128, 0, 128, 0.438);
        border: 1px;
        border-width: 2px;
        border-color: transparent;
        border-radius: 20px;
        font-weight: bold;
        font-size: 80%;
        color: white;
      }
      .labelDiv {
        width: 100%;
      }
      .hrConfig {
        width: 100%;
        height: 1px;
        background-color: white;
        margin-top: 2px;
        margin-bottom: 2px;
      }
      .inputDiv {
        display: flex;
        flex-direction: column;
        width: 100%;
        justify-content: center;
        align-items: start;
      }
      .inputTitle {
        width: 100%;
        text-align: start;
        color: white;
        font-weight: bold;
        margin-right: 20px;
        font-size: 120%;
      }
    </style>
"""

file_data = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <title>{data["name"]}</title>
  {style}
</head>
<body>
  <h1>{data["title"]}</h1>
  <div class="labelDiv">
      <span class="formTitle">{data["description"]}</span>
      <label class="labelText">{data["labels"]}</label>
</div>
<br />
<div class="hrConfig" />
"""

for item in data["body"]:
    print(item)
    file_data += "<br />"
    if item["type"] == "input":
        file_data += f"""
        <div id="{item["id"]}-{item["type"]} class="inputDiv"">
            <label class="inputTitle">{item["attributes"]["label"]}</label><br />
            <span>{item["attributes"]["description"]}</span><br />
            <input placeholder="{item["attributes"]["placeholder"]}" />****
        </div>
        """
    elif item["type"] == "markdown":
        file_data += f"""
        <div id="{item["type"]}-{item["attributes"]["value"]}">
            {item["attributes"]["value"]}
        </div>
        """
    elif item["type"] == "textarea":
        file_data += f"""
        <div id="{item["id"]}-{item["type"]}">
            <h2>{item["attributes"]["label"]}</h2><br />
            <h3>{item["description"]}</h3><br />
            <span>{item["attributes"]["description"]}</span><br />
            <textarea name="{item["attributes"]["placeholder"]}" rows="20" cols="80"></textarea>
        </div>
        """
    elif item["type"] == "dropdown":
        option = ""
        for value in item["attributes"]["options"]:
            option += f"""
                <option value="{value["value"]}">{value["label"]}</option>
            """

        file_data += f"""
        <div id="{item["id"]}-{item["type"]}">
            <label>{item["attributes"]["label"]}</label><br />
            <span>{item["attributes"]["description"]}</span><br />
            <select name="{item["id"]}{item["attributes"]["label"]}" id="{item["id"]}{item["attributes"]["description"]}">
            {option}
        </select>
        </div>
        """

file_data += """
</body>
</html>
"""

with open(f"{file_name.replace(".yml", "")}_test.html", 'w', encoding='utf-8') as file:
    file.write(file_data)