# /data/data/com.termux/usr/bin/python2.7
# coding:utf8
#<--module-->
from uncompyle6.main import decompile as dc
from sys import stdout as st
from os import system as sis
import subprocess as sp
import re,time,sys,base64,zlib,marshal,random,os,dis,types,struct,marshal,binascii

#<--warna-->
G='\033[92m'
R='\033[91m'
P='\033[97m'
B='\033[90m'
C='\033[96m'
Y='\033[93m'

#<--waktu-->
USR=time.ctime().split(' ')

#<--logo-->
LOG="""
{}   ___      _    {} ___            _
{}  | _ ) ___| |_  {}|   \ ___ __ __| |_ _
{}  | _ \/ _ \  _| {}| |) / -_) _/ _` | '_|
{}  |___/\___/\__| {}|___/\___\__\__,_|_|
""".format(C,B,C,B,C,B,C,B)

#<--logo1-->
LOG1="""
{}        _                 _ _
{}   _  _| |__ _ _ _   __ _(_) |__ _  {} ,-+
{}  | || | / _` | '_| / _` | | / _` | {} .
{}   \_,_|_\__,_|_|   \__, |_|_\__,_| {}--'
{}                    |___/""".format(R,R,P,R,P,R,P,R)

#<--logo2-->
LOG2="""
{}  ___           _
{} | _ \_  _   __| |___ __ {} {}|\-"-/|
{} |  _/ || | / _` / -_) _|{} \({}o o{})/
{} |_|  \_, | \__,_\___\__|{}   | |
{}      |__/               {}  -{}|_|{}-
""".format(
   G,G,B,B,G,B,R,B,
   G,B,
   G,P,B,P,)

LOG3="""
{} ___      _   {}  ___
{}| _ ) ___| |_ {} |   \ ___ __
{}| _ \/ _ \  _|{} | |) / -_) _|
{}|___/\___/\__|{} |___/\___\__|

""".format(B,R,B,R,B,R,B,R)


#<--variable unmarshal--->

nmmek="""#!/usr/bin/env python
import sys
import dis
import time
import types
import struct
import marshal
import binascii

def show_hex(label, h, indent):
    h = binascii.hexlify(h)
    if len(h) < 60:
        print ("%s%s %s" % (indent, label, h))
    else:
        print ("%s%s" % (indent, label))
        for i in range(0, len(h), 60):
            print ("%s   %s" % (indent, h[i:i+60]))

def show_code(code, indent=''):
    print ("%scode" % indent)
    indent += '   '
    print ("%sargcount %d" % (indent, code.co_argcount))
    print ("%snlocals %d" % (indent, code.co_nlocals))
    print ("%sstacksize %d" % (indent, code.co_stacksize))
    print ("%sflags %04x" % (indent, code.co_flags))
    show_hex("code", code.co_code, indent=indent)
    dis.disassemble(code)
    print ("%sconsts" % indent)
    for const in code.co_consts:
        if type(const) == types.CodeType:
            show_code(const, indent+'   ')
        else:
            print ("   %s%r" % (indent, const))
    print ("%snames %r" % (indent, code.co_names))
    print ("%svarnames %r" % (indent, code.co_varnames))
    print ("%sfreevars %r" % (indent, code.co_freevars))
    print ("%scellvars %r" % (indent, code.co_cellvars))
    print ("%sfilename %r" % (indent, code.co_filename))
    print ("%sname %r" % (indent, code.co_name))
    print ("%sfirstlineno %d" % (indent, code.co_firstlineno))
    show_hex("lnotab", code.co_lnotab, indent=indent)

"""
#<--variabel unmarshal-->
gass="""
e = ''
i,j = (0,0)

while 1:
    if i >= len(d): break
    if j >= len(k): j = 0
    e += chr(d[i] ^ k[j])
    i += 1
    j += 1

show_code(marshal.loads(e))
"""

#<--animasi-->
def jalan(z):
    for j in z+'\n':
        sys.stdout.write(j)
        sys.stdout.flush()
        time.sleep(0.05)

#<--back to menu others-->
def bacot():
    m=raw_input('  {}[{}?{}] Back to menu [{}y{}/{}n{}]: '.format(P,G,P,G,P,R,P)).lower()
    if m=='y':others()
    else:sys.exit()

#<--back to menu dis -->
def backd():
    m=raw_input('  {}[{}?{}] Back to menu [{}y{}/{}n{}]: '.format(P,G,P,G,P,R,P)).lower()
    if m=='y':mdis()
    else:sys.exit()

#<--back to menu-->
def back():
    m=raw_input('  {}[{}?{}] Back to menu [{}y{}/{}n{}]: '.format(P,G,P,G,P,R,P)).lower()
    if m=='y':menu()
    else:sys.exit()

#<--animasi-->
def load(file):
    i=1
    for i in range(101):
        print "\r  {}[{}#{}] processin {}{} {}load {}{}% ".format(P,R,P,C,file,P,G,i),;sys.stdout.flush();time.sleep(0.05)
    print ""

