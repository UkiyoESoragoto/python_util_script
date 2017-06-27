#! /usr/bin/env python
# coding=utf-8
import os
import hashlib
import time

def getmd5( filename ):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    file = open( filename, 'rb' )
    while True:
        b = file.read(1024 * 1024)
        if not b:
            break
        myhash.update(b)
    file.close()
    return myhash.hexdigest()

def delfile(flist_temp):
  dellist = []
  flist = []
  fsize = []

  for f in flist_temp:
    if os.path.isfile( f ):
      fsize.append( os.stat(f).st_size )
      flist.append( f )

  for i in range( len(fsize) ):
    for j in range( i+1, len(fsize) ):
      if fsize[i] == fsize[j]:
        if getmd5( flist[i] ) == getmd5( flist[j] ):
          dellist.append( flist[i] )
          break

  return dellist

def main():
  '''
  delete all iterate file
  include file in subfolders
  '''
  print('Start ...\n')
  start = time.clock()
  path = os.getcwd()
  list_fn = []
  for i in os.walk(path):
    for fn in i[-1]:
      full_path = os.path.join( i[0],fn )
      list_fn.append( full_path )

  list_fn.reverse()
  print('file count:\t',len( list_fn ),'\n')
  delf = delfile( list_fn )
  for f in delf:
    print('delete\t',f)
    #os.remove( f )
  end = time.clock()
  print('\ncount:\t',len( list_fn ),'\n')
  print('delete:\t',len( delf ),'\n')
  print('time:\t',end-start,'\n')
  #os.remove('delReFile.py')
  # time.sleep(30)
  return 0


if __name__ == '__main__':
  main()
