import subprocess
import json
import os

def read_template(template_path):
    with open(template_path, 'r') as file:
        return file.read()

def replace_placeholders(template_content, variables):
    for key, value in variables.items():
        template_content = template_content.replace(f'{{{{ {key} }}}}', value)
    return template_content

def write_final_script(final_script_path, content):
    with open(final_script_path, 'w') as file:
        file.write(content)

def execute_terraform_script(script_path):
    result = subprocess.run(['terraform', 'apply', '-auto-approve', script_path], capture_output=True, text=True)
    return result.stdout

def process_template(template_filename, output_filename, variables):
    template_content = read_template(template_filename)
    final_content = replace_placeholders(template_content, variables)
    write_final_script(output_filename, final_content)
    return output_filename

def read_config(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def get_directory_path(*paths):
  new_path = os.path.join(os.getcwd(), *paths)
  if not os.path.exists(new_path):
      raise FileNotFoundError(f"No such file or directory: '{new_path}'")
  return new_path

def get_output_path(*paths):
  return os.path.join(os.getcwd(), *paths)
