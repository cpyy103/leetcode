from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if self.is_palindrome(words[i] + words[j]):
                    res.append([i, j])
        return res

    def is_palindrome(self, s):
        right = len(s) - 1
        left = 0
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution1:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        dic = {word: i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                temp1 = word[:j]  # 第一部分
                temp2 = word[j:]  # 第二部分
                # 如果第一部分的逆序存在于字典中
                if temp1[::-1] in dic and dic[temp1[::-1]] != i and temp2 == temp2[::-1]:
                    res.append([i, dic[temp1[::-1]]])
                # 如果第二部分的逆序存在于字典中
                # j > 0 避免重复第一种情况
                if j > 0 and temp2[::-1] in dic and dic[temp2[::-1]] != i and temp1 == temp1[::-1]:
                    res.append([dic[temp2[::-1]], i])
        return res


if __name__ == '__main__':
    # words = ["abcd", "dcba", "lls", "s", "sssll"]
    words = ["jiaeegadjjj", "gcbjigjd", "bjdh", "gic", "bifecigeggbjbfedcgc", "hbbjhegaicihccaeai", "gbdejaii", "gddhbc", "jiciiebbbagfgdi", "icghahfcgjb", "jdicfahacfchgacefbgb",
             "ihi", "gjgciiiejb", "jaejbhghfdecje", "ee", "bfjiaefge", "jbbcd", "dhfefbcjcg", "jeifidajbcidiejj", "gjciddfchj", "h", "cdddbgjdgagbgch", "hedgejadaf",
             "jdfgdhhiajbaafdhciae", "ijgjfadfciggfgfiii", "jfhchd", "bc", "dh", "ceajgccgijfaiddddghj", "ccihfddjehgjchaafagj", "afjidcbbihdigdghfh", "hjadcega",
             "gbbhdbihdibehfhedhba", "efbfhacj", "efjhjcadhdeedeahiagj", "gghb", "fcghiaija", "ahceicffihaeg", "ah", "c", "bcdei", "hdfcgdcejb", "jjhhbdhgdhggcchii", "ghaiiiaid",
             "ibb", "hjdiafdjcchhihfhdd", "djd", "adhbdhbgha", "bjafjhbib", "gieid", "hfcf", "fdd", "afcahfjehifhiabfdec", "dighiif", "hggfffiaaifjgjibecd", "dga", "hjjhfecjajaae",
             "ciafide", "djadfjfg", "jedebhfiaagfbah", "bcde", "gdddjfdcai", "bbfd", "bgdeagfija", "gjidc", "b", "jecdg", "chgeafjdiafjh", "abcieb", "aihfifcfihc", "hjjbj", "cch",
             "jgigdcjbbebifi", "bfhhcbjadhcgcdgc", "efee", "cdfahidhacbf", "ggejhd", "fiihc", "afhfdcjjfad", "aejjgbccj", "ahjjijbcgbdidfbddf", "djefjdefhhgadabfc",
             "dijebbgggbjefebfgc", "cadiagee", "ggfi", "hchj", "cfcdhjabdeigbfacfgjb", "fbifeiccdaechide", "djbeeeaae", "gcfigaife", "jgdcia", "cjfjigcdhcjbhabhfaa", "djcbgbc",
             "ifbcjbifibdiacgdcii", "ecj", "ggddc", "jcbagdfejfehicbhh", "ibaffbgfbac", "igeaiab", "hfbjechcjcfjhcagdbg", "hgafbjfihffia", "cebbfcijbgcfih", "bbcejdhaajcchieeje",
             "d", "iahefgcgg", "ggecgebebgf", "bb", "acdiggbhgbhgf", "gahfiejfajgdcje", "fiidjicijaaae", "cjegbe", "aijhhfjbcfhf", "gcicbjihcddijjg", "fijd", "acjfjfdcfcebahiafbb",
             "fjehjibheghacbgffeg", "ihcfciachhaghhe", "hgigheche", "gciicaeiedihejheibe", "idjdhiaejciihieccj", "hddhbefjejjijj", "jiccfbjd", "g", "eibidbagaidc", "jdbb",
             "acfgbcgbhhfccfhji", "jbijafbeehabde", "fiecbjdiecaccbfjijhg", "jdcegei", "cgbfhacff", "bcdddffheaejadbcdab", "ddacgfdbhdcjhhahhej", "cfibeeeda", "cjj", "eaiagcf",
             "edfaici", "hbihgbjiica", "gdafbhgcjghfhediigd", "fhdahdefddfccgj", "fbfhiba", "djdgjcfi", "bhfa", "bdfddfgefieff", "iagfgdcjaggiacicei", "bggijhege", "aejadfeehhd",
             "heggedbcddbedaibchh", "ijh", "egfbic", "eahcbejffdhebedjfgef", "gbjb", "cfgge", "bhcbdbg", "aebibfeffcdiaidgbhbe", "ajeiaabdhgegbfdfdegg", "hcehbhiih",
             "dhfchefjhjaffadcd", "dfhbeejjd", "bibf", "gcbabcdhb", "eehciafbddbhejac", "hhfcfcibej", "hbabbbabac", "bjeagcijdbhbbiegj", "jc", "gjedddjejaaec", "ijhbe", "fcd",
             "aaaia", "accgdejhbfiecbie", "dhid", "ebjigebccbfdhaiigfg", "icecbfcfccficdfheei", "abgadgdhhaiahabdg", "hbcbdfjdbjacggbi", "fhcbggejgdja", "dcchcahafijgdiagjh",
             "ebjie", "bfchgcdcjjidbhe", "bbefigbf", "je", "jcfcideb", "ahbdiefgjggjiicabbef", "gccai", "ehb", "chcfbicaf", "hbigifgchai", "ciieife", "bggiefbbea", "heajfgi",
             "aagbjad", "bj", "hbabi", "icabcbdegaadhdaiif", "db", "hjjdchdcajhggcjdcbc", "egbdjecehijfabjfe", "fddbhgfiihdbagjfec", "fgjcciciegh", "iiaahijgjdeiedj",
             "aeijeehhajibegh", "gabh", "dbjbacd", "gcefdihibdhahbacaifb", "ahhhh", "dijid", "hgchecii", "faebcdhdbbiggdiacb", "dagcbdbjabcaabeiefcf", "jeb", "fi", "ffghjideg",
             "eejcba", "ijaacggjbecga", "dcbhabidacj", "eifgejacgfdccciigjcf", "iafbffaejbdfeiebiej", "edegfeebeafabggbib", "dj", "chiacgb", "hcdafagfe", "iijajdeghafcgdfg",
             "fihjcgdceccb", "caeagehbfjc", "iiaigah", "fgiiaebfa", "jgjhchadbjebd", "gchb", "acijgi", "ajjdei", "bgeibfejgbejgcfjbjh", "gcecceehcbadhjj", "haehgb", "gfefa",
             "fdfdh", "cbbjgbfjgaj", "ddfafdeedj", "fagbjacgajg", "cddfbefjb", "aiaahbfiaafeigegij", "dhaieaeghggjeif", "eaeegjeaggh", "jgfjaiga", "gadh", "jhfiabfab",
             "edjbijjeiidhddhfhcej", "bieji", "cggfbdb", "behhaggdjbeicceedgjd", "fjjccb", "bhfabbdghfhhegiaigj", "egefhif", "gjffaejhigfgjiaaaj", "hg", "bdgcgefcdg",
             "jgdiiiidaed", "jafeebjibjeefeicd", "djdfadjfgbdce", "ibh", "ijjdeb", "gidghhebejcfhacig", "edbdiagedejgacicaac", "ghibbgagjjdgeieb", "bcihgajjg", "ffbjbgieejegfgaa",
             "gfgfbffegbdeib", "hiefhicjabjdfbhgaha", "ci", "dhee", "bfehhaacaggefee", "j", "hiiec", "egibffhi", "efgbbbbecjeficjcjf", "daidjfc", "igacchhedbgihiaadgja",
             "eciacijjhcjcefeebdgf", "bjhgcdcaba", "dbdahfdiifhfia", "ifchajcjfeaabdi", "fjcccejhjigefjfi", "bjhdgfjfe", "bidedgfijgabfjb", "cifbjac", "gfjddbifdgjcaihafdgj",
             "bjhfajadibbhcd", "jga", "hae", "ijdeaijbbihhdgcg", "jjfhhecefjajgdigedb", "hidihhjc", "idcgdh", "cihag", "hhghhcbh", "baffic", "i", "jbadhd", "jbjcc",
             "eifdgjefacjhheejheb", "bdhaffhdaj", "hjccbgibdhhfbb", "aaejedjiagajbf", "adcfhjefc", "iececcjf", "dbdjjfgfccaffcb", "cjdcbichg", "ecgc", "ff", "fjbediidfcjhebac",
             "jfdgdhgc", "iehgjjhfacfb", "jdjhbgaefcad", "fhdacjijfagfi", "dfgeddhificfdcacag", "jaedecbhfeijic", "egjhfehjdghdchgg", "aeb", "bhf", "gf", "bgjjjdddabcjfebbcg",
             "bejfjiebgbhefdhehfeg", "icjfecjfhecddc", "fcddcdieicicee", "heibificfejdji", "a", "ehejbjdbjbccaiagcgc", "ghfbajcdjhgaaedjfh", "hbbfehhbbjjghfgehib", "gffhahdd",
             "ibcbejgidajjegb", "ajfbdgaaige", "ahhh", "ehcjheda", "ccjjjbegdi", "ch", "ejjgaggbegjg", "bjf", "fecahi", "dhjbebbgeagdf", "hgggigaehdbcjjaj", "chha",
             "chhcajhgbbbcabjgjg", "bbajibcfb", "chdaafehiiaaegefjhbe", "iihdacbdja", "caaafjccejfcbfhjeej", "hbdab", "cdhfdjhhdgcj", "ecdgigcjfdbfaejadhdb", "fcihafigiagcefhi",
             "bbefjejajjbifadaha", "eabeiafcjfbcjagbe", "jf", "hibhgdecdbdcahfjjc", "ciffddibfjchhgbajc", "dgaabjbhf", "iiebeih", "becbihjecjfaic", "dghjfjbeejigaadefbh", "edhf",
             "jhedhhacfgecea", "iee", "gbdga", "dhiabdgaficj", "ifiegifjcjie", "dhahgb", "gffdj", "gc", "ejcggdfiahedcfg", "gdjgdifabgfc", "dbbdgfeffajhfheja",
             "ecbffdiaejbadiigbiaj", "gaaafdh", "cdacadbdbfbi", "bddbj", "fcefecjahfchhei", "ibacebfj", "dcfafhbabggfagiddga", "fhhihaabaegeicg", "bfab", "bdf", "jaf",
             "bicegfgadbfjdagfj", "icg", "djbieabjeice", "hjggfggjeghahebdb", "ejfbjaeidejgidjf", "iahgfidegihfeiaaaec", "afeidjijciib", "cdjedcagihdehcfihge", "gbhacbicfihchj",
             "jcfhbhdghbfcfjgb", "gbijiabbahbgechb", "bhjbchjgcagebdj", "hhedbecgg", "fjhgjeajeghifgh", "fgggbdbbehhiiabia", "hjjfb", "bgahgadbgfebgj", "bjajcf", "jh",
             "jccfedggjcaiehga", "aejjdfdebebifdeedj", "idiceeicbbd", "gdffgdjdbeedcbd", "bbbfcejdbjefbbg", "adghdcafgfdhadggca", "bbcifd", "jiagdejdjhicgfhdifa",
             "fdcfjedegdcdjcgafgc", "abdhjbdjfg", "dacijecjieddfefj", "hhcahheecah", "ddecafhdjahgeiafbf", "fibehccedjhfj", "fegj", "fcad", "faadfdcgjgadhajf",
             "ccdjbabdgffhdhfbjdji", "ihichbheffgfiabacdbf", "fjiffecfhf", "jdechcfdeffiaafcce", "fbiigehdcgfgbbdhcidi", "dghbdgcf", "ifjffdjjafciidfadccf", "dagegjdagfgdgag",
             "beadcfec", "fififgagefiejggfhbgh", "idfahggfhbedechgdj", "gbegaaide", "ecc", "jfjcehgc", "gbfe", "ffih", "fajijcii", "gajc", "gccegfibh", "ijiheifich",
             "ijbcbbcjddcigai", "hfdifcbgicjahjjgh", "dajceihgaiahi", "eh", "bebjcdgcccdigigagj", "cijagihahaj", "dcbfdhjhhcgge", "eega", "fbbfgdcaiajf", "hadcjhjdfcjg",
             "egjfagfdcceai", "hc", "dabgddegghd", "ebf", "dfed", "ife", "agiiggbdjdjfdcfdgh", "bgfghj", "ddcibhbeejgciec", "bagjeijihhjcicjhbe", "aaciedgfegibbjhaciaj",
             "ebchiacai", "dgfaaficcaiijfgha", "bjgfhfciegifj", "jigfchcghi", "e", "dc", "fdjbefhacbgggeaide", "daabjbbcjbgc", "dfa", "fejicdhecicjjigdffi", "edddd", "cdchcedcebc",
             "df", "abfihihee", "cjidhaf", "igaahfhcjccg", "bhjifcdajaahefgf", "hhccdjddjehfhicbbj", "eagadaabjhfgbighjah", "cbdigdhafae", "ifhb", "bjfhiifaebadadidjhji", "jdhi",
             "dehgdadejhdbcefc", "ccjcjjhh", "eahgbig", "fbbggibcaidfjgbjijf", "hicaajigfed", "hchfcbjfah", "gdjie", "cbedjachjdjegficc", "fdedihdg", "ddaddjcagbg", "iefh",
             "aadbibjcebbgcg", "gafedcgegg", "afjbiefajj", "jhcjgbiiiaeaj", "ie", "iajjggfehcifejfbhbg", "eejhaici", "fdedghjaacdbgcbjacc", "idb", "hfjcaejhgighcfaejba",
             "giehbfgiihe", "edccfjjccfcefhijib", "ijiddhjdj", "ecaiddaieffd", "iefabfbebjcfgibc", "efccjcchehggbaihe", "bia", "fheiaijb", "de", "ibjafee", "bdbdgg",
             "ccifbdeagcjfegagcabc", "jhacahdjec", "bej", "hfhiehajbf", "jahdafec", "ichcihgigh", "fggiddhajigcbdijeh", "bcei", "fdjbbifhfbg", "ad", "fijbfgdjejace", "hgjaiehcf",
             "gdgfghbdeah", "caa", "ahebic", "djihicijdjjjgg", "agbdcebgeieidjec", "jbfhieajhb", "chafahbdeeiaibcja", "ajjdc", "dfhbadg", "aeebfaeeefddfgdaf", "dcgcfhf",
             "cjejfeeh", "gahedajgig", "bhhejecdebfg", "hacifcejegggiiebg", "ifceefab", "cd", "ehcffaecejdjbhffa", "becedcchi", "ibffji", "jhcgac", "igggeaji",
             "jehgeeadbiebaaejgaj", "jeaehdchfehiceheid", "bda", "edfhjfahiaaihfegfieg", "bbjdbfhebbbifcgebdb", "bifcfjjc", "djbfaebcedc", "icdigh", "accegabafaj",
             "cbfaahefhdgdciedijc", "idh", "gdaajj", "jiiecjj", "ggiaehfgcgjdjga", "jgbi", "aefbecaj", "bgahfbbhdced", "ed", "gfaaad", "dihjhcfaaehcjjdbaja", "hhcjaihgejjbahh",
             "bceadgdajiih", "dfigjjgbghh", "aededfi", "gijeg", "ifiijidcgbgefihd", "higbedifdjiedfbcbi", "idhfae", "eje", "bhc", "icgebbhhbjcb", "fheaighea", "ffdggighhc",
             "cgbjaibcfhijgahhbf", "bdbeebadegifbdgab", "dcc", "iae", "gfhcdhdffjidabjc", "bicfeideiai", "jaedi", "iah", "fgagidafcejhd", "cgedeeiaehjfdfe", "jcjjddcbjhbj",
             "dbgfbidhgjhiaj", "igcfjhegbceja", "ideebhaafidghhib", "deaiccfcdgciic", "gebcf", "gj", "gjhcdfchaachfiei", "bhccfahgaedda", "debiae", "dfechabeheaggigih", "f",
             "ecffhgabdafiggjgab", "aj", "ciefdijbaahjbdb", "iaabi", "jgdahjjdbb", "fihaeggjhg", "hcbfhgbagjcfiadfbef", "fbjbbijbj", "ebefdgfaedeieaddje", "jgifd",
             "aghidfffaafaebfibdhi", "gdicieeejad", "fd", "aijfgjeeafjdebf", "fhge", "jejdgjjeejef", "gchhiccbi", "bhddeih", "efdajjcgdcaihhgfag", "eaefjihfejgi",
             "jcfbidcfgfecaff", "faie", "gdfcjfibccggch", "chafficjgjhfcbhbbfh", "fiiiaac", "fdiaacagfghdgcjhbf", "edgeheaajicf", "ef", "bgjbeiajaea", "jbfgahhjajehhcbifje",
             "hjjejbccjccdjdh", "ajchedfifbebfihj", "bijjfahfefcbghejbjch", "jiaigjaidfacjhhjdd", "jifbecchifcbj", "hccifhhifaffbeegjjh", "cihghbjhjbjeahjahdc", "efjfieiifgghj",
             "jahagfcghgf", "ha", "jaefcheabcfjc", "jibhjfiaca", "gijgihea", "hdecejabjgdc", "bdcfjh", "geaa", "cabiabhbbgfbf", "caahedgiaicdecijc", "hjgehghjfgdafhbgdfa",
             "ejibjhefaeah", "jghhebgbhje", "fhigghbhcicg", "dfeigbjidie", "efbjjibhbaehjafa", "jgjcaidfbehh", "ebbfg", "ehgbbfecidbbfbdi", "ijjhbidddagijdgbaic",
             "fbhfghfchbeahabjbece", "jdbbhcifiaead", "jhdicja", "icbcciiabcchcii", "ijiiaeaddbah", "bfbefejhfegfegdgdg", "jcdgggefiffgijafdab", "cididajibfagehce",
             "cdfdfjdfebjjeaeecie", "hciih", "hjbehh", "fihgefcaefcagbdjfbif", "gbficdhbajghc", "fgigd", "cibaiacbgfia", "ghdifgjjfjeid", "cci", "eacdbj", "dgg", "cdg", "icchjh",
             "ceahbebaefbdj", "aafaddigajhghgi", "jhijggaggdgdgdghjhj", "cccje", "dhabjfhcjajgdgijhcbc", "affahfihcbfhafieaec", "cjgbegjbgih", "faahdccfheabha", "aibdaccaadbje",
             "dggafifefhchjfggig", "djdecefgbgfiadij", "eja", "aichhhhbcedj", "ghdjieaeejehgdigdagf", "cbaeehgfhhjiicfd", "cigccfebdggadg", "jcjddf", "ieajchic", "ddb",
             "chgbjdbiebbdcffi", "begjceg", "bdebjjje", "idijjgc", "hihhidhacigiah", "fahfifiaaigiegea", "eeeccd", "ifbhagaaaiijjj", "ebhgbaighidijiidi", "fcgedhhcdccj",
             "jdjhefbac", "abf", "bejdejhafadcgeijahg", "hgbicbidhjbdajajhbi", "fiecc", "heiiiah", "ghffbbaegfhjegi", "hfdbibfiijcida", "cegjajgajiai", "dbfcacceidcbgjjbgba",
             "jagcdhhddbhgca", "ebfjjbfb", "dchbaahebcabbjfi", "hcdfbf", "degiaefhcigijdehef", "gjecdhced", "dficefbihdeg", "jchg", "jbjdcfffcjifafbiihfc", "dighhdgjajgieiidbee",
             "bgfabfhecaf", "bfgi", "hjcfjbjdehfdehdfgdjb", "jdgcdccbdbedfdea", "giaahgah", "bgiihfebfj", "hibcdfiadchajeef", "ieghhdddcjdbia", "jijhcggdjebgd", "fgc", "jjfdidjhh",
             "afjchifcacdaihijh", "acfebiaace", "jggjiddaabaagef", "dgiafgeceidabjif", "agja", "gfdhc", "egejehijbhfchhhjce", "ajgdcbehbcjdjaafjbaj", "jjacdee", "jia",
             "dggihjbibcgbgadje", "aegghhdfgcbfhj", "ffab", "dchghddagjfaagieachf", "bebbeccbbjeebaf", "fjbaj", "dajehgf", "iiiaeihbjihiaeidebic", "efccihh", "eeeiafbbjifae",
             "abighbcdbibfbjgji", "fid", "gbdhgidefdcihf", "dhghdigfhcacebfcf", "jbdcgabeecgiiceachg", "jbacfh", "ffdbecidc", "egfecfga", "dd", "dgcjibjbhgh", "jjaebhfbffi",
             "efiiehffafeagaigg", "daigbbifajdid", "baebciediadd", "bdjgahgfghedb", "bbgjgjdb", "cahdeeaga", "hjgadjfe", "gbdiighebcdiggaij", "dejgjbjdehgfbgj", "ebceg",
             "hjedcbihd", "ebfegbfaccbhegabfbh", "eehecef", "bfhbfhfifdcgajac", "jcfebffcjaj", "hiecjje", "ijdbdbgiabgfhaf", "hjfhgajdji", "igjaibddgdihbbjbgcff", "djhc",
             "dcjdaaagfgfjddjj", "chhjdgafc", "gjbdchfbbfeaf", "degffdei", "eeacbfcjggg", "faehjfidf", "iejaiiggfigegibjhdf", "ighebfgccdacgjej", "idgifjcaf", "feej",
             "jegjbbafbga", "hbhciddjjfif", "fbhdaigigjbc", "ggje", "fiahggjfded", "bjeegechjjegifif", "dhaaid", "bgi", "dchcaigdfijeb", "gabifdaba", "adchid", "ddiahjahaiged",
             "gjicaejjehcaafb", "fj", "ceijdgcjai", "jihaajfcgdcacdbaidgh", "gcecihjbbbjfeeed", "gebcciagjaecfdjg", "cbjh", "hffedcigehfejgcd", "dcjbgdf", "gicjajgafiafcbfdggf",
             "ihhdbacefbg", "bccaa", "iiigijj", "jicbaji", "bbdcgihebii"]
    print(Solution().palindromePairs(words))
    print(Solution1().palindromePairs(words))
