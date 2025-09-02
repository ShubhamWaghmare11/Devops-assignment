resource "aws_instance" "app_server" {
  ami                         = "ami-076a25afeba570620" 
  instance_type               = var.instance_type
  key_name                    = var.key_name
  associate_public_ip_address = var.public_ip

  user_data = file("user_data.sh")

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
