# provider: aws
provider "aws" {
  access_key = "AKIAIHCEKOSFIC3GO4VA"
  secret_key = "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"
  region     = "ap-northeast-2"
}

# aws security group: sawtooth_sec
resource "aws_security_group" "sawtooth_secu" {
  name        = "sawtooth_secu"
  description = "sawtooth security group"
  
  #Allow ftp 
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
   
  #Allow remote access to transaction processor 
   ingress {
     from_port = 4004
     to_port = 4004
     protocol = "tcp"
     cidr_blocks = ["0.0.0.0/0"]
   }

  #Allow remote access to REST API
   ingress {
     from_port = 8008
     to_port = 8008
     protocol = "tcp"
     cidr_blocks = ["0.0.0.0/0"]
   }
  # Allow inbound traffic to other validators
   ingress {
    from_port   = 5500
    to_port     = 5500
    protocol    = "udp"
    cidr_blocks = ["0.0.0.0/0"]
  }

   # Allow inbound communication from other validators en clients
   ingress {
    from_port = 8800
    to_port = 8800
    protocol= "tcp"
    cidr_blocks = ["0.0.0.0/0"]
   }
   
   # Allow inbound http communiction
   ingress {
    from_port = 80
    to_port = 80
    protocol= "tcp"
    cidr_blocks = ["0.0.0.0/0"]
   } 

   # Allow inbound ssh communiction                             
   ingress {
    from_port = 22
    to_port = 22
    protocol= "tcp"
    cidr_blocks = ["0.0.0.0/0"]
   }

  
   # Allow outbound traffic to other validators
   egress {
    from_port = 5500
    to_port = 5500
    protocol = "udp"
    cidr_blocks = ["0.0.0.0/0"]
   }

   # Allow outbound communication to other validators and clients
   egress {
    from_port = 8800
    to_port = 8800
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
   }

   # Allow outbound http connection
   egress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

   # Allow outbound https connection (for git)
   egress {
     from_port   = 443
     to_port     = 443
     protocol    = "tcp"
     cidr_blocks = ["0.0.0.0/0"]
   }

  tags {
    Name = "sawtooth_sec"
  }
}

# EC2 Instance: sawtooth1 (Main instance --> includes Genesis block)
resource "aws_instance" "sawtooth1" {
    tags {
	Name = "sawtooth1"
    }
# Needs to be hvm-image
    ami = "ami-099f3667"

    instance_type = "t2.micro"

    root_block_device {
        volume_type = "gp2"
        volume_size = "100"
    }
    
    # Install and configure Sawtooth on first instance, including Genesis block (using script: installsawtooth.sh)
    provisioner "remote-exec" {
      script="installsawtooth.sh"
      connection {
        type     = "ssh"
        user     = "ubuntu"
        private_key = "${file("Sawtooth-Korea.pem")}"
      }
    }
    provisioner "local-exec" {
      command = "echo ${aws_instance.sawtooth1.public_ip} > sawtooth1.txt"
    }

    
    associate_public_ip_address = true
    private_ip="172.31.16.219"
    key_name = "Sawtooth-Korea"
    vpc_security_group_ids = ["${aws_security_group.sawtooth_secu.id}"]    
}


# EC2 Instance: sawtooth2
resource "aws_instance" "sawtooth2" {
    tags {
        Name = "sawtooth2"
    }
# Needs to be HVM-image
    ami = "ami-099f3667"

    instance_type = "t2.micro"

    root_block_device {
        volume_type = "gp2"
        volume_size = "100"
    }

    # Install and configure Sawtooth on second instance, without  Genesis block (using script: installsawtooth_noG.sh)
    provisioner "remote-exec" {
      script="installsawtooth_noG.sh"
      connection {
        type     = "ssh"
        user     = "ubuntu"
        private_key = "${file("Sawtooth-Korea.pem")}"
      }
    }
     provisioner "local-exec" {
      command = "echo ${aws_instance.sawtooth2.public_ip} > sawtooth2.txt"
    }

    associate_public_ip_address = true
    private_ip="172.31.29.97"
    key_name = "Sawtooth-Korea"
    vpc_security_group_ids = ["${aws_security_group.sawtooth_secu.id}"]
}

# EC2 Instance: sawtooth3
resource "aws_instance" "sawtooth3" {
    tags {
        Name = "sawtooth3"
    }
# Needs to be hvm-image
    ami = "ami-099f3667"

    instance_type = "t2.micro"

    root_block_device {
        volume_type = "gp2"
        volume_size = "100"
    }

    # Install and configure Sawtooth on third instance, without  Genesis block (using script: installsawtooth_noG.sh)
    provisioner "remote-exec" {
      script="installsawtooth_noG2.sh"
      connection {
        type     = "ssh"
        user     = "ubuntu"
        private_key = "${file("Sawtooth-Korea.pem")}"
      }
    }
     provisioner "local-exec" {
      command = "echo ${aws_instance.sawtooth3.public_ip} > sawtooth3.txt"
    }

    associate_public_ip_address = true
    private_ip="172.31.25.33"
    key_name = "Sawtooth-Korea"
    vpc_security_group_ids = ["${aws_security_group.sawtooth_secu.id}"]
}

