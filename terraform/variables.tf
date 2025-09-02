#AWS Region

variable "aws_region" {
    description = "AWS region"
    default = "us-east-1"
}


#EC2 instance

variable "instance_type" {
    description = "EC2 Instance type"
    default = "t2.micro"
}


#Name of existing key value pair in AWS

variable "key_name" {
    description = "AWS Key Pair name"
    type = string
}


# DockerHub credentials
variable "dockerhub_username" {
  description = "DockerHub username"
  type        = string
}

variable "dockerhub_password" {
  description = "DockerHub password"
  type        = string
  sensitive   = true
}
