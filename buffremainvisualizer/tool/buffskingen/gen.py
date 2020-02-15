import xml.etree.ElementTree as ET
import pandas
import re
import glob
datapath="E:\\Analyze\\newtos\\extract\\"
xmltable={}
bufftable={}
def main():
    global xmltable

    global bufftable
    alldata=""

    for s in glob.glob(datapath + "ui.ipf\\baseskinset\\*.xml"):
        p=ET.parse(s)
        r=p.getroot()
        for c in r :
            for i in c:
                if(i.tag=="image"):
                    if("name" in i.attrib):
                        xmltable[i.attrib["name"]]={
                            "name":i.attrib["name"],
                            "file":i.attrib["file"],
                            "imgrect":i.attrib["imgrect"],
                        }
    for s in glob.glob(datapath+"ies.ipf\\buff*.ies"):
        p=pandas.read_csv(s,encoding='utf-8')
        for r in p.iterrows():
            if("Icon" in r[1]):
                iconname="icon_"+str(r[1]["Icon"])
                if iconname in xmltable:
                    bufftable[iconname]=xmltable[iconname]

    # gen
    root=ET.Element("skinset")
    tree=ET.ElementTree(element=root)
    imglist=ET.SubElement(root,"skinlist")
    imglist.set("category","bmvaddon")
    for s in bufftable.values() :
        skin=ET.SubElement(imglist,"skin")
        skin.set("name","bmvaddon_"+s["name"])
        skin.set("texture",s["file"])
        # elem = ET.SubElement(skin, "img")
        # elem.set("name", "slot")
        # elem.set("imgrect", s["imgrect"])
        # elem = ET.SubElement(skin, "img")
        # elem.set("name", "mouseon")
        # elem.set("imgrect", s["imgrect"])
        # elem = ET.SubElement(skin, "img")
        # elem.set("name","selected")
        # elem.set("imgrect",s["imgrect"])

        elem = ET.SubElement(skin, "img")
        elem.set("name", "cooltime")
        elem.set("imgrect", s["imgrect"])

    tree.write("bmv_buff.xml",encoding='utf-8', xml_declaration=True)

if __name__=="__main__":
    main()
