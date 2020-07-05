import subprocess

try:
    print(f'python run_binary_preprocessing.py "BBNI.JK" "20" "50"')
    subprocess.call(f'python run_binary_preprocessing.py  "BBNI.JK" "20" "50" ', shell=True)

    print(f'python generatedata.py "dataset" "20_50/BBNI.JK" "dataset_BBNIJK_20_50" ')
    subprocess.call(f'python generatedata.py "dataset" "20_50/BBNI.JK" "dataset_BBNIJK_20_50" ', shell=True)

    print(f'python myDeepCNN.py "-i" "dataset/dataset_BBNIJK_20_50" "-e" "50" "-d" "50" "-b" "8" "-o" "outputresult.txt"')
    subprocess.call(f'python myDeepCNN.py "-i" "dataset/dataset_BBNIJK_20_50" "-e" "50" "-d" "50" "-b" "8" "-o" "outputresult.txt"', shell=True)
except Exception as identifier:
    print(identifier)