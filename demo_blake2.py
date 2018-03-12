

doc = """
    
    demo_blake2.py  --  version 1
    
    
    this runs under Python 2.7 and Python 3.3.
    
    see blake2.py's README for more information.
    
    Notes:
        1- printed output prefixed with:
             ??? is the result of blake2.py
             >>> is the result of blake2x-ref.c
           they should agree.

    -----
    
    License:

      Copyright (c) 2009-2018 Larry Bugbee, Kent, WA, USA

      Permission to use, copy, modify, and/or distribute this software 
      for any purpose with or without fee is hereby granted, provided 
      that the above copyright notice and this permission notice appear 
      in all copies.

      THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL 
      WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED 
      WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL 
      THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR 
      CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM 
      LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, 
      NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN 
      CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
      
        (the ISC license, a minor tweak of the BSD license)
    
    Enjoy,
        
    Larry Bugbee
    December 2013
    rev Mar 2018
    
"""

import sys, binascii, platform
from blake2 import BLAKE2b, BLAKE2s


#-----------------------------------------------------------------------

def print_compare_results(actual, expect):
    print('  ??? %s' % actual)
    print('  >>> %s' % expect)
    if actual != expect:
        print('         *** results do NOT agree ***')
    
#-----------------------------------------------------------------------

def demo_bfile(filename='blake2.py'):
    digest_size = 32
    
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        
    print('')
    print('BLAKE2b of %s (%d-byte digest) - bfile' % (filename, digest_size))
    
    data = open(filename, 'rb').read()
    print('  datalen: %d' % len(data))
    hexdigest = BLAKE2b(data, digest_size).hexdigest()
    
    print('  %s - %s' % (hexdigest, filename))


#-----------------------------------------------------------------------

def demo_b():
    data        = b'hello'
    digest_size = 64
    
    print('')
    print('BLAKE2b of %s (%d-byte digest) - b' % (data, digest_size))
    print('  datalen: %d' % len(data))
    
    b2 = BLAKE2b(digest_size=digest_size)
    b2.update(data)
    digest = b2.final()
    
    actual = binascii.hexlify(digest).decode()      # or b2.hexdigest()
    expect = ('e4cfa39a3d37be31c59609e807970799caa68a19bfaa15135f165085e01d41a6'
            + '5ba1e1b146aeb6bd0092b49eac214c103ccfa3a365954bbbe52f74a2b3620c94')
    print_compare_results(actual, expect)


#-----------------------------------------------------------------------

def demo_bk():
    data        = b'hello'
    key         = b'secret'
    digest_size = 64
    
    print('')
    print('BLAKE2b of %s w/key "%s" (%d-byte digest) - bk' % (data, key, digest_size))
    print('  datalen: %d' % len(data))
    
    b2 = BLAKE2b(digest_size=digest_size, key=key)
    b2.update(data)
    digest = b2.final()
    
    actual = binascii.hexlify(digest).decode()      # or b2.hexdigest()
    expect = ('6edf9aa44dfc7590de00fcfdbe2f0d917cdeeb170301416929cc625d19d24edc'
            + '1040ff760c1f9bb61ad439a0af5d492fbb01b46ed3feb4e6076383b7885a9486')
    print_compare_results(actual, expect)

#-----------------------------------------------------------------------

def demo_bksp():
    data        = b'hello'
    key         = b'secret'
    salt        = b"SALTy"
    person      = b"this is personal"
    digest_size = 64
    
    print('')
    print('BLAKE2b of %s w/key "%s" (%d-byte digest) - bksp' % (data, key, digest_size))
    print('  datalen: %d' % len(data))
    
    b2 = BLAKE2b(digest_size=digest_size, key=key, 
                                                 salt=salt, person=person)
    b2.update(data)
    digest = b2.final()
    
    actual = binascii.hexlify(digest).decode()      # or b2.hexdigest()
    expect = ('99e200174f8abe9ee0d4103fc5be406907d4c5a49fa670ad4cc4a932044bf435'
            + '04bce8f0bc3e8b3f7ece823ad433fe76e21208f7dea2deeaa0d32d0d14947035')
    print_compare_results(actual, expect)

#-----------------------------------------------------------------------

def demo_s():
    data        = b'hello'
    digest_size = 32
    
    print('')
    print('BLAKE2s of %s (%d-byte digest) - s' % (data, digest_size))
    print('  datalen: %d' % len(data))
    
    b2 = BLAKE2s(digest_size=digest_size)
    b2.update(data)
    digest = b2.final()
    
    print('  ??? %s' % binascii.hexlify(digest).decode())
    print('  >>> '
        + '19213bacc58dee6dbde3ceb9a47cbb330b3d86f8cca8997eb00be456f140ca25')

#-----------------------------------------------------------------------

def demo_sk():
    data        = b'hello'
    key         = b'secret'
    digest_size = 32
    
    print('')
    print('BLAKE2s of %s w/key "%s" (%d-byte digest) - sk' % (data, key, digest_size))
    print('  datalen: %d' % len(data))
    
    b2 = BLAKE2s(digest_size=digest_size, key=key)
    b2.update(data)
    digest = b2.final()
    
    print('  ??? %s' % binascii.hexlify(digest).decode())
    print('  >>> '
        + 'a9d4269517517303b7d086e51876ee881d315fab3fe9044e5e4c7e7cad7253be')

#-----------------------------------------------------------------------

