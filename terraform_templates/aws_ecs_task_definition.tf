resource "aws_ecs_task_definition" "erag_task_def_{{ resource_name }}" {{
  family                   = "erag_task_def_{{ resource_name }}"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "1024"
  memory                   = "8192"

  #   execution_role_arn      = "arn:aws:iam::471112747221:user/narendra"
  execution_role_arn = "arn:aws:iam::471112747221:role/ecsTaskExecutionRole"
  task_role_arn      = "arn:aws:iam::471112747221:role/ecsTaskExecutionRole"


  container_definitions = jsonencode([
    {{
      name      = "{{ resource_name }}"
      image     = "{{ container_image }}"
      essential = true
      
      portMappings = [
        {{
          containerPort = {{ host_port }} # First port for the container (TCP)
          protocol      = "tcp"
          hostPort={{ host_port }}
          name="{{ resource_name }}"
          appProtocol = "http"# Application protocol for the port
        }}
        
      ]
    }}
  ])
}}