#<--banner-->
def banner():
  print """  {}
  {}* {}version {}:{} v1.5
  {}* {}author  {}: Ikbal 154
  {}* {}date of {}: {}-{}-{}""".format(
   random.choice([LOG,LOG1,LOG2,LOG3]),
   B,G,P,Y,
   B,G,P,
   B,G,P,USR[2],USR[1],USR[4])

########################################################################################################
#             				OUTPUT MENU
########################################################################################################

def menus():
    print("""
   {}({}1{})-{}Unmarshal [{}Python{}({}2{},{}3{})]
   {}({}2{})-{}pyc to py
   {}({}3{})-{}unobfuscator [{}all{}]
   {}({}4{})-{}grab const [{}d,k{}]
   {}({}5{})-{}dec codece
   {}({}6{})-{}base64
   {}({}7{})-{}others [{}php{},{}html{},{}bash{}]
   {}({}0{})-{}keluar
   """.format(
   G,P,G,P,G,P,R,P,R,P,
   G,P,G,P,
   G,P,G,P,R,P,
   G,P,G,P,G,P,
   G,P,G,P,
   G,P,G,P,
   G,P,G,P,C,P,G,P,Y,P,
   G,R,G,P
   ))

########################################################################################################
#                                        OUTPUT M E N U
########################################################################################################

def menu():
    sis("clear")
    banner()
    menus()
    try:
       wk=raw_input(' {}[{}pilih{}]={}•{} '.format(G,P,G,R,P))
       if wk=='':menu()
       elif wk=='1':unmarshal()
       elif wk=='2':pyc()
       elif wk=='3':obfs()
       elif wk=='4':mdis()
       elif wk=='5':hex()
       elif wk=='6':base()
       elif wk=='7':others()
       elif wk=='0':sis('rm -rf /data/data/com.termux/files/.waktu/');sys.exit()
       else:menu()
    except (KeyboardInterrupt,EOFError):
       menu()
########################################################################################################
#                                      U N M A R S H A L 
########################################################################################################

