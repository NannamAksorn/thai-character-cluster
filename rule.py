# t = match begining of the line
# q = optional
# Thai consonants พยัญชนะต้น
consonant = '[กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ]'
consonantq = '[กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ]?'
tconsonant = '^[กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ]'

# Final consonant (speller) ตัวสะกด
fconsonant = '[กขคฆงจชซญฎฏฐฑฒณดตถทธนบปพฟภมยรลวศษสฬอ]'
tfconsonant = '^[กขคฆงจชซญฎฏฐฑฒณดตถทธนบปพฟภมยรลวศษสฬอ]'

# Mixed cluster consonant พยัญชนะควบกล้ำทั้งหมด
consonantc = '[กขคจฉซตถทบปผพฟศส]'
tconsonantc = '^[กขคจฉซตถทบปผพฟศส]'

# Cluster consonant with lo พยัญชนะควบ "ล"
consonantl = '[กขคฉถบปผพฟ]'
tconsonantl = '^[กขคฉถบปผพฟ]'

# Cluster consonant with wo พยัญชนะควบ "ว"
consonantw = '[กขค]'
tconsonantw = '^[กขค]'

# Cluster consonant with ho พยัญชนะ "ห" นำ
consonanth = '[งญนมยรลว]'

# Final character in mae kor kar กก, กด, กบ, กง, กน, กม, + กอ
fkconsonant = '[กดบงนมอ]'

# Thai vowel character
vowel = '[ะาิีึืุูโเแัำไใฤฦ]'
vowelq = '[ะาิีึืุูโเแัำไใฤฦ]?'

# Thai Front vowel
fvowel = '[เแไใโ]'

# Thai tonal mark
tone = "[ ่ ้ ๋ ๊ ]".replace(" ", "")
toneq = '[ ่่ ้ ๋ ๊ ]?'. replace(" ", "")

# Thai number
number = '[๐๑๒๓๔๕๖๗๘๙]'

# Thai special character
special = '[็์ฯๆาฺํ()!?:;,.]'

# Character that must follow a character
strongbondchar = '[ะัาำิีึืฺุู็่้๊๋์]'
nstrongbondchar = '[^ะัาำิีึืฺุู็่้๊๋์]'

# Character that never used in start position (of word)
nonstartchar = '[ะัาำิีึืฺุูิี้่็๋๊ํ]'
startchar = '[^ะัาำิีึืฺุูิี้่็๋๊ํ]'

# Character that never used in end position (of word)
nonendchar = '[เแโใไั]'

# Character that never used in the second position (of word)
nonsecondchar = '[ๆ์]'

# English Alphabet
alphabet = '[A-Za-z]'

# Number
number = '[0-9]'

# ------------------------ Default Rule ----------------------
# Rule d1 ; ฯลฯ
rule_d1 = r'(ฯลฯ)'

# Rule d2 ; Alphabet
rule_d2 = r'({}+)'.format(alphabet)

# Rule d3 ; Number
rule_d3 = r'({}+)'.format(number)

# Rule d4 ; Attach ร์, ดิ์, ตร์, ทธิ์, ถุ์ to the existing previous unit
rule_d4 = r'({}{}{}์)'.format(consonant, consonantq, vowelq)

# Rule d5 ; Attach non-starting char to the existing previous unit
rule_d5 = r'({})'.format(nonstartchar)

# ---- Level 0 very risky rule, apply to all types of cluster -----
# Rule l0.1 ใคร, ใกล้ ???? สา|เกล้|น|แก้ว, โคล้|อมวง X next must be fvowel
rule_l0_1 = r'([เแไใโ]{}[รลว]{}){}'.format(consonantc,toneq,fvowel)

# Rule l0.2 ; ไหน, ไหล่ X Edited
rule_l0_2 = r'([เแไใโ]ห{}{}){}'.format(consonanth, toneq, startchar)

# Rule l0.3 ; ครัว, ครั้ง ???? สิ|บวัน
rule_l0_3 = r'({}[รลว]ั{}{})'.format(consonantc,toneq,fconsonant)

# Rule l0.4 ; หนัง, หยั่ง
rule_l0_4 = r'(ห{}ั{}{})'.format(consonanth, toneq,fconsonant)

# Rule l0.5 ; คลำ, ประ, ??? แบ|บระ|บบ, แบ|บระ|ดับ
rule_l0_5 = r'({}[รลว]{}[ะำ])'.format(consonantc,toneq)

# Rule l0.6 ; หนำ, หวะ
rule_l0_6 = r'(ห{}{}[ะำ])'.format(consonanth, toneq)

# Rule l0.7 ; เสร็จ
rule_l0_7 = r'([เแ]{}[รลว]็{})'.format(consonantc,fconsonant)

# Rule l0.8 ; เหม็น
rule_l0_8 = r'([เแ]ห{}็{})'.format(consonanth,fconsonant)

# Rule l0.9 ; แคระ, โคร่ะ ???? แประ|ยะ
rule_l0_9 = r'([เแโ]{}[รลว]{}ะ)'.format(consonantc, toneq)

