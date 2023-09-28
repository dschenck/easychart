import easychart
import pandas as pd

# weight (kg), male (frequency, in %), female (frequency, in %)
data = pd.DataFrame(
    [
        [47, 0.0000000001, 0.0017325354],
        [48, 0.0000000137, 0.0092273479],
        [49, 0.0000012357, 0.0217685462],
        [50, 0.0000409917, 0.0240129299],
        [51, 0.0005057903, 0.0119799104],
        [52, 0.0024790321, 0.0033388295],
        [53, 0.006672813, 0.0052276464],
        [54, 0.0156350314, 0.0137715323],
        [55, 0.0225936429, 0.0291933993],
        [56, 0.0134423649, 0.075703902],
        [57, 0.0029915043, 0.1336510354],
        [58, 0.0002454699, 0.1307662196],
        [59, 0.0000074122, 0.107809777],
        [60, 0.0000000823, 0.0901067707],
        [61, 0.0000000003, 0.0565824027],
        [62, 0.0000000001, 0.0330846873],
        [63, 0.0000000138, 0.0234557019],
        [64, 0.0000012506, 0.0245703048],
        [65, 0.000042516, 0.0363239918],
        [66, 0.0005728216, 0.0528806679],
        [67, 0.0038528285, 0.0772371262],
        [68, 0.0199278846, 0.1011227761],
        [69, 0.0735023772, 0.1248143533],
        [70, 0.1414474114, 0.1517207478],
        [71, 0.1607587043, 0.1672892278],
        [72, 0.156768501, 0.1824645205],
        [73, 0.1308448738, 0.1755546923],
        [74, 0.0834651242, 0.1838775534],
        [75, 0.0563959845, 0.2096699261],
        [76, 0.0398640979, 0.1892703603],
        [77, 0.0227904317, 0.1235155259],
        [78, 0.0120117582, 0.0719616415],
        [79, 0.0106464086, 0.056531489],
        [80, 0.0144492207, 0.0534323581],
        [81, 0.0137476296, 0.0423568695],
        [82, 0.0131739785, 0.0292163848],
        [83, 0.0185500407, 0.0290915812],
        [84, 0.0327089601, 0.031320166],
        [85, 0.0541732651, 0.0317749474],
        [86, 0.064825504, 0.0292041446],
        [87, 0.062043502, 0.0178709328],
        [88, 0.0677900685, 0.0074437339],
        [89, 0.095027945, 0.0078785516],
        [90, 0.1252078637, 0.0114674412],
        [91, 0.1287641091, 0.006915425],
        [92, 0.1295199599, 0.0015426205],
        [93, 0.1370474632, 0.0001266243],
        [94, 0.1471844913, 0.0000038237],
        [95, 0.1540815861, 0.0000000002],
        [96, 0.1365084578, 0.0],
        [97, 0.1104704032, 0.0],
        [98, 0.0850848159, 0.0],
        [99, 0.0727715407, 0.0],
        [100, 0.0791960134, 0.0],
        [101, 0.066495959, 0.0],
        [102, 0.0479174096, 0.0],
        [103, 0.0380685259, 0.0],
        [104, 0.0340806527, 0.0],
        [105, 0.0282240322, 0.0],
        [106, 0.0179733594, 0.0],
        [107, 0.0126260293, 0.0],
        [108, 0.011262419, 0.0],
        [109, 0.0094785877, 0.0],
        [110, 0.0084040444, 0.0],
        [111, 0.0045502199, 0.0],
        [112, 0.0009992408, 0.0],
        [113, 0.0000818462, 0.0],
        [114, 0.0000024708, 0.0],
        [115, 0.0000000274, 0.0],
        [44, 0.0, 0.0000000004],
        [45, 0.0, 0.0000038874],
        [46, 0.0, 0.0001323598],
    ]
)

chart = easychart.new("streamgraph")
chart.title.text = "Distribution of the weight of rowing athletes"
chart.subtitle.text = "2012 Olympic games, by gender"

chart.chart.inverted = True  # xAxis plotted vertically, yAxes plotted horizontally
chart.xAxis.reversed = False  # xAxis from low to high

with chart.yAxis as axes:
    axes.append(width="45%", offset=0, visible=False)
    axes.append(width="45%", offset=0, visible=False, left="55%")

chart.plot(data.iloc[:, [0, 1]].values, name="Male", yAxis=0)
chart.plot(data.iloc[:, [0, 2]].values, name="Female", yAxis=1)

chart