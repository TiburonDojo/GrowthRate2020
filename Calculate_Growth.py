initial = 1
changed = 60
timeLapse = 27

growth=((changed /initial) ** (1/timeLapse)-1)

print('{0:.2f}%'.format(growth*100))
