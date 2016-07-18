#!/usr/bin/env python

import time, tarfile, os, hashlib, multiprocessing

filesDir = '/samba'
tarDir = '/root'
processNum = 2

def md5Sum(fname):
    m = hashlib.md5()
    with open(fname) as f:
        while 1:
            data = f.read(4096)
            if len(data) == 0:
                break
            m.update(data)
    return m.hexdigest()

def findAllDir(filesDir, filesQueue):
    os.chdir(filesDir)
    for (root, dirs, files) in os.walk('.'):
        for i in files:
            fname = os.path.join(root, i)
            filesQueue.put(fname)

def func(filesQueue, lock, tar):
    tar = tarfile.open('%s/full_%s.tar.gz' % (tarDir, timer), 'w:gz')
    while not filesQueue.empty():
        fname = filesQueue.get()
        md5 = md5Sum(fname)
        md5Dict[fname] = md5
        with lock:
            tar.add('%s' % fname)
    tar.close()
    print 'pid:', os.getpid() 
    print md5Dict


def fullBackup():
   
    lock = multiprocessing.Lock()
    filesQueue = multiprocessing.Manager().Queue()
    findAllDir(filesDir, filesQueue)
    timer = time.strftime('%Y-%m-%d_%H-%M')
    tar = tarfile.open('%s/full_%s.tar.gz' % (tarDir, timer), 'w:gz')
    #func(filesQueue, lock, tar)
    process = [multiprocessing.Process(target=func, args=(filesQueue, lock, tar)) for i in range(processNum)]
    for i in process:
        i.start()
        i.join()
    tar.close()

def main():
    fullBackup()

if __name__ == "__main__":
    main()