def unmarshal():
    sis('clear')
    banner()
    print "\n  {}Ex{}:{}path/file.py\n".format(R,B,P)
    file=raw_input('  {}[{}file{}]={}: {}'.format(G,P,G,R,P))
    out=raw_input('  {}[{}outp{}]={}: {}'.format(G,P,G,R,P))
    jalan('  '+20*"-"+'{}[{}start{}]'.format(P,G,P))
    time.sleep(1)
    jalan('  {}[{}*{}] checkin filess ....'.format(P,G,P))
    try:
        q=open(file,'r').read()
        #<--checking file-->
        if len(q)==0:
	   time.sleep(1)
           print "  {}[{}!{}] file empty !!!".format(P,R,P)
           back()
        else:
            time.sleep(1)
            print "  {}[{}+{}] files found ..".format(P,G,P)
            time.sleep(1)
            sis('cp '+file+' /data/data/com.termux/files/.waktu/.se')
	    jlh=[] #<--total loping-->
	    lh=[]  #<--total decom-->
            def jejak():
		#<--data perulangan marsbas64-->
		    j=open('/data/data/com.termux/files/.waktu/.se','r').read()
		    if "print" in j or "sys.exit()" in j:
		#<--checking base64-->
	   	       for i in range(1,101):
                           who=time.time()
                           print "\r  {}[{}#{}] processin savening to {} {}{}% ".format(P,R,P,out,G,i),;sys.stdout.flush();time.sleep(0.005)
                       sis('mv /data/data/com.termux/files/.waktu/.se '+out)
                       print "\n  {}[{}*{}] succes save to: {}{}".format(P,G,P,C,out)
                       print "  {}[{}*{}] waiting time: {}{}".format(P,G,P,G,time.clock())
                       print "  {}[{}*{}] decompile loop:{} {}".format(P,G,P,G,jlh[len(jlh)-1])
                       if 'base64' in lh:
                           print "  {}[{}*{}] base64: {}{}".format(P,G,P,G,lh.count('base64'))
                       else:
                           print "  {}[{}*{}] base64: {}{}".format(P,R,P,R,lh.count('base64'))
                       if 'marshal py2' in lh:
                           print "  {}[{}*{}] mrshl2: {}{}".format(P,G,P,G,lh.count('marshal py2'))
                       else:
                           print "  {}[{}*{}] mrshl2: {}{}".format(P,R,P,R,lh.count('marshal py2'))
                       if 'marshal py3' in lh:
                           print "  {}[{}*{}] mrshl3: {}{}".format(P,G,P,G,lh.count('marshal py3'))
                       else:
                           print "  {}[{}*{}] mrshl3: {}{}".format(P,R,P,R,lh.count('marshal py3'))
                       back()
		    elif "exec base64.b" in j or "exec zlib.de" in j or "exec(base64" in j or "exec(zlib.d" in j:
		       bhk=open('/data/data/com.termux/files/.waktu/.se','r').read()
		       jrg=open('/data/data/com.termux/files/.waktu/.kanne','w')
		       jrg.write('import base64,zlib,marshal\n')
		       if "exec zlib.decompress(base64.b64decode(" in bhk or "exec zlib.decompress(base64.b32decode(" in bhk or "exec zlib.decompress(base64.b16decode(" in bhk or "exec(zlib.decompress(base64.b16decode(" in bhk or "exec(zlib.decompress(base64.b32decode(" in bhk or "exec(zlib.decompress(base64.b16decode(" in bhk or "exec(base64.base16decode(" in bhk or "exec base64.base16decode" in bhk or "exec base64.base32decode" in bhk or "exec(base64.base32decode" in bhk or "exec base64.base64decode" in bhk or "exec(base64.base64decode" in bhk  or "exec(zlib.decompress(" in bhk or "exec zlib.decompress(" in bhk:
			   if "exec(zlib.decompress(base64" in bhk or "exec(zlib.decompress(" in bhk:
                               jrg.write('print '+j[j.find('(zlib.de')-0:])
			   else:
			       jrg.write('print '+j[j.find('zlib.de')-0:])
		       else:
			   if "exec(base64.b64decode(" in bhk or "exec(base64.b32decode(" in bhk or "exec(base64.b16decode(" in bhk or "exec(base64.b16decode(" in bhk: 
			       jrg.write('print '+j[j.find('(base64.b')-0:])
			   else:
			       jrg.write('print '+j[j.find('base64.b')-0:])
		       jrg.close()
		       lh.append('base64')
		       os.system('python2 /data/data/com.termux/files/.waktu/.kanne > /data/data/com.termux/files/.waktu/.se')
		       jlh.append(len(jlh)+1)
		       jejak()
                    elif "exec(marshal.loads(zlib.decompress(base64.b64decode(" in j or "exec marshal.loads(zlib.decompress(base64.b64decode(" in j or "exec(marshal.loads(zlib.decompress(base64.b32decode(" in j or "exec marshal.loads(zlib.decompress(base64.b32decode(" in j or "exec(marshal.loads(zlib.decompress(base64.b16decode(" in j or "exec marshal.loads(zlib.decompress(base16.b64decode(" in j or "exec(marshal.loads(base64.b" in j or "exec marshal.loads(base64.b" in j or "exec(marshal.loads(b" in j or "exec marshal.loads(b" in j or "exec(marshal.loads(" in j or "exec marshal.loads(" in j:
		       fj=open('/data/data/com.termux/files/.waktu/.se','r').read()
		       if "exec(marshal.loads(" in j:
  		           b=fj[fj.find('(marshal.loads')-0:]
	               else:
	                   b=fj[fj.find('marshal.loads(')-0:]
                       d=open('/data/data/com.termux/files/.waktu/.kanne','w')
                       d.write('import marshal,base64,zlib\nfrom uncompyle6.main import decompile\nfrom sys import stdout\nx = '+b+'\n')
   	  	       bj=open('/data/data/com.termux/files/.waktu/.se','r').read()
		       if "marshal.loads(b'" in bj:
                           d.write('decompile(3.7,x,stdout)')
		       else:
		           d.write('decompile(2.7,x,stdout)')
                       d.close()
		       jo9=open('/data/data/com.termux/files/.waktu/.se','r').read()
		       if "marshal.loads('c" in jo9 or "marshal.loads(zlib" in jo9 or "marshaal.loads(base64" in jo9:
		           #<--un python2-->
                           os.system('python2 /data/data/com.termux/files/.waktu/.kanne > /data/data/com.termux/files/.waktu/.se')
		           lh.append('marshal py2')
		           jlh.append(len(jlh)+1)
			      
                       else:
		           #<--un python3-->
		           os.system('python3 /data/data/com.termux/files/.waktu/.kanne > /data/data/com.termux/files/.waktu/.se')
	                   jlh.append('marshal py3')
    	                   lh.append(len(jlh)+1)
		       jejak()
	            b=open("/data/data/com.termux/files/.waktu/.se",'r').read()
                    if 'os.system' in b or 'print' in b or 'if __name__' in b or 'try:' in b or 'except Exception as F:' in b or 'exception:' in b or 'elif' in b or 'else' in b or 'sys.exit()' in b or "import os" in b or "else:" in b:
                         for i in range(1,101):
                             print "\r  {}[{}#{}] processin savening to {} {}{}% ".format(P,R,P,out,G,i),;sys.stdout.flush();time.sleep(0.05)
                         sis('mv /data/data/com.termux/files/.waktu/.se '+out)
                         print "\n  {}[{}*{}] succes save to: {}{}".format(P,G,P,G,out)
                         print "  {}[{}*{}] waiting time: {}{}".format(P,G,P,G,time.clock())
                         
                         print "  {}[{}*{}] decompile loop:{} {}".format(P,G,P,G,jlh[len(jlh)])
                       
                         if 'base64' in lh:
                             print "  {}[{}*{}] base64: {}{}".format(P,G,P,G,lh.count('base64'))
                         else:
                             print "  {}[{}*{}] base64: {}{}".format(P,R,P,R,lh.count('base64'))
                         if 'marshal py2' in lh: 
                             print "  {}[{}*{}] mrshl2: {}{}".format(P,G,P,G,lh.count('marshal py2'))
                         else:
                             print "  {}[{}*{}] mrshl2: {}{}".format(P,R,P,R,lh.count('marshal py2'))
                         if 'marshal py3' in lh:
                             print "  {}[{}*{}] mrshl3: {}{}".format(P,G,P,G,lh.count('marshal py3'))
	                 else:
                             print "  {}[{}*{}] mrshl3: {}{}".format(P,R,P,R,lh.count('marshal py3'))
		         back()
                    elif 'exec(marshal.loads(zlib.decompress(base64' in b or 'exec marshal.loads(zlib.decompress(base64' in b:
			 jejak()
 		    elif 'exec(marshal.loads(zlib.decompress(' in b or 'exec marshal.loads(zlib.decompress(' in b:
		 	 jejak()
   		    elif 'exec(marshal.loads(b' in b or 'exec marshal.loads(b' in b:
			 jejak()
		    elif "exec marshal.loads('c" in b or "exec marshal.loads('c" in b: 
			 jejak()
		    elif 'exec base64.b' in b or 'exec zlib.de' in b or "exec(base64.b" in b or "exec(zlib.de" in b:
                         jejak()
		    else:
		#<--output-->
                       for i in range(1,101):
			   who=time.time()
                           print "\r  {}[{}#{}] processin savening to {} {}{}% ".format(P,R,P,out,G,i),;sys.stdout.flush();time.sleep(0.010)
  		       sis('mv /data/data/com.termux/files/.waktu/.se '+out)
                       print "\n  {}[{}*{}] succes save to: {}{}".format(P,G,P,C,out)
                       print "  {}[{}*{}] waiting time: {}{}".format(P,G,P,G,time.clock())
                       print "  {}[{}*{}] decompile loop:{} {}".format(P,G,P,G,jlh[len(jlh)-1])
		       if 'base64' in lh:
                           print "  {}[{}*{}] base64: {}{}".format(P,G,P,G,lh.count('base64'))
                       else:
                           print "  {}[{}*{}] base64: {}{}".format(P,R,P,R,lh.count('base64'))
                       if 'marshal py2' in lh:
                           print "  {}[{}*{}] mrshl2: {}{}".format(P,G,P,G,lh.count('marshal py2'))
                       else:
                           print "  {}[{}*{}] mrshl2: {}{}".format(P,R,P,R,lh.count('marshal py2'))
                       if 'marshal py3' in lh:
                           print "  {}[{}*{}] mrshl3: {}{}".format(P,G,P,G,lh.count('marshal py3'))
                       else:
                           print "  {}[{}*{}] mrshl3: {}{}".format(P,R,P,R,lh.count('marshal py3'))
		       back()

            jejak()
    except KeyboardInterrupt:
         print '  {}[{}!{}] Keyboard interupt !!!'.format(P,R,P)
         back()
    except IOError:
        time.sleep(1)
        print '  {}[{}!{}]{} {} {}no suc file or dictonary'.format(P,R,P,R,file,P)
        back()

