import os
os.environ['PYTHONPATH']=os.environ['PYTHONPATH']+":/opt/module/spark-3.5.2-bin-hadoop3/python/lib/pyspark.zip:/opt/module/spark-3.5.2-bin-hadoop3/python/lib/py4j-0.10.9.7-src.zip"
environ = os.environ
print(len(environ))
for k,v in environ.items():
    print(f"\033[1;31m{k}\033[0m",v)

print(os.environ['PYTHONPATH'])