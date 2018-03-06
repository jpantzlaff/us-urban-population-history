inTable = open(r'..\Population_PartIII.txt', 'r')
inData = inTable.read()
inTable.close()
outTable = open(r'..\counties_out.txt', 'a')

out = {}
states = inData.split(' -- ')
states1 = []
for a in states:
    state = a[:(a.find(':'))]
    a = a[:(a.find(state + ' NOTES'))]
    out[state] = {}
    years = []
    lines = a.split('\n')
    yearsLine = lines[1].split('\t')
    for b in yearsLine:
        if b.isdigit():
            years.append(b)
    countyLines = lines[5:-2]
    for c in countyLines:
        columns = c.split('\t')
        county = (columns.pop(0)).strip()
        out[state][county] = {}
        popValues = []
        for d in columns:
            if len(popValues) < len(columns):
                if d.isdigit():
                    popValues.append(d)
                else:
                    popValues.append('')
        outTable.write(county + '\t' + state + '\t' + '\t'.join(popValues) + '\n')
        for e in range(len(years)):
            try:
                out[state][county][years[e]] = popValues[e]
            except:
                pass

outTable.close()
