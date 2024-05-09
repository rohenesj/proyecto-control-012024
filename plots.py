import matplotlib.pyplot as plt

def plotting2(xAxisVector,yAxisVector1,yAxisVector2,titleString1,titleString2,stringXaxis,stringYaxis,stringFileName):
    fig, ax1 = plt.subplots()
    ax1.plot(xAxisVector, yAxisVector1, color='blue', label=titleString1)
    ax1.set_xlabel(stringXaxis)
    ax1.set_ylabel(stringYaxis, color='blue')
    ##ax2 = ax1.twinx()
    ax1.plot(xAxisVector, yAxisVector2, color='red', label=titleString2)
    ##ax2.set_ylabel('v(V)', color='red')
    #lines, labels = ax1.get_legend_handles_labels()
    #lines2, labels2 = ax2.get_legend_handles_labels()
    #ax2.legend(lines + lines2, labels + labels2, loc='upper right')
    plt.tick_params(axis='both',which='major',labelsize=14)
    plt.grid(visible=True)
    plt.savefig(stringFileName,dpi=600)
    plt.show()

## Validacion impulso pwm 255
def plotting(xAxisVector,yAxisVector,titleString,stringXaxis,stringYaxis,stringFileName):
    plt.figure(figsize=(8,6))
    plt.plot(xAxisVector,yAxisVector, color='blue',linewidth=4)
    plt.title(titleString, fontsize=14)
    plt.xlabel(stringXaxis, fontsize=14)
    plt.ylabel(stringYaxis,fontsize=14)
    plt.tick_params(axis='both',which='major',labelsize=14)
    plt.grid(visible=True)
    plt.savefig(stringFileName,dpi=600)
    plt.show()

def locus(stringFileName):
    plt.grid(True)
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.title('Root Locus Plot')
    plt.savefig(stringFileName,dpi=600)
    plt.show()