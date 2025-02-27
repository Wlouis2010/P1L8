# coding: utf-8
# Bovenstaande comment is noodzakelijk voor een goede werking
bestand_nummer = 1
ontcijfersleutel = {'\n': '', '': '\n', '⢶': '⠀', '⠀': '⠁', '⢘': '⠂', '⢳': '⠃', '⣛': '⠄', '⠯': '⠅', '⢧': '⠆', '⠓': '⠇', '⠈': '⠈', '⡝': '⠉', '⠰': '⠊', '⠽': '⠋', '⣞': '⠌', '⠦': '⠍', '⡽': '⠎', '⠆': '⠏', '⡏': '⠐', '⡥': '⠑', '⣲': '⠒', '⣺': '⠓', '⢩': '⠔', '⢊': '⠕', '⢠': '⠖', '⡶': '⠗', '⡸': '⠘', '⣹': '⠙', '⢝': '⠚', '⡗': '⠛', '⠂': '⠜', '⣻': '⠝', '⡅': '⠞', '⣋': '⠟', '⠬': '⠠', '⢉': '⠡', '⠒': '⠢', '⣑': '⠣', '⣽': '⠤', '⡬': '⠥', '⣸': '⠦', '⣿': '⠧', '⠨': '⠨', '⢑': '⠩', '⠪': '⠪', '⣊': '⠫', '⡰': '⠬', '⠎': '⠭', '⢈': '⠮', '⢲': '⠯', '⢅': '⠰', '⢀': '⠱', '⢏': '⠲', '⣅': '⠳', '⠲': '⠴', '⡂': '⠵', '⢍': '⠶', '⢖': '⠷', '⠺': '⠸', '⡞': '⠹', '⡿': '⠺', '⢌': '⠻', '⢰': '⠼', '⢦': '⠽', '⠚': '⠾', '⡾': '⠿', '⠗': '⡀', '⡷': '⡁', '⣇': '⡂', '⡎': '⡃', '⡋': '⡄', '⣏': '⡅', '⣚': '⡆', '⠑': '⡇', '⡔': '⡈', '⣎': '⡉', '⡹': '⡊', '⡯': '⡋', '⣰': '⡌', '⡕': '⡍', '⢆': '⡎', '⡁': '⡏', '⡍': '⡐', '⠫': '⡑', '⠛': '⡒', '⡺': '⡓', '⡌': '⡔', '⢙': '⡕', '⢓': '⡖', '⠩': '⡗', '⠭': '⡘', '⡖': '⡙', '⠏': '⡚', '⢐': '⡛', '⡆': '⡜', '⢪': '⡝', '⠸': '⡞', '⡇': '⡟', '⣣': '⡠', '⠥': '⡡', '⢁': '⡢', '⡲': '⡣', '⡩': '⡤', '⣒': '⡥', '⠷': '⡦', '⠌': '⡧', '⠣': '⡨', '⢟': '⡩', '⡑': '⡪', '⣯': '⡫', '⡭': '⡬', '⡉': '⡭', '⣆': '⡮', '⣩': '⡯', '⠋': '⡰', '⡡': '⡱', '⡘': '⡲', '⡵': '⡳', '⠃': '⡴', '⢿': '⡵', '⣫': '⡶', '⠶': '⡷', '⣠': '⡸', '⢢': '⡹', '⣃': '⡺', '⡀': '⡻', '⠜': '⡼', '⢨': '⡽', '⡟': '⡾', '⡐': '⡿', '⣷': '⢀', '⣖': '⢁', '⠡': '⢂', '⣝': '⢃', '⣟': '⢄', '⡱': '⢅', '⣀': '⢆', '⣓': '⢇', '⠾': '⢈', '⡤': '⢉', '⡢': '⢊', '⣕': '⢋', '⢴': '⢌', '⡜': '⢍', '⣴': '⢎', '⢗': '⢏', '⣙': '⢐', '⡨': '⢑', '⢬': '⢒', '⢽': '⢓', '⡳': '⢔', '⢃': '⢕', '⢇': '⢖', '⢹': '⢗', '⠧': '⢘', '⡮': '⢙', '⢡': '⢚', '⡃': '⢛', '⠹': '⢜', '⠁': '⢝', '⡠': '⢞', '⠄': '⢟', '⠞': '⢠', '⡚': '⢡', '⢷': '⢢', '⢛': '⢣', '⡧': '⢤', '⠊': '⢥', '⣾': '⢦', '⠕': '⢧', '⠖': '⢨', '⠅': '⢩', '⡣': '⢪', '⠮': '⢫', '⣮': '⢬', '⣭': '⢭', '⣡': '⢮', '⡄': '⢯', ' ': '⢰', '⢾': '⢱', '⢼': '⢲', '⠱': '⢳', '⣗': '⢴', '⣍': '⢵', '⣤': '⢶', '⠵': '⢷', '⡊': '⢸', '⢕': '⢹', '⢚': '⢺', '⣈': '⢻', '⣥': '⢼', '⠢': '⢽', '⢎': '⢾', '⢄': '⢿', '⠉': '⣀', '⢸': '⣁', '⠼': '⣂', '⠘': '⣃', '⣵': '⣄', '⣐': '⣅', '⡈': '⣆', '⢜': '⣇', '⡓': '⣈', '⡼': '⣉', '⢔': '⣊', '⠟': '⣋', '⢒': '⣌', '⣄': '⣍', '⣼': '⣎', '⢞': '⣏', '⡙': '⣐', '⠔': '⣑', '⢭': '⣒', '⢥': '⣓', '⣁': '⣔', '⣬': '⣕', '⠙': '⣖', '⣶': '⣗', '⢣': '⣘', '⢮': '⣙', '⢂': '⣚', '⣌': '⣛', '⡪': '⣜', '⠳': '⣝', '⣂': '⣞', '⢫': '⣟', '⣜': '⣠', '⠤': '⣡', '⢵': '⣢', '⣨': '⣣', '⢤': '⣤', '⠍': '⣥', '⡴': '⣦', '⢋': '⣧', '⢯': '⣨', '⣧': '⣩', '⠠': '⣪', '⡦': '⣫', '⡻': '⣬', '⡛': '⣭', '⣉': '⣮', '⣱': '⣯', '⣘': '⣰', '⠿': '⣱', '⢻': '⣲', '⠻': '⣳', '⣳': '⣴', '⣔': '⣵', '⢺': '⣶', '⣪': '⣷', '⢱': '⣸', '⣦': '⣹', '⠴': '⣺', '⡫': '⣻', '⠇': '⣼', '⠐': '⣽', '⣢': '⣾', '⠝': '⣿', '⡒': ' '}
for i in range(6):


    bestand = open(f"ascii{bestand_nummer}.txt", "r", encoding="utf8")
    print(f"\n\n\nNummer {bestand_nummer}:\n")
    bestand_nummer += 1
    for lijn in bestand:
        vertaalde_lijn = ""
        # Ontcijfer elk karakter in de lijn, en print vervolgens de ontcijferde lijn
        for teken in lijn:
            vertaalde_lijn += ontcijfersleutel[teken]
        print(vertaalde_lijn)


