import os
from shutil import copyfile
import sys


def cre8outputdir(pathdir, targetdir):
    # create folder output
    if not os.path.exists("{}/{}".format(pathdir, targetdir)):
        os.mkdir("{}/{}".format(pathdir, targetdir))

    if not os.path.exists("{}/{}/train".format(pathdir, targetdir)):
        os.mkdir("{}/{}/train".format(pathdir, targetdir))

    if not os.path.exists("{}/{}/test".format(pathdir, targetdir)):
        os.mkdir("{}/{}/test".format(pathdir, targetdir))

    if not os.path.exists("{}/{}/train/0".format(pathdir, targetdir)):
        os.mkdir("{}/{}/train/0".format(pathdir, targetdir))

    if not os.path.exists("{}/{}/train/1".format(pathdir, targetdir)):
        os.mkdir("{}/{}/train/1".format(pathdir, targetdir))

    if not os.path.exists("{}/{}/test/0".format(pathdir, targetdir)):
        os.mkdir("{}/{}/test/0".format(pathdir, targetdir))

    if not os.path.exists("{}/{}/test/1".format(pathdir, targetdir)):
        os.mkdir("{}/{}/test/1".format(pathdir, targetdir))


pathdir = sys.argv[1]
origindir = sys.argv[2]
targetdir = sys.argv[3]

cre8outputdir(pathdir, targetdir)

counttest = 0
counttrain = 0
for root, dirs, files in os.walk("{}/{}".format(pathdir, origindir)):
    for file in files:


        tmp = root.replace('\\','/')
        tmp_label = tmp.split('/')[-1]

        if tmp_label == '0':
            if 'test' in file:
                origin = "{}/{}".format(root, file)
                destination = "{}/{}/test/0/{}".format(
                    pathdir, targetdir, file)
                copyfile(origin, destination)
                counttest += 1
            elif 'train' in file:
                origin = "{}/{}".format(root, file)
                destination = "{}/{}/train/0/{}".format(
                    pathdir, targetdir, file)
                copyfile(origin, destination)
                counttrain += 1
        elif tmp_label == '1':
            if 'test' in file:
                origin = "{}/{}".format(root, file)
                destination = "{}/{}/test/1/{}".format(
                    pathdir, targetdir, file)
                copyfile(origin, destination)
                counttest += 1
            elif 'train' in file:
                origin = "{}/{}".format(root, file)
                destination = "{}/{}/train/1/{}".format(
                    pathdir, targetdir, file)
                copyfile(origin, destination)
                counttrain += 1

print(counttest)
print(counttrain)