def demo_sksp():
    data        = b'hello'
    key         = b'secret'
    salt        = b"SALTy"
    person      = b"personal"
    digest_size = 32
    
    print('')
    print('BLAKE2s of %s w/key "%s" (%d-byte digest) - sksp' % (data, key, digest_size))
    print('  datalen: %d' % len(data))
    
    b2 = BLAKE2s(digest_size=digest_size, key=key, 
                                                 salt=salt, person=person)
    b2.update(data)
    digest = b2.final()
    
    print('  salt = "%s",  person = "%s"' % (salt, person))
    print('  ??? %s' % binascii.hexlify(digest).decode())
    print('  >>> '
        + '55ece82d0647dcefd7d1af675c62fb25a2b2388e5e277d9728d0f1ab45ca9fb3')

#-----------------------------------------------------------------------

def demo_b2():
    data = b"""


The Gettysburg Address
Gettysburg, Pennsylvania
November 19, 1863


Four score and seven years ago our fathers brought forth on this
continent, a new nation, conceived in Liberty, and dedicated to the
proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation,
or any nation so conceived and so dedicated, can long endure. We are
met on a great battle-field of that war. We have come to dedicate a
portion of that field, as a final resting place for those who here
gave their lives that that nation might live. It is altogether fitting
and proper that we should do this.

But, in a larger sense, we can not dedicate -- we can not consecrate
-- we can not hallow -- this ground. The brave men, living and dead,
who struggled here, have consecrated it, far above our poor power to
add or detract. The world will little note, nor long remember what we
say here, but it can never forget what they did here. It is for us the
living, rather, to be dedicated here to the unfinished work which they
who fought here have thus far so nobly advanced. It is rather for us
to be here dedicated to the great task remaining before us -- that
from these honored dead we take increased devotion to that cause for
which they gave the last full measure of devotion -- that we here
highly resolve that these dead shall not have died in vain -- that
this nation, under God, shall have a new birth of freedom -- and that
government of the people, by the people, for the people, shall not
perish from the earth. 


                             -- Abraham Lincoln

"""
    digest_size = 64

    print('')
    print('BLAKE2b of %s (%d-byte digest) - b2' % ('Gettysburg Address', digest_size))
    print('  datalen: %d' % len(data))
    
    b2 = BLAKE2b(digest_size=digest_size)
    b2.update(data)
    digest = b2.final()
    
    actual = binascii.hexlify(digest).decode()      # or b2.hexdigest()
    expect = ('d1e31c4b3b68a12bf6df4a35b94feb2409ba8dd0b1a19ca0cb4aebce518ed8d5'
            + '2d860c22db39f297483eead5b4e8f2bda955da2b22eb08bcf4e3b047906a757f')
    print_compare_results(actual, expect)


#-----------------------------------------------------------------------

def demo_s2():
    data = b'hello world'
    
    print('')
    print('BLAKE2s of %s (%d-byte digest) - s2' % (b'hello world', 32))
    print('  datalen: %d' % len(data))
    
    digest = BLAKE2s(b'hello world').final()
    
    print('  ??? %s' % binascii.hexlify(digest).decode())
    print('  >>> '
        + '9aec6806794561107e594b1f6a8a6b0c92a0cba9acf5e5e93cca06f781813b0b')

#-----------------------------------------------------------------------

def demo_errs():
    data        = b'hello'
    key         = b'secret'
    salt        = b"SALTy"
    person      = b"personal"
    digest_size = 32
    
    print('')
    print('BLAKE2s of %s w/key "%s" (%d-byte digest) - errs' % (data, key, digest_size))
    print('  datalen: %d' % len(data))
    
    b2 = blake2.BLAKE2(digest_size=digest_size, key=key, 
                                                salt=salt, person=person)
    b2.update(data)
    digest = b2.final()
    
    print('  salt = "%s",  person = "%s"' % (salt, person))
    print('  ??? %s' % binascii.hexlify(digest).decode())
    print('  >>> '
        + '55ece82d0647dcefd7d1af675c62fb25a2b2388e5e277d9728d0f1ab45ca9fb3')

#-----------------------------------------------------------------------

def tree():    
    title = "Dimetry's tree hash example"
    print('')
    print(title)
    
    FANOUT = 2
    DEPTH = 2
    LEAF_SIZE = 4096
    INNER_SIZE = 64
    
    buf = bytearray(6000)
    
    # Left leaf
    h00 = BLAKE2b(buf[0:LEAF_SIZE], fanout=FANOUT, depth=DEPTH,
                  leaf_size=LEAF_SIZE, inner_size=INNER_SIZE,
                  node_offset=0, node_depth=0, last_node=False)
    h00_digest = h00.final()
    
    # Right leaf
    h01 = BLAKE2b(buf[LEAF_SIZE:], fanout=FANOUT, depth=DEPTH,
                  leaf_size=LEAF_SIZE, inner_size=INNER_SIZE,
                  node_offset=1, node_depth=0, last_node=True)
    h01_digest = h01.final()
    
    # Root node
    h10 = BLAKE2b(digest_size=32, fanout=FANOUT, depth=DEPTH,
                  leaf_size=LEAF_SIZE, inner_size=INNER_SIZE,
                  node_offset=0, node_depth=1, last_node=True)
    h10.update(h00_digest)
    h10.update(h01_digest)
    
    print('  ??? %s' % h10.hexdigest())
    print('  >>> '
        + '3ad2a9b37c6070e374c7a8c508fe20ca86b6ed54e286e93a0318e95e881db5aa')


#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

if __name__ == '__main__':

    print('')
    print(platform.python_version())

    if 1:
        # < 1blk
        demo_b()
        demo_bk()
        demo_bksp()
        demo_s()
        demo_sk()
        demo_sksp()

    if 1:
        # > 1blk
        demo_b2()
    #    demo_bfile()

    if 9:
        
        tree()
        
    if 0:
        # special
        demo_s2()
        demo_errs()
        pass
    
    print('')

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
