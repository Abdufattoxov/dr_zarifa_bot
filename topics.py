# -*- coding: utf-8 -*-
"""
Dr. Zarifa - Ginekologik Mavzular Ro'yxati
Manba: Dr_Zarifa_Ginekologik_Mavzular_Jadval.pdf
"""

SECTIONS = [
    {
        "id": 1,
        "name": "Hayz sikli va gormonal o'zgarishlar",
        "completed": True,
        "topics": [
            "Hayz vaqtidagi chidab bo'lmas og'riqlar (Dismenoreya).",
            "Hayzning sababsiz kechikishi yoki umuman kelmasligi.",
            "Ko'p qon ketishi va uzoq davom etuvchi sikl.",
            "Hayz oldi sindromi (PMS) – asabiylik, ko'krak shishi, yig'loqilik.",
            "Ovulyatsiya kunlaridagi sanchiqlar va qorin pastidagi og'riqlar.",
            "Sikl o'rtasidagi qonli ajralmalar.",
            "Tuxumdonlar polikistozi (PCOS) va uzluksiz vazn to'plash.",
            "Yuz, ko'krak va orqaga toshadigan akne (gormonal toshmalar).",
            "Erkaklar tipidagi tuklanish (iyak, mo'ylov, qorin qismida qora tuklar o'sishi).",
            "Sochlarning kuchli to'kilishi va gormonal disbalans.",
            "Qalqonsimon bez muammolari va uning ayol sog'lig'iga ta'siri.",
            "Erta menopauza (35-40 yoshda hayz to'xtashi).",
            "Klimaks davridagi 'issiq isitish' (pripadkalar), asabiylik va terlash.",
            "Sut bezlaridagi og'riq, sanchiqlar va mastopatiya.",
            "Gormonal kontratseptiv dorilar qabul qilishdagi xatolar va asoratlar."
        ]
    },
    {
        "id": 2,
        "name": "Infeksiyalar, yallig'lanish va shaxsiy gigiyena",
        "completed": False,
        "topics": [
            "Molochnitsa (Kandidoz) – qichishish va tvorogsimon ajralma.",
            "Bakterial vaginoz (ajralmadan yoqimsiz baliq hidi kelishi).",
            "Sistit – tez-tez siyish va achishishning ginekologik infeksiyalar bilan bog'liqligi.",
            "Yashirin infeksiyalar (Xlamidiya, Ureaplazma, Mikoplazma).",
            "Bachadon ortiqlari (tuxumdon va naylar) yallig'lanishi va shamollashi.",
            "Odam papilloma virusi (VPCh) va jinsiy a'zolardagi so'gallar.",
            "Qin quruqligi va kundalik faoliyatdagi noqulaylik hissi.",
            "Noto'g'ri yuvinish – atirsovun va margansovkadan foydalanish oqibatlari.",
            "Kundalik prokladkalardan har kuni foydalanishning yashirin xavfi.",
            "Shpritsirovaniya (qinni ichkarigacha suv yoki dori bilan yuvish) amaliyoti.",
            "Sintetik va tor ichki kiyimlarning infeksiya o'chog'iga aylanishi.",
            "Jinsiy aloqa vaqtidagi og'riqlar (Dispareuniya).",
            "Libido (jinsiy xohish) pasayib ketishi yoki yo'qolishi."
        ]
    },
    {
        "id": 3,
        "name": "Bachadon, tuxumdon va anatomik o'zgarishlar",
        "completed": False,
        "topics": [
            "Bachadon bo'yni eroziyasi – qachon kuydirish shart, qachon dori yetarli?",
            "Bachadon miomasi – qachon xavfsiz va qachon operatsiya talab etiladi?",
            "Tuxumdon kistalari va ularning yorilish xavfi.",
            "Endometrioz – og'riq va bepushtlikning eng katta sabablaridan biri.",
            "Bachadon ichidagi poliplar.",
            "Kichik chanoq a'zolaridagi varikoz (tomir kengayishi) sababli doimiy og'riq.",
            "Tug'ruqdan keyin yoki og'ir ko'tarish oqibatida bachadon tushishi (prolaps).",
            "Kulganda, yo'talganda yoki aksirganda siydik tuta olmaslik.",
            "Qabziyat (ich qotishi)ning ginekologik a'zolarga bosimi va zarari.",
            "Tos tubi muskullarining zaiflashishi (Kegel mashqlari yetishmasligi)."
        ]
    },
    {
        "id": 4,
        "name": "Homiladorlik, bepushtlik va muhim defitsitlar",
        "completed": False,
        "topics": [
            "Bepushtlik – homilador bo'la olmaslikning turli sabablari va tahlillar.",
            "Homilani to'g'ri rejalashtirish (tayyorgarliksiz homilador bo'lish xatolari).",
            "Homila tushishi (vykidish) – sabablari va kelajakdagi xavflarni oldini olish.",
            "Homiladorlikdagi toksikoz – holatni yengillashtirish sirlari.",
            "Tug'ruqdan keyingi depressiya va gormonal tiklanish muammolari.",
            "Emizish davridagi ko'krak yallig'lanishlari (laktostaz, mastit).",
            "Spiral qo'ydirishning asoratlari – qon ketishi va og'riqlar.",
            "Ayollarda surunkali charchoq, energiya yo'qligi va Ferretin (Temir) tanqisligi.",
            "Vitamin D yetishmovchiligi va uning ginekologiyadagi o'rni.",
            "Foly kislotasini to'g'ri ichish (nafaqat homiladorlar, balki barcha ayollar uchun).",
            "Ginekolog ko'rigiga borishdan oldin qilinadigan eng katta xatolar (analizlarni buzuvchi harakatlar).",
            "Profilaktik ko'rik – hech narsa bezovta qilmasa ham, yiliga 1 marta o'tish zarurati (Pap-test va UZI)."
        ]
    }
]

def get_active_topics():
    """Hayz mavzulari tugagan, faol (2, 3, 4-bo'lim) mavzular ro'yxatini qaytaradi."""
    active = []
    for sec in SECTIONS:
        if not sec["completed"]:
            for idx, top in enumerate(sec["topics"], 1):
                active.append({
                    "section_id": sec["id"],
                    "section_name": sec["name"],
                    "topic_num": idx,
                    "title": top
                })
    return active
