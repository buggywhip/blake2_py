
    blake2.py  --  version 1
    
    This pure Python implementation of BLAKE2 supports both 
    BLAKE2b and BLAKE2s.  It runs under both Python 2.7 and 
    Python 3.3.  For information about the BLAKE2 algorithm 
    please see https://blake2.net
    
    blake2.py differs from the structure of the C reference 
    version primarily by effecting classes (object orientation) 
    and certain optimizations in the area of compress() and 
    G().  The goal of these optimizations was to improve 
    performance, and while a gain of about 50% was attained, 
    this program is way too slow to be competitive with C 
    implementations.  This program can be useful, however, 
    where a pure Python implementation is required, where the 
    data to be hashed is small, and, of course, for educational 
    purposes.  
    
    Credit is given to Dmitry Chestnykh <dmitry@codingrobots.com> 
    for his work defining a Python API for pyblake2 and his 
    excellent documentation of that interface.  Please see 
    http://pythonhosted.org/pyblake2/  
    
    I have adoped much of Dmitry's API and many of his data 
    names.  Here are a few known differences between blake2.py 
    and pyblake2.
    
      - capitalization of BLAKE2b and BLAKE2s class names
      
      - digest() is an alias for final()
      
      - under Python 2.7 the returned digest is a str; under 
        Python 3.3 the digest is a bytes object.  Neither is 
        a pyblake2 hash object.
      
      - hexdigest() returns a str under Pythons 2.7 and 3.3
      
      - http://pythonhosted.org/pyblake2/module.html#pyblake2.hash.digest
        says "Return the digest of the data so far" which 
        implies hashing may be resumed after a digest is 
        retrieved at some arbitrary interim point.  What really 
        happens is that when final() is called, padding is 
        added (if needed), and a final compress is performed on 
        the last block.  An intermediate digest value will NOT 
        include a residual value left in the buffer (unless you 
        just happen to be on an exact multiple of BLOCKSIZE).  
        IMO, to resume hashing after "closing out" the state 
        should NOT be permitted, hence blake2.py will throw an 
        exception if resumption is attempted.  
        
        Arguably, a better approach would be to make a deepcopy 
        by calling copy() and then call digest() or hexdigest() 
        on the copy, and resume hashing on the original.  
        
      - digest() and hexdigest() may be called multiple times 
        when finished hashing.  Each calls final(), but final() 
        performs the final compression only once.  
    
    
    Other notes:
      
      - All data, key, salt, and person inputs are big endian 
        bytes, NOT strings.  Likewise, the final digest is 
        big endian bytes.
        
      - blake2.py has been tested in sequential and tree modes; 
        it has NOT been tested in parallel mode.
        
      - blake2.py is NOT a secure implementation.  For example, 
        keys are not securely overwritten after use.  Use this 
        implementation on a presumably secure platform only.
    
    
    Simple usage example:
        
        import blake2
        
        digest = blake2.BLAKE2b(b'hello world').digest()
    
    
    Another, generating a 20-byte digest (in hex):
        
        from blake2 import BLAKE2b
        
        data1 = b'hello '
        data2 = b'world'
        b2 = BLAKE2b(digest_size=20)
        b2.update(data1)
        b2.update(data2)
        hexdigest = b2.hexdigest()
    
            
    -----
    
    
    "miniServer" BLAKE2b thruput (OSX 2.53GHz Core2Duo):
       MiB/sec
        0.22  python 2.7, blake2.py v2
        0.36  python 3.3, blake2.py v2
        0.60  pypy 2.2 (python 2.7), blake2.py v2
        
        0.35  python 2.7, cythonized blake2.py v2
        0.59  python 3.3, cythonized blake2.py v2
        1.99  python 2.7, cython + some cdef unsigned long long
    
 >>>  301.01  python 2.7, Dmitry's pyblake2 wrapper  <<<

    "godspeed" BLAKE2b thruput (Ubuntu 12.4LTS 4.4GHz i5-3570K):
       MiB/sec
        0.72  python 2.7, blake2.py v2
        0.84  python 3.2, blake2.py v2
        0.96  pypy 2.2 (python 2.7), blake2.py v2
          
      ...still [very] slow.  :-/
    
    Consider using blake2.py when you need a pure Python 
    implementation, and convert to Dmitry's pyblake2, with 
    hopefully minimum effort, when more speed is required.
    
    -----
    
    This copyright and license may change for future 
    versions.  Until then...
    
      Copyright (c) 2013 by Larry Bugbee, Kent, WA
      ALL RIGHTS RESERVED.
      
      blake2.py IS EXPERIMENTAL SOFTWARE FOR EDUCATIONAL
      PURPOSES ONLY.  IT IS MADE AVAILABLE "AS-IS" WITHOUT 
      WARRANTY OR GUARANTEE OF ANY KIND.  USE SIGNIFIES 
      ACCEPTANCE OF ALL RISK.  
    
      To make your learning and experimentation less 
      cumbersome, blake2.py is free for any use.      
    
    
    Enjoy,
        
    Larry Bugbee
    December 2013
    rev Mar 2014



