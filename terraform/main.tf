resource "aws_instance" "app_instance" {
  ami           = "ami-0d5d9d301c853a04a"
  instance_type = var.instance_type
  key_name      = var.key_name
  user_data     = file("${path.module}/user_data.sh")

  provisioner "file" {
    source      = "${path.module}/docker-compose.yml"
    destination = "/tmp/docker-compose.yml"
  }

  tags = {
    Name = "DevOpsAssignmentInstance"
  }
}
