class MyFirstClass():
	"""my very MyFirstClass"""
	version=0.1
        def __init__(self,nm="Lyon"):
                """constructor"""
                self.name=nm
                print("Created a class instance for ",nm)

        def showname(self):
                """display instance attribute and class name"""
                print("Your name is ",self.name)
                print("My name is ",self.__class__.name)

        def showver(self):
                """display class version"""
                print("My version is ",self.version)
        def addMe2Me(self,x):
                """apply + operation to argument"""
                return x+x

