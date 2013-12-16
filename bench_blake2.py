

doc = """
    
    bench_blake2.py  --  version 1, beta 1
        
    Early "miniServer" (2.53GHz Core2Duo) results:
      no special optimizations while running with other apps
    
      BLAKE2s   CPython 2.7.3         1m    9.871 secs   1.0
      BLAKE2s   CPython 3.3.3         1m    5.742 secs   1.7x
      BLAKE2s   PyPy 2.0.2 (2.7.3)    1m    2.543 secs   3.9x
    

      BLAKE2b   CPython 2.7.3         1m    5.552 secs   1.0
      BLAKE2b   CPython 3.3.3         1m    3.714 secs   1.5x
      BLAKE2b   PyPy 2.0.2 (2.7.3)    1m    1.830 secs   3.0x
    
      BLAKE2b   CPython 2.7.3        25m  137.655 secs   1.0
      BLAKE2b   CPython 3.3.3        25m   93.269 secs   1.5x
      BLAKE2b   PyPy 2.0.2 (2.7.3)   25m   39.099 secs   3.5x
                              ...or about 640,000 bytes per second
    -----
    
    Early "godspeed" (4.4GHz i5-3570K) results:
      no special optimizations 

      BLAKE2b   CPython 2.7.3        25m   47.573 secs   1.0
      BLAKE2b   CPython 3.2.3        25m   39.361 secs   1.2x
      BLAKE2b   PyPy 2.0.2 (2.7.3)   25m   26.128 secs   1.8x
    
    -----
    
    *** AFTER G() optimizations (on miniServer) ***
      python2.7  BLAKE2b  1 MiB  4.254 secs  0.24 MiB per sec
      python3.3  BLAKE2b  1 MiB  2.719 secs  0.37 MiB per sec
      
      ...still slow.  :-/

    
    Enjoy,
        
    Larry Bugbee
    December 2013
    
"""

import time, binascii, platform
import blake2

#-----------------------------------------------------------------------

def bench2b(loops=1):
    mib = 2**20
    numbytes = mib
    text = b' '*numbytes
    
    print('')
    print('BLAKE2b hashing %s MiB' % (loops))
    
    mibs = mib * loops
    t0 = time.time()
    b2 = blake2.BLAKE2b()
    for i in range(loops):
        b2.update(text)
    digest = b2.final()
    t1 = time.time()
    
    print('  ??? %s' % binascii.hexlify(digest).decode())
    
    elapsed = t1-t0
    print('  time for %d MiB hashed: %.3f seconds' % (loops, elapsed))
    print('  hashed %.2f MiB per second' % (mibs/mib/elapsed))

#-----------------------------------------------------------------------

def bench2s(loops=1):
    mb = 1000 * 1000
    text = b' '*mb
    
    print('')
    print('BLAKE2s hashing %s MB' % (loops))
    
    t0 = time.time()
    b2 = blake2.BLAKE2s()
    for i in range(loops):
        b2.update(text)
    digest = b2.final()
    t1 = time.time()
    
    print('  ??? %s' % binascii.hexlify(digest).decode())
    
    elapsed = t1-t0
    print('  time for %d MB hashed: %.3f seconds' % (loops, elapsed))

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

if __name__ == '__main__':

    print('')
    print(platform.python_version())

    bench2b(1)

    if 0:
        bench2b(25)
    
    if 0:
        bench2s(1)
    
    print

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
