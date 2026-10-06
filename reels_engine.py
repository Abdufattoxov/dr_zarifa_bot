# -*- coding: utf-8 -*-
"""
Reels va Hook Generator Engine
dr-zarifa-reels skill qoidalari asosida 10 ta professional hook,
30 soniyalik ssenariy va Lid-magnit loyihasini yaratadi.
"""

def generate_10_hooks(topic_title: str):
    """
    Mavzuga mos 10 xil psixologik toifadagi ilmoqlar (hook) generatsiya qiladi.
    """
    clean_topic = topic_title.split("–")[0].split("(")[0].strip()
    
    hooks = [
        {
            "id": 1,
            "type": "Provokatsion (Qiziqtiruvchi)",
            "text": f"Siz buni oddiy shamollash deb o'ylaysiz, lekin bu — {clean_topic}! Nega ko'pchilik ayollar adashadi?"
        },
        {
            "id": 2,
            "type": "Identifikatsiya (O'zini ko'rish)",
            "text": f"Agar sizda ham {clean_topic.lower()} belgilari bo'lsa, bu videoni oxirigacha ko'ring — sababini bilmasdan dori ichmang!"
        },
        {
            "id": 3,
            "type": "Mif buzish (Xatolarni tuzatish)",
            "text": f"'{clean_topic} o'z-o'zidan o'tib ketadi' deb o'ylaysizmi? 28 yillik tajribamda buni eng xavfli xato deb bilaman!"
        },
        {
            "id": 4,
            "type": "Raqamli (Aniq faktlar)",
            "text": f"Ayollarda {clean_topic.lower()} qaytalanishining 3 ta yashirin sababi — bittasi sizda ham borligi aniq."
        },
        {
            "id": 5,
            "type": "Vaqt chegarasi (Tezkorlik)",
            "text": f"Agar bu belgi 3 kundan ortiq davom etayotgan bo'lsa, darhol to'xtang: {clean_topic.lower()} qachon xavfli bo'ladi?"
        },
        {
            "id": 6,
            "type": "Shaxsiy tajriba (Klinik amaliyot)",
            "text": f"Menga qabulga kelgan 10 ta ayoldan 6 tasi aynan {clean_topic.lower()} bo'yicha bitta xatoni takrorlaydi..."
        },
        {
            "id": 7,
            "type": "Savolga asoslangan",
            "text": f"Siz ham {clean_topic.lower()}dan qutulolmay dorixonadagi barcha shamchalarni sinab ko'rdingizmi? Keling, to'g'ri yo'lini aytaman."
        },
        {
            "id": 8,
            "type": "Ogohlantirish (Ehtiyotkorlik)",
            "text": f"Diqqat qiling: {clean_topic.lower()} vaqtida qilinadigan ushbu 1 ta harakat surunkali kasallikka olib kelishi mumkin!"
        },
        {
            "id": 9,
            "type": "Qiyoslash va Pulni tejash",
            "text": f"Ortiqcha qimmat analizlarsiz {clean_topic.lower()}ni qanday aniqlash va oqilona davolash mumkin?"
        },
        {
            "id": 10,
            "type": "Lokal (Hududiy urg'u)",
            "text": f"Bulung'ur ayollarida eng ko'p uchraydigan va e'tiborsiz qoldiriladigan muammo: bu {clean_topic.lower()}!"
        }
    ]
    return hooks


