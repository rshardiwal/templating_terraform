resource "aws_lb_target_group" "erag_tg_{{ resource_name }}" {{
  name        = "erag-target-{{ resource_clean_name }}"
  port        = {{ host_port }}             # Port where ECS container listens
  protocol    = "HTTP"            # Protocol used
  vpc_id      = aws_vpc.my_vpc.id # VPC where ECS tasks run
  target_type = "ip"              # Use "ip" for ECS tasks
  health_check {{
    healthy_threshold   = 3
    unhealthy_threshold = 3
    timeout             = 10
    interval            = 60
    protocol            = "HTTP"
    port                = {{ host_port }}
    path                = "/" # ECS health check path
  }}
  tags = {{
    Name = "erag-target-{{ resource_clean_name }}"
  }}
}}
