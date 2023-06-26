import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

plt.style.use('bmh')


def organize_data(data, technique, mappingsEG_TS):
    # technique = ['Reification', 'RDF-star', 'Named-graphs', 'N-ary']
    # mappingsEG_TS = ['Oxigraph', 'Fuseki']
    ordered_data = pd.DataFrame(index=mappingsEG_TS)
    ordered_data = data[1:]
    ordered_data.columns = technique
    ordered_data.replace(np.nan, 0)
    print(ordered_data)
    for i in range(0, len(ordered_data.index)):
        for j in range(0, len(ordered_data.columns)):
            new_data = float(ordered_data.iloc[i][j])
            ordered_data.iloc[i][j]=np.log10(new_data)

    #ordered_data=np.log10(ordered_data)
    print(ordered_data)
    return ordered_data


def plot(data, scale):
    # Create dataframe
    technique = ['Reification', 'RDF-star', 'Named-graphs', 'N-ary']
    mappingsEG_TS = ['Oxigraph', 'Fuseki', 'GraphDB', 'Morph-KGC', 'SPARQL-Anything']
    data = np.transpose(data)
    ordered_data = organize_data(data, [x.lower() for x in technique], mappingsEG_TS)
    # print("+++++++++++++++++++++")
    print(ordered_data)
    # np.log10(ordered_data)
    barWidth = 0.11
    r1 = np.arange(len(ordered_data.columns))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth * 2 for x in r1]
    r4 = [x + barWidth * 3 for x in r1]
    r5 = [x + barWidth * 4 for x in r1]
    # r6 = [x + barWidth * 5 for x in r1]
    # r7 = [x + barWidth * 6 for x in r1]
    # r9 = [x + barWidth * 8 for x in r1]
    # r10 = [x + barWidth * 9 for x in r1]

    plt.bar(r1, ordered_data.values.tolist()[0], width=barWidth, color='#F2BABA',  # F2BABA
            label='Oxigraph')
    plt.bar(r2, ordered_data.values.tolist()[1], width=barWidth, color='#A46593',  # A46593
            label='Fuseki', )
    plt.bar(r3, ordered_data.values.tolist()[2], width=barWidth, color='#FCAB64',  # B1ACAA
            label='GraphDB')
    plt.bar(r4, ordered_data.values.tolist()[3], width=barWidth, color='#B1ACAA',  # B1ACAA
            label='Morph-KGC')
    plt.bar(r5, ordered_data.values.tolist()[4], width=barWidth, color='#2862CC',  # 2862CC
            label='SPARQL-Anything')

    plt.xticks([r + barWidth * 1.5 for r in range(len(r1))], map(lambda each: each.strip(""), technique),
               fontsize=12)
    plt.yticks(np.arange(0, 6), ('0', '1', '2', '3', '4', 'TO'), fontsize=14)
    plt.ylim(top=5)
    plt.ylabel("Time (log$_{10}$(s))", fontsize=15)
    plt.xlabel("Format", fontsize=15)
    plt.title(scale, fontsize=20)
    plt.legend(mappingsEG_TS, loc='lower center', ncol=6, bbox_to_anchor=[0.5, -0.26], fontsize=13)
    # plt.legend(engines, loc='lower center', prop={'size': 10}, ncol=6, bbox_to_anchor=(0.5, -0.28))
    # plt.grid(False)
    plt.grid(axis='x')

    # plt.show()
    plt.savefig("./figures/time_" + scale.lower() + ".png", bbox_inches='tight', dpi=700)

    plt.clf()

    print("Finished: 'figures/time_" + scale + "'")


def handler():
    # scales = ['GTFS-1', 'GTFS-10', 'GTFS-100', 'GTFS-1000']
    scales = ['1K','10K', '100K', '1M']
    for scale in scales:
        plot(pd.read_csv("./" + scale + ".csv"), scale)
        # if scale == 'GTFS-100':
        #     plot100(pd.read_csv("./" + scale + ".csv"), scale)
        # elif scale == 'GTFS-1000':
        #     plot1000(pd.read_csv("./" + scale + ".csv"), scale)
        # else:
        #     plot(pd.read_csv("./"+ scale + ".csv"), scale)


if __name__ == "__main__":
    handler()
