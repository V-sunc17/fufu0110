# fufu F87441C
# fufu 2020/10/12 13:13
import difflib
from nltk.tokenize import LineTokenizer, SpaceTokenizer, TweetTokenizer
from nltk import word_tokenize
import re

def text_match(text, patterns):
    if re.search(patterns,text):
        return re.search(patterns,text)
    else:
        return 'Not found'

#---------text_match----------------------------------------------------------------------------------------------


CCC = text_match('''澎湃新闻（www.thepaper.cn）梳理发现，9月24日，青岛市在对青岛港大港公司进口冷链产品装卸工人进行定期例行检测时，发现2例新型冠状病毒肺炎无症状感染者。10月11日，青岛市又发现3例新冠肺炎无症状感染者
随后，青岛将上述3例无症状感染者的密切接触者和市胸科医院相关人员作为''',"青岛")

#CCC = text_match('''asdccc''',"ccc")
print("CCC text_match",CCC)
print("CCC text_match",CCC.start())
print("CCC text_match",CCC.group(0))  #青岛
print("CCC text_match",CCC.groups())
print("CCC text_match",CCC.group()) #青岛

print("-------------------------------------------------------------")
print("-------------------------------------------------------------")
#---------line split----------------------------------------------------------------------------------------------
lTokenizer = LineTokenizer();
#Print("lTokenizer result:",
AAA = lTokenizer.tokenize('''澎湃新闻（www.thepaper.cn）梳理发现，9月24日，青岛市在对青岛港大港公司进口冷链产品装卸工人进行定期例行检测时，发现2例新型冠状病毒肺炎无症状感染者。10月11日，青岛市又发现3例新冠肺炎无症状感染者
随后，青岛将上述3例无症状感染者的密切接触者和市胸科医院相关人员作为高风险人群进行重点监测，共排查到密切接触者和市胸科医院所有在院患者及陪护人员377人，其中新增核酸检测结果阳性9人，包括8名市胸科医院在院患者及陪护人员、1名患者家属，经专家组判定，其中4例为确诊病例、5例为无症状感染者。
青岛市卫健委通报称，截至10月11日23时，青岛市共发现6例确诊病例，6例无症状感染者。到目前发现的所有确诊病例和无症状感染者均与市胸科医院高度关联。而市胸科医院部分独立区域承担着收治境外输入新冠病毒感染者的任务。
澎湃新闻（www.thepaper.cn）注意到，山东正调集全省流调和检测方面的机动力量，赴青岛提供支持。山东省委、省政府已经在青岛设立前方指挥部，青岛市正开展大规模核酸检测，全面彻底排查可能的感染者，以尽快实现城区人员检测全覆盖。
''')
print(AAA)

#---------get_close_matche----------------------------------------------------------------------------------------------
aaa = difflib.get_close_matches('（www.thepaper.cn）注意到，山东正调集全省流调和检测方面的机动力量，赴青岛提供支持。山东省委、省政府已经在青岛设立前方指挥部，青岛市正开展大规模核酸检测，全面彻底排查可能的感染者，以尽快实现城区人员检测全覆盖。',AAA,1, cutoff=0.1)

print("get_close_matche -  aaa match", aaa)