from distutils.core import setup
import py2exe

setup(
	console=['D:\gridster2\Desktop\LangMap\langmap.py'],
	data_files = [('maps', ['maps/europe_map.svg'])]
)