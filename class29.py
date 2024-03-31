import os
import argparse

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--file",required = True,help = "This is a input file option")
	parser.add_argument("-o","--output",default = "all",
	choices = ['name','surname', 'age', 'profession', 'all'],help="This is output format")
	args = parser.parse_args()
	filename = args.file
	output = args.output
	return filename,output

def get_contect(file):
	with open(file) as f:
		return f.readlines()

def create_person_dict(ml):
	dc = {}
	dc['name'] = ml[0]
	dc['surname'] = ml[1]
	dc['age'] = ml[2]
	dc['profession'] = ml[3]
	return dc

def create_people_list(content):
	peoples = []
	for line in content:
		person = line.strip().split()
		peoples.append(create_person_dict(person))
	return peoples

def print_based_on_category(plist,cat):
	data = [people[cat] for people in plist]
	for cat in data:
		print(cat)
def print_people_data(plist):
	for people in plist:
		print("{")
		print("\t\"name:\" %s," %people["name"])
		print("\t\"surname:\" %s," %people["surname"])
		print("\t\"age:\" %s," %people["age"])
		print("\t\"profession:\" %s," %people["profession"])
		print("}")

def main():
	fname,out = get_arguments()
	cnt = get_contect(fname)
	peoples = create_people_list(cnt)
	if out == 'all':
		print_people_data(peoples)
	else:
		print_based_on_category(peoples,out)
if __name__ == '__main__':
	main()


