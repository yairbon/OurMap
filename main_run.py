import folium
from folium import plugins

# 1. רשימת הזכרונות שלכם (כפי שכתבת)
memories = [
    [32.11334351752411, 34.82451353092783, "זוריק", "כאן הכל התחיל...", 'https://github.com/yairbon/OurMap/blob/main/images/Maor.png?raw=true'],
    [32.11612971701936, 34.824230026858814, "הבית של צ'יזי", "רואים הרבה סרטים", None],
    [29.554286078353417, 34.96347304056956, "חצי שנה באילת מי לא ישתגע", "לילות משוגעים לפנינו", None],
    [32.119177, 34.821454,"ממסאג' לנשיקה", "הנשיקה הראשונה... אני לא אדבר יותר מידי אבל היא הייתה מושלמת",'https://github.com/yairbon/OurMap/blob/main/images/FirstKiss.png?raw=true'],
    [32.12301749051284, 34.796344793133535,"הבית של מאמצ'י", "מאוד כיף בבית שלך מאמי",'https://github.com/yairbon/OurMap/blob/main/images/CopFlowert.png?raw=true'],
    [32.12307247678932, 34.796111656415505,"הספוט", "מקום טוב לריקודים וחיבוקים",None],
    [32.068586401959415, 34.78379535225245,"ביקורים באלו", "אני תמיד אבוא לתמוך בך ולהיות איתך יפה שלי",None],
    [32.09706910694193, 34.82277662555583,"מי לא אוהב דאבל דייט","פעם ראשונה במסעדה!!!!",None],
    [32.08448912922599, 34.7691806596383,"ספא ספא ספא","אחד הימים הכי מצחקים שלנו ובאמת שבוע שגרם לי להתאהב בך אפילו יותר",'https://github.com/yairbon/OurMap/blob/main/images/herods.png?raw=true'],
    [32.0973178638277, 34.77374865035221,"נמל נמל נמל","למה אנחנו כל כך אוהבים לבוא לפה בכלל",None],
    [32.91887354965823, 35.06960991896012,"קופצים לעכו וחוזרים","אחד מהטיולים הראשונים שלנו והמרעיבים חחחח",None],
    [50.07627449811814, 14.436252950921983,"פראגגגגגג","אל תדאגי מאמי נגיע לפראג",None],
    [32.820690877304, 34.990943482725534,"קריסמס בחיפה","אז.... מי לא אוהב קריסמס? אני? את? או שבעצם כולם",None],
    [32.612246118644975, 35.118217268202656,"נחל גחר","מהטיולים הכיפים שלנו ונופים באמת מדהימים (והטרדה כמובן)",'https://github.com/yairbon/OurMap/blob/main/images/gahar.png?raw=true'],
    [31.76944348570288, 35.11228767036008,"טיול בהר איתן","עוד טיול מוצלח שלנו ממש לפני שטסתי לתאילנד וגם הכרתי לך את אבא שלי והיה מדהים",'https://github.com/yairbon/OurMap/blob/main/images/Eitan.png?raw=true'],
    [31.98340130786961, 34.77120559384451,"מה שקורה בראשון נשאר בראשון","שנינו זוכרים שהשתגענו בראשון אבל בטוח לא מדברים על זה",None],
    [32.122760143328726, 34.806675517914535,"לעבוד ביחד? איך לא חשבנו על זה קודם","כן כן לעבוד ביחד מי חשב שנגיע אפילו לזה חחח",'https://github.com/yairbon/OurMap/blob/main/images/WorkingTog.png?raw=true'],
    [32.502762215364335, 34.89084525580821,"ערב טוב קיסריה!! (או רק לשנינו)","לזכרוני הטיול הראשון שלנו לא? קצת השתגעת עלי אבל אנחנו שורדים הכל אהבה שלי",'https://github.com/yairbon/OurMap/blob/main/images/perfec.png?raw=true'],
    [32.0976945478919, 34.775783658435245,"המאנצ' הכי טוב בתל אביב","איך אפשר לעשות מפת זכרונות בלי לדבר על המקום האהוב עלינו",'https://github.com/yairbon/OurMap/blob/main/images/Abu.png?raw=true']
]

# 2. יצירת המפה - כאן החלפתי ל-OpenStreetMap
# אפשרות 1: מפה צבעונית
m = folium.Map(location=[32.5, 34.8], zoom_start=8, tiles='OpenStreetMap')

# אפשרות 2 (אם תרצה, תוריד את ה-# בתחילת השורה ותוסיף לראשונה):
# m = folium.Map(location=[32.5, 34.8], zoom_start=8, tiles='Stamen Terrain', attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.')

# אפשרות 3 (למפה כהה):
# m = folium.Map(location=[32.5, 34.8], zoom_start=8, tiles='CartoDB dark_matter')


# 3. הוספת הנקודות למפה (הקוד שלך המצוין)
for lat, lon, title, description, img_url in memories:
    
    img_tag = ""
    # בדיקה בטוחה יותר ל-None או סטרינג ריק
    if img_url and str(img_url).strip().lower() != 'none':
        img_tag = f'<img src="{img_url}" alt="{title}" style="width:100%; border-radius: 5px; margin-bottom: 5px;">'
    
    html = f"""
    <div style="font-family: 'Arial', sans-serif; direction: rtl; text-align: right; width: 200px;">
        <h4 style="margin-bottom: 5px; color: #e63946;">{title}</h4>
        {img_tag}
        <p style="font-size: 13px; line-height: 1.4;">{description}</p>
        <hr style="border: 0.5px solid #eee;">
        <p style="font-size: 11px; color: gray;">קואורדינטות: {lat}, {lon}</p>
    </div>
    """
    
    popup = folium.Popup(html, max_width=250)
    folium.Marker(
        [lat, lon],
        popup=popup,
        icon=folium.Icon(color='red', icon='heart', prefix='fa'),
        tooltip=title
    ).add_to(m)

# הוספתי גם כפתור מסך מלא שיהיה יותר נוח בטלפון
plugins.Fullscreen(
    position='topright',
    title='מסך מלא',
    title_cancel='צא ממסך מלא',
    force_separate_button=True
).add_to(m)


# 4. שמירה
m.save("index.html")
print("המפה הצבעונית החדשה נוצרה! תעשה git add, commit ו-push כדי לעדכן את האתר.")