from pwn import *
s1=ssh(host="65.0.124.36",user="student", password="caesar")
# r1=s1.remote(65.0.124.)
io=s1.run('sh')

io.sendline("White_Walkers")
io.sendline('arti')

io.recvuntil('You have solved ')
lev_sol = int(io.recv(1).decode())
print("Levels solved = ", lev_sol)
io.sendline(str(lev_sol+1))

# lev_sol1 = str(io.recvuntil('decide to investigate ...').decode())
# print("Levels solved = ", lev_sol1)

#Level specific
# io.recvuntil('decide to investigate ...')
# io.sendline('go')

# io.recvuntil('your hands in it.')
# io.sendline('wave')

# io.recvuntil('the small hole.\n\n')
# io.sendline('wave')
# io.recvuntil('but see no one!\n\n')
# io.sendline('back')
# io.recvuntil('your hands in it.\n\n')
# io.sendline('back')
# io.recvuntil('decide to investigate ...\n\n')
# io.sendline('thrnxxtzy')
# io.recvuntil('next to it!!\n\n')
# io.sendline('read')
# io.recvuntil('loudly to pass this level!\n')
# io.sendline('3608528850368400786036725')
# io.recvuntil('Masquerades Cryptovikings\n\n\n\n')
# io.sendline('c')
# io.recvuntil('and you shiver again.\n\n')
# io.sendline('read')


io.sendline('read')
io.recvuntil('it out though ..."')

# io.sendline('bcshdjcmhs')

# lev_sol1 = str(io.recvuntil('Press c to continue>').decode())
# print("Levels solved = ", lev_sol1)
# io.recuvuntil('Press c to continue> ')
# io.sendline('c')




inpput = open('input.txt','r')
outtput = open("output.txt", "a")
Lines = inpput.readlines()
for line in Lines:
    io.sendline(line)
    io.recvuntil('It reads ...\r\n\t\t')
    out = io.recvuntil('\r\n\r\n\r\nPress').decode()[:-11]
    io.recvuntil('> ')
    io.sendline('c')
    outtput.write(out+"\n")

outtput.close()

   