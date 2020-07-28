from cx_Freeze import setup, Executable

def exe_creator(name, exe_name, script_file, version='1.0',
 description='Default description', pkg_list=[], icon=None):
	try:
		setup(name=name, version=version, author='José',
		description=description,
		options={'build_exe':{'packages':pkg_list}},
		executables=[Executable(script=script_file, 
		base=None, targetName=exe_name, icon=icon)])
	except Exception as e:
		return "ERROR: " + str(e)

if __name__ == '__main__':
	exe_creator('Fake Steam Key Generator', 'keygen.exe', 'key_generator.py',
		 description="A generator of fake keys, if you're (a bit) lucky\
		  you can activate something on Steam...", icon='vault_boy.ico',
		   pkg_list=['random', 'string', 'os'])