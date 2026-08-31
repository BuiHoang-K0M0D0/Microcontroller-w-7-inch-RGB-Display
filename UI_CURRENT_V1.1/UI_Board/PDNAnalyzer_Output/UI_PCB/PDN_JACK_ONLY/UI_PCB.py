designFile = "C:/Users/buima/Desktop/UI_Board/UI_CURRENT/UI_Board/PDNAnalyzer_Output/UI_PCB/odb.tgz"

powerNets = ["Vsupply", "9V", "5V", "NetQ6_3", "NetQ5_3", "3V3", "PA0", "TEST", "NetD2_2", "NetD9_2", "3V", "2.5V", "SVREF", "1.1V", "10.4V", "NetC31_2", "VLED+", "16V", "-7V", "pdna_net_3V3_LCD_1"]

groundNets = ["GND", "NetC50_1", "STM_RST", "F1C_RST", "NetC84_2", "SPI_NSS", "NetC81_2", "SD_CMD", "SD_D0", "SD_D1", "SD_D2", "SD_D3", "VLED-", "LCD_RST"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J1", "1") ],
"ground_pins": [ ("J1", "2") ],
"voltage": 9,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("R27", "2") ],
"ground_pins": [ ("R27", "1") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("U5", "11"), ("U5", "100"), ("U5", "28"), ("U5", "75"), ("U5", "50") ],
"ground_pins": [ ("U5", "27"), ("U5", "10"), ("U5", "99"), ("U5", "74") ],
"current": 0.2,
"Rpin": 2.22222222222222,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("SD1", "pdna_pin_4_1"), ("SD1", "pdna_pin_4_2"), ("SD1", "pdna_pin_4_3") ],
"ground_pins": [ ("SD1", "pdna_pin_6_1"), ("SD1", "pdna_pin_6_2"), ("SD1", "9"), ("SD1", "pdna_pin_6_3"), ("SD1", "pdna_pin_6_4"), ("SD1", "pdna_pin_6_5") ],
"current": 0.2,
"Rpin": 2,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("D2", "2") ],
"ground_pins": [ ("D2", "1") ],
"current": 0.00681,
"Rpin": 14.6842878120411,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("D9", "2") ],
"ground_pins": [ ("D9", "1") ],
"current": 0.00318,
"Rpin": 31.4465408805031,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("U10", "8"), ("U10", "7"), ("U10", "3") ],
"ground_pins": [ ("U10", "4") ],
"current": 0.025,
"Rpin": 6,
}
,
{
"id": "7",
"type": "load",
"power_pins": [ ("R20", "2") ],
"ground_pins": [ ("R20", "1") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "8",
"type": "load",
"power_pins": [ ("R59", "2") ],
"ground_pins": [ ("R59", "1") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "9",
"type": "load",
"power_pins": [ ("R70", "2") ],
"ground_pins": [ ("R70", "1") ],
"resistance": 1E-09,
"Rpin": 500,
}
,
{
"id": "10",
"type": "load",
"power_pins": [ ("R54", "2") ],
"ground_pins": [ ("R54", "1") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "11",
"type": "load",
"power_pins": [ ("R65", "2") ],
"ground_pins": [ ("R65", "1") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "12",
"type": "load",
"power_pins": [ ("U11", "4"), ("U11", "5"), ("U11", "20"), ("U11", "74"), ("U11", "67"), ("U11", "50") ],
"ground_pins": [ ("U11", "82"), ("U11", "89"), ("U11", "73") ],
"current": 0.14,
"Rpin": 2.85714285714286,
}
,
{
"id": "13",
"type": "load",
"power_pins": [ ("R49", "2") ],
"ground_pins": [ ("R49", "1") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "14",
"type": "load",
"power_pins": [ ("R45", "2") ],
"ground_pins": [ ("R45", "1") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "15",
"type": "load",
"power_pins": [ ("R46", "2") ],
"ground_pins": [ ("R46", "1") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "16",
"type": "load",
"power_pins": [ ("R47", "2") ],
"ground_pins": [ ("R47", "1") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "17",
"type": "load",
"power_pins": [ ("R48", "2") ],
"ground_pins": [ ("R48", "1") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "18",
"type": "load",
"power_pins": [ ("U11", "80") ],
"ground_pins": [ ("U11", "82"), ("U11", "89"), ("U11", "73") ],
"current": 0.03,
"Rpin": 5,
}
,
{
"id": "19",
"type": "load",
"power_pins": [ ("U11", "30"), ("U11", "31"), ("U11", "32"), ("U11", "34"), ("U11", "36") ],
"ground_pins": [ ("U11", "82"), ("U11", "89"), ("U11", "73") ],
"current": 0.1776,
"Rpin": 2.11148648648649,
}
,
{
"id": "20",
"type": "load",
"power_pins": [ ("R63", "2") ],
"ground_pins": [ ("R63", "1") ],
"resistance": 1E-09,
"Rpin": 1000,
}
,
{
"id": "21",
"type": "load",
"power_pins": [ ("U11", "22"), ("U11", "71"), ("U11", "35") ],
"ground_pins": [ ("U11", "82"), ("U11", "89"), ("U11", "73") ],
"current": 0.34551,
"Rpin": 0.868281670573934,
}
,
{
"id": "22",
"type": "load",
"power_pins": [ ("LCD1", "43") ],
"ground_pins": [ ("LCD1", "52"), ("LCD1", "40"), ("LCD1", "38"), ("LCD1", "48"), ("LCD1", "5"), ("LCD1", "36"), ("LCD1", "51") ],
"current": 0.05,
"Rpin": 3.5,
}
,
{
"id": "23",
"type": "load",
"power_pins": [ ("LCD1", "1"), ("LCD1", "2") ],
"ground_pins": [ ("LCD1", "3"), ("LCD1", "4") ],
"current": 0.18,
"Rpin": 1.11111111111111,
}
,
{
"id": "24",
"type": "load",
"power_pins": [ ("LCD1", "41") ],
"ground_pins": [ ("LCD1", "52"), ("LCD1", "40"), ("LCD1", "38"), ("LCD1", "48"), ("LCD1", "5"), ("LCD1", "36"), ("LCD1", "51") ],
"current": 0.001,
"Rpin": 175,
}
,
{
"id": "25",
"type": "load",
"power_pins": [ ("LCD1", "42") ],
"ground_pins": [ ("LCD1", "52"), ("LCD1", "40"), ("LCD1", "38"), ("LCD1", "48"), ("LCD1", "5"), ("LCD1", "36"), ("LCD1", "51") ],
"current": -0.001,
"Rpin": 175,
}
,
{
"id": "26",
"type": "load",
"power_pins": [ ("LCD1", "47"), ("LCD1", "6"), ("LCD1", "7"), ("LCD1", "8"), ("LCD1", "39"), ("LCD1", "46") ],
"ground_pins": [ ("LCD1", "52"), ("LCD1", "40"), ("LCD1", "38"), ("LCD1", "48"), ("LCD1", "5"), ("LCD1", "36"), ("LCD1", "51") ],
"current": 0.01,
"Rpin": 64.6153846153846,
}
,
{
"id": "27",
"type": "load",
"power_pins": [ ("R40", "2") ],
"ground_pins": [ ("R40", "1") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "28",
"type": "load",
"power_pins": [ ("U4", "2") ],
"ground_pins": [ ("U4", "1") ],
"current": 0.03,
"Rpin": 3.33333333333333,
}
,
{
"id": "29",
"type": "source",
"power_pins": [ ("U2", "4") ],
"ground_pins": [ ("L2", "2") ],
"voltage": 9.3,
"Rpin": 0,
}
,
{
"id": "30",
"type": "load",
"power_pins": [ ("U2", "5") ],
"ground_pins": [ ("U2", "2") ],
"current": 0.170568809898068,
"Rpin": 0.586273657298542,
}
,
{
"id": "31",
"type": "source",
"power_pins": [ ("L1", "2") ],
"ground_pins": [ ("U1", "2") ],
"voltage": 5.001775116,
"Rpin": 0,
}
,
{
"id": "32",
"type": "load",
"power_pins": [ ("U1", "5") ],
"ground_pins": [ ("U1", "2") ],
"current": 0.3318,
"Rpin": 0.301386377335744,
}
,
{
"id": "33",
"type": "load",
"power_pins": [ ("R1", "2") ],
"ground_pins": [ ("R4", "1") ],
"resistance": 1E-09,
"Rpin": 500000,
}
,
{
"id": "34",
"type": "source",
"power_pins": [ ("L3", "1") ],
"ground_pins": [ ("U3", "5"), ("U3", "4"), ("U3", "1"), ("U3", "21"), ("U3", "13"), ("U3", "12"), ("U3", "17"), ("U3", "15") ],
"voltage": 3.3023295551,
"Rpin": 0,
}
,
{
"id": "35",
"type": "load",
"power_pins": [ ("U3", "9"), ("U3", "10"), ("U3", "7"), ("U3", "8"), ("U3", "19"), ("U3", "18"), ("U3", "16") ],
"ground_pins": [ ("U3", "5"), ("U3", "4"), ("U3", "1"), ("U3", "21"), ("U3", "13"), ("U3", "12"), ("U3", "17"), ("U3", "15") ],
"current": 0.3796,
"Rpin": 1.9669827889006,
}
,
{
"id": "36",
"type": "load",
"power_pins": [ ("R8", "2") ],
"ground_pins": [ ("R9", "1") ],
"resistance": 1E-09,
"Rpin": 500000,
}
,
{
"id": "37",
"type": "source",
"power_pins": [ ("L4", "1") ],
"ground_pins": [ ("U3", "5"), ("U3", "4"), ("U3", "1"), ("U3", "21"), ("U3", "13"), ("U3", "12"), ("U3", "17"), ("U3", "15") ],
"voltage": 2.5004342948,
"Rpin": 0,
}
,
{
"id": "38",
"type": "load",
"power_pins": [ ("U3", "9"), ("U3", "10"), ("U3", "7"), ("U3", "8"), ("U3", "19"), ("U3", "18"), ("U3", "16") ],
"ground_pins": [ ("U3", "5"), ("U3", "4"), ("U3", "1"), ("U3", "21"), ("U3", "13"), ("U3", "12"), ("U3", "17"), ("U3", "15") ],
"current": 0.1021,
"Rpin": 7.31309174012406,
}
,
{
"id": "39",
"type": "load",
"power_pins": [ ("R10", "2") ],
"ground_pins": [ ("R11", "1") ],
"resistance": 1E-09,
"Rpin": 500000,
}
,
{
"id": "40",
"type": "source",
"power_pins": [ ("L5", "1") ],
"ground_pins": [ ("U3", "5"), ("U3", "4"), ("U3", "1"), ("U3", "21"), ("U3", "13"), ("U3", "12"), ("U3", "17"), ("U3", "15") ],
"voltage": 1.1007462635,
"Rpin": 0,
}
,
{
"id": "41",
"type": "load",
"power_pins": [ ("U3", "9"), ("U3", "10"), ("U3", "7"), ("U3", "8"), ("U3", "19"), ("U3", "18"), ("U3", "16") ],
"ground_pins": [ ("U3", "5"), ("U3", "4"), ("U3", "1"), ("U3", "21"), ("U3", "13"), ("U3", "12"), ("U3", "17"), ("U3", "15") ],
"current": 0.0792,
"Rpin": 9.42760942760943,
}
,
{
"id": "42",
"type": "load",
"power_pins": [ ("R12", "2") ],
"ground_pins": [ ("R13", "1") ],
"resistance": 1E-09,
"Rpin": 500000,
}
,
{
"id": "43",
"type": "source",
"power_pins": [ ("Q4", "3") ],
"ground_pins": [ ("U7", "7"), ("U7", "pdna_pin_28_2"), ("U7", "6"), ("U7", "23") ],
"voltage": 10.4001813351,
"Rpin": 0,
}
,
{
"id": "44",
"type": "load",
"power_pins": [ ("U7", "22"), ("U7", "21"), ("U7", "20"), ("U7", "16"), ("U7", "12"), ("U7", "9"), ("U7", "8") ],
"ground_pins": [ ("U7", "7"), ("U7", "pdna_pin_28_2"), ("U7", "6"), ("U7", "23") ],
"current": 0.2693,
"Rpin": 1.89042298214225,
}
,
{
"id": "45",
"type": "load",
"power_pins": [ ("R30", "2") ],
"ground_pins": [ ("R32", "1") ],
"resistance": 1E-09,
"Rpin": 500000,
}
,
{
"id": "46",
"type": "source",
"power_pins": [ ("D6", "1") ],
"ground_pins": [ ("U7", "7"), ("U7", "pdna_pin_28_2"), ("U7", "6"), ("U7", "23") ],
"voltage": 15.99999366105,
"Rpin": 0,
}
,
{
"id": "47",
"type": "load",
"power_pins": [ ("U7", "22"), ("U7", "21"), ("U7", "20"), ("U7", "16"), ("U7", "12"), ("U7", "9"), ("U7", "8") ],
"ground_pins": [ ("U7", "7"), ("U7", "pdna_pin_28_2"), ("U7", "6"), ("U7", "23") ],
"current": 0.00254,
"Rpin": 200.429491768074,
}
,
{
"id": "48",
"type": "load",
"power_pins": [ ("R33", "2") ],
"ground_pins": [ ("R35", "1") ],
"resistance": 1E-09,
"Rpin": 500000,
}
,
{
"id": "49",
"type": "source",
"power_pins": [ ("D5", "2") ],
"ground_pins": [ ("U7", "7"), ("U7", "pdna_pin_28_2"), ("U7", "6"), ("U7", "23") ],
"voltage": -7.00000891937,
"Rpin": 0,
}
,
{
"id": "50",
"type": "load",
"power_pins": [ ("U7", "22"), ("U7", "21"), ("U7", "20"), ("U7", "16"), ("U7", "12"), ("U7", "9"), ("U7", "8") ],
"ground_pins": [ ("U7", "7"), ("U7", "pdna_pin_28_2"), ("U7", "6"), ("U7", "23") ],
"current": 0.00111,
"Rpin": 458.640458640459,
}
,
{
"id": "51",
"type": "load",
"power_pins": [ ("R34", "2") ],
"ground_pins": [ ("R36", "1") ],
"resistance": 1E-09,
"Rpin": 500000,
}
,
{
"id": "52",
"type": "source",
"power_pins": [ ("L7", "2") ],
"ground_pins": [ ("U7", "7"), ("U7", "pdna_pin_28_2"), ("U7", "6"), ("U7", "23") ],
"voltage": 3.30000397839,
"Rpin": 0,
}
,
{
"id": "53",
"type": "load",
"power_pins": [ ("U7", "22"), ("U7", "21"), ("U7", "20"), ("U7", "16"), ("U7", "12"), ("U7", "9"), ("U7", "8") ],
"ground_pins": [ ("U7", "7"), ("U7", "pdna_pin_28_2"), ("U7", "6"), ("U7", "23") ],
"current": 0.03667,
"Rpin": 13.8830354265315,
}
,
{
"id": "54",
"type": "load",
"power_pins": [ ("R37", "2") ],
"ground_pins": [ ("R38", "1") ],
"resistance": 1E-09,
"Rpin": 500000,
}
]


voltage_regulators = [
{
"id": "55",
"type": "linear",

"in": [ ("U4", "2") ],
"out": [ ("U4", "3") ],
"ref": [ ("U4", "1") ],

"v2": -0.29191,
"i1": 0.03,
"Ro": 0,
"Rpin": 0,
}
,
{
"id": "56",
"type": "linear",

"in": [ ("Q1", "3") ],
"out": [ ("Q1", "2") ],
"ref": [],

"v2": -0.2,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "57",
"type": "linear",

"in": [ ("C50", "2") ],
"out": [ ("C50", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "58",
"type": "linear",

"in": [ ("Q5", "3") ],
"out": [ ("Q5", "2") ],
"ref": [],

"v2": -0.2,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "59",
"type": "linear",

"in": [ ("Q6", "3") ],
"out": [ ("Q6", "2") ],
"ref": [],

"v2": -0.2,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "60",
"type": "linear",

"in": [ ("SW2", "2") ],
"out": [ ("SW2", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "61",
"type": "linear",

"in": [ ("U5", "11"), ("U5", "100"), ("U5", "28"), ("U5", "75"), ("U5", "50") ],
"out": [ ("U5", "67") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 8.33333333333333E-07,
}
,
{
"id": "62",
"type": "linear",

"in": [ ("R17", "2") ],
"out": [ ("R17", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 110,
}
,
{
"id": "63",
"type": "linear",

"in": [ ("R39", "2") ],
"out": [ ("R39", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 110,
}
,
{
"id": "64",
"type": "linear",

"in": [ ("SW1", "1") ],
"out": [ ("SW1", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "65",
"type": "linear",

"in": [ ("SW5", "1") ],
"out": [ ("SW5", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "66",
"type": "linear",

"in": [ ("SW4", "1") ],
"out": [ ("SW4", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "67",
"type": "linear",

"in": [ ("U10", "4") ],
"out": [ ("U10", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "68",
"type": "linear",

"in": [ ("SW10", "1") ],
"out": [ ("SW10", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "69",
"type": "linear",

"in": [ ("SD1", "pdna_pin_6_1"), ("SD1", "pdna_pin_6_2"), ("SD1", "9"), ("SD1", "pdna_pin_6_3"), ("SD1", "pdna_pin_6_4"), ("SD1", "pdna_pin_6_5") ],
"out": [ ("SD1", "3") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 8.57142857142857E-07,
}
,
{
"id": "70",
"type": "linear",

"in": [ ("SD1", "pdna_pin_6_1"), ("SD1", "pdna_pin_6_2"), ("SD1", "9"), ("SD1", "pdna_pin_6_3"), ("SD1", "pdna_pin_6_4"), ("SD1", "pdna_pin_6_5") ],
"out": [ ("SD1", "7") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 8.57142857142857E-07,
}
,
{
"id": "71",
"type": "linear",

"in": [ ("SD1", "pdna_pin_6_1"), ("SD1", "pdna_pin_6_2"), ("SD1", "9"), ("SD1", "pdna_pin_6_3"), ("SD1", "pdna_pin_6_4"), ("SD1", "pdna_pin_6_5") ],
"out": [ ("SD1", "8") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 8.57142857142857E-07,
}
,
{
"id": "72",
"type": "linear",

"in": [ ("SD1", "pdna_pin_6_1"), ("SD1", "pdna_pin_6_2"), ("SD1", "9"), ("SD1", "pdna_pin_6_3"), ("SD1", "pdna_pin_6_4"), ("SD1", "pdna_pin_6_5") ],
"out": [ ("SD1", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 8.57142857142857E-07,
}
,
{
"id": "73",
"type": "linear",

"in": [ ("SD1", "pdna_pin_6_1"), ("SD1", "pdna_pin_6_2"), ("SD1", "9"), ("SD1", "pdna_pin_6_3"), ("SD1", "pdna_pin_6_4"), ("SD1", "pdna_pin_6_5") ],
"out": [ ("SD1", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 8.57142857142857E-07,
}
,
{
"id": "74",
"type": "linear",

"in": [ ("R60", "2") ],
"out": [ ("R60", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 1000,
}
,
{
"id": "75",
"type": "linear",

"in": [ ("Q4", "3") ],
"out": [ ("Q4", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "76",
"type": "linear",

"in": [ ("SW3", "1") ],
"out": [ ("SW3", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'SIG_PWR1', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.1, 'Thickness': 0.00011481},
        {'name': 'GND1', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.8, 'Thickness': 0.00080896},
        {'name': 'GNS2', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.1, 'Thickness': 0.00011481},
        {'name': 'SIG_PWR2', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
