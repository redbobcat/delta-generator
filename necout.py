#this file contains output functions to generate .nec file for nec2c

def write_CM(name, line):
    outfile=open(name, 'w')
    outfile.write('CM ---NEC file, automaticaly generated--- \nCM    by python script\n')
    line='CM '+line
    outfile.write(line)
    outfile.write('CE ---End of comments section--- \n\n\n')
    outfile.close()

def write_GW (name, tag, segs, start[], end[], diameter):
    radius=diameter/2
    outfile=open(name, 'a')
    GW_card=f'GW {tag:3} {segs:3} {start[0]:5} {start[1]:5} {start[2]:5} \
        {end[0]:5} {end[1]:5} {end[2]:5} {radius} \n'
    outfile.write(GW_card)
    outfile.close()

def write_GE (name, ground):
    outfile=open(name, 'a')
    GE_card=f'GE 0 0 0 0 0 0 0 0 0\n'
    outfile.write(GE_card)
    outfile.close()


    
