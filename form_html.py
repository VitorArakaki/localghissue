import yaml
file_form_name_valid = 0
file_form_data = ""

while file_form_name_valid ==0:
    file_name = input("Insira o caminho para o arquivo .yml do formulário: ")

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        file_form_name_valid += 1
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist or can't be found.")
    except yaml.YAMLError as e:
        print(f"Erro parsin YAML file: {e}")

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
            background-color: rgb(48, 41, 50);
        }
        h1 {
            width: 100%;
            text-align: start;
            color: white;
            font-size: 3vw;
        }
        h2 {
            width: 100%;
            text-align: start;
            color: white;
            font-size: 2.5;
        }
        h3 {
            width: 100%;
            text-align: start;
            color: white;
            font-size: 2.1vw;
        }
        .validator {
            color: red;
            margin-left: 5px;
        }
        .formTitle {
            width: 100%;
            text-align: start;
            color: white;
            font-weight: bold;
            margin-right: 20px;
            font-size: 2vw;
        }
        .labelText {
            padding: 5px;
            background-color: rgba(128, 0, 128, 0.438);
            border: 1px;
            border-width: 2px;
            border-color: transparent;
            border-radius: 20px;
            font-weight: bold;
            font-size: 1.3vw;
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
            width: 100%;
            justify-content: center;
            align-items:start;
        }
        .inputTitle {
            width: 100%;
            text-align: start;
            color: white;
            font-weight: bold;
            margin-right: 20px;
            font-size: 2vw;
        }
        .inputDescription {
            width: 100%;
            text-align: start;
            color: white;
            font-size: 1.5vw;
        }
        .inputField {
            width: 60%;
            height: 25px;
            font-size: 1.8vw;
            margin-top: 5px;
            border: 1px;
            border-color: grey;
            border-style: solid;
            border-radius: 5px;
            padding-left: 10px;
            padding-right: 10px;
            color: white;
            background-color: rgb(82, 70, 85);
            font-family: 'Courier New', Courier, monospace;
        }
        .inputField:placeholder {
            color: rgb(152, 151, 151);
            font-size: 1.8vw;
            font-family: 'Courier New', Courier, monospace;
        }
        .dependencies-textarea {
            width: 100%;
            justify-content: center;
            align-items: start;
        }
        .textareaTitle {
            width: 100%;
            text-align: start;
            color: white;
            font-weight: bold;
            margin-bottom: 20px;
            font-size: 2vw;
        }
        .textareaDescription {
            width: 100%;
            padding-top: 10px;
            text-align: start;
            color: white;
            font-size: 1.8vw;
        }
        .textareaSubDescription {
            width: 100%;
            text-align: start;
            color: white;
            font-size: 1.5vw
        }
        .textareaInput {
            width: 100%;
            height: 100px;
            font-size: 1.8px;
            margin-top: 5px;
            border: 1px;
            border-color: grey;
            border-style: solid;
            border-radius: 5px;
            padding-left: 10px;
            padding-right: 10px;
            color: white;
            background-color: rgb(82,70, 85);
            font-family: 'Courier New, Courier, monospace;
        }
        .textareaInput:placeholder {
            color: rgb(152, 151, 151);
            font-size: 1.8vw;
            font-family: 'Courier New, Courier, monospace;
        }
        .env-dropdown {
            width: 100%;
            justify-content: center;
            align-items: start;
        }
        .dropdownItems {
            height: 30px;
            font-size: 1.8vw;
            margin-top: 5px;
            border: 1px;
            border-color: grey;
            border-style: solid;
            border-radius: 5px;
            padding-left: 10px;
            padding-right: 10px;
            color: white;
            background-color: rgb(82, 70, 85);
        }
    </style>
"""

file_form_data = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{str(data["name"]).replace('<', '&lt;').replace('>', '&gt;')}</title>
    {style}
</head>
<body>
    <h1>{str(data['title']).replace('<', '&lt;').replace('>', '&gt;')}</h1>
    <div class="labelDiv">
        <span class="formTitle">{str(data["description"]).replace('<', '&lt;').replace('>', '&gt;')}</span>
        <span class="labelText">{str(data["labels"]).replace('<', '&lt;').replace('>', '&gt;')}</span>
    </div>
    <br />
    <div class="hrConfig" />
"""

for item in data["body"]:
    file_form_data += "<br />"
    if item["type"] == "input":
        file_form_data += f"""
        <div id="{item['id']}-{item['type']}" class="inputDiv">
            <span class="inputTitle">{str(item["attributes"]["label"]).replace('<', '&lt;').replace('>', '&gt;')}</span><br />
            <span class"inputDescription">{str(item["attributes"]["description"]).replace('<', '&lt;').replace('>', '&gt;')}</span><br /><br />
            <input class="inputField" placeholder="{str(item["attributes"]["placeholder"]).replace('<', '&lt;').replace('>', '&gt;')}"<span class="validator">*</span>
        </div>
        """
    elif item["type"] == "markdown":
        file_form_data += f"""
            <div id={item['type']}-{item["attributes"]["value"]}>
                {str(item["attributes"]["value"])}
            </div>
        """
    elif item["type"] == "textarea":
        file_form_data += f"""
            <div id="{item['id']}-{item['type']}">
                <span class="textareaTitle">{str(item["attributes"]["label"]).replace('<', '&lt;').replace('>', '&gt;')}</span><br /><br />
                <span class="textareaDescription">{str(item["description"]).replace('<', '&lt;').replace('>', '&gt;')}</span><br /><br />
                <span class="textareaSubDescription">{str(item["attributes"]["description"]).replace('<', '&lt;').replace('>', '&gt;')}</span>
                <textarea class="textareaInput" name="{item["id"]}" placeholder="{str(item["attributes"]["placeholder"]).replace('<', '&lt;').replace('>', '&gt;')}" rows="20" cols="80"></textarea>
            </div>
        """
    elif item["type"] == "dropdown":
        option = ""
        for value in item["attributes"]["options"]:
            option += f"""
                <option value="{str(value["value"])}">{str(value["label"]).replace('<', '&lt;').replace('>', '&gt;')}</option>
            """
        
        file_form_data += f"""
            <div id="{item['id']}-{item['type']}">
                <span class="inputTitle">{str(item["attributes"]["label"]).replace('<', '&lt;').replace('>', '&gt;')}</span><br />
                <span class="inputDescription">{str(item["attributes"]["description"]).replace('<', '&lt;').replace('>', '&gt;')}</span><br /><br />
                <select class="dropdownItems" name="{item["id"]}{str(item["attributes"]["label"]).replace('<', '&lt;').replace('>', '&gt;')}" id="{item["id"]}{str(item["attributes"]["description"]).replace('<', '&lt;').replace('>', '&gt;')}">
                {option}"
                </select><br /><br />
            </div>
        """

file_form_data += """
</body>
</html>
"""

with open(f"{str(file_name).replace('.yml', '')}.html", "w", encoding='utf-8') as file:
    file.write(file_form_data)

