#!/usr/bin/python3

import nbtlib
from pprint import pprint

#
# electricalAgeWorld<DIM>.dat:
# This seems to store all of the components placed in the world.
# |- nodes
# \- ghost
#

# This node looks to be a sixnode.
#'n0': {'ED0': {'front': Byte(1),
#                'outputGateProcessU': Double(50.0),
#                'outputGateProcesshighImpedance': Byte(0),
#                'outputGateUc': Float(49.99995040893555),
#                'sixFront': Byte(1)},
#        'ED3': {'LSPstableProb': Double(0.0),
#                'alphaZ': Float(0.0),
#                'channel': String('ccsystems_lights'),
#                'color': Byte(15),
#                'front': Byte(7),
#                'inv': List[Compound]([Compound({'Slot': Byte(0), 'id': Short(4669), 'Count': Byte(1), 'tag': Compound({}), 'Damage': Short(294)}), Compound({'Slot': Byte(1), 'id': Short(762), 'Count': Byte(1), 'Damage': Short(2056)})]),
#                'lbCoordInstd': Int(0),
#                'lbCoordInstx': Int(-77),
#                'lbCoordInsty': Int(65),
#                'lbCoordInstz': Int(204),
#                'light': Int(0),
#                'positiveLoadUc': Float(0.0),
#                'poweredByLampSupply': Byte(0),
#                'sixFront': Byte(3)},
#        'EID0': Short(6081),
#        'EID1': Short(0),
#        'EID2': Short(0),
#        'EID3': Short(4101),
#        'EID4': Short(0),
#        'EID5': Short(0),
#        'cacheBlockId': Int(0),
#        'cacheBlockMeta': Byte(0),
#        'node': {'NBOpaque': Byte(63),
#                 'NBWrap': Byte(38),
#                 'cd': Int(0),
#                 'cx': Int(-77),
#                 'cy': Int(65),
#                 'cz': Int(204),
#                 'lastLight': Byte(0)},
#        'tag': String('s')},

# This node looks to be a pole
# 'n1': {'eid': Short(7876),
#        'element': {'electricalLoadUc': Float(14575.5576171875),
#                    'gridLinks': {'0': {'Count': Byte(17),
#                                        'Damage': Short(2060),
#                                        'ad': Int(0),
#                                        'as': Byte(3),
#                                        'ax': Int(-86),
#                                        'ay': Int(67),
#                                        'az': Int(156),
#                                        'bd': Int(0),
#                                        'bs': Byte(3),
#                                        'bx': Int(-70),
#                                        'by': Int(67),
#                                        'bz': Int(161),
#                                        'id': Short(762),
#                                        'rs': Double(1.7000000000000002)},
#                                  '1': {'Count': Byte(5),
#                                        'Damage': Short(2060),
#                                        'ad': Int(0),
#                                        'as': Byte(3),
#                                        'ax': Int(-86),
#                                        'ay': Int(67),
#                                        'az': Int(151),
#                                        'bd': Int(0),
#                                        'bs': Byte(3),
#                                        'bx': Int(-86),
#                                        'by': Int(67),
#                                        'bz': Int(156),
#                                        'id': Short(762),
#                                        'rs': Double(0.5)}},
#                    'others': Byte(13),
#                    'thermalLoadTc': Float(0.007191025651991367)},
#        'node': {'NBOpaque': Byte(63),
#                 'NBWrap': Byte(43),
#                 'cd': Int(0),
#                 'cx': Int(-86),
#                 'cy': Int(67),
#                 'cz': Int(156),
#                 'lastLight': Byte(0)},
#        'tag': String('t')},

