variable "aws_region" {
  description = "AWS Region"
  default     = "ap-south-1"  # Mumbai
}

variable "instance_type" {
  description = "EC2 Instance Type"
  default     = "t2.micro"
}

variable "key_name" {
  description = "EC2 Key Pair Name for SSH"
  type        = string
}

variable "public_ip" {
  description = "Assign public IP to EC2"
  type = bool

  default = true
}
