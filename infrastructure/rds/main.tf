provider "aws" {
    profile=var.profile
    region  = "eu-west-1"

}

resource "aws_db_instance" "default" {
    allocated_storage=20
    storage_type="gp2"
    engine = "postgres"
    instance_class = "db.t2.micro"
    name = "stamps_db"
    username = "postgres"
    password = var.password
    identifier = var.id
    skip_final_snapshot = true
    multi_az = true
    //final_snapshot_identifier = true
    vpc_security_group_ids =["sg-0ec9cca6916bec066"]
    publicly_accessible= true
    
}
