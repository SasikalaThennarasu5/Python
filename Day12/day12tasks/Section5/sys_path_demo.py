import sys
print('Before:', sys.path)
sys.path.append('/custom/path/to/modules')
print('After:', sys.path)
