
    blake2.py  --  version 1, beta 1
    
    
    This 100% Python implementation of BLAKE2 supports both 
    BLAKE2b and BLAKE2s.  It runs under both Python 2.7 and 
    Python 3.3.
    
    Here a simple usage example:
        
        import blake2
        
        digest = blake2.BLAKE2b(b'hello world').digest()
    
    
    Another, generating a 20-byte digest (in hex):
        
        from blake2 import BLAKE2b
        
        data = b'hello world'
        b2 = BLAKE2b(digest_size=20)
        b2.update(data)
        hexdigest = b2.hexdigest()
    
    
    Credit is given to Dmitry Chestnykh <dmitry@codingrobots.com> 
    for his work defining a Python API for pyblake2 and his 
    excellent documentation of that interface.  Please see 
    http://pythonhosted.org/pyblake2/
    
    I have adoped much of Dmitry's API and many of his data 
    names.  Consider using blake2.py when you need a pure Python 
    implementation, and convert to Dmitry's pyblake2, with 
    hopefully minimum effort, when more speed is required.
    
    Here are a few known differences between blake2.py and 
    pyblake2.
    
      - capitalization of BLAKE2b and BLAKE2s class names
      
      - digest() is an alias for final()
      
      - under Python 2.7 the returned digest is a str; under 
        Python 3.3 the digest is a bytes object.  Neither is 
        a hash object.
      
      - hexdigest() returns a str under Pythons 2.7 and 3.3
      
      - http://pythonhosted.org/pyblake2/module.html#pyblake2.hash.digest
        says "Return the digest of the data so far." which 
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
        
        Arguably, a better approach would be to make a copy by 
        calling copy() and then call digest() or hexdigest() on 
        the copy, and resume hashing on the original.  
        
        Note: digest() and hexdigest() may be called multiple 
        times when finished hashing.  Each calls final(), but 
        final() performs the final compression only once.  
    
    
    Other notes:
      
      - All data, key, salt, and person inputs are big endian 
        bytes, NOT strings.  Likewise, the final digest is 
        big endian bytes.
        
      - blake2.py has been tested in sequential and tree modes; 
        it has NOT been tested in parallel mode.
        
      - blake2.py is not a secure implementation.  For example, 
        keys are NOT securely overwritten after use.  Use this 
        implementation on a presumably secure platform only.
    
    
    TODO:
        - test against KATs
        
    -----
    
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