########################################################################################################
# 				UN CO MPYLE6
########################################################################################################

def pyc():
    try:
       sis('clear')
       banner()
       print "\n  {}Ex{}:{}path/file.pyc\n".format(R,B,P)
       fle=raw_input('  {}[{}file{}]={}: {}'.format(G,P,G,R,P))
       out=raw_input('  {}[{}outp{}]={}: {}'.format(G,P,G,R,P))
       jalan('  '+20*"-"+'{}[{}start{}]'.format(P,G,P))
       sis('cp '+fle+' nak.pyc')
       file='nak.pyc'
       h=open(file,'r').read()
    #<--check file-->
       if len(h)==0:
          time.sleep(1)
          print "  {}[{}!{}] file empty !!!".format(P,R,P)
          back()
       else:
          time.sleep(1)
          os.system('uncompyle6 '+file+' > '+out)
          cek=open(out,'r').read()
          if '# okay' in cek:
              time.sleep(1)
              load(fle)
	      os.remove(file)
              print "  {}[{}*{}] succes save to {}{} {}time watch {}{}".format(P,G,P,C,out,P,G,time.clock())
              back()
          else:
              os.remove(out)
	      os.remove(file)
              print '  {}[{}!{}] {}{}{} decompyle error'.format(P,R,P,R,file,P)
              back()
    except KeyboardInterrupt:
         print '  {}[{}!{}] Keyboard interupt !!!'.format(P,R,P)
         back()
    except IOError:
        time.sleep(1)
        print '  {}[{}!{}]{} {} {}no suc file or dictonary!!'.format(P,R,P,R,file,P)
        back()