# This looks to be a six node.
# 'n10': {'ED2': {'channel': String('System Motors'),
#                 'connection': Byte(1),
#                 'outputGateProcessU': Double(0.0),
#                 'outputGateProcesshighImpedance': Byte(0),
#                 'outputGateUc': Float(0.0),
#                 'selectedAggregator': Int(0),
#                 'sixFront': Byte(0),
#                 'toogleAggregatoroldValue': Double(1.0),
#                 'toogleAggregatorstate': Byte(0)},
#         'EID0': Short(0),
#         'EID1': Short(0),
#         'EID2': Short(5888),
#         'EID3': Short(0),
#         'EID4': Short(0),
#         'EID5': Short(0),
#         'cacheBlockId': Int(0),
#         'cacheBlockMeta': Byte(0),
#         'node': {'NBOpaque': Byte(63),
#                  'NBWrap': Byte(59),
#                  'cd': Int(0),
#                  'cx': Int(-149),
#                  'cy': Int(67),
#                  'cz': Int(190),
#                  'lastLight': Byte(0)},
#         'tag': String('s')},

# This looks to be a shaft clutch.
#'n103': {'eid': Short(273),
#          'element': {'clutchInUc': Float(0.0),
#                      'inv': List[Compound]([Compound({'Slot': Byte(0), 'id': Short(4669), 'Count': Byte(1), 'tag': Compound({'wear': Double(0.03110965616335245)}), 'Damage': Short(7736)}), Compound({'Slot': Byte(1), 'id': Short(4669), 'Count': Byte(1), 'Damage': Short(7735)})]),
#                      'leftShaftrads': Float(802.020263671875),
#                      'others': Byte(8),
#                      'rightShaftrads': Float(0.0),
#                      'shaftrads': Float(0.0),
#                      'sides': Int(48),
#                      'slipping': Byte(1)},
#          'node': {'NBOpaque': Byte(63),
#                   'NBWrap': Byte(9),
#                   'cd': Int(0),
#                   'cx': Int(-80),
#                   'cy': Int(62),
#                   'cz': Int(235),
#                   'lastLight': Byte(0)},
#          'tag': String('t')},

#
#{'ghost': {'n0': {'UUID': Int(-1),
#                  'elemCoordd': Int(0),
#                  'elemCoordx': Int(-94),
#                  'elemCoordy': Int(69),
#                  'elemCoordz': Int(236),
#                  'obserCoordd': Int(0),
#                  'obserCoordx': Int(-94),
#                  'obserCoordy': Int(67),
#                  'obserCoordz': Int(236)},
#


#
# eln.worldStorage0.dat
# Not exactly sure what this is used for. Has a list of ghost cords to element cords.
#
# data
# |- nodes
# |- ghost
# |  \ 'n78': { 'UUID': Int(-1),
#                'elemCoordd': Int(0),
#                'elemCoordx': Int(-107),
#                'elemCoordy': Int(73),
#                'elemCoordz': Int(233),
#                'obserCoordd': Int(0),
#                'obserCoordx': Int(-108),
#                'obserCoordy': Int(73),
#                'obserCoordz': Int(232)},
# \- dim: Int(0)
#


nbt_file = nbtlib.load('examples/electricalAgeWorld0.dat')
#nbt_file = nbtlib.load('examples/eln.worldStorage0.dat')

#print("loaded")

#pprint(nbt_file.root["nodes"])

totalSixPop = 0

def parseRegSix(node):
    global totalSixPop

    # Each side has a EID<N>: short which is the code for the element type
    # If it is 0, the node is unpopulated.
    # If it exists, there is also an ED<N> that has the properties for it.

    myCount = 0

    for entry in node:
        if (entry[0:3] == "EID"):
            if (node[entry] != 0):
                #print(node[entry])
                totalSixPop += 1

    #pprint(node)
    return myCount != 0 # for now, things are good in the hood.

def parseRegTrans(node):

    #print("==============")

    eid = node["eid"]
    element = node["element"]
    #print(eid)
    if (eid == 129):
        pprint(node)

    return True

