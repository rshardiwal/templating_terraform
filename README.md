## Things done

1. **Create Template**: Design terraform script templates with placeholders for variables. Store in `terraform_templates` but can be configured from `config.json`
2. **Read and Replace**: Read the templates and replace the placeholders variables with actual values.
3. **Write Final Scripts**: Write the final terraform scripts to a file. Write to `terraform_scripts` but can be configured from `config.json`
4. **Execute Scripts**: Execute the terraform scripts using the `terraform` command.
5. **Return Output**: Capture and return the output of the terraform execution.