# Rule l0.10 ; โหละ โหล่ะ
rule_l0_10 = r'([เแโ]ห{}{}ะ)'.format(consonanth, toneq)

# Rule l0.11 ; เพราะ, เพร๋าะ
rule_l0_11 = r'(เ{}[รลว]{}าะ)'.format(consonantc, toneq)

# Rule l0.12 ; เหวาะ, เหร๊าะ
rule_l0_12 = r'(เห{}{}าะ)'.format(consonanth, toneq)

# Rule l0.13 ; เคว้า, เขย่า ??? เทลา|ด
rule_l0_13 = r'(เ{}[รลว]{}า)'.format(consonantc, toneq)

# Rule l0.14 ; เหว่า
rule_l0_14 = r'(เห{}{}า)'.format(consonanth, toneq)

# Rule l0.15 ; เกรอะ
rule_l0_15 = r'(เ{}[รลว]{}อะ)'.format(consonantc, toneq)

# Rule l0.16 ; เหล้อะ
rule_l0_16 = r'(เห{}{}อะ)'.format(consonanth, toneq)

# Rule l0.17 ; เคล๋ ????
rule_l0_17 = r'(เ{}[รลว]{})'.format(consonantc, toneq)

# Rule l0.18 ; เหล๋ ???
rule_l0_18 = r'(เห{}{})'.format(consonanth, toneq)

# Rule l0.19 ; เคลียะ
rule_l0_19 = r'(เ{}[รลว]ี{}ยะ)'.format(consonantc, toneq)

# Rule l0.20 ; เหรียะ
rule_l0_20 = r'(เห{}ี{}ยะ)'.format(consonanth, toneq)

# Rule l0.21 ; เครือะ
rule_l0_21 = r'(เ{}[รลว]ื{}อะ)'.format(consonantc, toneq)

# Rule l0.22 ; เหรือะ
rule_l0_22 = r'(เห{}ื{}อะ)'.format(consonanth, toneq)

# -- Level 1 cluster consonant may take additional final consonant. --
# Rule l1.1 ; ??? ค้า:15|เสรียั:l1_1|ง:d5| X followed by starter
rule_l1_1 = r'(เ{}[รลว]ี?{}ย){}'.format(consonantc, toneq,startchar)

# Rule l1.2 ; เหลี่ย|ม
rule_l1_2 = r'(เห{}ี?{}ย)'.format(consonanth, toneq)

# Rule l1.3 ; เคลือ เครอ
rule_l1_3 = r'(เ{}[รลว]ื?{}อ)'.format(consonantc, toneq)

# Rule l1.4 ; เหลือ
rule_l1_4 = r'(เห{}ื{}อ)'.format(consonanth, toneq)

# Rule l1.5 ; ???? มา|กว่า
rule_l1_5 = r'({}[รลว]{}า)'.format(consonantc,toneq)

# Rule l1.6 ; หนา, หน้า
rule_l1_6 = '(ห{}{}า)'.format(consonanth,toneq)

# Rule l1.7 ; ???? คลูก
rule_l1_7 = '({}[รลว][ิีุู]{})'.format(consonantc,toneq)

# Rule l1.8 ; หลี|อ
rule_l1_8 = '(ห{}[ิี]{})'.format(consonanth, toneq)

# ---------- Level 2 never take any more final consonant. ----------
# Rule 1 ; กัน
rule_1 = '({}ั{}{})'.format(consonant,toneq,fconsonant)

# Rule 1.1 ; ก็
rule_1_1 = '({}็)'.format(consonant)

# Rule 1.2 ; กำ น่ะ
rule_1_2 = '({}{}[ะำ])'.format(consonant, toneq)

# Rule 2 ; กั๊วะ
rule_2 = '({}ั{}วะ)'.format(consonant, toneq)

# Rule 3 ; เห็น
rule_3 = '([เแ]{}็{})'.format(consonant, fconsonant)

# Rule 4 ; โฮ๋ะ
rule_4 = '([เแโ]{}{}ะ)'.format(consonant, toneq)

# Rule 5 ; เงาะ
rule_5 = '(เ{}{}าะ)'.format(consonant, toneq)

# Rule 6 ; เงา
rule_6 = '(เ{}{}า)'.format(consonant, toneq)

# Rule 7 ; เงอะ
rule_7 = '(เ{}{}อะ)'.format(consonant, toneq)

# Rule 8 ; เงิก
rule_8 = '(เ{}ิ{}{})'.format(consonant, toneq, fconsonant)

# Rule 9 ; เงียะ
rule_9 = '(เ{}ี{}ยะ)'.format(consonant, toneq)

# Rule 10 ; เงือะ 
rule_10 =  '(เ{}ื{}อะ)'.format(consonant, toneq)

# Rule 11 ; หวย ??? ค|ล่|อ|ง|แค|ล่วดี|
rule_11 = '({}{}ว{}){}'.format(consonant, toneq, fconsonant,startchar)

# Rule 12 ; กฤศ ??? ล|ดฤท|ธิ์|
rule_12 = '({}ฤ{})'.format(consonant, fconsonant)

# Rule 12.1 ; ให้
rule_12_1 = '(ใ{}{})'.format(consonant, toneq)

