

doc = """
    
    bench_blake2.py  --  version 1
        
    see blake2.py's README for more information.
    
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
