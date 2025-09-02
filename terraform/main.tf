resource "aws_security_group" "allow_ssh_http" {
  name        = "allow_ssh_http"
  description = "Allow SSH and port 8080"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # For testing; restrict to your IP if needed
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "app_server" {
  ami                    = "ami-076a25afeba570620" # ✅ Ubuntu 22.04 in ap-south-1
  instance_type          = var.instance_type
  key_name               = var.key_name
  user_data              = file("user_data.sh")
  vpc_security_group_ids = [aws_security_group.allow_ssh_http.id]

  tags = {
    Name = "Python-DevOps-App"
  }
}

output "public_ip" {
  value = aws_instance.app_server.public_ip
}

output "public_dns" {
  value = aws_instance.app_server.public_dns
}