########################################################################################################
#				OBUSCATOR
########################################################################################################

def obfs():
    try:
       sis('clear')
       banner()
       print "\n  {}Ex{}:{}path/file.py\n".format(R,B,P)
       file=raw_input('  {}[{}file{}]={}: {}'.format(G,P,G,R,P))
       out=raw_input('  {}[{}outp{}]={}: {}'.format(G,P,G,R,P))
       jalan('  '+20*"-"+'{}[{}start{}]'.format(P,G,P))
       h=open(file,'r').read()
    #<--CHECK FILE-->
       if len(h)==0:
            time.sleep(1)
            print "  {}[{}!{}] file empty !!!".format(P,R,P)
            back()
       else:
            time.sleep(1)
            print "  {}[{}+{}] files found ..".format(P,G,P)
            time.sleep(1)
            i=1
            h=open(file,'r').read()
            b=h.replace('exec','print')
            d=open('/data/data/com.termux/files/.waktu/.kanne.py','w')
	    d.write('#coding:utf8')
            d.write(b)
            d.close()
            os.system('python2 /data/data/com.termux/files/.waktu/.kanne.py > '+out)
            if 'import' in open(out,'r').read():
                os.remove('/data/data/com.termux/files/.waktu/.kanne.py')
		load(file)
                print "  {}[{}*{}] succes save to {}{} {}time watch{}{}".format(P,G,P,C,out,P,G,tim.clock())
                back()
            else:
                os.remove(out)
                os.remove('/data/data/com.termux/files/.waktu/.kanne.py')
                print '  {}[{}!{}] {}{}{} decompyle error'.format(P,R,P,R,file,P)
                back()
    except KeyboardInterrupt:
         print '  {}[{}!{}] Keyboard interupt !!!'.format(P,R,P)
         back()
    except IOError:
        time.sleep(1)
        print '  {}[{}!{}]{} {} {}no suc file or dictonary ....'.format(P,R,P,R,file,P)
        back()



########################################################################################################
#					marshal to dis and lain2
########################################################################################################

def mdis():
    sis('clear')
    banner()
    print """
    {}({}1{})-{}Grab const [{}d,k{}]
    {}({}2{})-{}Dec code [{}d,k{}]
    {}({}3{})-{}marshal to dis
    {}({}4{})-{}marshal to dis [{}2{}]
    {}({}0{})-{}Back
      """.format(
          G,P,G,P,G,P,
          G,P,G,P,G,P,
          G,P,G,P,
	  G,P,G,P,G,P,
          G,R,G,P
          )
    wk=raw_input(' {}[{}pilih{}]={}•{} '.format(
    G,P,G,R,P))
    if wk=='1':grab()
    elif wk=='2':grep()
    elif wk=='0':menu()
    elif wk=='':mdis()
    elif wk=='3':fids()
    elif wk=='4':mds2()
    else:mdis()

def mds2():
    sis('clear')
    banner()
    print "\n  {}Ex{}:{}path/file.dis\n".format(R,B,P)
    file=raw_input('  {}[{}file{}]={}: {}'.format(G,P,G,R,P))
    out=raw_input('  {}[{}outp{}]={}: {}'.format(G,P,G,R,P))
    jalan('  '+20*"-"+'{}[{}start{}]'.format(P,G,P))
    time.sleep(1)
    jalan('  {}[{}*{}] checkin filess ....'.format(P,G,P))
    try:
       q=open(file,'r').read()
       if len(q)==0:
          time.sleep(1)
          print "  {}[{}!{}] file empty !!!".format(P,R,P)
          backd()
       elif "d = [" in q and 'k = [' in q:
          bh=open(file,'r').read()
          bbb=re.findall(r'd = .*',bh)
          bbx=re.findall(r'k = .*',bh)
          cod=open('.tinu.py','w')
          cod.write(nmmek)
          cod.write(bbb[0]+'\n')
          cod.write(bbx[0]+'\n')
          cod.write(gass)
          cod.close()
          os.system('python2 .tinu.py >'+out+'.pyc')
          os.remove('.tinu.py')
          os.system('uncompyle6 '+out+'.pyc > '+out)
	  load(file)
          print "  {}[{}*{}] succes save to {}{}".format(P,G,P,C,out)
          back()
       elif "d=[" in q and 'k=[' in q:
          bh=open(file,'r').read()
          bbb=re.findall(r'd=.*',bh)
          bbx=re.findall(r'k=.*',bh)
          cod=open('.tinu.py','w')
          cod.write(nmmek)
          cod.write(bbb[0]+'\n')
          cod.write(bbx[0]+'\n')
          cod.write(gass)
          cod.close()
          os.system('python2 .tinu.py >'+out+'.pyc')
          os.remove('.tinu.py')
          os.system('uncompyle6 '+out+'.pyc > '+out)
	  load(file)
          print "  {}[{}*{}] succes save to {}{} {}time watch {}{}".format(P,G,P,C,out,G,P,time.clock())
          back()
       else:
          time.sleep(1)
          print '  {}[{}!{}]{} {} {} no exsits'.format(P,R,P,R,file,P)
          backd()
    except KeyboardInterrupt:
         print '  {}[{}!{}] Keyboard interupt !!!'.format(P,R,P)
         backd()
    except ValueError:
        os.remove(out)
        print '  {}[{}!{}] {}{}{} process error'.format(P,R,P,R,file,P)
        backd()
    except IOError:
        time.sleep(1)
        print '  {}[{}!{}]{} {} {}no suc file or dictonary ....'.format(P,R,P,R,file,P)
        backd()

