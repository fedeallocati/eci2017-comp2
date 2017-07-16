from subprocess import call

project_name = "eci2017-comp2"

def main():
	call(["pip", "install", "-r", "requirements.txt"])
	call(["python", "-m", "ipykernel", "install", "--user", "--name={}".format(project_name)])

if __name__ == "__main__":
	main()