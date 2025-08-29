file1=open("sample.txt",'r')
print("---Reading file content---")
line1=file1.readline()
line2=file1.readline()
print(f"line1: {line1}")
print(f"line2: {line2}")
file1.close()

try:
    file1=open("sample.txt",'r')
except FileNotFoundError:
    print(" ERROR: The file sample.txt was not found.")