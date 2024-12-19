from flask import Blueprint, Response
from flask_cors import CORS

from utils import get_directory_path, get_output_path, process_template, read_config

apis = Blueprint('create', __name__)
CORS(apis)  # Enable CORS for the blueprint

@apis.route('/create_files')
def create_script():
    config = read_config('config.json')
    template_dir = config['template_dir']
    output_dir = config['output_dir']
    variables = {
        'resource_name': 'value1',
        'resource_clean_name': 'value2',
        'host_port': '8080',
        'container_image': 'xyz.com',
    }

    # Read template from the templates directory
    template_path = get_directory_path(template_dir, 'aws_lb_target_group.tf')
    final_script_path = get_output_path(output_dir, 'final_aws_lb_target_group.tf')
    # Process template
    output_filename = generate_terraform_script(template_path, final_script_path, variables)

    # Read template from the templates directory
    template_path = get_directory_path(template_dir, 'aws_ecs_task_definition.tf')
    final_script_path = get_output_path(output_dir, 'final_aws_ecs_task_definition.tf')
    # Process template
    output_filename = generate_terraform_script(template_path, final_script_path, variables)

    # Execute terraform script
    # output = execute_terraform_script(final_script_path)
    # print(output)
    return Response('Terraform files created', status=200, mimetype='application/json')

def generate_terraform_script(template_path, final_script_path, variables):
    # Process template
    output_filename = process_template(template_path, final_script_path, variables)
    print(f'Terraform script generated at {output_filename})')
    return final_script_path