def grab():
    sis('clear')
    banner()
    print "\n  {}Ex{}:{}path/file.dis\n".format(R,B,P)
    file=raw_input('  {}[{}file{}]={}: {}'.format(G,P,G,R,P))
    out=raw_input('  {}[{}outp{}]={}: {}'.format(G,P,G,R,P))
    jalan('  '+20*"-"+'{}[{}start{}]'.format(P,G,P))
    time.sleep(1)
    jalan('  {}[{}*{}] checkin filess ....'.format(P,G,P))
    try:
        q=open(file,'r').read()
	if len(q)==0:
            time.sleep(1)
            print "  {}[{}!{}] file empty !!!".format(P,R,P)                                        
            backd()
        else:
           oou=open(file,'r').readlines()
           o=open(file,'r').read()
	   jalan('  {}[{}*{}] checkin zize file ....'.format(P,G,P))
           if 1000 < len(oou):
              d=['d','k']
              r=re.findall(r'(?si).*?1 \(d\)',o)
              os.system('touch '+out)
              for i in range(2):
                  z=re.findall(r"(?si)load_const.*?\((\d*)\)",r[i])
                  if i == 1:
                     z=z[2:]
                  z=[int(j) for j in z]
                  with open(out,'a') as f:
                     f.write(d[i]+'='+str(z)+'\n')
              ek=open(out,'r').read()
              if '=' in ek or 'd =' in ek:
  	         time.sleep(1)
	         load(file)
                 print "  {}[{}*{}] succes save to {}{}{} time watch {}{}".format(P,G,P,C,out,P,G,time.clock())
                 backd()
              else:
                 os.remove(out)
                 print '  {}[{}!{}] {}{}{} process error'.format(P,R,P,R,file,P)
                 backd()
           else:
               print "  {}[{}!{}]{} {} {}baris line {} not level :(".format(P,R,P,C,file,P,len(oou))
               time.sleep(0.5)
	       backd()
    except KeyboardInterrupt:
         print '  {}[{}!{}] Keyboard interupt !!!'.format(P,R,P)
         backd()
    except ValueError:
        os.remove(out)
        print '  {}[{}!{}] {}{}{} process error'.format(P,R,P,R,file,P)
        backd()
    except IOError:
        time.sleep(1)
        print '  {}[{}!{}]{} {} {}no suc file or dictonary ....'.format(P,R,P,R,file,P)
        backd()

def grep():
    sis('clear')
    banner()
    print "\n  {}Ex{}:{}path/file.dis\n".format(R,B,P)
    file=raw_input('  {}[{}file{}]={}: {}'.format(G,P,G,R,P))
    out=raw_input('  {}[{}outp{}]={}: {}'.format(G,P,G,R,P))
    jalan('  '+20*"-"+'{}[{}start{}]'.format(P,G,P))
    jk=open(file,'r').read()
    sis('cat '+file+' > damai.py')
    time.sleep(1)
    jalan('  {}[{}*{}] checkin filess ....'.format(P,G,P))
    try:
       import damai
       d=damai.d
       k=damai.k
       e = ''
       i,j = (0,0)
       while 1:
             if i >= len(d): break
             if j >= len(k): j = 0
             e += chr(d[i] ^ k[j])
             i += 1
             j += 1
       with open(out,'wb') as f:
             f.write('\x03\xf3\x0d\x0a\xeb\x56\x92\x5a'+e)
       os.remove('damai.py')
       ha=open(out,'r').read()
       if len(ha)==len(ha):
          time.sleep(1)
	  load(file)
          print "  {}[{}*{}] succes save to {}{} {}time watch {}{}".format(P,G,P,C,out,G,P,time.clock())
          backd()
       else:
          os.remove(out)
          print '\n  {}[{}!{}] {}{}{} process error'.format(P,R,P,R,file,P)
          backd()
    except KeyboardInterrupt:
         print '  {}[{}!{}] Keyboard interupt !!!'.format(P,R,P)
         backd()
    except (IOError,AttributeError):
        os.remove('damai.py')
        time.sleep(1)
        print '  {}[{}!{}]{} {} {}no suc file or dictonary'.format(P,R,P,R,file,P)
        backd()



