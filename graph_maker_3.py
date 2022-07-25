import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import random

fig, ax = plt.subplots(figsize=(8,5))

#Legend
# |---EDIT HERE for legend---|Preparation of markers to be used for legend
label1 = mlines.Line2D([], [], color='black', marker='^', linestyle='None',
                          markersize=10, label='C1')
label3 = mlines.Line2D([], [], color='magenta', marker='>', linestyle='None',
                          markersize=10, label='C4')
label4 = mlines.Line2D([], [], color='blue', marker='o', linestyle='None',
                          markersize=10, label='C5')
label5 = mlines.Line2D([], [], color='green', marker='*', linestyle='None',
                          markersize=10, label='C6')

#|---EDIT HERE for input file: input.txt---|
with open("input.txt") as file:
    files=file.readlines()

#Plotting the graph
#|---EDIT HERE for plot marker params---|Markers are in order colour,shape,size,transparency
markers=[('black','^',120,0.80),('magenta','>',100,0.70),('blue','o',90,0.70),('green','*',150,0.70)]

for mark, file in enumerate(files):
    file=file.rstrip()
    df = pd.read_csv(file)
    df.set_index('Residue',inplace=True)
    #df=df.transpose()
    #print(df)
    df['level'] = [i for i in range(0, len(df))]
    for ind, carbon in enumerate(df.columns[0:-1]):
        #print(idx)
        df_carbon=df[[carbon, 'level']]
        #print("\n",df_carbon,"\n")
        #encoding = ['blue' if x == 1 else 'white' for x in df[carbon]]
        for y,z in enumerate(df['level']):
            #print(y,z)
            
            encoding = [ markers[mark][0] if x == 1 else '' for x in df[carbon]]
            #print(ind,z)
            jittered_x = ind + 0.01 *random.randrange(-10,10) 
            jittered_y = z + 0.01 *random.randrange(-10,10) 
            #print(jittered_x,jittered_y)
            plt.scatter(x=jittered_x, y=jittered_y, c=encoding[y], s=markers[mark][2],marker=markers[mark][1], 
                                             alpha = markers[mark][3])
#fig.tight_layout()
plt.yticks([i for i in range(len(df.index))], list(df.index))
plt.xticks([i for i in range(len(df.columns)-1)], list(df.columns[0:-1]))
plt.legend(handles=[label1, label3, label4, label5], loc = 'lower left', bbox_to_anchor = (1,0))
plt.show()
fig.savefig('figure_hires2022.png', dpi=600)
