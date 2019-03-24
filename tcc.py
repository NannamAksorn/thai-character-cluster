'''
Thai Character Cluster
'''
import re
import os
import codecs
from rule import rules 


class TCC():
    @staticmethod
    def segment(sentence, debug=False):
        """
        Return list of character clusters
        arg: string sentence
        """
        output = []
        rule_list = []
        rlength = 1
        i = 0
        while i < len(sentence):
            for rid in rules:
                sub_field = sentence[i:]
                match = re.match(rules[rid], sub_field)
                if match:
                    rule_list.append(rid)
                    output.append(match.group(1))
                    rlength = len(match.group(1))
                    break
            if not match:
                rlength = 1
                rule_list.append("x")
                output.append(sub_field[0])
            i += rlength
            
        # join rule d5
        if len(output) <= 0:
            return []
        temp_output = [output[0]]
        for i in range(1, len(rule_list)):
            if rule_list[i] == "d5":
                temp_output[-1] += output[i]
            else:
                temp_output.append(output[i])
        output = temp_output
        if debug:
            print("input: " , sentence)
            print("Output: ", end = " ")
            for i, o in enumerate(output):
                print('{}:{}|'.format(o,rule_list[i]), end="")
        #print("|".join(output))
        #print("|".join(rule_list))
        return output 

if __name__ == "__main__":
    print('testing')
    print(TCC.segment('สวัสดีครับ'))