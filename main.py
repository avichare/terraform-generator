
#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import argparse

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input')
args = my_parser.parse_args()
architecture_name = args.input
#print(argument)
a = architecture_name
b = ".txt"
c = str(a + "" + b)

region =input("\nEnter the region: ")
instance_type =input("Enter instance_type:")
vpc_id =input("Enter vpc_id :")
subnet_id =input("Enter subnet_id :")
ami_id =input("Enter ami_id :")

#tier(argument)

def terraform_generator(architecture_name):
  print("This is " + architecture_name + " Architecture")
  template = env.get_template(c)
  output = template.render(region=region , instance_type=instance_type, vpc_id=vpc_id, subnet_id=subnet_id, ami_id=ami_id)
  print(output)

terraform_generator(architecture_name)