def parseRegComp(node):
    # TODO: check ioGateXUc and the process high impedance and may be the U in process.

    # TODO: check wireless channel info

    """    NBOpaque': Byte(63),
    'NBWrap': Byte(59),
    'SNdescriptorKey': String(''),
    'SNfront': Byte(3),
    'cd': Int(0),
    'cx': Int(-108),
    'cy': Int(71),
    'cz': Int(292),
    'ioGate0Uc': Float(0.0),
    'ioGate1Uc': Float(0.0),
    'ioGate2Uc': Float(0.0),
    'ioGate3Uc': Float(0.0),
    'ioGate4Uc': Float(0.0),
    'ioGate5Uc': Float(0.0),
    'ioGateProcess0U': Double(0.0),
    'ioGateProcess0highImpedance': Byte(1),
    'ioGateProcess1U': Double(0.0),
    'ioGateProcess1highImpedance': Byte(1),
    'ioGateProcess2U': Double(0.0),
    'ioGateProcess2highImpedance': Byte(1),
    'ioGateProcess3U': Double(0.0),
    'ioGateProcess3highImpedance': Byte(1),
    'ioGateProcess4U': Double(0.0),
    'ioGateProcess4highImpedance': Byte(1),
    'ioGateProcess5U': Double(0.0),
    'ioGateProcess5highImpedance': Byte(1),
    'tag': String('ElnComputerProbe'),
    'wirelessTxCount': Int(0)}"""

    #pprint(node)
    return True # for now, this node passes

def parseRegExport(node):

    # TODO: Check input vales.

    # R is the resistance of the device. It can either be High-Z or a calculated value:

    """double factor = Math.min(1, energyMiss / energyBufferMax * 2);
    if (factor < 0.005) factor = 0;
    double inP = factor * inPowerMax * inPowerFactor;
    powerInResistor.setR(inStdVoltage * inStdVoltage / inP);"""

    # inPowerFactor should probably be between 0 and 1

    # energyBufferMax = maxP (per tier) * 2

    # loadUc is part of NbtElectricalLoad.

    """{'NBOpaque': Byte(63),
    'NBWrap': Byte(57),
    'R': Double(1000000000.0),
    'SNdescriptorKey': String('EnergyConverterElnToOtherMVU'),
    'SNfront': Byte(0),
    'cd': Int(0),
    'cx': Int(-72),
    'cy': Int(69),
    'cz': Int(303),
    'energyBuffer': Double(0.09661806867870837),
    'inPowerFactor': Double(0.25999999046325684),
    'loadUc': Float(0.0),
    'tag': String('ElnToOther')}"""

    #pprint(node)
    return True # for now, this node passess

def parseRegular(nbt_file):

    tCount = 0
    sCount = 0
    probeCount = 0
    exporterCount = 0

    print("This would handle a regular file")
    for node in nbt_file.root["nodes"]:
        tag = nbt_file.root["nodes"][node]["tag"]
        if (tag == "t"):
            # This is a TransparentNode
            #print("TransparentNode")
            parseRegTrans(nbt_file.root["nodes"][node])
            tCount += 1
        elif(tag == "s"):
            # This is a SixNode
            #print("SixNode")
            parseRegSix(nbt_file.root["nodes"][node])
            sCount += 1
            #pprint(nbt_file.root["nodes"][node])
        elif(tag == "ElnComputerProbe"):
            # This is an Electrical Age computer probe
            #print("Electrical Age Computer Probe")
            parseRegComp(nbt_file.root["nodes"][node])
            probeCount += 1
        elif(tag == "ElnToOther"):
            # This is an Eln Energy Converter
            #print("Electrical Age Energy Expoter")
            parseRegExport(nbt_file.root["nodes"][node])
            exporterCount += 1
        else:
            print("WAT: {}".format(tag))
            pprint(nbt_file.root["nodes"][node])

    print("TransparentNode Count: {}".format(tCount))
    print("SixNode Count: {}".format(sCount))
    print("Total Six: {}".format(totalSixPop))
    print("Computer Probes: {}".format(probeCount))
    print("Energy Exporters: {}".format(exporterCount))
    # Step 2: Parse the regular nodes one by one

    # Step 3: Find all of the ghost nodes, and map them to the correct element nodes

def parseWorldStorage(nbt_file):
    print("currently, we don't handle worldStorage files")


# Step 1: Determine whether it's a world node file or the other "world storage" format
# This can be determined by discovering if it has the "dim" tag (int) on root.

if ("dim" in nbt_file.root):
    parseWorldStorage(nbt_file)
else:
    parseRegular(nbt_file)