def fids():
    sis('clear')
    banner()
    jus="""import sys
import dis
import time
import types
import struct
import marshal
import binascii
#from ktp import h
def show_hex(label, h, indent):
    h = binascii.hexlify(h)
    if len(h) < 60:
        print ("%s%s %s" % (indent, label, h))
    else:
        print ("%s%s" % (indent, label))
        for i in range(0, len(h), 60):
            print ("%s   %s" % (indent, h[i:i+60]))

def show_code(code, indent=''):
    print ("%scode" % indent)
    indent += '   '
    print ("%sargcount %d" % (indent, code.co_argcount))
    print ("%snlocals %d" % (indent, code.co_nlocals))
    print ("%sstacksize %d" % (indent, code.co_stacksize))
    print ("%sflags %04x" % (indent, code.co_flags))
    show_hex("code", code.co_code, indent=indent)
    dis.disassemble(code)
    print ("%sconsts" % indent)
    for const in code.co_consts:
        if type(const) == types.CodeType:
            show_code(const, indent+'   ')
        else:
            print ("   %s%r" % (indent, const))
    print ("%snames %r" % (indent, code.co_names))
    print ("%svarnames %r" % (indent, code.co_varnames))
    print ("%sfreevars %r" % (indent, code.co_freevars))
    print ("%scellvars %r" % (indent, code.co_cellvars))
    print ("%sfilename %r" % (indent, code.co_filename))
    print ("%sname %r" % (indent, code.co_name))
    print ("%sfirstlineno %d" % (indent, code.co_firstlineno))
    show_hex("lnotab", code.co_lnotab, indent=indent)

"""
    print "\n  {}Ex{}:{}path/file.dis\n".format(R,B,P)
    file=raw_input('  {}[{}file{}]={}: {}'.format(G,P,G,R,P))
    out=raw_input('  {}[{}outp{}]={}: {}'.format(G,P,G,R,P))
    jalan('  '+20*"-"+'{}[{}start{}]'.format(P,G,P))
    os.system('touch '+out)
    time.sleep(1)
    jalan('  {}[{}*{}] checkin filess ....'.format(P,G,P))
    try:
        q=open(file,'r').read()
        if len(q)==0:
            time.sleep(1)
            print "  {}[{}!{}] file empty !!!".format(P,R,P)                           
            backd()
        elif 'base64.b64decode' in q or 'base64.b16decode' in q or 'base64.b32decode' in q or 'zlib.decompress' in q:
            print "  {}[{}!{}] file not support!!!".format(P,R,P)
            backd()
        else:
            def iniku():
                ek=open(out,'r').read()
                if len(ek)!=0:
                   os.remove('/data/data/com.termux/files/.waktu/.kanne.py')
                   time.sleep(1)
                   load(file)
                   print "  {}[{}*{}] succes save to {}{}{} time watch {}{}".format(P,G,P,C,out,G,P,time.clock())
                   backd()
                else:
                   os.remove('/data/data/com.termux/files/.waktu/.kanne.py')
                   os.remove(out)
                   print '\n  {}[{}!{}] {}{}{} process error'.format(P,R,P,R,file,P)
                   backd()
            qm=open(file,'r').read()
            if "'))" in qm:
		o=open(file,'r').read()
                ngh=open('/data/data/com.termux/files/.waktu/.kanne.py','w')
                likk=o[o.find("marshal.loads")-0:]
     	        ngh.write(jus)
   	        ngh.write('show_code('+likk)
	        ngh.close()
                os.system('python2 /data/data/com.termux/files/.waktu/.kanne.py > '+out)
                iniku()
            else:
                o=open(file,'r').read()
                ja=o[o.find("marshal.loads")-0:]
                gg=open('/data/data/com.termux/files/.waktu/.kanne.py','w')
                gg.write(jus)
                gg.write('show_code('+ja+')')
                gg.close()
                os.system('python2 /data/data/com.termux/files/.waktu/.kanne.py >'+out)
                iniku()
    except KeyboardInterrupt:
         print '  {}[{}!{}] Keyboard interupt !!!'.format(P,R,P)
         backd()
    except AttributeError:os.remove('/data/data/com.termux/files/.waktu/.kanne.py');os.remove(out);print '\n  {}[{}!{}] {}{}{} process error'.format(P,R,P,R,file,P);back()

    except IOError:
        time.sleep(1)
        print '  {}[{}!{}]{} {} {}no suc file or dictonary'.format(P,R,P,R,file,P)
        backd()

########################################################################################################
########################################################################################################