# Rule 16.1 ; หืม
rule_16_1 = '({}[ื]{}{})'.format(consonant, toneq, fconsonant)

# --- Level 3 may take additional final consonant ---
# Rule 13 ; เมีย
rule_13 = '(เ{}ี{}ย)'.format(consonant, toneq)

# Rule 14 ; เสือ, เออ
rule_14 = '(เ{}ื{}อ){}'.format(consonant, toneq, startchar)

# Rule 14e ; เสือ
rule_14e = '(เ{}ื{}อ)'.format(consonant, toneq)

# Rule 15 ; ง่า
rule_15 = '({}{}า)'.format(consonant, toneq)

# Rule 16 ; งี่ งิ งุ งู
rule_16 = '({}[ิีุู]{})'.format(consonant, toneq)

# Rule 17 ; แง่
rule_17 = '([เแไโ]{}{})'.format(consonant, toneq)

# ------- Ad hoc rule --------
# Rule a1 ; อย่า ??? ห่|อยา|
rule_a1 = '(อย{}า)'.format(toneq)

# Rule a2 ; อยู่ ??? ข้|อยุ|ติ
rule_a2 = '(อย[ูุ]{})'.format(toneq)

# Rule a3 ; หล่น
rule_a3 = '(ห{}{}{})'.format(consonanth, tone, fkconsonant)

# Rule a4 ; หน่วย
rule_a4 = '(ห{}{}ว{})'.format(consonanth, tone, fconsonant)

# Rule a5 ; ช่ง
rule_a5 = '({}{}{})'.format(consonant, tone, fkconsonant)
# Rule a6 ; อ้วน
rule_a6 = '(อ{}ว{})'.format(tone, fkconsonant)


# ----- All TCC rules. Please Comment out risky rule -----
rules = {
    'd1': rule_d1, # ฯลฯ
    'd2': rule_d2, # Alphabet
    'd3': rule_d3, # Number
    'd4': rule_d4, # Attach ร์, ดิ์, ตร์, ทธิ์, ถุ์ to the existing previous unit
    'd5': rule_d5, # Attach non-starting char to the existing previous unit
    'l1_4': rule_l1_4,
#    'l0_1': rule_l0_1, # ใคร, ใกล้ ???? สา|เกล้|น|แก้ว, โคล้|อมวง, ใหญ่:l0_2|โตร:l0_1|โห:17|ฐา:15|น:x|
    'l0_2': rule_l0_2,  # ไหน, ไหล่
#    'l0_3': rule_l0_3, # ครัว, ครั้ง ???? สิ|บวัน
    'l0_4': rule_l0_4,  # หนัง, หยั่ง
#    'l0_5': rule_l0_5, # คลำ, ประ, ??? แบ|บระ|บบ, แบ|บระ|ดับ
    'l0_6': rule_l0_6,  # หนำ, หวะ
    'l0_7': rule_l0_7,  # เสร็จ
    'l0_8': rule_l0_8,  # เหม็น
#    'l0_9': rule_l0_9, # แคระ, โคร่ะ ???? แประ|ยะ
    'l0_10': rule_l0_10,
    'l0_11': rule_l0_11,
    'l0_12': rule_l0_12,
#    'l0_13': rule_l0_13, # เคว้า, เขย่า ??? เทลา|ด
    'l0_14': rule_l0_14,
    'l0_15': rule_l0_15,
    'l0_16': rule_l0_16,
#    'l0_17': rule_l0_17, # เคล๋ ????
#    'l0_18': rule_l0_18, # เหล๋ ????
    'l0_19': rule_l0_19,
    'l0_20': rule_l0_20,
    'l0_20': rule_l0_20,
    'l0_21': rule_l0_21,
    'l0_22': rule_l0_22,
    
    'l1_1': rule_l1_1, # ??? ค้า:15|เสรียั:l1_1|ง:d5| X
    'l1_2': rule_l1_2,
#    'l1_3': rule_l1_3,

#    'l1_5': rule_l1_5,
    'l1_6': rule_l1_6,
#    'l1_7': rule_l1_7,
    'l1_8': rule_l1_8,
    
    '1': rule_1,
#    '1_1': rule_1_1, # เพล่่ยั|ง
    '1_2': rule_1_2,
    '2': rule_2,
    '3': rule_3,
    '4': rule_4,
    '5': rule_5,
    '6': rule_6,
#    '7': rule_7, # เทอะ|ไร
    '8': rule_8,
    '9': rule_9,
    '10': rule_10,
#    '11': rule_11, # ค|ล่|อ|ง|แค|ล่วดี|
#    '12': rule_12, # ??? ล|ดฤท|ธิ์|
    '12_1': rule_12_1,
    '16_1': rule_16_1,
    
    '13': rule_13,
    '14': rule_14,
    '14e': rule_14e,
    '15': rule_15,
    '16': rule_16,
    '17': rule_17,
    
#    'a1': rule_a1, # ห่|อยา|
#    'a2': rule_a2, # อยู่ ??? ข้|อยุ|ติ
    'a3': rule_a3,
    'a4': rule_a4,
#    'a5': rule_a5,
    'a6': rule_a6
}