def generate_full_reels_script(topic_title: str, chosen_hook: dict, with_lead_magnet: bool):
    """
    Tanlangan hook asosida 30 soniyalik Reels ssenariysi va Lid-magnit loyihasini tuzadi.
    """
    clean_topic = topic_title.split("–")[0].split("(")[0].strip()
    
    # Trigger kalit so'zi (Chatplace uchun)
    trigger_word = clean_topic.replace(" ", "").upper()[:7]
    if len(trigger_word) < 4:
        trigger_word = "QOLLANMA"

    if with_lead_magnet:
        cta_text = f"Ushbu muammoni uy sharoitida to'g'ri nazorat qilish va xatolarga yo'l qo'ymaslik uchun maxsus qo'llanma tayyorladim. Izohda '{trigger_word}' deb yozing, to'liq PDF yo'riqnomani Direct'ingizga bepul yuboraman!"
        cta_type = "Lid-magnit va Chatplace kalit so'zi"
        lead_magnet_info = f"""
━━━━━━━━━━━━━━━━━━━━
📄 TAYYORLANGAN LID-MAGNIT (PDF LOYIHASI):
Nomi: "{clean_topic} bo'yicha Shifokor Zarifadan 5 ta Oltin Qoida"
Hajmi: 2 betlik qulay PDF qo'llanma.
Mazmuni:
1. Birinchi yordam: nima qilish mumkin, nima qat'iyan taqiqlanadi (margansovka/atirsovun xavfi).
2. Qaysi tahlillarni topshirish kerak va qaysi qimmat tahlillar shart emas.
3. Qaytalanishning oldini oluvchi shaxsiy gigiyena tartibi.
4. Shifokor ko'rigi zarur bo'lgan xavfli 'qizil bayroqchalar'.
5. Qabul manzili: Bulung'ur, Gamma Med klinikasi (+998 95 507-33-30).

🤖 CHATPLACE UCHUN TRIGGER:
• Izoh kalit so'zi: {trigger_word}
• Direct 1-xabari: "Assalomu alaykum! {clean_topic} bo'yicha shifokor tavsiyalari jamlangan PDF qo'llanmani yuklab olish uchun pastdagi tugmani bosing 👇"
━━━━━━━━━━━━━━━━━━━━
"""
    else:
        cta_text = f"Sizda ham ushbu belgilar kuzatilganmi? O'zingizda nimalarni sezasiz, izohda yozib qoldiring, eng ko'p so'ralgan savollarga keyingi videoda javob beraman!"
        cta_type = "Savol va Munozara uyg'otish"
        lead_magnet_info = "Lid-magnit tanlanmadi (Faqatgina munozarali qisqa video)."

    script_body = f"""
00:00 - 00:03 (HOOK / Kadr 1 - Yirik plan):
"{chosen_hook['text']}"

00:03 - 00:20 (ASOSIY QISM / Kadr 2 - Shifokor stoli, professional ko'rinish):
"Ko'pchilik ayollar {clean_topic.lower()} paytida o'zboshimchalik bilan dugonasining maslahatiga yoki dorixonachi tavsiyasiga tayanadi. Natijada esa kasallik vaqtincha bosiladi-yu, lekin surunkali shaklga o'tib ketadi.
Birinchidan, noo'rin dori ichish qin mikroflorasini butunlay buzadi.
Ikkinchidan, infeksiyaning asl sababi aniqlanmay, vaqt va ortiqcha pul sarflanadi."

00:20 - 00:30 (CTA / Kadr 3 - Tabassum va qat'iy chaqiruv):
"{cta_text}"
"""

    response_text = f"""
🎬 **30 SONIYoLIK REELS SSENARIYSI**

**Mavzu:** {topic_title}
**Hook turi:** {chosen_hook['type']}
**CTA turi:** {cta_type}
**Viral baho:** 8.8 / 9
**Davomiyligi:** ~30 soniya (110 so'z)

━━━━━━━━━━━━━━━━━━━━
**SSENARIY MATNI:**
{script_body.strip()}
━━━━━━━━━━━━━━━━━━━━
{lead_magnet_info.strip()}

**Tushuntirish:** Ssenariy birinchi 1.5 soniyada tomoshabinning og'riqli nuqtasini ushlaydi, xatoni ko'rsatib ekspertlik ishonchini uyg'otadi va izoh yozishga (algoritmik faollikka) undaydi.
"""
    return response_text