def hex():
    sis("clear")
    banner()
    try:
       sis('clear')
       banner()
       print "\n  {}Ex{}:{}path/file.py\n".format(R,B,P)
       file=raw_input('  {}[{}file{}]={}: {}'.format(G,P,G,R,P))
       out=raw_input('  {}[{}outp{}]={}: {}'.format(G,P,G,R,P))
       jalan('  '+20*"-"+'{}[{}start{}]'.format(P,G,P))
       h=open(file,'r').read()
       if len(h)==0:
            time.sleep(1)
            print "  {}[{}!{}] file empty !!!".format(P,R,P)
            back()
       else:
           He=open('/data/data/com.termux/files/.waktu/.apa.py','w')
           h=open(file,'r').read()
           ab=re.findall(r'import.*',h)
           a=re.findall(r'magic.*',h)
           b=re.findall(r'love.*',h)
           c=re.findall(r'god.*',h)
           d=re.findall(r'destiny.*',h)
           e=re.findall(r'joy.*',h)
           f=re.findall(r'trust.*',h)
           He.write(ab[0]+'\n')
           He.write(a[0]+'\n')
           He.write(b[0]+'\n')
           He.write(c[0]+'\n')
           He.write(d[0]+'\n')
           He.write(e[0]+'\n')
           He.write(f[0]+'\n'+'print base64.b64decode(trust)')
           He.close()
           os.system('python2 /data/data/com.termux/files/.waktu/.apa.py > '+out)
           os.remove('/data/data/com.termux/files/.waktu/.apa.py')
	   load(file)
           print "  {}[{}*{}] succes save to {}{}{} watch time {}{}".format(P,G,P,C,out,G,P,time.clock())
           back()
    except KeyboardInterrupt:
         print '  {}[{}!{}] Keyboard interupt !!!'.format(P,R,P)
         back()
    except IOError:
        time.sleep(1)
        print '  {}[{}!{}]{} {} {}no suc file or dictonary'.format(P,R,P,R,file,P)
        back()



def others():
    sis('clear')
    banner()
    print """
    {}({}1{})-{}bashh
    {}({}2{})-{}php
    {}({}3{})-{}html
    {}({}0{})-{}Back
      """.format(
          G,P,G,P,
          G,P,G,P,
          G,P,G,P,
          G,R,G,P
          )
    wk=raw_input(' {}[{}pilih{}]={}•{} '.format(
    G,P,G,R,P))
    if wk=='1':bash()
    elif wk=='2':php()
    elif wk=='0':menu()
    elif wk=='':others()
    elif wk=='3':html()
    else:others()

def bash():
    sis('clear')
    banner()
    print "\n  {}Ex{}:{}path/file.sh\n".format(R,B,P)
    file=raw_input('  {}[{}file{}]={}: {}'.format(G,P,G,R,P))
    out=raw_input('  {}[{}outp{}]={}: {}'.format(G,P,G,R,P)).replace('.sh','')
    jalan('  '+20*"-"+'{}[{}start{}]'.format(P,G,P))
    jalan('  {}[{}*{}] checkin filess ....'.format(P,G,P))
    try:
        h=open(file,'r').read()
        if len(h)==0:
           time.sleep(1)
           print "  {}[{}!{}] file empty !!!".format(P,R,P)
           bacot()
        else:
	   jalan('  {}[{}*{}] filess found ..'.format(P,G,P))
    	   os.system('cat '+file+'> /data/data/com.termux/files/.waktu/.naninuneno.sh')
           def man():
               j=open('/data/data/com.termux/files/.waktu/.naninuneno.sh','r').read()
               o=open("/data/data/com.termux/files/.waktu/.bk.sh","w")
               o.write(j.replace('eval','echo'))
               o.close()
               os.system('bash /data/data/com.termux/files/.waktu/.bk.sh > /data/data/com.termux/files/.waktu/.naninuneno.sh')
               hv=open('/data/data/com.termux/files/.waktu/.naninuneno.sh','r').read()
               if "eval" in hv:
                   man()
               elif 'echo ==' in hv or "base64" in hv:
                   man()
               else:
                   os.remove('/data/data/com.termux/files/.waktu/.bk.sh')
                   load(file)
                   os.rename('/data/data/com.termux/files/.waktu/.naninuneno.sh',out+'.sh')
		   print "  {}[{}*{}] succes save to {}{}.sh {}time watch {}{}".format(P,G,P,C,out,G,P,time.clock())
                   bacot()
           man()
    except KeyboardInterrupt:
         os.remove('/data/data/com.termux/files/.waktu/.naninuneno.sh')
         print '  {}[{}!{}] Keyboard interupt !!!'.format(P,R,P)
         bacot()
    except IOError:
        time.sleep(1)
        print '  {}[{}!{}]{} {} {}no suc file or dictonary'.format(P,R,P,R,file,P)
        bacot()




if __name__ == '__main__':
     try:
        os.mkdir('/data/data/com.termux/files/.waktu')
     except Exception:pass
     menu()

